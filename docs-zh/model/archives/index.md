---
title: 档案
up_href: "/model/"
up_label: "模型概述"
---



## 简介

Linked Art 包括一个描述档案和档案材料的简单模型。该模型使用[集合](/model/collection/)作为将实体分组到层次结构中的方式。档案项目本身通常是[人造物](/model/object/)或[数字对象](/model/digital/)，可以详细描述，但在档案实践中通常只是非常简短地描述，如果有的话。为支持档案描述添加的唯一新功能是集合与保存概念集合成员的物理容器之间的链接。


## 档案层次结构

档案传统通常不明确区分档案的知识安排和物理容器，但在 Linked Art 中，这些是模型中两个非常独立的部分。Linked Art 将档案层次结构视为概念性的——它是思维的产物，不是物理世界的特征。这可以通过以下方式理解：如果从档案文件夹中取出一封信，它不是从"档案"中取出，而是从其当前容器中取出。某人可能临时将其添加到恰好是第二个档案一部分的另一个文件夹中……也许是为了将它们一起带给读者。同样，这也不会将其添加到第二个档案中。

考虑到这一点，档案可以描述为 `Set` 的层次结构，其中代表子系列的 `Set` 是代表系列的 `Set` 的 `member_of`，而系列是子全宗的 `member_of`，依此类推。层次结构的深度没有限制，并且鉴于 Linked Art 的基于图的性质，这使得同一对象可以同时成为两个档案的一部分。

项目，如果被描述，是也是 `Set` 的 `member_of` 的 `HumanMadeObject` 或 `DigitalObject`，并遵循常规的物理或数字模型。

请注意，档案组成员的排序可以以与任何其他集合排序相同的方式[给出](/model/collection/#order-of-members)。


__示例：__

Alfred Stieglitz 和 Bertha Obermeyer 之间的一封信，日期为 1920 年，是"Stieglitz 家族信件"子系列的一部分，该子系列是"系列 I：Alfred Stieglitz 通信"的一部分（该系列是耶鲁大学"Alfred Stieglitz / Georgia O'Keeffe 档案"的一部分）

这封信……

```crom
top = model.HumanMadeObject(ident="letter/1", label="Obermeyer 1920")
top.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300026879", label="Letter")
top.identified_by = vocab.PrimaryName(content="Obermeyer, Bertha (1920)")
top.member_of = model.Set(ident="archive_sfl", label="Stieglitz Family Letters")
```

是子系列的成员……

```crom
top = vocab.ArchiveSubGroupSet(ident="archive_sfl/1", label="Stieglitz Family Letters")
top.identified_by = vocab.PrimaryName(content="Stieglitz Family Letters")
top.member_of = model.Set(ident="archive_asc", label="Alfred Stiegliz Correspondence")
```

该子系列是系列的成员……

```crom
top = vocab.ArchiveGroupSet(ident="archive_asc/1", label="Alfred Stiegliz Correspondence")
top.identified_by = vocab.PrimaryName(content="Alfred Stiegliz Correspondence")
```

（依此类推）

### 概念层次结构和物理层次结构之间的一致

在档案层次结构的一个或多个点中，在概念安排和对象的物理存储之间进行一致性对齐是有用的。这是通过档案 Set 实体上的 `members_contained_by` 属性完成的，引用物理上包含或保存对象的 `HumanMadeObject`，如盒子、文件夹或架子。如果单独描述，物理对象也可以使用 `held_or_supported_by` 属性成为此物理层次结构的一部分。


__示例：__

Stieglitz 家族信件集合的成员位于第 55 号盒中。

```crom
top = vocab.ArchiveSubGroupSet(ident="archive_sfl/2", label="Stieglitz Family Letters")
top.identified_by = vocab.PrimaryName(content="Stieglitz Family Letters")
top.members_contained_by = model.HumanMadeObject(ident="box55", label="Archival Box 55")
```

这封信在盒子内。

```crom
top = model.HumanMadeObject(ident="letter/3", label="Obermeyer 1920")
top.identified_by = vocab.PrimaryName(content="Obermeyer, Bertha (1920)")
top.held_or_supported_by = model.HumanMadeObject(ident="box55", label="Archival Box 55")
top.member_of = model.Set(ident="archive_sfl", label="Stieglitz Family Letters")
```

## 集体描述

可以使用 Set 实例上的 `members_exemplified_by` 属性来描述集合成员的共同特征。这在[收藏](/model/collection/)页面中有更详细的描述。这对于建立档案收藏成员的创作日期范围、内容语言、类型等特别有用。

否则，档案的大部分描述都是通过遵循[声明](/model/base/)模式的纯文本完成的。
