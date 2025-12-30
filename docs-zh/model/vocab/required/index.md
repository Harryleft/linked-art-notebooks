---
title: 必需词汇表术语
up_href: "/model/vocab/"
up_label: "词汇表术语"
---



## 简介

为了促进对数据的最基本理解，需要使用这些术语。如果术语在这里列出，那么你必须**不**为相同概念使用不同的术语，因为系统期望这些术语。这并不是说你必须在每个记录中都有这些术语，你可能不知道（例如）对象的形状，但如果你知道，那么你必须使用约定的"形状"概念的 URI。

## 摘要

为了在表格中简洁，AAT URI 用命名空间压缩，但在数据中**必须**使用完整的 URI。例如，主要名称的 URI 是 `http://vocab.getty.edu/aat/300404670`

| 名称 | URI | 分类 | 描述 |
|-----------------------|---------------|------------|-------------|
| Primary Name | aat:300404670 | Name | 实体的主要名称 |
| Display Name | aat:300404669 | Name | 用于显示节点的名称 |
| Sort Name | aat:300451544 | Name | 将此实体与其他实体排序时使用的名称 |
| Sort Value | aat:300456575 | Identifier | 将此实体与其他实体排序时使用的标识符 |
| Statement | aat:300418049 | Type | 声明的类型 |
| Type of Work | aat:300435443 | Type | 作品的类型 |
| Style | aat:300015646 | Type | 风格 |
| Shape | aat:300056273 | Type | 形状 |
| Occupation | aat:300263369 | Type | 职业 |
| Nationality | aat:300379842 | Type | 国籍 |
| Color | aat:300080438 | Dimension | 颜色 |
| Exhibition Activity | aat:300054766 | Activity | 展览活动 |
| Provenance Activity | aat:300055863 | Activity | 流传历史活动 |
| Professional Activity | aat:300393177 | Activity | 专业活动 |
| Publication Activity | aat:300054686 | Activity | 出版活动 |
| Promise Activity | aat:300435599 | Activity | 承诺 |
| Collection Item | aat:300404024 | Any | 实体是文化遗产集合的一部分 |
| Artwork | aat:300133025 | Any | 实体是艺术品 |


详情请见下文

## 名称类型

有四个必需的词汇条目用于名称和标识符，以便将其与其他名称和标识符区分开来。每个都有特定的要求，供客户端或搜索系统使用。

### 主要名称

