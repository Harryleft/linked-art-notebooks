#!/usr/bin/env python3
"""
Markdown 到 Jupyter Notebook 转换器
专门用于将 Linked Art 中文文档转换为可交互的 Jupyter Notebook

功能：
- 解析 Markdown 文件（包括 YAML front matter）
- 识别 crom 代码块并自动增强（添加导入和 JSON 输出）
- 保持文档结构和格式
"""

import re
from pathlib import Path
from typing import List, Tuple, Any


def parse_markdown(content: str) -> dict:
    """
    解析 Markdown 文件内容

    Args:
        content: Markdown 文件内容

    Returns:
        包含 front_matter 和 body 的字典
    """
    result = {
        "front_matter": {},
        "body": content
    }

    # 检测并解析 YAML front matter
    front_matter_pattern = r'^---\n(.*?)\n---\n'
    match = re.match(front_matter_pattern, content, re.DOTALL)

    if match:
        front_matter_text = match.group(1)
        result["body"] = content[match.end():]
        # 解析 YAML 键值对
        for line in front_matter_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                result["front_matter"][key.strip()] = value.strip()

    return result


def detect_crom_variable(code: str) -> str:
    """
    检测 crom 代码块中的主变量名（通常是 top）

    Args:
        code: crom 代码

    Returns:
        检测到的主变量名，如果未检测到则返回 None
    """
    # 查找形如 "top = model." 或 "top = vocab." 的模式
    patterns = [
        r'(\w+)\s*=\s*model\.',
        r'(\w+)\s*=\s*vocab\.',
    ]

    for pattern in patterns:
        matches = re.findall(pattern, code)
        if matches:
            # 返回最常出现的变量名
            from collections import Counter
            return Counter(matches).most_common(1)[0][0]

    return None


def enhance_crom_code(code: str, add_json_output: bool = True) -> str:
    """
    增强 crom 代码块，添加必要的导入和输出

    Args:
        code: 原始 crom 代码
        add_json_output: 是否添加 JSON 输出

    Returns:
        增强后的代码（单个字符串，包含换行符）
    """
    lines = []

    # 检查是否需要添加导入
    has_model_import = 'from cromulent import' in code or 'import cromulent' in code

    # 添加导入（在开头）
    if not has_model_import:
        lines.append("# 导入 cromulent 库")
        lines.append("from cromulent import model, vocab")
        lines.append("")

    # 添加原始代码
    lines.extend(code.split('\n'))

    # 添加输出
    if add_json_output:
        main_var = detect_crom_variable(code)
        if main_var:
            lines.append("")
            lines.append("# 展示生成的 JSON-LD")
            lines.append(f"print(model.factory.toString({main_var}, compact=False))")

    return '\n'.join(lines)


def markdown_to_cells(content: str, add_json_output: bool = True) -> List[Tuple[str, str]]:
    """
    从 Markdown 内容创建 Notebook 单元格

    Args:
        content: Markdown 内容（不含 front matter）
        add_json_output: 是否在 crom 代码块后添加 JSON 输出

    Returns:
        单元格列表，每个元素是 (cell_type, content) 元组
    """
    cells = []

    # 在开头添加环境设置单元格
    setup_code = """# 环境设置
from cromulent import model, vocab

# 设置 base_url 以获得更清晰的输出
model.factory.base_url = 'http://test.com/museum/'
"""
    cells.append(('code', setup_code))

    # 使用正则表达式分割代码块
    # 匹配 ```语言 ... ``` 格式的代码块
    fence_pattern = r'```(\w*)\n(.*?)```'
    parts = []
    last_end = 0

    for match in re.finditer(fence_pattern, content, re.DOTALL):
        # 添加代码块前的文本
        if match.start() > last_end:
            text_before = content[last_end:match.start()]
            if text_before.strip():
                parts.append(('markdown', text_before))

        # 添加代码块
        lang = match.group(1)
        code = match.group(2)
        parts.append(('code', code, lang))
        last_end = match.end()

    # 添加剩余文本
    if last_end < len(content):
        remaining = content[last_end:]
        if remaining.strip():
            parts.append(('markdown', remaining))

    # 如果没有找到代码块，整个内容是 markdown
    if not parts:
        parts.append(('markdown', content))

    # 转换为 notebook 单元格
    for part in parts:
        if part[0] == 'markdown':
            cells.append(('markdown', part[1]))
        elif part[0] == 'code':
            _, code, lang = part

            # 处理 crom 代码块
            if lang == 'crom':
                enhanced_code = enhance_crom_code(code, add_json_output)
                cells.append(('code', enhanced_code))
            elif lang == 'python' or lang == '':
                cells.append(('code', code))
            else:
                # 其他语言的代码块转换为 markdown 显示
                md_code = f"```{lang}\n{code}\n```"
                cells.append(('markdown', md_code))

    return cells


