---
title: Linked Art 中的词汇表术语
up_href: "/model/"
up_label: "模型概述"
---



## 简介

由于 Linked Art 模型在其类和属性方面非常广泛，我们大量使用词汇表术语来更具体地描述各个实体。在本体层面上，书籍、绘画或桥梁之间没有区别，它们都是类 `HumanMadeObject` 的实例。这使得在本体层面上易于互操作，然而为了跨机构或数据集比较数据，还必须在词汇表层面具有互操作性，以避免认为桥梁应该以与绘画相同的方式计算。

模型中的任何实体都可以使用 `classified_as` 属性关联一个或多个分类，如[类型和分类](/model/base/#types-and-classifications)节所述。这些分类的 URI 使用的一致性将使数据对每个人都更容易使用。词汇表已根据重用术语的重要性分为三个不同的集合。


## 按要求类别的术语

* [必需术语](required/) -- 你**必须**使用这些术语才能被认为是实现了 Linked Art
* [推荐术语](recommended/) -- 你**应该**使用这些术语，除非你有特定的理由不使用
* [可选术语](optional/) -- 你**可以**使用这些术语，但如果有不使用的理由，不应该感到有压力

## 用法

对词汇表条目的引用可以直接在引用的 `id` 中，也可以作为对中介的嵌入式 `equivalent`。为了符合性和实用性，以下两者都是同样可接受的。

在 `id` 中的词汇表：

```crom
top = model.HumanMadeObject(ident="spring/30", label="马奈的让娜（春天）")
top.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300033618",label="绘画")
```

在 `equivalent` 中的词汇表：

```crom
top = model.HumanMadeObject(ident="spring/31", label="马奈的让娜（春天）")
typ = model.Type(ident="https://linked.art/vocab/terms/painting", label="绘画")
eq = model.Type(ident="http://vocab.getty.edu/aat/300033618",label="绘画")
typ.equivalent = eq
top.classified_as = typ
```

## 词汇表列表的更新

必需列表中的条目只会在 Linked Art 的新主要版本中更改或删除，但可能会在次要版本中添加新要求。虽然这是对语义版本控制要求的弱解释，但它旨在促进语义层面的互操作性，因为最佳实践和一致性在社区内出现，而无需等待主要版本。

推荐列表也可以在新的次要版本中更新，因为不遵循列表不会破坏与以前次要版本的兼容性。这包括添加、删除和更改列表中条目的 URI。

可选列表仅作为信息，没有语义版本控制，因此可以随时更新。

社区应该通过 [github](https://github.com/linked-art/linked.art/issues) 问题提出对列表的添加。