主要名称的 URI 是：[http://vocab.getty.edu/aat/300404670](http://vocab.getty.edu/aat/300404670)

实体的主要或首要名称。每条记录必须有一个带有主要名称分类的名称，以便用户界面知道使用哪个名称。单条记录可能有多个主要名称，但每个必须具有唯一的语言或不指定语言。请参阅[名称文档](/model/base/#names)。

示例：

```crom
top = model.HumanMadeObject(ident="nightwatch/41", label="Night Watch by Rembrandt")
ttl = vocab.PrimaryName(content="The Night Watch")
ttl.language = vocab.instances['english']
top.identified_by = ttl
```

### 显示名称

显示名称的 URI 是：[http://vocab.getty.edu/aat/300404669](http://vocab.getty.edu/aat/300404669)

用于显示具有关联名称的节点时使用的名称。对于声明，这通常由界面用作声明的标签。对于[时间跨度](/model/base/#time-span-details)或其他结构化数据，它用于替代结构化数据。

示例 1：

```crom
top = model.HumanMadeObject(ident="nightwatch/42", label="Night Watch by Rembrandt")
lo = vocab.MaterialStatement(content="Oil on Canvas")
lo.identified_by = vocab.DisplayName(content="Materials")
top.referred_to_by = lo
```

示例 2：

```crom
top = model.HumanMadeObject(ident="nightwatch/43", label="Night Watch by Rembrandt")
prod = model.Production()
top.produced_by = prod
ts = model.TimeSpan()
ts.begin_of_the_begin = "1642-01-01T00:00:00Z"
ts.end_of_the_end = "1842-12-31T23:59:59Z"
ts.identified_by = vocab.DisplayName("1642")
prod.timespan = ts
```

### 排序名称

排序名称的 URI 是：[http://vocab.getty.edu/aat/300451544](http://vocab.getty.edu/aat/300451544)

用于将实体与列表中的其他实体一起排序时使用的名称。此分类可以用于与主要名称相同的名称，或用于实体名称的不同形式。不同语言可以有不同的排序名称，但是每种语言不得超过一个。

```crom
top = model.Person(ident="rembrandt/41", label="Rembrandt")
top.identified_by = vocab.PrimaryName(content="Rembrandt van Rijn")
top.identified_by = vocab.SortName(content="van Rijn, Rembrandt Harmenszoon")
```

### 排序值

排序名称的 URI 是：[http://vocab.getty.edu/aat/300456575](http://vocab.getty.edu/aat/300456575)

用于将实体与列表中的其他实体一起排序的非语言标识符，而不是如上所述的语言形式。每个实体不得超过一个排序值。用户界面不应将排序值呈现给最终用户。

```crom
top = model.Person(ident="rembrandt/42", label="Rembrandt")
top.identified_by = vocab.SortValue(content="r0000011")
```

## 分类类型

有六个分类作为类别，用于在同一属性中区分非常相似的构造。这些在[类型类型部分](/model/base/#types-of-types)中描述，有时称为"元类型"。一个相关的必需术语是颜色，但它对维度而不是另一个类型进行分类。

### 声明

声明类型的 URI 是：[http://vocab.getty.edu/aat/300418049](http://vocab.getty.edu/aat/300418049)

有许多类型的[声明](/model/base/#statements-about-an-entity)，不可能以一种可以成功且可用地实现的方式枚举所有这些不同的类型。相反，声明的类型（例如材料声明）被赋予"简短文本"的元类型，以便它们可以被识别为声明类型。

```crom
top = model.HumanMadeObject(ident="nightwatch/44", label="Night Watch by Rembrandt")
top.referred_to_by = vocab.MaterialStatement(content="Oil on Canvas")
```

### 作品类型

作品类型的 URI 是：[http://vocab.getty.edu/aat/300435443](http://vocab.getty.edu/aat/300435443)

有许多[作品类型](/model/base/#types-and-classifications)（绘画、雕像、版画......），任何系统同样不可能先验地知道所有这些类型。相反，对象的作品类型被归类为作品类型的元类型，以便它可以被识别。

```crom
top = vocab.Painting(ident="nightwatch/45", label="Night Watch by Rembrandt")
```

### 风格

风格的 URI 是：[http://vocab.getty.edu/aat/300015646](http://vocab.getty.edu/aat/300015646)

同样，有许多[风格](/model/object/aboutness/#style-classification)，我们使用 aat:300015646 来区分风格概念与作品的其他分类。

```crom
top = model.VisualItem(ident="nightwatch/40", label="Appearance of Night Watch")
top.classified_as = vocab.instances['baroque style']
```

### 形状

形状的 URI 是：[http://vocab.getty.edu/aat/300056273](http://vocab.getty.edu/aat/300056273)

同样，有许多[形状](/model/object/physical/#shapes)，我们需要将形状与其他分类区分开来。

```crom
top = model.HumanMadeObject(ident="nightwatch/48", label="Night Watch by Rembrandt")
top.classified_as = vocab.instances['rectangular']
```

### 国籍

国籍的 URI 是：[http://vocab.getty.edu/aat/300379842](http://vocab.getty.edu/aat/300379842)

与对象和作品一样，人们也有多种与之相关的分类类型。常见的一个是[国籍](/model/actor/#nationality)。

```crom
top = model.Person(ident="rembrandt/44", label="Rembrandt")
top.classified_as = vocab.instances['dutch nationality']
```

### 职业

职业的 URI 是：[http://vocab.getty.edu/aat/300263369](http://vocab.getty.edu/aat/300263369)

人们也可以按其职业进行分类。

```crom
top = model.Person(ident="rembrandt/43", label="Rembrandt")
top.classified_as = vocab.instances['artist occupation']
```

### 颜色

颜色的 URI 是：[http://vocab.getty.edu/aat/300080438](http://vocab.getty.edu/aat/300080438)

由于[颜色](/model/object/physical/#colors)可以精确测量，也可以被视为类别，因此分类位于维度上。维度可能最终没有值和单位，只有关于它是哪种颜色的第二个分类（在这种情况下是棕色），但是必需的术语是在维度上使用 aat:300080438。

```crom
top = model.HumanMadeObject(ident="nightwatch/47", label="Night Watch by Rembrandt")
c = vocab.Color(label="brown")
c.value = 11754015.0
c.unit = vocab.instances['rgb_colorspace']
top.dimension = c
```

## 活动类型

有几个活动的分类很重要，因为它们定义了核心的遗产组织实践。

### 展览活动

展览的 URI 是：[http://vocab.getty.edu/aat/300054766](http://vocab.getty.edu/aat/300054766)

展览在[自己的部分中有记录](/model/exhibition/)，但在本体论中没有自己的类。因此，我们需要给它们一个必需的分类，以便它们可以被识别。

```crom
top = vocab.Exhibition(ident="exha/40", label="Manet and Modern Beauty (Getty)")
```

### 流传历史活动

流传历史条目的 URI 是：[http://vocab.getty.edu/aat/300055863](http://vocab.getty.edu/aat/300055863)

流传历史活动也有文档的自己的[部分](/model/provenance/)，并且在本体论中没有类。此分类用于将其他部分组合在一起的最高级别活动。

```crom
top = vocab.ProvenanceEntry(ident="manet_proust/40", label="Purchase of Spring by Proust")
```

### 出版活动

出版活动的 URI 是：[http://vocab.getty.edu/aat/300054686](http://vocab.getty.edu/aat/300054686)

作品，尤其是书籍等文本，在活动中被[出版](/model/document/#creation-and-publication)。这些活动嵌入在作品的记录中，但能够区分它们同样重要。

```crom
top = vocab.LinguisticObject(ident="koot_nightwatch/40", label="Content of Koot's Night Watch")
pub = vocab.Publishing(label="MI's Publishing")
pub.carried_out_by = model.Group(ident="meulenhoff", label="Meulenhoff International")
top.used_for = pub
```

### 专业活动

专业活动的 URI 是：[http://vocab.getty.edu/aat/300393177](http://vocab.getty.edu/aat/300393177)

```crom
top = model.Person(ident="rembrandt/44", label="Rembrandt")
top.carried_out = vocab.Active()
```

### 承诺活动

承诺的 URI 是：[http://vocab.getty.edu/aat/300435599](http://vocab.getty.edu/aat/300435599)

尽管是详细流传历史的一小部分，但在本体论中没有[承诺](/model/provenance/promises/)的类，因此我们必须要求术语来填充这个角色。

```crom
top = vocab.ProvenanceEntry(ident="coffin_promise/40", label="Promised Gift of Painting")
promise = vocab.Promise(label="Promise of Gift")
top.part = promise
```

## 对象/项目标志

有两个标志可用于区分广泛类别的项目。

### 集藏项目

集藏项目的 URI 是：[http://vocab.getty.edu/aat/300404024](http://vocab.getty.edu/aat/300404024)

能够描述机构"集藏"中项目的记录与描述其他物理或数字对象或智力作品的记录区分开来是有用的。同样，有些东西是集藏的一部分，但人们可能不会描述为艺术品，如档案材料或参考集藏。

```crom
top = model.HumanMadeObject(ident="nightwatch/49", label="Night Watch by Rembrandt")
top.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300404024", label="Collection Item")
```

### 艺术品

第二个重要的区别是作为艺术品的对象和不是艺术品的对象之间。画廊里可能有两把椅子 —— 一把是艺术，另一把只是供参观者坐的椅子。

```crom
top = model.HumanMadeObject(ident="nightwatch/50", label="Night Watch by Rembrandt", artwork=1)
```