def convert_file(md_path: str, ipynb_path: str, add_json_output: bool = True) -> None:
    """
    转换单个 Markdown 文件为 Notebook

    Args:
        md_path: 源 Markdown 文件路径
        ipynb_path: 目标 Notebook 文件路径
        add_json_output: 是否在 crom 代码块后添加 JSON 输出
    """
    import nbformat

    # 读取 Markdown 文件
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # 解析 Markdown
    parsed = parse_markdown(md_content)

    # 创建 Notebook 对象
    nb = nbformat.v4.new_notebook()

    # 添加标题单元格（包含 front matter 信息）
    title = parsed['front_matter'].get('title', 'Linked Art 文档')
    up_label = parsed['front_matter'].get('up_label', '')
    up_href = parsed['front_matter'].get('up_href', '')

    header_md = f"# {title}\n\n"
    if up_label and up_href:
        header_md += f"> **上级页面**: [{up_label}]({up_href})\n\n"
    header_md += "---\n\n"

    nb.cells.append(nbformat.v4.new_markdown_cell(header_md))

    # 添加内容单元格
    cells = markdown_to_cells(parsed['body'], add_json_output)
    for cell_type, cell_content in cells:
        if cell_type == 'markdown':
            nb.cells.append(nbformat.v4.new_markdown_cell(cell_content))
        else:  # code
            # 使用单个字符串作为 source（nbformat 4.5+ 支持）
            # 这样 Jupyter 会自动按行分割显示
            nb.cells.append(nbformat.v4.new_code_cell(cell_content))

    # 确保目标目录存在
    ipynb_file = Path(ipynb_path)
    ipynb_file.parent.mkdir(parents=True, exist_ok=True)

    # 写入 Notebook 文件 - 使用 JSON 而不是 nbformat.write()
    # nbformat.write() 会自动在每行末尾添加 \n
    # 我们直接使用 JSON 来控制格式
    import json
    with open(ipynb_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    print(f"已转换: {md_path} -> {ipynb_path}")


def convert_directory(src_dir: str, dst_dir: str, add_json_output: bool = True) -> None:
    """
    批量转换目录中的所有 Markdown 文件

    Args:
        src_dir: 源目录
        dst_dir: 目标目录
        add_json_output: 是否在 crom 代码块后添加 JSON 输出
    """
    src_path = Path(src_dir)
    dst_path = Path(dst_dir)

    for md_file in src_path.rglob('*.md'):
        # 计算相对路径
        rel_path = md_file.relative_to(src_path)
        # 更改扩展名为 .ipynb
        ipynb_file = dst_path / rel_path.with_suffix('.ipynb')

        convert_file(str(md_file), str(ipynb_file), add_json_output)


def main():
    """主函数 - 示例用法"""

    # 示例：转换单个文件
    convert_file(
        'docs-zh/model/object/production/index.md',
        'notebooks/model/object/production.ipynb'
    )

    # 示例：批量转换目录
    # convert_directory('docs-zh/model', 'notebooks/model')
    # convert_directory('docs-zh/api/1.0', 'notebooks/api/1.0')


if __name__ == '__main__':
    main()
