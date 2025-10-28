# User Manual | Manual do Usuário

## 📖 Language | Idioma

- [English](#english)
- [Português (Brasil)](#português-brasil)

---

<a name="english"></a>
## 🇺🇸 English

### Quick Start

#### Installation

**Python:** `python filename-character-remover-z.py`

**Windows Executable:** Just double-click the `.exe` file

**Build Executable:**
```bash
pip install pyinstaller
pyinstaller --onefile --windowed filename-character-remover-z.py
```

### How to Use

1. **Enter characters to remove** (e.g., `[]`, `abc123`, `@#$`)
2. Click **"Select Folder"**
3. Click **"Scan Files"** to find matching files
4. Click **"Preview Changes"** to verify
5. **Uncheck "TEST MODE"**
6. Click **"RENAME FILES"**

### Examples

#### Remove brackets
- Input: `[]`
- `photo[1].jpg` → `photo1.jpg`

#### Remove multiple characters
- Input: `[]()-_`
- `file[test]_01.txt` → `filetest01.txt`

#### Remove numbers
- Input: `123`
- `report-2023.pdf` → `report-0.pdf`

#### Remove letters
- Input: `abc`
- `backup_abc.zip` → `bckup_.zip`

### Interface Overview

| Element | Description |
|---------|-------------|
| **Yellow Warning Banner** | Reminds you files are only renamed, never modified |
| **Character Input** | Type any characters to remove |
| **TEST MODE** (checkbox) | Prevents accidental changes - keep ON until ready |
| **Select Folder** (Blue) | Choose directory |
| **Scan Files** (Teal) | Find files with those characters |
| **Preview Changes** (Orange) | See what will happen |
| **RENAME FILES** (Red) | Execute the renaming |
| **File List** | Shows `old_name → new_name` for each file |
| **Status Bar** | Progress and results |

### Safety Features

✅ **Test Mode** - Default ON, prevents accidents  
✅ **Preview** - See changes before applying  
✅ **Only uses os.rename()** - Cannot corrupt file contents  
✅ **Conflict detection** - Won't overwrite existing files  
✅ **Multiple confirmations** - You must explicitly approve

### Troubleshooting

#### "No files found"
- Check you entered the right characters
- Verify you selected the correct folder

#### "Target file already exists"
- A file with the new name already exists
- Rename the existing file first or choose different characters

#### "New filename would be empty"
- You're removing all characters from the filename
- Don't remove characters that make up the entire name

#### "Permission denied"
- Close programs using the files
- Run as administrator
- Remove read-only flag from files

### FAQ

**Q: Will this corrupt my files?**  
A: No. It only renames files using `os.rename()`. File contents are never touched.

**Q: Can I undo?**  
A: No automatic undo. Make backups before using or restore from Windows Previous Versions.

**Q: Does it scan subfolders?**  
A: Yes, recursively scans all subfolders.

**Q: What characters can I remove?**  
A: Any - letters, numbers, symbols, spaces.

**Q: Works on Mac/Linux?**  
A: Yes, cross-platform.

### Best Practices

✅ Always backup important files first  
✅ Test on copies before using on originals  
✅ Use Preview before renaming  
✅ Keep Test Mode ON until you're sure  
✅ Close programs using the files

---

<a name="português-brasil"></a>
## 🇧🇷 Português (Brasil)

### Início Rápido

#### Instalação

**Python:** `python filename-character-remover-z.py`

**Executável Windows:** Apenas clique duas vezes no arquivo `.exe`

**Construir Executável:**
```bash
pip install pyinstaller
pyinstaller --onefile --windowed filename-character-remover-z.py
```

### Como Usar

1. **Digite os caracteres a remover** (ex: `[]`, `abc123`, `@#$`)
2. Clique em **"Select Folder"**
3. Clique em **"Scan Files"** para encontrar arquivos correspondentes
4. Clique em **"Preview Changes"** para verificar
5. **Desmarque "TEST MODE"**
6. Clique em **"RENAME FILES"**

### Exemplos

#### Remover colchetes
- Entrada: `[]`
- `foto[1].jpg` → `foto1.jpg`

#### Remover múltiplos caracteres
- Entrada: `[]()-_`
- `arquivo[teste]_01.txt` → `arquivoteste01.txt`

#### Remover números
- Entrada: `123`
- `relatorio-2023.pdf` → `relatorio-0.pdf`

#### Remover letras
- Entrada: `abc`
- `backup_abc.zip` → `bkup_.zip`

### Visão Geral da Interface

| Elemento | Descrição |
|----------|-----------|
| **Banner Amarelo de Aviso** | Lembra que arquivos são apenas renomeados, nunca modificados |
| **Entrada de Caracteres** | Digite quaisquer caracteres para remover |
| **TEST MODE** (checkbox) | Previne mudanças acidentais - mantenha LIGADO até estar pronto |
| **Select Folder** (Azul) | Escolha o diretório |
| **Scan Files** (Verde-azulado) | Encontra arquivos com esses caracteres |
| **Preview Changes** (Laranja) | Veja o que vai acontecer |
| **RENAME FILES** (Vermelho) | Executa a renomeação |
| **Lista de Arquivos** | Mostra `nome_antigo → nome_novo` para cada arquivo |
| **Barra de Status** | Progresso e resultados |

### Recursos de Segurança

✅ **Modo de Teste** - Padrão LIGADO, previne acidentes  
✅ **Pré-visualização** - Veja mudanças antes de aplicar  
✅ **Usa apenas os.rename()** - Não pode corromper conteúdo de arquivos  
✅ **Detecção de conflitos** - Não sobrescreve arquivos existentes  
✅ **Múltiplas confirmações** - Você deve aprovar explicitamente

### Solução de Problemas

#### "No files found" (Nenhum arquivo encontrado)
- Verifique se digitou os caracteres corretos
- Verifique se selecionou a pasta correta

#### "Target file already exists" (Arquivo de destino já existe)
- Um arquivo com o novo nome já existe
- Renomeie o arquivo existente primeiro ou escolha caracteres diferentes

#### "New filename would be empty" (Novo nome de arquivo seria vazio)
- Você está removendo todos os caracteres do nome do arquivo
- Não remova caracteres que compõem o nome inteiro

#### "Permission denied" (Permissão negada)
- Feche programas usando os arquivos
- Execute como administrador
- Remova a flag de somente leitura dos arquivos

### Perguntas Frequentes

**P: Isso vai corromper meus arquivos?**  
R: Não. Apenas renomeia arquivos usando `os.rename()`. O conteúdo dos arquivos nunca é tocado.

**P: Posso desfazer?**  
R: Não há desfazer automático. Faça backups antes de usar ou restaure das Versões Anteriores do Windows.

**P: Varre subpastas?**  
R: Sim, varre recursivamente todas as subpastas.

**P: Quais caracteres posso remover?**  
R: Quaisquer - letras, números, símbolos, espaços.

**P: Funciona no Mac/Linux?**  
R: Sim, é multiplataforma.

### Melhores Práticas

✅ Sempre faça backup de arquivos importantes primeiro  
✅ Teste em cópias antes de usar nos originais  
✅ Use Pré-visualização antes de renomear  
✅ Mantenha o Modo de Teste LIGADO até ter certeza  
✅ Feche programas usando os arquivos

---

<div align="center">

**Important | Importante:** This tool ONLY renames files. It does NOT modify file contents.

Esta ferramenta APENAS renomeia arquivos. NÃO modifica o conteúdo dos arquivos.

</div>