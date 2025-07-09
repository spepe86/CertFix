"""Tkinter-based user interface for LDCertFix."""

import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from . import signing
from .logging_config import setup_logging
from .translations import TRANSLATIONS, LANGUAGES
from .config import load_config, save_config

SUPPORTED_EXTS = {'.ps1', '.exe', '.dll', '.msi', '.ocx', '.js', '.vbs', '.wsf'}


class MainWindow(tk.Tk):
    """Main application window containing all controls."""
    def __init__(self):
        super().__init__()
        self.title('LDCertFix')
        self._set_app_icon()
        self.logger = setup_logging()

        self.style = ttk.Style(self)
        # Use a modern theme if available
        if 'clam' in self.style.theme_names():
            self.style.theme_use('clam')

        cfg = load_config()
        self.lang = cfg.get('language', 'DE')
        if self.lang not in LANGUAGES:
            self.lang = 'DE'
        self.tr = TRANSLATIONS[self.lang]

        self.cert_var = tk.StringVar()
        self.lang_var = tk.StringVar(value=self.lang)

        self._build_widgets()
        self.refresh_certs()
        # start with empty list; user can add files manually

    def _apply_icon(self, window):
        """Attempt to set icon from 'logo.ico' for the given window."""
        icon_path = Path(__file__).resolve().parent.parent / 'logo.ico'
        try:
            window.iconbitmap(default=str(icon_path))
        except Exception:
            pass

    def _set_app_icon(self):
        self._apply_icon(self)

    def _build_widgets(self):
        top = ttk.Frame(self)
        top.pack(fill=tk.X, padx=5, pady=5)

        self.cert_label = ttk.Label(top, text=self.tr['certificate'])
        self.cert_label.pack(side=tk.LEFT)
        self.cert_combo = ttk.Combobox(top, textvariable=self.cert_var, width=50)
        self.cert_combo.pack(side=tk.LEFT, padx=5)

        self.lang_label = ttk.Label(top, text=self.tr['language_label'])
        self.lang_label.pack(side=tk.LEFT, padx=(10, 0))
        self.lang_combo = ttk.Combobox(top, textvariable=self.lang_var, values=LANGUAGES, width=5, state='readonly')
        self.lang_combo.pack(side=tk.LEFT)
        self.lang_combo.bind('<<ComboboxSelected>>', self.change_language)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill=tk.X, padx=5, pady=5)

        self._buttons = [
            (ttk.Button(btn_frame, text=self.tr['add_files'], command=self.add_files), 'add_files'),
            (ttk.Button(btn_frame, text=self.tr['remove'], command=self.remove_selected), 'remove'),
            (ttk.Button(btn_frame, text=self.tr['sign'], command=self.sign_selected), 'sign'),
            (ttk.Button(btn_frame, text=self.tr['verify_single'], command=self.verify_single), 'verify_single'),
            (ttk.Button(btn_frame, text=self.tr['show_log'], command=self.show_log), 'show_log'),
            (ttk.Button(btn_frame, text=self.tr['info'], command=self.show_info), 'info'),
        ]
        for btn, _ in self._buttons:
            btn.pack(side=tk.LEFT, padx=2)

        self.tree = ttk.Treeview(
            self,
            columns=('path', 'type', 'status'),
            show='headings',
            selectmode='extended'
        )
        self.tree.heading('path', text=self.tr['file'])
        self.tree.heading('type', text=self.tr['type'])
        self.tree.heading('status', text=self.tr['status'])
        self.tree.column('path', width=300)
        self.tree.column('type', width=60, anchor='center')
        self.tree.column('status', width=100, anchor='center')
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def refresh_certs(self):
        certs = signing.list_certificates()
        display = [c[0] for c in certs]
        self.cert_combo['values'] = display
        if certs:
            self.cert_combo.current(0)
        self._cert_map = {c[0]: c[1] for c in certs}

    def populate_files(self):
        """Populate list with supported files from current directory."""
        self.tree.delete(*self.tree.get_children())
        for name in os.listdir('.'):
            path = Path(name).resolve()
            ext = path.suffix.lower()
            if ext in SUPPORTED_EXTS:
                display = os.path.relpath(path)
                self.tree.insert('', tk.END, iid=str(path), values=(display, ext or '', ''))

    def add_files(self):
        filenames = filedialog.askopenfilenames()
        for fname in filenames:
            path = Path(fname).resolve()
            ext = path.suffix.lower()
            if ext in SUPPORTED_EXTS and not self.tree.exists(str(path)):
                display = os.path.relpath(path)
                self.tree.insert('', tk.END, iid=str(path), values=(display, ext or '', ''))

    def remove_selected(self):
        for item in self.tree.selection():
            self.tree.delete(item)

    def change_language(self, *_):
        sel = self.lang_var.get()
        if sel not in LANGUAGES:
            return
        self.lang = sel
        self.tr = TRANSLATIONS[self.lang]
        self.update_language()
        save_config({'language': self.lang})

    def update_language(self):
        self.cert_label.configure(text=self.tr['certificate'])
        self.lang_label.configure(text=self.tr['language_label'])
        for idx, (btn, key) in enumerate(self._buttons):
            btn.configure(text=self.tr[key])
        self.tree.heading('path', text=self.tr['file'])
        self.tree.heading('type', text=self.tr['type'])
        self.tree.heading('status', text=self.tr['status'])

    def selected_thumbprint(self):
        name = self.cert_var.get()
        return self._cert_map.get(name)

    def sign_selected(self):
        thumb = self.selected_thumbprint()
        if not thumb:
            messagebox.showerror(self.tr['error_title'], self.tr['error_no_cert'])
            return
        items = self.tree.selection() or self.tree.get_children()
        if not items:
            messagebox.showwarning(
                self.tr['error_title'],
                self.tr.get('error_no_files', 'Keine Dateien ausgewählt')
            )
            return
        messages = []
        for item in items:
            path = Path(item)
            result = signing.sign_file(path, thumb)
            self.logger.info('Sign %s: %s', path, result.strip())
            self.tree.set(item, 'status', 'signed')
            messages.append(f"{path.name}: {result.strip() or self.tr['no_output']}")
        messagebox.showinfo(
            self.tr.get('sign_title', self.tr['sign']),
            "\n\n".join(messages)
        )

    def verify_single(self):
        filename = filedialog.askopenfilename()
        if not filename:
            return
        path = Path(filename)
        result = signing.verify_file(path)
        messagebox.showinfo(self.tr['verification_title'], result or self.tr['no_output'])
        self.logger.info('Verify %s: %s', path, result.strip())

    def show_log(self):
        log_window = tk.Toplevel(self)
        log_window.title(self.tr['log_title'])
        self._apply_icon(log_window)
        text = tk.Text(log_window, wrap='none')
        text.pack(fill=tk.BOTH, expand=True)
        try:
            with open('ldcertfix.log', 'r', encoding='utf-8') as f:
                text.insert('1.0', f.read())
        except FileNotFoundError:
            text.insert('1.0', self.tr['no_log'])

    def show_info(self):
        win = tk.Toplevel(self)
        win.title(self.tr['info_title'])
        self._apply_icon(win)

        frame = ttk.Frame(win)
        frame.pack(padx=10, pady=10)

        icon_path = Path(__file__).resolve().parent.parent / 'logo.ico'
        try:
            img = tk.PhotoImage(file=str(icon_path))
        except Exception:
            img = None
        if img:
            icon_label = ttk.Label(frame, image=img)
            icon_label.image = img
            icon_label.pack(side=tk.LEFT, padx=(0, 10))

        msg = ttk.Label(frame, text=self.tr['info_text'], justify='left')
        msg.pack(side=tk.LEFT)


def run() -> None:
    """Launch the GUI application."""
    app = MainWindow()
    app.mainloop()
