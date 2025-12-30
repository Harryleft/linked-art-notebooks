---
title: 属性分配的关系和上下文
---



## 简介

获取历史信息对研究很有用，例如之前被认为是谁创作了作品，或对象的先前估价。然而，大多数用例是获取当前信息。属性分配模型允许关联这些额外信息，而无需将每个属性都变成历史值列表。

此模式也用于特定上下文的断言，例如当对象为展览或其他事件的目的被给予标签或描述时。这个展览标签不会取代拥有博物馆的标题，但对历史比较和研究目的很有用。

应尽可能最少使用特定上下文断言或其他属性分配。数据结构比其他模式显著复杂，这降低了实现的可能性，增加了搜索查询的困难。只有在没有其他方式表达知识，并且重要的是用所有细节捕获时，才应使用此模式。

## 分配属性

`AttributeAssignment` 类是一个 `Activity`，通常由策展人或研究人员执行，而不是由艺术家或收藏家执行，它将信息分配给模型中的实体。这可以用于分配可以是此类属性 _subject_ 的任何实体上的任何属性或关系。通用的活动属性 `carried_out_by`、`timespan` 和 `took_place_at` 可用于分配发生的时间和地点，以及谁进行了分配。`timespan` 是分配发生的时刻，而不是某些受众认为分配为真的时间段。

当你不想直接断言关系时，此模式很有用，例如先前给对象的名称但不再积极使用。或者艺术家的归属可能为真，但可能只是有根据的猜测。

分配的值使用 `assigned` 给出，它可以是对任何实体的引用。值被分配到的实体使用该实体上的 `attributed_by` 属性给出，它们之间的关系使用 `assigned_property` 给出。因此，`AttributeAssignment` 可以通过 `carried_out_by` 关系将 `Actor` 分配给 `Production`，或通过 `made_of` 属性将 `Material` 分配给对象。就 `AttributeAssignment` 表达的关系而言，具有 `attributed_by` 属性的实体是关系的主语，关系本身在 `assigned_property` 中给出，关系的宾语在 `assigned` 中给出，从而构成主语-谓语-宾语的常规三元组。

__示例：__

2015年断言"春天"的材料是画布。

**请注意** 这仅是一个说明性示例，如果没有进一步的 reason，应改为使用简单的 `made_of` 属性。

```crom
top = vocab.Painting(ident="spring/21", label="春天")
aa = model.AttributeAssignment()
aa.assigned_property = "made_of"
mat = model.Material(ident="http://vocab.getty.edu/aat/300014078", _label="画布")
aa.assigned = mat
top.attributed_by = aa
ts = model.TimeSpan()
ts.begin_of_the_begin = "2015-01-01T00:00:00Z"
ts.end_of_the_end = "2015-12-31T23:59:59Z"
aa.timespan = ts
```

### 分配值作为主语实体

在其他情况下，与 `AttributeAssignment` 关联的适当实体是被分配的实体。在这种情况下，我们将 `AttributeAssignment` 反转过来，在分配的值（关系的宾语）上使用 `assigned_by`，并且不指定关系的主语，因为它是引用该值的实体。例如，能够断言哪个组织创建并分配了对象的 `Identifier` 非常有用，以便将该组织的标识符与另一个组织的同类型标识符区分开来，例如入藏号。另一个用例是提供与对象关联的特定 `Dimension` 的更多信息，例如谁测量了它、何时、使用什么仪器等等。

在这种情况下，关系的主语是引用值的实体，谓语是该关系，宾语是具有 `assigned_by` 属性的实体，该属性引用 AttributeAssignment。

__示例:__

Kehinde Wiley 的绘画"Lynette Yiadom-Boakye、Jacob Morland of Capplethwaite 的肖像"由耶鲁大学艺术博物馆和耶鲁英国艺术中心共同拥有。两个组织都分配了自己的入藏号，两者同时正确。

```crom
top = vocab.Painting(ident="yiadom-boakye/1", label="Lynette Yiadom-Boakye 的肖像")
acc1 = vocab.AccessionNumber(value="2021.25.1")
acc2 = vocab.AccessionNumber(value="B2021.5")
aa1 = model.AttributeAssignment()
aa1.carried_out_by = vocab.MuseumOrg(ident="yuag", label="耶鲁大学艺术博物馆")
aa2 = model.AttributeAssignment()
aa2.carried_out_by = vocab.MuseumOrg(ident="ycba", label="耶鲁英国艺术中心")
acc1.assigned_by = aa1
acc2.assigned_by = aa2
top.identified_by = acc1
top.identified_by = acc2
```

