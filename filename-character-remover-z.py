import tkinter as tk
from tkinter import filedialog, messagebox
import os
import re

class CustomCharacterRemover:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Character Remover - FILENAMES ONLY")
        self.root.geometry("900x650")
        self.files = []
        self.base_folder = None
        
        # BIG WARNING
        warning_frame = tk.Frame(root, bg="yellow", pady=10)
        warning_frame.pack(fill=tk.X)
        
        tk.Label(warning_frame, text="⚠️ THIS TOOL ONLY RENAMES FILENAMES ⚠️", 
                font=("Arial", 18, "bold"), bg="yellow", fg="red").pack()
        tk.Label(warning_frame, text="IT DOES NOT OPEN, READ, OR MODIFY FILE CONTENTS", 
                font=("Arial", 12), bg="yellow", fg="black").pack()
        tk.Label(warning_frame, text="IT ONLY USES os.rename() - THE SAFEST RENAME METHOD", 
                font=("Arial", 10), bg="yellow", fg="black").pack()
        
        # Title
        title = tk.Label(root, text="Remove Custom Characters from Filenames", font=("Arial", 14, "bold"))
        title.pack(pady=10)
        
        # Character input section
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Characters to remove:", font=("Arial", 11, "bold")).pack(side=tk.LEFT, padx=5)
        self.char_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
        self.char_entry.pack(side=tk.LEFT, padx=5)
        self.char_entry.insert(0, "[]")  # Default value
        
        tk.Label(input_frame, text="← Enter any characters: letters, numbers, symbols (e.g., []abc123 )", 
                font=("Arial", 9), fg="gray").pack(side=tk.LEFT, padx=5)
        
        # Test mode checkbox
        self.test_mode = tk.BooleanVar(value=True)
        test_frame = tk.Frame(root)
        test_frame.pack(pady=5)
        tk.Checkbutton(test_frame, text="TEST MODE (shows what will happen, doesn't rename)", 
                      variable=self.test_mode, font=("Arial", 11, "bold"), 
                      fg="green").pack()
        
        # Buttons frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="1. Select Folder", command=self.select_folder, 
                 bg="#007ACC", fg="white", padx=20, pady=8, font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="2. Scan Files", command=self.scan_files,
                 bg="#17A2B8", fg="white", padx=20, pady=8, font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="3. Preview Changes", command=self.preview_changes,
                 bg="#FFA500", fg="white", padx=20, pady=8, font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="4. RENAME FILES", command=self.rename_files,
                 bg="#DC3545", fg="white", padx=20, pady=8, font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        
        # File list
        list_label = tk.Label(root, text="Files that will be renamed:", font=("Arial", 10, "bold"))
        list_label.pack()
        
        list_frame = tk.Frame(root)
        list_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.file_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, 
                                       font=("Consolas", 9), selectmode=tk.SINGLE)
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.file_listbox.yview)
        
        # Status label
        self.status = tk.Label(root, text="Step 1: Enter characters to remove, then select a folder", 
                              font=("Arial", 11), fg="blue", wraplength=800)
        self.status.pack(pady=10)
        
    def select_folder(self):
        folder = filedialog.askdirectory(title="Select Folder")
        if not folder:
            return
            
        self.base_folder = folder
        self.status.config(
            text=f"Selected: {folder}\nClick 'Scan Files' to find files with those characters.",
            fg="blue"
        )
    
    def scan_files(self):
        if not self.base_folder:
            messagebox.showwarning("No Folder", "Please select a folder first")
            return
        
        chars_to_remove = self.char_entry.get()
        if not chars_to_remove:
            messagebox.showwarning("No Characters", "Please enter characters to remove")
            return
        
        self.files = []
        self.file_listbox.delete(0, tk.END)
        
        # Escape special regex characters for safety
        chars_pattern = re.escape(chars_to_remove)
        
        # Scan for files with those characters
        found_count = 0
        for root, dirs, files in os.walk(self.base_folder):
            for file in files:
                # Check if any of the characters are in the filename
                if any(char in file for char in chars_to_remove):
                    full_path = os.path.join(root, file)
                    # Remove all specified characters
                    new_name = file
                    for char in chars_to_remove:
                        new_name = new_name.replace(char, '')
                    
                    # Only add if name actually changes
                    if new_name != file:
                        self.files.append((full_path, file, new_name))
                        self.file_listbox.insert(tk.END, f"{file}  →  {new_name}")
                        found_count += 1
        
        if found_count == 0:
            self.status.config(
                text=f"✅ No files found with characters: {chars_to_remove}", 
                fg="green"
            )
            messagebox.showinfo("No Files", f"No files with those characters were found.")
        else:
            self.status.config(
                text=f"Found {found_count} files to rename. Click 'Preview Changes' to verify.",
                fg="blue"
            )
    
    def preview_changes(self):
        if not self.files:
            messagebox.showwarning("No Files", "Please scan for files first")
            return
        
        chars_to_remove = self.char_entry.get()
        preview_msg = f"PREVIEW: Removing characters: {chars_to_remove}\n"
        preview_msg += f"This will rename {len(self.files)} files\n\n"
        preview_msg += "Examples (first 10):\n"
        preview_msg += "="*70 + "\n"
        
        for i, (full_path, old_name, new_name) in enumerate(self.files[:10]):
            preview_msg += f"\n{old_name}\n  → {new_name}\n"
        
        if len(self.files) > 10:
            preview_msg += f"\n... and {len(self.files) - 10} more files\n"
        
        preview_msg += "\n" + "="*70 + "\n"
        preview_msg += "\n⚠️ THIS ONLY RENAMES FILES - NO FILE CONTENTS ARE TOUCHED\n"
        preview_msg += "Method used: os.rename() - safest Python rename function\n"
        
        messagebox.showinfo("Preview", preview_msg)
        self.status.config(
            text=f"Preview ready! Uncheck 'TEST MODE' and click 'RENAME FILES' to proceed.",
            fg="orange"
        )
    
    def rename_files(self):
        if not self.files:
            messagebox.showwarning("No Files", "Please scan for files first")
            return
        
        if self.test_mode.get():
            messagebox.showinfo(
                "Test Mode Active",
                "TEST MODE is ON - no files will be renamed.\n\n"
                "Uncheck 'TEST MODE' to actually rename files."
            )
            return
        
        chars_to_remove = self.char_entry.get()
        
        # Final confirmation
        confirm = messagebox.askyesno(
            "FINAL CONFIRMATION",
            f"This will RENAME {len(self.files)} files.\n"
            f"Removing characters: {chars_to_remove}\n\n"
            "⚠️ Make sure you have BACKUPS first!\n\n"
            "This action ONLY renames files - it does NOT modify file contents.\n\n"
            "Continue?"
        )
        
        if not confirm:
            return
        
        success = 0
        failed = 0
        errors = []
        
        for full_path, old_name, new_name in self.files:
            try:
                directory = os.path.dirname(full_path)
                new_path = os.path.join(directory, new_name)
                
                # Skip if new name is empty or only whitespace
                if not new_name.strip():
                    errors.append(f"{old_name}: New filename would be empty")
                    failed += 1
                    continue
                
                # Check if target exists
                if os.path.exists(new_path):
                    errors.append(f"{old_name}: Target already exists")
                    failed += 1
                    continue
                
                # ONLY RENAME - NEVER OPEN THE FILE
                # os.rename() only changes the filename entry in the filesystem
                # It does NOT read or modify the file contents
                os.rename(full_path, new_path)
                success += 1
                
            except Exception as e:
                errors.append(f"{old_name}: {str(e)}")
                failed += 1
        
        # Show results
        result = f"✅ Successfully renamed {success} files!"
        if failed > 0:
            result += f"\n❌ Failed: {failed} files"
            if errors:
                result += "\n\nErrors (first 10):\n" + "\n".join(errors[:10])
        
        messagebox.showinfo("Complete", result)
        self.status.config(text=f"Done! Renamed {success} files, Failed: {failed}", fg="green")
        
        # Clear the list
        self.files = []
        self.file_listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomCharacterRemover(root)
    root.mainloop()