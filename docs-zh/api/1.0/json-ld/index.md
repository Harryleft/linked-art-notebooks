---
title: JSON-LD 序列化
up_href: "/api/1.0/"
up_label: "Linked Art API 1.0"
---



## 简介

JSON-LD 是使用流行 JSON（JavaScript 对象表示法）格式的关联开放数据序列化，对后端和基于浏览器的开发都很方便。它由 [W3C](https://www.w3.org/TR/json-ld11/) 指定为官方序列化。持续的开发工作在数据链接 JSON W3C [社区组](https://www.w3.org/community/json-ld/)中进行。

JSON-LD 的序列化通过使用上下文文档对开发人员友好，上下文文档指定了 json 对象中使用的键与模型中使用的 RDF 谓词之间的映射。这种抽象允许开发人员使用现有的模式和框架，而数据仍然在底层作为图进行管理。本文档描述了用于 CIDOC-CRM 和其他本体的上下文。

提供模型中使用的术语映射的上下文发布为：
> `https://linked.art/ns/v1/linked-art.json`

## 媒体类型

用于使用上下文的 JSON-LD 表示的媒体类型是：

> `application/ld+json;profile="https://linked.art/ns/v1/linked-art.json"`

这将是响应上 `Content-Type` HTTP 头的值，如果通过内容协商有其他表示可用，那么它可以在请求中的 `Accept` 头中发送。


## 核心要求

对于 JSON 和 JSON-LD 表示，有几个核心要求需要牢记：

* 术语区分大小写。`Type`（类 `crm:E55_Type`）和 `type`（属性 `rdf:type`）是不同的术语，仅通过首字母的大写来区分。如上所述，类和属性名称的 JSON 表示尽可能一致。
* 属性不能在单个对象上重复。相反，如果一个属性有多个值或关系的多个实例，那么 JSON 将有一个数组作为值，其中每个条目都被认为具有该属性。Linked Art 不使用 RDF 的有序列表（如 `rdf:List`），而是依赖序列化中的顺序。


## 其他序列化格式

底层图的其他序列化格式也可能可用，例如 [RDF/XML](https://www.w3.org/TR/rdf-syntax-grammar/)、[Turtle](https://www.w3.org/TR/turtle/)、其他标准化格式，甚至非标准化表示。这些不是完全符合 Linked Art API 所必需的，不应假设它们存在。如何广告和请求这些替代序列化在[协议](../protocol/)部分中有记录。


## 示例

文档中的示例使用 JSON-LD 序列化。每个都有指向原始 JSON-LD 的链接，并将其加载到非常有用的 JSON-LD 游乐场中，您可以在那里探索详细信息。我们不尝试描述所有谓词和类（只需阅读 CIDOC-CRM 规范），而是为已知用例展示模型，以试图更实用和结果导向。我们力求开发人员的可用性和熟悉性，同时示例旨在在易于遵循的同时展示最佳实践。

一幅使用水彩在画布支撑上制作的绘画的 JSON-LD 序列化示例：

```crom
top = vocab.Painting(ident="auto int-per-segment", label="Example Painting", art=1)
top.made_of = vocab.instances['watercolor']
part = vocab.SupportPart(label="Canvas Support")
part.made_of = vocab.instances['canvas']
top.part = part
```

## 上下文设计

JSON-LD 序列化的重要部分是共享上下文文档。这个上下文有一些设计约束，在查看数据模型和从本体映射之前理解这些约束很有用。特别是：

* 生成的 JSON 必须是__有效的__关联开放数据和有效的 JSON-LD。JSON 中的嵌套对象结构是资源图的结果。
* 生成的 JSON 必须被不熟悉模型和 RDF 的开发人员__理解__。如果目标技术受众是拥有全套 RDF 工具的开发人员，那么 Turtle 和 SPARQL 可能更可取。序列化试图使内容在模型允许的范围内尽可能易于访问，以尽可能广泛的受众。
* 生成的 JSON 必须是__可用的__，无论编程语言或应用程序环境如何，以确保尽可能广泛的采用和价值。上下文旨在允许使用尽可能多的便利，并最大化可以使用它的情况。一致性是可用性的核心特征，因此上下文尽可能一致。

CIDOC-CRM 本体对这些原则有一些挑战。

* 在类和属性中使用数字与可理解和可用原则相悖。
* 在某些类和属性名称中使用 `-` 降低了可用性，因为在大多数编程语言中不允许作为属性的名称。
* 使用相同的名称作为属性，减去其数字，在 JSON-LD 中是不可能的，因为键必须唯一映射到谓词。
* 在类或属性名称中使用下划线在 Javascript 或 RDF 本体中并不常见，后者倾向于使用驼峰命名法。
* 资源之间的相同概念关系在本体中有不同的实例化，引入了不必要的不一致性。例如，核心分区关系是特定于类的，而不是所有东西都使用更明显的 `part` 关系。

上下文试图以实用和编程可访问的方式从本体定义中管理所有这些问题。

## 上下文

以下过程用于从 CIDOC-CRM 本体创建 JSON-LD 键：

* 删除 `@` 符号（`id` 而不是 `@id`）作为 JSON-LD 最佳实践
* 从类和属性中删除命名空间（`E22_Man-Made_Object` 而不是 `crm:E22_Man-Made_Object`），因为上下文映射不需要
* 删除前缀数字（`Human-Made_Object` 而不是 `E22_Human-Made_Object`），因为不可能记住
* 删除连字符（`HumanMade_Object` 而不是 `Human-Made_Object`），因为在类名中无效
* 对类使用大写驼峰命名法（`HumanMadeObject` 而不是 `HumanMade_Object`）作为常见实践
* 对属性使用小写 snake_case（`is_identified_by`），因为为此类广泛的术语集自动生成驼峰命名法很困难
* 从属性的开头删除 `is_`、`was_`、`has_` 和 `had_`，因为在本体中应用不一致且难以记住（`identified_by` 而不是 `is_identified_by`；比较 `created` 和 `destroyed` 属性，它们在本体中不是 `was_created` 的形式）
* 从层次结构的最低端开始重命名有冲突的属性，首先是将范围的类添加到谓词名称，但更倾向于人类可理解的术语
* 重命名使用时不一致命名的属性
* 提供包含所有术语的单一上下文，以促进使用核心术语进行扩展
* 包括常用本体（`skos`、`schema`、`rdf`）和词汇表（`aat`、`tgn`、`geonames`）的前缀

上下文实现了这样的概念，即如果一个属性可以有多个值，那么它必须始终是一个数组。在 JSON-LD 中，这是通过在此类属性上使用 `@container: @set` 来完成的，您将在示例中看到许多实例，其中属性有一个包含单个对象的数组。

上下文是为 JSON-LD 1.1 设计的，并使用称为"作用域上下文"的功能：为每个类或每个关系定义的子上下文，仅适用于该术语。这用于将所有各种分区关系映射到 `part` 和 `part_of`，而不管被分区的资源类型如何。此功能使 JSON 更易于读写，而不会失去单独底层术语的语义精度。

本体中的名称冲突和命名不一致已解决如下：

>
属性 | 键
-------- | ---
P2 | `classified_as`
P5 | `subState`
P5i | `subState_of`
P7i | `location_of`
P9 | `part`
P9i | `part_of`
P12 | `involved`
P14i | `carried_out`
P20i | `specific_purpose_of`
P28 | `transferred_custody_from`
P29 | `transferred_custody_to`
P29i | `acquired_custody_through`
P32 | `technique`
P33 | `specific_technique`
P35i | `condition_identified_by`
P37 | `assigned_identifier`
P37i | `identifier_assigned_by`
P42 | `assigned_type`
P42i | `type_assigned_by`
P45 | `made_of`
P46 | `part`
P46i | `part_of`
P50 | `current_custodian`
P50i | `current_custodian_of`
P56 | `bears`
P65 | `shows`
P74 | `residence`
P86 | `part_of`
P86i | `part`
P89 | `part_of`
P89i | `part`
P100i | `died`
P101 | `general_use`
P106 | `part`
P106i | `part_of`
P107 | `member`
P107i | `member_of`
P127 | `part_of`
P127i | `part`
P132 | `volume_overlaps_with`
P133 | `distinct_from`
P135i | `type_created_by`
P139 | `alternative`
P140 | `assigned_to`
P148 | `conceptual_part`
P148i | `conceptually_part_of`
P151i | `participated_in_formation`
P164i | `timespan_of_presence`
P165 | `presence_of`
P165i | `incorporated_by`
P168 | `defined_by`
P172 | `spatially_contains`
P177 | `assigned_property`
P186i | `type_produced_by`
P190 | `content`
P195 | `presence_of_thing`
P195i | `thing_presence`
P196i | `thing_defined_by`
la:has_member | `member`
la:member_of | `member_of`
skos:closeMatch | `close_match`
skos:exactMatch | `exact_match`
dcterms:conformsTo | `conforms_to`
dcterms:relation | `related`
schema:genre | `style`
rdfs:seeAlso | `see_also`
rdfs:label | `_label`
sci:O13_triggers | `caused`
sci:O13i_is_triggered_by | `caused_by`
sci:O19_encountered_object | `encountered`
sci:O19i_was_object_encountered_at | `encountered_by`