# Custom Character Remover | Removedor de Caracteres Personalizado

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

---

## 📖 Language | Idioma

- [English](#english)
- [Português (Brasil)](#português-brasil)

---

<a name="english"></a>
## 🇺🇸 English

### Overview

A safe and simple GUI tool to remove specific characters from filenames in bulk.

### ⚠️ Important Notice

**THIS TOOL ONLY RENAMES FILES - IT DOES NOT MODIFY FILE CONTENTS**

This application uses `os.rename()` which only changes filenames in the file system. Your file contents remain completely untouched and safe.

### ✨ Features

- 🎯 Remove any custom characters from filenames (letters, numbers, symbols)
- 👀 Preview changes before applying them
- 🔒 Test mode enabled by default for safety
- 📊 Recursive scanning of all subfolders
- ✅ Shows before/after preview for each file
- 🚫 Prevents overwriting existing files
- 📝 Detailed error reporting

### 🚀 Quick Start

#### Requirements

- Python 3.6 or higher
- tkinter (included with Python)

#### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/custom-character-remover.git
cd custom-character-remover
```

2. Run the application:
```bash
python filename-character-remover-z.py
```

#### Building Executable

To create a standalone executable:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed filename-character-remover-z.py
```

The executable will be in the `dist` folder.

### 📖 Usage

1. **Enter characters to remove** in the text field (e.g., `[]`, `abc123`, `@#$`)
2. Click **"Select Folder"** to choose the directory
3. Click **"Scan Files"** to find files with those characters
4. Click **"Preview Changes"** to see what will happen
5. Uncheck **"TEST MODE"** when ready
6. Click **"RENAME FILES"** to apply changes

### 💡 Examples

| Input | Before | After |
|-------|--------|-------|
| `[]` | `photo[1].jpg` | `photo1.jpg` |
| `[]()-_` | `file[test]_01.txt` | `filetest01.txt` |
| `123` | `report-2023.pdf` | `report-0.pdf` |
| `abc` | `backup_abc.zip` | `bkup_.zip` |

### 🛡️ Safety Features

- ✅ Test mode prevents accidental changes
- ✅ Preview shows exact changes before applying
- ✅ Multiple confirmation dialogs
- ✅ Never modifies file contents
- ✅ Checks for existing files to prevent overwrites
- ✅ Detailed error reporting

### 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

### ⚠️ Disclaimer

Always backup your files before performing bulk rename operations. While this tool is designed to be safe, unexpected issues can occur.

### 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

<a name="português-brasil"></a>
## 🇧🇷 Português (Brasil)

### Visão Geral

Uma ferramenta GUI segura e simples para remover caracteres específicos de nomes de arquivos em massa.

### ⚠️ Aviso Importante

**ESTA FERRAMENTA APENAS RENOMEIA ARQUIVOS - NÃO MODIFICA O CONTEÚDO DOS ARQUIVOS**

Esta aplicação usa `os.rename()` que apenas altera nomes de arquivos no sistema de arquivos. O conteúdo dos seus arquivos permanece completamente intocado e seguro.

### ✨ Recursos

- 🎯 Remove qualquer caractere personalizado dos nomes de arquivos (letras, números, símbolos)
- 👀 Pré-visualize mudanças antes de aplicá-las
- 🔒 Modo de teste ativado por padrão para segurança
- 📊 Varredura recursiva de todas as subpastas
- ✅ Mostra pré-visualização antes/depois para cada arquivo
- 🚫 Previne sobrescrita de arquivos existentes
- 📝 Relatório detalhado de erros

### 🚀 Início Rápido

#### Requisitos

- Python 3.6 ou superior
- tkinter (incluído com Python)

#### Instalação

1. Clone este repositório:
```bash
git clone https://github.com/yourusername/custom-character-remover.git
cd custom-character-remover
```

2. Execute a aplicação:
```bash
python filename-character-remover-z.py
```

#### Construindo Executável

Para criar um executável standalone:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed filename-character-remover-z.py
```

O executável estará na pasta `dist`.

### 📖 Uso

1. **Digite os caracteres a remover** no campo de texto (ex: `[]`, `abc123`, `@#$`)
2. Clique em **"Select Folder"** para escolher o diretório
3. Clique em **"Scan Files"** para encontrar arquivos com esses caracteres
4. Clique em **"Preview Changes"** para ver o que vai acontecer
5. Desmarque **"TEST MODE"** quando estiver pronto
6. Clique em **"RENAME FILES"** para aplicar as mudanças

### 💡 Exemplos

| Entrada | Antes | Depois |
|---------|-------|--------|
| `[]` | `foto[1].jpg` | `foto1.jpg` |
| `[]()-_` | `arquivo[teste]_01.txt` | `arquivoteste01.txt` |
| `123` | `relatorio-2023.pdf` | `relatorio-0.pdf` |
| `abc` | `backup_abc.zip` | `bkup_.zip` |

### 🛡️ Recursos de Segurança

- ✅ Modo de teste previne mudanças acidentais
- ✅ Pré-visualização mostra mudanças exatas antes de aplicar
- ✅ Múltiplos diálogos de confirmação
- ✅ Nunca modifica conteúdo de arquivos
- ✅ Verifica arquivos existentes para prevenir sobrescrita
- ✅ Relatório detalhado de erros

### 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se livre para enviar um Pull Request.

### 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

### ⚠️ Aviso Legal

Sempre faça backup dos seus arquivos antes de realizar operações de renomeação em massa. Embora esta ferramenta seja projetada para ser segura, problemas inesperados podem ocorrer.

### 📞 Suporte

Para problemas, questões ou sugestões, por favor abra uma issue no GitHub.

---

<div align="center">

Made with ❤️ for safe and easy file management

Feito com ❤️ para gerenciamento de arquivos seguro e fácil

</div>