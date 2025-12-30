---
title: 文本和文档
---



## 简介

本节记录包含文本的文档的模型，包括中世纪手稿等艺术品，信件、账本或日记等档案材料，期刊、文章和专著等学术交流，网页等数字对象，或任何其他类型的书面交流。

目的不是成为一个全面的模型，适用于基于图的图书馆管理系统、档案查找辅助工具或任何数字资源的目录，而是提供足够的描述，使对象能够被识别、理解，并能够在其他更具体的系统和本体中被引用。该模型旨在足以用于引用与艺术品相关的文本的基本用例，无论它们是在图书馆、档案馆、博物馆还是互联网上保存。

值得注意的是，它不尝试重现 [FRBR](https://www.ifla.org/node/2016) 和类似抽象模型的形式化，如 [FRBRoo](https://www.ifla.org/publications/node/11240)、[BibFrame](http://www.loc.gov/bibframe/docs/index.html) 或其他复杂的概念层次结构，而是提供尽可能简单的模型来完成核心的书目引用任务。

## 物理对象、概念文本

第一个需要的区别是文本的物理或数字载体与文本本身之间的区别。像[对象显示的艺术品视觉内容](/model/object/aboutness/#depiction)的 `VisualItem` 模式一样，代表作品文本的 `LinguisticObject` 可以被多个 `HumanMadeObject` `carried`，并被 `DigitalObject` 实例 `digitally_carried_by`。这样，特定书籍的所有副本都携带相同的信息内容，只需要描述一次，并可以作为单个连接点。

像其他 `LinguisticObject` 一样，它可以有用于作品实际文本的 `content` 属性、分类、语言等。

!!! note "口述历史"
    语言内容不需要用符号写下来才能被认为是 `LinguisticObject`，它可以完全通过口头传统传播。同样，采访可以在没有转录的情况下被记录，传播的信息仍然是 `LinguisticObject`，因为它是通过人类语言的使用传播的，而不是视觉描述。


__示例：__

耶鲁大学图书馆收藏了一本 Koot 关于《夜巡》的书的副本。

```crom
top = vocab.Book(ident="yul_10801219/1", label="Yale's copy of Koot's Night Watch")
top.identified_by = vocab.PrimaryName(content="Rembrandt's Night Watch. A Fascinating Story")
top.identified_by = vocab.SystemNumber(content="mfhd:10801219")
top.referred_to_by = vocab.PhysicalStatement(content="92 p. with illus.")
li = model.LinguisticObject(ident="koot_nightwatch", label="Content of Koot's Night Watch")
top.carries = li
```

## 共同特征

模型的共同特征也适用于用于表示文本的 `LinguisticObject`。它们必须具有 `id` 和 `type`，它们应该具有 `label`，它们应该具有与 `Type` 的 `classified_as` 关系，以进一步描述对象的类型，等等。它们也可能具有 `language` 属性，该属性引用文本的 `Language`。

文本的标题使用 `Name` 模式捕获，并使用 `Identifier` 模式分配标识符，两者都使用 `identified_by` 关系。

__示例：__

Koot 作品的文本内容。

```crom
top = vocab.MonographText(ident="koot_nightwatch/1", label="Content of Koot's Night Watch")
top.identified_by = vocab.PrimaryName(content="Rembrandt's Night Watch. A Fascinating Story")
top.identified_by = vocab.SystemNumber(content="75441784")
top.language = vocab.instances['english']
```

## 创作和出版

文本的物理载体的制作使用与其他物理对象相同的模型，并且可能对手稿、非常早期的印刷作品（摇篮本）、信件或其他类似文档感兴趣，但是捕获特定现代书籍的工厂细节可能不太重要。

有两个主要的文本特定活动被捕获 —— 文本的创作和它的出版。文本由作者的 `Creation` 活动创建，但是然后有一个出版组织执行的出版 `Activity`（_aat:300054686_），针对同一实体。

__示例：__

文本的作者身份和出版。

```crom
top = vocab.MonographText(ident="koot_nightwatch/2", label="Content of Koot's Night Watch")
cre = model.Creation(label="Koot's writing of the work")
cre.carried_out_by = model.Person(ident="koot", label="Ton Koot")
top.created_by = cre
pub = vocab.Publishing(label="MI's Publishing")
pub.carried_out_by = model.Group(ident="meulenhoff", label="Meulenhoff International")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1969-01-01T00:00:00Z"
ts.end_of_the_end = "1969-12-31T23:59:59Z"
pub.timespan = ts
top.used_for = pub
```

## 结构

文本结构可以通过 `part_of` 属性对 `LinguisticObject` 进行分区来建模，就像物理对象的部分可以分区一样。因此，文章的内容可以是包含期刊的一部分，期刊是卷的一部分，卷是期刊或其他期刊的一部分。类似地，章节可以是书籍或会议录的一部分，目录中的特定条目等等。

请注意，除非创建单独的记录很重要（例如，章节由不同的作者撰写，或者有其他重要细节），否则也可以只将结构的描述作为注释添加，使用 Statement 模式。

__示例：__

```crom
top = vocab.ChapterText(ident="koot_nightwatch_ch1/1", label="Chapter 1 of Koot")
top.identified_by = vocab.PrimaryName(content="Introduction")
top.part_of = model.LinguisticObject(ident="koot_nightwatch", label="Koot's Night Watch")
```

## 页面

文本内容通常在页面或对开页上呈现。由于可能有许多具有相同结构的物理副本，因此通常描述一般适用于内容的分页，而不是携带该内容的许多物理对象。这是合理的，主要是为了方便，但也因为文本被分成恰好与物理载体结构相对应的部分。分页（_aat:300200294_）或对开（_aat:300200662_）声明是表示这一点的最常见方式，作为遵循核心声明模式的简单描述字段。

结构化方法是让对象或作品具有一个维度，该维度给出页面计数。这遵循计算部分的常规模式。描述较大集合的特定部分的页面范围的最简单方法是使用分页声明。该方法的缺点是它在计算上不可用于处理。

__示例：__

Koot 书籍的介绍章节长 10 页。

```crom
top = vocab.ChapterText(ident="koot_nightwatch_ch1/2", label="Chapter 1 of Koot")
top.identified_by = vocab.PrimaryName(content="Introduction")
top.referred_to_by = vocab.PaginationStatement(content="5 - 15")
dim = model.Dimension(label="10 pages")
dim.value = 10
dim.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300404433", label="Count Of")
dim.unit = model.MeasurementUnit(ident="http://vocab.getty.edu/aat/300194222", label="Pages")
top.dimension = dim
```

## 对其他实体的引用

文本内容可以 `about` 使用模型描述的任何其他实体。这些应该是核心实体，而不是像 `Dimension` 或 `Identifier` 这样的结构实体，这是实现 API 所必需的。

__示例：__

Koot 的书是关于《夜巡》的。

```crom
top = vocab.MonographText(ident="koot_nightwatch/3", label="Content of Koot's Night Watch")
top.about = model.HumanMadeObject(ident="nightwatch", label="The Night Watch")
```

## 抽象作品

有时将内容与更高级别的抽象联系起来是很有价值的，这种抽象甚至不区分文本、音频、视频、图像或其他形式，更不用说该思想的各种版本、翻译或其他表现形式。一些一般的例子包括《指环王》，由托尔金用英语概念化和最初撰写，但随后被改编成电影，例如彼得·杰克逊的电影，以及同一抽象作品的其他解释。虽然不是严格的 LRM 或 FRBR 模型，但这确实允许将"作品"级别映射到 Linked Art 中适当抽象的类。

抽象作品具有与语言对象相同的所有特征，除了 `language`。语言、视觉和其他抽象作品可以 `conceptually_part_of` 抽象作品，以将它们在层次结构中连接在一起。

__示例：__

Koot 书籍的文本在概念上是他对研究和讨论的更大型、更抽象的作品的一部分，可能有多个版本、翻译或实例化。

```crom
top = model.LinguisticObject(ident="koot_nightwatch/1", label="Content of Koot's Night Watch")
top.identified_by = vocab.PrimaryName(content="Rembrant's Night Watch. A Fascinating Story")
top.conceptually_part_of = model.PropositionalObject(ident="koot_idea", label="Koot's Conceptualization")
```