### 知识来源

能够断言信息来源很有用，例如为实体名称的特定形式提供权威或见证的文本。这使用属性分配模式建模，在 `used_specific_object` 字段中引用提供信息的实体。这可以是数据库、书籍文本、物理对象或其他实体类型。但是，要求是对该实体的引用，而不是字符串引用。

对于作为字符串的引用，可以在属性分配上使用常规的 Statement 模式和 `referred_to_by`。

__示例:__

名称形式"Rembrandt van Rijn"是从 Gardner 的"Art through the Ages"中添加的。

```crom
top = model.Person(ident="rembrandt/10", label="伦勃朗")
name = model.Name(content="Rembrandt van Rijn")
aa1 = model.AttributeAssignment()
aa1.used_specific_object = model.LinguisticObject(ident="gardner-art", label="Art through the Ages")
name.assigned_by = aa1
top.identified_by = name
```

### 嵌入语句的创作详细信息

为了给予嵌入在其他记录中的[语句](/model/base/)的创作以荣誉，可以在语句上添加 `created_by` 属性，就好像它是完整的文本作品记录一样。这允许创作者和其他创作信息以常规方式使用 `carried_out_by` 记录。这对于注意来自外部或更初级参与者的贡献特别有用，这些参与者可能不会因参与知识创造而获得任何认可。

人工智能的使用可以记录为创作的 `technique`，推荐的[词汇术语](/model/vocab/)为 "aat:300456842"，或者如果使用特定的 AI 工具，可以在 `Creation` 上使用 `used_specific_object` 列出。目前不推荐特定 AI 工具的 URI，但是如果某些工具变得流行，它们将被添加到词汇部分。请注意，如果使用了 AI 但没有关于语句创作的其他信息，那么更简单的选择是直接在 Statement 上使用 `classified_as`，词汇术语为 "aat:300456841"，表示"AI 生成的内容"。当分配由 AI 进行时，technique 或分类也可以与 `AttributeAssignment` 一起使用。以这些方式标记为使用 AI 系统生成的内容的消费者可能希望在用户界面中这样标记内容，或者以其他方式允许过滤或排序此类人工内容。

!!! note "描述范围"
    请注意，此模式不允许将单个关系标记为由 AI
    生成。例如，如果软件从语句中提取材料列表并创建了一系列 `made_of`
    对实际 `Material` 实例的引用，则无法重新实现这些链接以添加创作信息，就像
    无法重新实现它们以添加断言关系的人一样。如上所述使用 `AttributeAssignment`
    是可能的但不鼓励。

另一个用例是将权利信息与语句关联，与对整个数据集的任何声明的许可分开。这遵循常规的 `subject_to` 模式，如[权利部分](/model/object/rights/)中所述。这样，关于对象或人物的整体事实信息可以比文本或其他更定制或潜在有价值的内容具有更宽松的许可。

必须注意，所有这些功能也可用于任何 `LinguisticObject` 记录。

__示例:__

《夜巡》的描述在特定时间点由 AI 生成，并获得 CC-BY 许可。

```crom
top = model.HumanMadeObject(ident="nightwatch/70", label="夜巡")
stmt = vocab.Description(content="伦勃朗的《夜巡》是一幅充满活力的 17 世纪阿姆斯特丹民兵公司团体肖像...")
cre = model.Creation()
ts = model.TimeSpan()
ts.begin_of_the_begin = "2024-11-07T20:50:00Z"
ts.end_of_the_end = "2024-11-07T20:50:00Z"
cre.timespan = ts
cre.technique = model.Type(ident="http://vocab.getty.edu/aat/300456842")
stmt.created_by = cre
stmt.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300456841")
right = model.Right()
right.classified_as = model.Type(ident="https://creativecommons.org/licenses/by/4.0/", label="CC-BY")
right.identified_by = model.Name(content="CC-BY 4.0")
stmt.subject_to = right
top.referred_to_by = stmt
```


### 不确定或以前的分配

与上面第一个示例中采用的方法类似，可以在 `Production` 节点上使用 `attributed_by` 来对它做出不确定或以前被认为正确的断言。然后分配创建另一个 `Production` 来封装不确定或以前被认为正确的信息，包括艺术家但也可能包括其他链接，例如创作地点、日期或其他影响。

__示例:__

水彩画"Forum Romanum"可能由 Salomon Corrodi 创作

