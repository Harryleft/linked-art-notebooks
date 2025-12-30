---
title: "Linked Art API: 标识符结构"
up_href: "/api/1.0/shared/"
up_label: "Linked Art API 1.0 共享数据结构"
---





## 简介

标识符是分配给某个资源以在特定上下文中标识它的字符串形式的代码。所有不同类型的实体都可以分配标识符。标识符在结构上与[名称](../name/)非常相似，但明确不是自然语言的一部分，因此没有 `language` 属性，也不能被翻译或有替代形式，因此单独记录。

标识符在模型文档的[基础模式](/model/base/#types-and-classifications)中描述，实际上每个类都有示例。

## 属性定义

标识符具有以下属性。

### 标识符的属性

| 属性名称          | 数据类型      | 要求        | 描述 |
|-------------------|---------------|-------------|-------------|
| `id`              | string        | 可选        | 如果存在，值必须是标识标识符的 URI，可以从该 URI 检索分配的表示 |
| `type`            | string        | 必需        | 名称的类，必须是值 `"Identifier"` |
| `_label`          | string        | 推荐        | 易读标签，面向开发人员 |
| `_complete`       | boolean       | 可选        | 非语义。如果存在带有 URI 的 `id` 属性，并且从该 URI 的表示中可以获得关于标识符的更多信息，那么 `_complete` 必须存在，值为 `false`，以通知消费应用程序它可能想要检索它 |
| `content`         | string        | 必需        | 标识符的字符串内容 |
| `classified_as`   | array         | 推荐        | json 对象数组，每个都是标识符的进一步分类，必须遵循 [类型](../type/) 的要求 |
| `identified_by`   | array         | 推荐        | json 对象数组，每个都是为标识符显示的名称，必须遵循 [名称](../name/) 的要求 |
| `referred_to_by`  | array         | 可选        | json 对象数组，每个都是引用标识符的 [文本作品](../../endpoint/textual_work/) 的 [引用](../reference/)，或者是关于标识符的嵌入 [陈述](../statement/)。 |
| `assigned_by`     | array         | 可选        | json 对象数组，每个都是标识符的分配，必须遵循 [分配](../assignment/) 的要求 |

### 属性图

> ![图](identifier_properties.png){:.diagram_img width="600px"}


### 传入属性

标识符实例通常作为以下属性的对象被找到。此列表并不详尽，但旨在涵盖可能的情况。

| 属性名称   | 源端点   | 描述 |
|-----------------|-------------------|-------------|
| `identified_by` | 所有端点     | 最常见的情况是资源由标识符标识，可以在每个端点中找到 |
| `contact_point` | [人物](../../endpoint/person/)、[团体](../../endpoint/group/) | 人物和团体也可以有联系点，建模为标识符。 |

## 示例

对象的入藏号，在1997年的某个时间由示例博物馆创建和分配。

* 它在 `id` 中给出了一个 URI（标识标识符，而不是对象）
* 它的 `type` 是 "Identifier"
* 它有一个易读的 `_label` "示例博物馆入藏号" 来解释它是什么
* 它 `classified_as` 为入藏号，`id` 为 _aat:300312355_，`type` 为 Type
* 它 `referred_to_by` 一个陈述，`type` 为 "LinguisticObject"，`content` 为 "这是原始..."。LinguisticObject `classified_as` 为笔记，`id` 为 _aat:300418049_，`type` 为 Type
* 它的 `content` 值为 "1997-A1752"
* 它 `assigned_by` 一个标识符分配，该分配...
    * ...在 `id` 中给出了一个 URI（标识分配）
    * ...的 `type` 为 "AttributeAssignment"
    * ...有一个 `timespan` 结构，`begin_of_the_begin` 日期为 1997 年 1 月 1 日，`end_of_the_end` 日期为 1997 年 12 月 31 日
    * ... `carried_out_by` 创建标识符的组织的 [引用](../reference/)，`type` 为 "Group"

```crom
top = model.HumanMadeObject(ident="auto int-per-segment")
id = vocab.AccessionNumber(label="示例博物馆入藏号", content="1997-A1752")
top.identified_by = id
id.identified_by = vocab.PrimaryName(content="入藏号")
id.referred_to_by = vocab.Note(content="这是 1997 年的原始入藏号")
aa = model.AttributeAssignment(label="分配 1997-A1752")
id.assigned_by = aa
aa.carried_out_by = model.Group(label="示例博物馆")
ts = model.TimeSpan(label="1997")
aa.timespan = ts
ts.begin_of_the_begin = "1997-01-01T00:00:00Z"
ts.end_of_the_end = "1997-12-31T00:00:00Z"
```
