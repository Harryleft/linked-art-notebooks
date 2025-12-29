# Linked Art 中文文档 - 可交互式学习环境

## 为什么需要这个项目？

想象一下，你正在为GLAM建立数字化档案系统。你需要记录：每件艺术品是谁创作的、何时何地完成、经历过哪些收藏者的流转、参加过哪些展览...如果把这些信息分散在不同的表格和数据库中，不仅难以维护，更无法与其他机构共享数据。

这就是 Linked Art 要解决的问题——它提供了一套**标准的数据模型**，让文化遗产信息的记录和共享变得简单。就像图书馆使用 ISBN 标准来标识书籍一样，Linked Art 让博物馆、美术馆、档案馆可以用同一种"语言"来描述他们的收藏。

## 这个项目提供了什么？

**1. 完整的中文翻译**
- 187 个文档的中文翻译，覆盖数据模型、API 规范、实施指南
- 所有翻译遵循博物馆学界和艺术史领域的专业术语标准

**2. 可交互的 Jupyter Notebook**
- 257 个 Notebook，包含所有代码示例
- 每个代码块都可以直接运行、修改、实验
- 自动显示生成的 JSON-LD 数据，直观理解数据结构

**3. 一键转换工具**
- 提供 Python 脚本，可随时将 Markdown 转换为 Notebook
- 支持批量转换，便于自定义学习材料

## 快速开始

### 1. 安装依赖

打开终端，执行以下命令：

```bash
# 安装 Python 依赖
pip install cromulent jupyter
```

**安装说明**：
- `cromulent` - Linked Art 的 Python 库，用于生成文化遗产数据
- `jupyter` - 交互式 Notebook 环境

### 2. 打开学习环境

根据你的偏好选择：

**中文版**：
```bash
jupyter lab notebooks
```
然后在浏览器中打开 `00-README.ipynb`

**英文版**：
```bash
jupyter lab notebooks-en
```

### 3. 运行第一个代码示例

打开任意 Notebook，你会看到类似这样的代码：

```python
# 环境设置（每个 Notebook 开头都有）
from cromulent import model, vocab

# 创建一件艺术品对象
artwork = model.HumanMadeObject(
    ident="painting/1",
    label="星空"
)

# 显示生成的 JSON 数据
print(model.factory.toString(artwork, compact=False))
```

运行后，你会看到结构化的 JSON 输出：

```json
{
  "@context": "https://linked.art/ns/v1/linked-art.json",
  "id": "http://test.com/museum/HumanMadeObject/painting/1",
  "type": "HumanMadeObject",
  "_label": "星空"
}
```

## 项目结构

```
linked-art-docs-zh/
├── docs/              # 原始英文文档
├── docs-zh/           # 中文翻译
├── notebooks/         # 中文版 Notebook
├── notebooks-en/      # 英文版 Notebook
├── scripts/           # 转换工具
└── 术语对照表.md       # 专业术语标准
```

## 核心概念速览

### 数据模型是什么？

数据模型定义了如何描述一个文化遗产对象。例如，描述一幅画作需要：

| 属性 | 说明 | Linked Art 术语 |
|------|------|-----------------|
| **创作** | 谁在何时何地创作了它 | Production |
| **材质** | 用什么材料制成 | Material |
| **尺寸** | 有多大 | Dimension |
| **流传** | 曾被谁收藏 | Provenance |
| **展览** | 参加过哪些展览 | Exhibition |

### 为什么选择 Linked Art？

- **标准化**：被 Getty、Smithsonian、Yale 等机构采用
- **可扩展**：可以记录从简单到复杂的各种信息
- **互操作**：数据可以在不同系统间无缝交换
- **免费开源**：遵循 CC BY 4.0 许可证

## 学习路径建议

### 初学者（推荐）

1. **从入门开始**：`notebooks/00-README.ipynb`
2. **理解核心概念**：`notebooks/model/index.ipynb`
3. **实践创建对象**：`notebooks/model/object/production.ipynb`

### 进阶用户

1. **深入数据模型**：`notebooks/model/provenance/index.ipynb`
2. **学习 API 使用**：`notebooks/api/1.0/endpoint/index.ipynb`
3. **构建自己的应用**：参考 `notebooks/cookbook/`

### 开发者

1. **阅读 API 文档**：`notebooks-en/api/1.0/index.ipynb`
2. **查看实现示例**：`notebooks-en/example/index.ipynb`
3. **使用转换工具**：参考 `scripts/md_to_ipynb_converter.py`

## 常见任务

### 创建一个新的艺术品记录

```python
from cromulent import model, vocab

# 创建对象
painting = model.HumanMadeObject(
    ident="mona-lisa",
    label="蒙娜丽莎"
)

# 添加创作信息
production = model.Production()
painting.produced_by = production

# 添加创作者
leonardo = model.Person(
    ident="leonardo-da-vinci",
    label="列奥纳多·达·芬奇"
)
production.carried_out_by = leonardo

# 查看结果
print(model.factory.toString(painting, compact=False))
```

### 转换你自己的 Markdown 文档

```python
# 安装必要依赖
pip install nbformat

# 转换单个文件
python -c "from scripts.md_to_ipynb_converter import convert_file; \
    convert_file('你的文档.md', '输出.ipynb')"

# 批量转换目录
python -c "from scripts.md_to_ipynb_converter import convert_directory; \
    convert_directory('源目录', '目标目录')"
```

## 术语对照（重要）

在阅读本文档时，以下术语会频繁出现：

| 英文 | 中文 | 说明 |
|------|------|------|
| Linked Art | Linked Art | 保持原文，项目名称 |
| HumanMadeObject | 人工制品 | 人造的文化遗产对象 |
| Provenance | 流传历史 | 所有权的转移历史 |
| Actor | 行动者 | 人或组织 |
| Collection | 集藏 | 博物馆的收藏 |

完整术语表请参考 [`术语对照表.md`](术语对照表.md)。

## 贡献指南

### 翻译改进

如果你发现翻译问题或有改进建议：

1. 查看 [`术语对照表.md`](术语对照表.md) 确认标准译法
2. 在 GitHub 上提交 Issue 或 Pull Request
3. 说明修改理由和参考依据

### 转换工具改进

如果你想改进转换脚本：

1. 修改 `scripts/md_to_ipynb_converter.py`
2. 确保向后兼容
3. 添加测试用例

## 原项目信息

- **官方网站**: https://linked.art/
- **GitHub**: https://github.com/linked-art/linked.art
- **许可证**: CC BY 4.0

## 致谢

感谢 Linked Art 社区，特别是 Rob Sanderson 和所有贡献者。