```crom
top = vocab.Painting(ident="forum/1", label="Forum Romanum")
top.identified_by = vocab.PrimaryName(content="Forum Romanum")
prod = model.Production()
top.produced_by = prod
aa = model.AttributeAssignment()
aa.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300404272", label="可能由")
part = model.Production()
aa.assigned = part
part.carried_out_by = model.Person(ident="corrodi", label="Salomon Corrodi")
aa.assigned_property = "part"
prod.attributed_by = aa
```

### 特定上下文的分配

某些断言仅在特定上下文中为真，最常见的情况是为特定展览分配的描述、名称和标识符。为了记录这些特定上下文的断言，应使用 `attributed_by` 模式，即使对于可能具有 `assigned_by` 模式的名称和标识符也是如此，因为这使标识符与主记录分离。

我们使用 `caused_by` 关系将属性分配与展览连接起来。

__Example:__

1980年，春天在国家艺术博物馆的展览"后印象主义：欧洲和美国绘画的交叉潮流"中展出，并被分配了一个展览特定的标识符（称为"dexid"）。

```crom
top = vocab.Painting(ident="spring/31", label="春天")
top.identified_by = vocab.PrimaryName(content="让娜（春天）")
aa = model.AttributeAssignment()
idt = model.Identifier(content="2497-12")
idt.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300445023", label="入场号码")
aa.assigned = idt
aa.assigned_property = 'identified_by'
aa.carried_out_by = model.Group(ident="nga", label="国家艺术博物馆")
aa.caused_by = model.Activity(ident="post_impressionism", label="后印象主义展览")
top.attributed_by = aa
```

## 关系

### 相关实体

`AttributeAssignment` 的另一个用途是当关系的性质未知时捕获实体之间的关系。这通常会在面向人类用户界面中以"相关地点"或"相关人物"之类的标签出现。以这种方式使用 AttributeAssignment 应该是最后的选择，当没有办法比仅"存在关系"更具体时。这可能有用且合理的一个场景是明确连接集合中的"相关"对象，其中相关性是通过某种计算的相似性度量。同样，底层数据格式可能不明确实体之间的关系，属性分配模式是最接近的表达方式。

这也涵盖了艺术家的"代表性对象"或其他类似的"精选"集合的用例。艺术家和对象之间没有特定关系未被模型覆盖，但希望有一些预先确定的选择，而不是让系统随机选择要使用的对象。这些可以在 `AttributeAssignment` 的 `classified_as` 中引用 http://vocab.getty.edu/aat/300028875 来区分它们。

__Example:__

《夜巡》与国家博物馆收藏中的另一个对象"Nachtwacht"相关，但没有具体捕获关系。

```crom
top = vocab.Painting(ident="nightwatch/57", label="夜巡")
top.identified_by = vocab.PrimaryName(content="夜巡")
aa = model.AttributeAssignment()
top.attributed_by = aa
aa.identified_by = vocab.DisplayName(content="相关对象")
aa.assigned = model.HumanMadeObject(ident="rppob-28-106", label="Nachtwacht")
```

### 未建模的关系

相反，可能知道关系但没有办法在模型中描述它。例如，人物之间的学生/教师关系是一种社会结构，无法轻易捕获，但对艺术史仍然很重要。这种关系太多了，尤其是在社交领域，无法单独建模它们或为每个关系创建扩展属性，因此对关系使用 `AttributeAssignment` 是采取的方法。找到适当的属性来描述关系，无论是作为 `classified_as` 还是 `assigned_property`，都取决于实现者。建议在 `AttributeAssignment` 上使用 `identified_by` 给出显示名称。

/// note | 作为群体的社会结构
请注意，许多社会关系可以通过 `classified_as` 在 `Joining` 活动上建模为以特定角色 `加入` 和 `离开` `群体`。例如，群体代表教师和学生之间的社会纽带，教师作为教师加入群体，学生作为学生加入。这是可能的，但引入了大量额外开销，需要为关系的"群体"提供身份。
///


__Example:__

Ferdinand Bol 是伦勃朗的学生。

```crom
top = model.Person(ident="bol/1", label="Ferdinand Bol")
top.identified_by = vocab.PrimaryName(content="Ferdinand Bol")
aa = model.AttributeAssignment()
aa.assigned = model.Person(ident="rembrandt", label="伦勃朗")
aa.identified_by = vocab.DisplayName(content="学生")
top.attributed_by = aa
```
