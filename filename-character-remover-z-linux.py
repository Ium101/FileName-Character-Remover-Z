#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import re
import sys
import platform

# DPI awareness fix for Windows high-DPI screens (Windows only)
if platform.system() == "Windows":
    try:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)  # SYSTEM_AWARE
    except Exception:
        pass


# ---------------------------------------------------------------------------
# Translations
# ---------------------------------------------------------------------------

STRINGS = {
    "en": {
        # window
        "window_title":        "Filename Character Remover Z - FILENAMES ONLY",
        # warning banner
        "warn1":               "WARNING: THIS TOOL ONLY RENAMES FILENAMES",
        "warn2":               "IT DOES NOT OPEN, READ, OR MODIFY FILE CONTENTS",
        "warn3":               "IT ONLY USES os.rename() - THE SAFEST RENAME METHOD",
        # title
        "app_title":           "Remove Custom Characters from Filenames",
        # dolphin row
        "dolphin_cb":          'Fix Dolphin/KDE duplicate artefacts  (example:  "photo (1).png (1)"  ->  "photo (1).png")',
        # add-ext row
        "addext_cb":           "Add extension to files that have no extension:",
        "addext_hint":         "(example: .png  .jpg  .txt - dot optional)",
        # substring row
        "substr_label":        "Substring to remove:",
        "substr_hint":         "<- Enter any characters/string (example: []abc123 )",
        # case row
        "case_cb":             "Case-sensitive matching",
        # buttons
        "btn_folder":          "Select Folder",
        "btn_file":            "Select File",
        "btn_rename":          "RENAME FILES",
        # list label
        "list_label":          "Files that will be renamed:",
        # status messages
        "status_init":         "Step 1: Configure options above, then select a folder or file",
        "status_scanning":     "Selected folder: {folder}\nScanning for files...",
        "status_found1":       "Found 1 file to rename.",
        "status_no_change":    "No changes needed for the selected file.",
        "status_none":         "No files matched the current settings.",
        "status_found":        "Found {n} files to rename.",
        "status_done":         "Done! Renamed {ok} files, Failed: {fail}",
        # warnings / dialogs
        "warn_no_folder":      "No Folder",
        "warn_no_folder_msg":  "Please select a folder first",
        "warn_no_ext":         "No Extension",
        "warn_no_ext_msg":     "Please enter the extension to add (example: .png)",
        "warn_no_files":       "No Files",
        "warn_no_files_msg":   "Please scan for files first",
        "err_scan":            "Error scanning folder: {e}",
        # extension-change dialog
        "extchg_title":        "WARNING: File Extensions Will Change",
        "extchg_body":         (
            "The following {n} file(s) will have their existing extension changed:\n\n"
            "{sample}\n\n"
            "Changing extensions can make files unreadable by their associated applications.\n\n"
            "Are you sure you want to proceed?"
        ),
        "extchg_more":         "  ... and {n} more",
        # final confirmation
        "confirm_title":       "FINAL CONFIRMATION",
        "confirm_body":        (
            "This will RENAME {n} file(s).\n\n"
            "Operations:\n{notes}\n\n"
            "WARNING: Make sure you have BACKUPS first!\n\n"
            "Duplicate targets will be resolved automatically by adding (N).\n"
            "This action ONLY renames files - file contents are never touched.\n\n"
            "Continue?"
        ),
        "note_substr":         "Removing substring: '{s}'",
        "note_dolphin":        "Fixing Dolphin/KDE duplicate artefacts",
        "note_addext":         "Adding '{ext}' to {n} extensionless file(s)",
        # result dialog
        "result_title":        "Complete",
        "result_ok":           "Successfully renamed {n} files!",
        "result_fail":         "\nFailed: {n} files",
        "result_errors":       "\n\nErrors (first 10):\n",
        "err_empty":           "{f}: New filename would be empty",
        # language button
        "lang_btn":            "PT-BR",
        # credits
        "credits":             "Made by Ium101",
    },
    "pt": {
        # window
        "window_title":        "Filename Character Remover Z - SOMENTE NOMES DE ARQUIVO",
        # warning banner
        "warn1":               "AVISO: ESTA FERRAMENTA RENOMEIA APENAS NOMES DE ARQUIVO",
        "warn2":               "ELA NAO ABRE, LE NEM MODIFICA O CONTEUDO DOS ARQUIVOS",
        "warn3":               "USA APENAS os.rename() - O METODO MAIS SEGURO DE RENOMEAR",
        # title
        "app_title":           "Remover Caracteres Personalizados de Nomes de Arquivo",
        # dolphin row
        "dolphin_cb":          'Corrigir artefatos duplicados do Dolphin/KDE  (exemplo:  "foto (1).png (1)"  ->  "foto (1).png")',
        # add-ext row
        "addext_cb":           "Adicionar extensao a arquivos sem extensao:",
        "addext_hint":         "(exemplo: .png  .jpg  .txt - ponto opcional)",
        # substring row
        "substr_label":        "Substring a remover:",
        "substr_hint":         "<- Digite caracteres/texto (exemplo: []abc123 )",
        # case row
        "case_cb":             "Correspondencia com diferenciacao de maiusculas",
        # buttons
        "btn_folder":          "Selecionar Pasta",
        "btn_file":            "Selecionar Arquivo",
        "btn_rename":          "RENOMEAR ARQUIVOS",
        # list label
        "list_label":          "Arquivos que serao renomeados:",
        # status messages
        "status_init":         "Passo 1: Configure as opcoes acima, depois selecione uma pasta ou arquivo",
        "status_scanning":     "Pasta selecionada: {folder}\nVarendo arquivos...",
        "status_found1":       "1 arquivo encontrado para renomear.",
        "status_no_change":    "Nenhuma alteracao necessaria para o arquivo selecionado.",
        "status_none":         "Nenhum arquivo correspondeu as configuracoes atuais.",
        "status_found":        "{n} arquivos encontrados para renomear.",
        "status_done":         "Concluido! Renomeados: {ok}, Falhas: {fail}",
        # warnings / dialogs
        "warn_no_folder":      "Sem Pasta",
        "warn_no_folder_msg":  "Selecione uma pasta primeiro",
        "warn_no_ext":         "Sem Extensao",
        "warn_no_ext_msg":     "Digite a extensao a adicionar (exemplo: .png)",
        "warn_no_files":       "Sem Arquivos",
        "warn_no_files_msg":   "Varredura de arquivos necessaria antes de renomear",
        "err_scan":            "Erro ao varrer a pasta: {e}",
        # extension-change dialog
        "extchg_title":        "AVISO: Extensoes de Arquivo Serao Alteradas",
        "extchg_body":         (
            "Os seguintes {n} arquivo(s) terao sua extensao existente alterada:\n\n"
            "{sample}\n\n"
            "Alterar extensoes pode tornar arquivos ilegíveis pelos aplicativos associados.\n\n"
            "Tem certeza que deseja continuar?"
        ),
        "extchg_more":         "  ... e mais {n}",
        # final confirmation
        "confirm_title":       "CONFIRMACAO FINAL",
        "confirm_body":        (
            "Isso ira RENOMEAR {n} arquivo(s).\n\n"
            "Operacoes:\n{notes}\n\n"
            "AVISO: Certifique-se de ter BACKUPS primeiro!\n\n"
            "Alvos duplicados serao resolvidos automaticamente adicionando (N).\n"
            "Esta acao APENAS renomeia arquivos - o conteudo nunca e tocado.\n\n"
            "Continuar?"
        ),
        "note_substr":         "Removendo substring: '{s}'",
        "note_dolphin":        "Corrigindo artefatos duplicados do Dolphin/KDE",
        "note_addext":         "Adicionando '{ext}' a {n} arquivo(s) sem extensao",
        # result dialog
        "result_title":        "Concluido",
        "result_ok":           "Renomeados com sucesso: {n} arquivos!",
        "result_fail":         "\nFalhas: {n} arquivos",
        "result_errors":       "\n\nErros (primeiros 10):\n",
        "err_empty":           "{f}: Novo nome ficaria vazio",
        # language button
        "lang_btn":            "EN",
        # credits
        "credits":             "Feito por Ium101",
    },
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def fix_dolphin_duplicate(filename):
    pattern = re.compile(r'^(.*\.[^./ \\]+?)(\s+\(\d+\))+$')
    m = pattern.match(filename)
    return m.group(1) if m else filename


def safe_target_path(directory, new_name):
    target = os.path.join(directory, new_name)
    if not os.path.exists(target):
        return target, new_name
    base, ext = os.path.splitext(new_name)
    base_clean = re.sub(r'\s*\(\d+\)$', '', base)
    counter = 2
    while True:
        candidate_name = f"{base_clean} ({counter}){ext}"
        candidate_path = os.path.join(directory, candidate_name)
        if not os.path.exists(candidate_path):
            return candidate_path, candidate_name
        counter += 1


def extension_changed(old_name, new_name):
    real_old_ext = os.path.splitext(fix_dolphin_duplicate(old_name))[1].lower()
    new_ext = os.path.splitext(new_name)[1].lower()
    return real_old_ext != new_ext


def has_no_extension(filename):
    _, ext = os.path.splitext(filename)
    return ext == ""


def normalise_extension(raw):
    raw = raw.strip().lower()
    if not raw:
        return ""
    if not raw.startswith("."):
        raw = "." + raw
    return raw


# ---------------------------------------------------------------------------
# GUI
# ---------------------------------------------------------------------------

class CustomCharacterRemover:
    def __init__(self, root):
        self.root = root
        self.lang = "en"           # current language key
        self.files = []
        self.base_folder = None

        try:
            self.root.tk.call('tk', 'scaling', 1.5)
        except Exception:
            pass

        self._build_ui()
        self._apply_lang()         # set all text to current language
        # Lock size after the first event-loop tick so all text is rendered
        root.after(0, self._lock_size)

    def _lock_size(self):
        """
        Lock the window to the tallest size across all languages so switching
        never clips widgets (e.g. credits disappearing on Linux with PT-BR).
        Applies every language, measures, keeps the max, then restores.
        """
        max_w = 960
        max_h = 0
        original_lang = self.lang

        for lang in STRINGS:
            self.lang = lang
            self._apply_lang()
            self.root.update_idletasks()
            w = self.root.winfo_reqwidth()
            h = self.root.winfo_reqheight()
            max_w = max(max_w, w)
            max_h = max(max_h, h)

        # Restore the original language
        self.lang = original_lang
        self._apply_lang()

        self.root.resizable(False, False)
        self.root.minsize(max_w, max_h)
        self.root.maxsize(max_w, max_h)

    # -----------------------------------------------------------------------
    # UI construction  (widgets created once; text set via _apply_lang)
    # -----------------------------------------------------------------------

    def _build_ui(self):
        root = self.root

        # Size is locked after full render — see _lock_size() called via root.after()

        # ── BIG WARNING  (language button lives here, top-right) ───────────
        warning_frame = tk.Frame(root, bg="yellow", pady=10)
        warning_frame.pack(fill=tk.X)

        # Language button anchored to the top-right of the banner
        self.lang_btn = tk.Button(
            warning_frame, text="", width=6,
            font=("Arial", 9, "bold"),
            bg="#555555", fg="white",
            relief=tk.FLAT, cursor="hand2",
            command=self._toggle_lang,
        )
        self.lang_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-6, y=4)

        self.lbl_warn1 = tk.Label(warning_frame, text="",
                 font=("Arial", 16, "bold"), bg="yellow", fg="red",
                 wraplength=880)
        self.lbl_warn1.pack()
        self.lbl_warn2 = tk.Label(warning_frame, text="",
                 font=("Arial", 11), bg="yellow", fg="black",
                 wraplength=880)
        self.lbl_warn2.pack()
        self.lbl_warn3 = tk.Label(warning_frame, text="",
                 font=("Arial", 9), bg="yellow", fg="black",
                 wraplength=880)
        self.lbl_warn3.pack()

        # ── App title ──────────────────────────────────────────────────────
        self.lbl_title = tk.Label(root, text="", font=("Arial", 14, "bold"))
        self.lbl_title.pack(pady=8)

        # ── Dolphin fix toggle ─────────────────────────────────────────────
        dolphin_frame = tk.Frame(root, bg="#E8F4FD", pady=6, padx=10,
                                 relief=tk.GROOVE, bd=1)
        dolphin_frame.pack(fill=tk.X, padx=20, pady=(0, 4))
        self.fix_dolphin = tk.BooleanVar(value=False)
        self.dolphin_cb_widget = tk.Checkbutton(
            dolphin_frame, text="",
            variable=self.fix_dolphin,
            font=("Arial", 10, "bold"), fg="#005A8E", bg="#E8F4FD",
            wraplength=880,
            command=self._on_dolphin_toggle,
        )
        self.dolphin_cb_widget.pack(side=tk.LEFT)

        # ── Add-extension toggle ───────────────────────────────────────────
        addext_frame = tk.Frame(root, bg="#F0FFF0", pady=6, padx=10,
                                relief=tk.GROOVE, bd=1)
        addext_frame.pack(fill=tk.X, padx=20, pady=(0, 4))
        self.add_ext_enabled = tk.BooleanVar(value=False)
        self.addext_cb_widget = tk.Checkbutton(
            addext_frame, text="",
            variable=self.add_ext_enabled,
            font=("Arial", 10, "bold"), fg="#1A6B1A", bg="#F0FFF0",
            wraplength=880,
            command=self._on_addext_toggle,
        )
        self.addext_cb_widget.pack(side=tk.LEFT)
        self.add_ext_entry = tk.Entry(addext_frame, font=("Arial", 11),
                                      width=10, state=tk.DISABLED,
                                      disabledbackground="#D8D8D8")
        self.add_ext_entry.pack(side=tk.LEFT, padx=(6, 2))
        self.add_ext_entry.insert(0, ".png")
        self.add_ext_entry.bind("<FocusOut>", lambda e: self._rescan())
        self.add_ext_entry.bind("<Return>",   lambda e: self._rescan())
        self.lbl_addext_hint = tk.Label(addext_frame, text="",
                 font=("Arial", 9), fg="gray", bg="#F0FFF0")
        self.lbl_addext_hint.pack(side=tk.LEFT, padx=4)

        # ── Substring input ────────────────────────────────────────────────
        input_frame = tk.Frame(root)
        input_frame.pack(pady=6)
        self.lbl_substr = tk.Label(input_frame, text="",
                 font=("Arial", 11, "bold"))
        self.lbl_substr.pack(side=tk.LEFT, padx=5)
        self.char_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
        self.char_entry.pack(side=tk.LEFT, padx=5)
        self.char_entry.insert(0, "[]")
        self.lbl_substr_hint = tk.Label(input_frame, text="",
                 font=("Arial", 9), fg="gray")
        self.lbl_substr_hint.pack(side=tk.LEFT, padx=5)

        # ── Case sensitivity ───────────────────────────────────────────────
        self.case_sensitive = tk.BooleanVar(value=True)
        case_frame = tk.Frame(root)
        case_frame.pack(pady=3)
        self.case_cb = tk.Checkbutton(case_frame, text="",
                       variable=self.case_sensitive,
                       font=("Arial", 11, "bold"), fg="blue")
        self.case_cb.pack()

        # ── Buttons ────────────────────────────────────────────────────────
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=8)
        self.btn_folder = tk.Button(btn_frame, text="",
                  command=self.select_folder,
                  bg="#007ACC", fg="white", padx=20, pady=8,
                  font=("Arial", 10, "bold"))
        self.btn_folder.pack(side=tk.LEFT, padx=5)
        self.btn_file = tk.Button(btn_frame, text="",
                  command=self.select_file,
                  bg="#17A2B8", fg="white", padx=20, pady=8,
                  font=("Arial", 10, "bold"))
        self.btn_file.pack(side=tk.LEFT, padx=5)
        self.btn_rename = tk.Button(btn_frame, text="",
                  command=self.rename_files,
                  bg="#DC3545", fg="white", padx=20, pady=8,
                  font=("Arial", 10, "bold"))
        self.btn_rename.pack(side=tk.LEFT, padx=5)

        # ── File list ──────────────────────────────────────────────────────
        self.lbl_list = tk.Label(root, text="", font=("Arial", 10, "bold"))
        self.lbl_list.pack()
        list_frame = tk.Frame(root)
        list_frame.pack(pady=6, padx=20, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set,
                                       font=("Monospace", 9), selectmode=tk.SINGLE)
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.file_listbox.yview)

        # ── Status ─────────────────────────────────────────────────────────
        self.status = tk.Label(root, text="",
                              font=("Arial", 11), fg="blue", wraplength=880)
        self.status.pack(pady=(4, 0))

        # ── Credits ────────────────────────────────────────────────────────
        self.lbl_credits = tk.Label(root, text="",
                                    font=("Arial", 8), fg="#999999")
        self.lbl_credits.pack(pady=(2, 6))

    # -----------------------------------------------------------------------
    # Language
    # -----------------------------------------------------------------------

    def _t(self, key):
        """Return translated string for current language."""
        return STRINGS[self.lang][key]

    def _toggle_lang(self):
        self.lang = "pt" if self.lang == "en" else "en"
        self._apply_lang()

    def _apply_lang(self):
        """Re-label every widget and update window title."""
        t = self._t
        self.root.title(t("window_title"))
        self.lang_btn.config(text=t("lang_btn"))
        self.lbl_warn1.config(text=t("warn1"))
        self.lbl_warn2.config(text=t("warn2"))
        self.lbl_warn3.config(text=t("warn3"))
        self.lbl_title.config(text=t("app_title"))
        self.dolphin_cb_widget.config(text=t("dolphin_cb"))
        self.addext_cb_widget.config(text=t("addext_cb"))
        self.lbl_addext_hint.config(text=t("addext_hint"))
        self.lbl_substr.config(text=t("substr_label"))
        self.lbl_substr_hint.config(text=t("substr_hint"))
        self.case_cb.config(text=t("case_cb"))
        self.btn_folder.config(text=t("btn_folder"))
        self.btn_file.config(text=t("btn_file"))
        self.btn_rename.config(text=t("btn_rename"))
        self.lbl_list.config(text=t("list_label"))
        self.lbl_credits.config(text=t("credits"))
        # Re-apply status only if it's still the init message
        current = self.status.cget("text")
        if current in (STRINGS["en"]["status_init"], STRINGS["pt"]["status_init"]):
            self.status.config(text=t("status_init"))

    # -----------------------------------------------------------------------
    # Mode / mutual-exclusion logic
    # -----------------------------------------------------------------------

    def _on_dolphin_toggle(self):
        if self.fix_dolphin.get():
            self.add_ext_enabled.set(False)
        self._update_mode()

    def _on_addext_toggle(self):
        if self.add_ext_enabled.get():
            self.fix_dolphin.set(False)
        self._update_mode()

    def _update_mode(self):
        either_on = self.fix_dolphin.get() or self.add_ext_enabled.get()
        if either_on:
            self.char_entry.config(state=tk.DISABLED,
                                   disabledbackground="#D8D8D8",
                                   disabledforeground="#888888")
            self.case_cb.config(state=tk.DISABLED)
        else:
            self.char_entry.config(state=tk.NORMAL, bg="white", fg="black")
            self.case_cb.config(state=tk.NORMAL)
        if self.add_ext_enabled.get():
            self.add_ext_entry.config(state=tk.NORMAL, bg="white")
        else:
            self.add_ext_entry.config(state=tk.DISABLED,
                                      disabledbackground="#D8D8D8")
        self._rescan()

    def _rescan(self):
        if self.base_folder:
            self.scan_files()

    # -----------------------------------------------------------------------
    # Core logic
    # -----------------------------------------------------------------------

    def _get_add_ext(self):
        if not self.add_ext_enabled.get():
            return ""
        return normalise_extension(self.add_ext_entry.get())

    def _build_entry(self, full_path, old_name):
        substring = self.char_entry.get()
        add_ext   = self._get_add_ext()

        after_dolphin = fix_dolphin_duplicate(old_name) if self.fix_dolphin.get() else old_name

        if substring:
            if self.case_sensitive.get():
                after_sub = after_dolphin.replace(substring, "")
            else:
                pat = re.compile(re.escape(substring), re.IGNORECASE)
                after_sub = pat.sub("", after_dolphin)
        else:
            after_sub = after_dolphin

        if add_ext and has_no_extension(after_sub):
            new_name = after_sub + add_ext
        else:
            new_name = after_sub

        if new_name == old_name:
            return None
        return (full_path, old_name, new_name)

    # -----------------------------------------------------------------------
    # Actions
    # -----------------------------------------------------------------------

    def select_folder(self):
        folder = filedialog.askdirectory(title=self._t("btn_folder"))
        if not folder:
            return
        self.base_folder = folder
        self.status.config(
            text=self._t("status_scanning").format(folder=folder), fg="blue")
        self.scan_files()

    def select_file(self):
        file_path = filedialog.askopenfilename(title=self._t("btn_file"))
        if not file_path:
            return
        self.base_folder = None
        self.files = []
        self.file_listbox.delete(0, tk.END)

        old_name = os.path.basename(file_path)
        entry = self._build_entry(file_path, old_name)

        if entry:
            self.files.append(entry)
            _, old, new = entry
            self.file_listbox.insert(tk.END, f"{old}  ->  {new}")
            self.status.config(text=self._t("status_found1"), fg="blue")
        else:
            self.status.config(text=self._t("status_no_change"), fg="green")

    def scan_files(self):
        if not self.base_folder:
            messagebox.showwarning(self._t("warn_no_folder"),
                                   self._t("warn_no_folder_msg"))
            return

        add_ext = self._get_add_ext()
        if self.add_ext_enabled.get() and not add_ext:
            messagebox.showwarning(self._t("warn_no_ext"),
                                   self._t("warn_no_ext_msg"))
            return

        self.files = []
        self.file_listbox.delete(0, tk.END)
        found_count = 0

        try:
            for file in sorted(os.listdir(self.base_folder)):
                full_path = os.path.join(self.base_folder, file)
                if not os.path.isfile(full_path):
                    continue
                entry = self._build_entry(full_path, file)
                if entry:
                    self.files.append(entry)
                    _, old, new = entry
                    self.file_listbox.insert(tk.END, f"{old}  ->  {new}")
                    found_count += 1
        except Exception as e:
            messagebox.showerror("Error", self._t("err_scan").format(e=e))
            return

        if found_count == 0:
            self.status.config(text=self._t("status_none"), fg="green")
        else:
            self.status.config(
                text=self._t("status_found").format(n=found_count), fg="blue")

    def rename_files(self):
        if not self.files:
            messagebox.showwarning(self._t("warn_no_files"),
                                   self._t("warn_no_files_msg"))
            return

        substring = self.char_entry.get()
        add_ext   = self._get_add_ext()

        # Extension-change warning (only for files that already had an extension)
        ext_changes = [
            (old, new) for _, old, new in self.files
            if extension_changed(old, new)
            and not has_no_extension(fix_dolphin_duplicate(old))
        ]
        if ext_changes:
            sample = "\n".join(
                f"  {old}  ->  {new}" for old, new in ext_changes[:8])
            if len(ext_changes) > 8:
                sample += "\n" + self._t("extchg_more").format(
                    n=len(ext_changes) - 8)
            proceed = messagebox.askyesno(
                self._t("extchg_title"),
                self._t("extchg_body").format(
                    n=len(ext_changes), sample=sample),
                icon="warning",
            )
            if not proceed:
                return

        # Final confirmation
        notes = []
        if substring:
            notes.append(self._t("note_substr").format(s=substring))
        if self.fix_dolphin.get():
            notes.append(self._t("note_dolphin"))
        if add_ext:
            ext_targets = [old for _, old, _ in self.files
                           if has_no_extension(fix_dolphin_duplicate(old))]
            notes.append(self._t("note_addext").format(
                ext=add_ext, n=len(ext_targets)))
        notes_text = "\n".join(f"  - {n}" for n in notes)

        confirm = messagebox.askyesno(
            self._t("confirm_title"),
            self._t("confirm_body").format(
                n=len(self.files), notes=notes_text),
        )
        if not confirm:
            return

        success = 0
        failed  = 0
        errors  = []

        for full_path, old_name, new_name in self.files:
            try:
                directory = os.path.dirname(full_path)
                if not new_name.strip():
                    errors.append(self._t("err_empty").format(f=old_name))
                    failed += 1
                    continue
                final_path, _ = safe_target_path(directory, new_name)
                os.rename(full_path, final_path)
                success += 1
            except Exception as e:
                errors.append(f"{old_name}: {str(e)}")
                failed += 1

        result = self._t("result_ok").format(n=success)
        if failed > 0:
            result += self._t("result_fail").format(n=failed)
            if errors:
                result += self._t("result_errors") + "\n".join(errors[:10])

        messagebox.showinfo(self._t("result_title"), result)
        self.status.config(
            text=self._t("status_done").format(ok=success, fail=failed),
            fg="green")

        self.files = []
        self.file_listbox.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = CustomCharacterRemover(root)
    root.mainloop()
