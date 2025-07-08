import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from . import signing
from .logging_config import setup_logging

SUPPORTED_EXTS = {'.ps1', '.exe', '.dll', '.msi', '.ocx', '.js', '.vbs', '.wsf'}


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('LDCertFix')
        self._set_app_icon()
        self.logger = setup_logging()

        self.style = ttk.Style(self)
        # Use a modern theme if available
        if 'clam' in self.style.theme_names():
            self.style.theme_use('clam')

        self.cert_var = tk.StringVar()
        self._build_widgets()
        self.refresh_certs()
        # start with empty list; user can add files manually

    def _set_app_icon(self):
        """Attempt to set window icon from 'logo.ico'."""
        icon_path = Path(__file__).resolve().parent.parent / 'logo.ico'
        try:
            self.iconbitmap(default=str(icon_path))
        except Exception:
            # Ignore missing or invalid icon files
            pass

    def _build_widgets(self):
        top = ttk.Frame(self)
        top.pack(fill=tk.X, padx=5, pady=5)

        ttk.Label(top, text='Zertifikat:').pack(side=tk.LEFT)
        self.cert_combo = ttk.Combobox(top, textvariable=self.cert_var, width=50)
        self.cert_combo.pack(side=tk.LEFT, padx=5)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill=tk.X, padx=5, pady=5)

        ttk.Button(btn_frame, text='➕ Dateien hinzufügen', command=self.add_files).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text='➖ Entfernen', command=self.remove_selected).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text='🔏 Signieren', command=self.sign_selected).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text='🧪 Alle prüfen', command=self.verify_all).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text='📂 Datei prüfen', command=self.verify_single).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text='📄 Log anzeigen', command=self.show_log).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text='ℹ️ Info', command=self.show_info).pack(side=tk.LEFT, padx=2)

        self.tree = ttk.Treeview(
            self,
            columns=('path', 'type', 'status'),
            show='headings',
            selectmode='extended'
        )
        self.tree.heading('path', text='Datei')
        self.tree.heading('type', text='Typ')
        self.tree.heading('status', text='Status')
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

    def selected_thumbprint(self):
        name = self.cert_var.get()
        return self._cert_map.get(name)

    def sign_selected(self):
        thumb = self.selected_thumbprint()
        if not thumb:
            messagebox.showerror('Fehler', 'Kein Zertifikat ausgewählt')
            return
        for item in self.tree.selection() or self.tree.get_children():
            path = Path(item)
            result = signing.sign_file(path, thumb)
            self.logger.info('Sign %s: %s', path, result.strip())
            self.tree.set(item, 'status', 'signed')

    def verify_all(self):
        messages = []
        for item in self.tree.get_children():
            path = Path(item)
            result = signing.verify_file(path)
            self.logger.info('Verify %s: %s', path, result.strip())
            self.tree.set(item, 'status', 'checked')
            msg = f"{path.name}: {result.strip() or 'Keine Ausgabe'}"
            messages.append(msg)
        if messages:
            messagebox.showinfo('Alle prüfen', "\n\n".join(messages))

    def verify_single(self):
        filename = filedialog.askopenfilename()
        if not filename:
            return
        path = Path(filename)
        result = signing.verify_file(path)
        messagebox.showinfo('Verifikation', result or 'Keine Ausgabe')
        self.logger.info('Verify %s: %s', path, result.strip())

    def show_log(self):
        log_window = tk.Toplevel(self)
        log_window.title('Log')
        text = tk.Text(log_window, wrap='none')
        text.pack(fill=tk.BOTH, expand=True)
        try:
            with open('ldcertfix.log', 'r', encoding='utf-8') as f:
                text.insert('1.0', f.read())
        except FileNotFoundError:
            text.insert('1.0', 'Kein Log gefunden')

    def show_info(self):
        info = (
            "LDCertFix\n\n"
            "Benötigte Komponenten:\n"
            "\u2022 Python 3.9 oder neuer\n"
            "\u2022 signtool.exe aus dem Windows SDK\n"
            "\u2022 PowerShell ab Version 5\n"
            "\u2022 Optional: PyInstaller f\u00fcr eine eigene EXE\n\n"
            "\u00a9 2024 Let's Do. – Inh. Peter Seidl\n"
            "Alle Rechte vorbehalten."
        )
        messagebox.showinfo('Informationen', info)


def run():
    app = MainWindow()
    app.mainloop()
