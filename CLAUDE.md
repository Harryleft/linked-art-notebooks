# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Chinese translation project for Linked Art documentation with interactive Jupyter Notebook versions. The project is **100% complete** with 187 translated documents and 257 generated Notebooks.

**Project Status**: Translation complete, Jupyter Notebooks generated
- Chinese translations: `docs-zh/` (187 files)
- Chinese Notebooks: `notebooks/` (70 files - model + api)
- English Notebooks: `notebooks-en/` (187 files - all docs)
- Conversion tool: `scripts/md_to_ipynb_converter.py`

## Project Structure

```
linked-art-docs-zh/
├── docs/              # Original English documentation (preserve - don't modify)
├── docs-zh/           # Chinese translations (complete)
├── notebooks/         # Chinese Jupyter Notebooks (complete)
├── notebooks-en/      # English Jupyter Notebooks (complete)
├── scripts/           # Conversion utilities
├── 术语对照表.md      # Chinese terminology standard (reference for new translations)
└── 翻译任务计划.md    # Translation tracking (archived - project complete)
```

## Jupyter Notebook Conversion

### Conversion Tool

**Location**: `scripts/md_to_ipynb_converter.py`

**Key Functions**:
- `convert_file(md_path, ipynb_path)` - Convert single Markdown to Notebook
- `convert_directory(src_dir, dst_dir)` - Batch convert directory

**Usage**:
```python
# Single file
python -c "from scripts.md_to_ipynb_converter import convert_file; \
    convert_file('docs/model/index.md', 'notebooks/model/index.ipynb')"

# Batch directory
python -c "from scripts.md_to_ipynb_converter import convert_directory; \
    convert_directory('docs/model', 'notebooks/model')"
```

### Conversion Architecture

The converter processes Markdown files with the following pipeline:

1. **Parse YAML front matter** (`title`, `up_href`, `up_label`)
2. **Split content by code fences** - Identify ```crom blocks vs other content
3. **Enhance crom code blocks**:
   - Auto-add `from cromulent import model, vocab` if missing
   - Detect main variable (e.g., `top`, `obj`) via regex pattern matching
   - Append `print(model.factory.toString(var, compact=False))` for output
4. **Create Jupyter structure** using `nbformat.v4` API
5. **Write as JSON** - Ensures proper source format (array of lines without trailing \n)

**Critical Implementation Detail**:
- The source field must be a string (not array) with embedded `\n` characters
- nbformat 4.5+ accepts this format and displays code correctly
- Using `json.dump()` instead of `nbformat.write()` to control format

### Crom Code Enhancement

The `enhance_crom_code()` function modifies crom code blocks:

```python
# Original crom code:
top = model.HumanMadeObject(ident="example", label="Example")
prod = model.Production()

# Enhanced output:
# 导入 cromulent 库
from cromulent import model, vocab

top = model.HumanMadeObject(ident="example", label="Example")
prod = model.Production()

# 展示生成的 JSON-LD
print(model.factory.toString(top, compact=False))
```

## Translation Principles

When adding new translations or updating existing ones:

### Core Principles (from 术语对照表.md)

1. **意境相通 > 字面对应** - Capture the spirit, not just the words
2. **引发共鸣 > 准确传达** - Evoke resonance in the target audience
3. **文化重构 > 机械转换** - Reconstruct culturally, don't just translate
4. **余味悠长 > 一目了然** - Leave room for interpretation

### Required Resources

**Always reference** `术语对照表.md` before translating:
- 11 categories of professional terminology
- Translation principles and usage guidelines
- Selection rationale for professional terms

### Critical Terminology

| English | Chinese |
|---------|---------|
| Linked Art | Linked Art (keep original) |
| Cultural Heritage | 文化遗产 |
| HumanMadeObject | 人工制品 |
| Provenance | 流传历史 |
| Collections | 集藏 |
| Actors | 行动者 |
| Interoperability | 互操作性 |
| Production | 创作/生产 |
| Acquisition | 获得/收藏 |

### File Handling Rules

- **Never modify** files in `docs/` (original English source)
- **Always preserve** YAML front matter in translated files
- **Maintain same file names** in `docs-zh/` as in `docs/` for internal links
- **Keep code blocks in English** - Only translate explanatory text
- **Translate link text** but preserve file paths

## Running Notebooks

### Environment Setup

```bash
pip install cromulent
pip install jupyter
```

### Entry Points

- **Chinese**: `notebooks/00-导航索引.ipynb`
- **English**: `notebooks-en/00-导航索引.ipynb`

### Code Execution

Every Notebook automatically includes:
```python
from cromulent import model, vocab
import json
model.factory.base_url = 'http://test.com/museum/'
```

## Original Project References

- **Official Site**: https://linked.art/
- **Original Repository**: https://github.com/linked-art/linked.art
- **License**: CC BY 4.0
- **Maintainers**: Linked Art Editorial Board
