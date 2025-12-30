---
title: "Linked Art API：文本作品"
up_href: "/api/1.0/endpoint/"
up_label: "Linked Art API 1.0 端点"
-----




## 简介

文本作品 API 是获取文本作品描述的方法，包括书籍、文章、手稿、诗歌或任何其他主要由文本组成的创作。文本作品模型具有中等复杂度，具有许多熟悉的属性和模式，以及描述语言、内容主题等的字段。

关于文本作品用法的更多信息，请参阅[文档模型](/model/document/)描述。


## 属性定义

通过文本作品端点解析实体会得到一个包含单个 JSON 对象的 JSON-LD 文档，该对象具有以下属性。

### 文本作品的属性

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `@context`        | string, array | 必需    | 值必须是[Linked Art 上下文](../../json-ld/)的 URI，作为字符串 `"https://linked.art/ns/v1/linked-art.json"` 或数组，其中 URI 是最后一个条目以允许[扩展](../../json-ld/extensions) |
| `id`              | string        | 必需    | 值必须是文本作品表示可以[解析](../../protocol/)的 HTTP(S) URI |
| `type`            | string        | 必需    | 文本作品的类，必须是值 `"LinguisticObject"` |
| `_label`          | string        | 推荐    | 文本作品的人类可读标签，面向开发者 |
| `classified_as`   | array         | 推荐    | JSON 对象数组，每个对象都是文本作品的分类，必须遵循[类型](../../shared/type/)的要求 |
| `identified_by`   | array         | 推荐    | JSON 对象数组，每个对象都是文本作品的名称/标题，必须遵循[名称](../../shared/name/)的要求，或文本作品的标识符，必须遵循[标识符](../../shared/identifier/)的要求 |
| `referred_to_by`  | array         | 可选    | JSON 对象数组，每个对象都是关于文本作品的人类可读声明，必须遵循[声明](../../shared/statement/)的要求 |
| `equivalent`      | array         | 可选    | JSON 对象数组，每个对象都是对当前文本作品外部身份的[引用](../../shared/reference) |
| `member_of`       | array         | 可选    | JSON 对象数组，每个对象都是当前文本作品成员的集合，必须遵循对集合的[引用](../../shared/reference/)的要求 |
| `subject_of`      | array         | 可选    | JSON 对象数组，每个对象都是对其他[文本作品](../textual_work/)的引用，其内容聚焦于当前文本作品，必须遵循[引用](../../shared/reference/)的要求 |
| `representation`  | array         | 可选    | JSON 对象数组，每个对象都是对代表当前文本作品的[视觉作品](../visual_work)的引用，必须遵循[引用](../../shared/reference/)的要求 |
| `attributed_by`   | array         | 可选    | JSON 对象数组，每个对象都是将当前文本作品与另一个实体相关联的[关系分配](../../shared/assignment/) |
| `language` | array | 可选 | JSON 对象数组，每个对象都是文本作品所表达的语言，必须遵循[语言](../../shared/type)的要求 |
| `dimension` | array | 可选 | JSON 对象数组，每个对象都是当前文本作品的[维度](../../shared/dimension)，如总字数 |
| `part_of` | array | 可选 | JSON 对象数组，每个对象都是对当前文本作品所属的另一个文本作品或[视觉作品](../visual_work/)的[引用](../../shared/reference/) |
| `conceptually_part_of` | array | 可选 | JSON 对象数组，每个对象都是对当前作品概念上所属的[抽象作品](../abstract_work/)的[引用](../../shared/reference/) |
| `content` | string | 可选 | 作品文本内容的字符串表示 |
| `format` | string | 可选 | `content` 属性中给出的字符串表示的编码的媒体类型 |
| `about` | array | 可选 | JSON 对象数组，每个对象都是对此文本主要关于的任何类型的另一个实体的[引用](../../shared/reference/) |
| `subject_to` | array | 可选 | JSON 对象数组，每个对象都是对知识产权作品持有的[权利](../../shared/right) |
| `created_by` | json object | 可选 | 表示文本作品创建的 JSON 对象，遵循[创建](../../shared/activity)的要求 |
| `used_for` | array | 可选 | JSON 对象数组，每个对象都是出版活动，遵循[活动](../../shared/activity)的要求 |

### 属性图

> ![diagram](text_properties.png){:.diagram_img width="600px"}

### JSON 模式

请参阅[模式文档](../../schema_docs/text)和[模式本身](../../schema/text.json)


### 引用属性

文本作品实例通常作为以下属性的对象出现，除了上述自引用属性。此列表并非详尽无遗，而是旨在涵盖其他端点可能引用文本作品的可能情况。

| 属性名称              | 源端点 | 描述 |
|----------------------------|-----------------|-------------|
| `subject_of`               | 所有             | 任何实体都可以是文本内容的主题 |
| `carries`                  | [物理对象](../physical_object/) | 物理对象可以承载文本，如手稿及其页面上书写的文本 |
| `digitally_carries`        | [数字对象](../digital_object/)  | 数字对象也可以数字承载文本，如 Word 文档和其中编码的文本 |

## 示例

关于 Gainsborough 作品的书籍的文本作品条目的 JSON 可能如下所示。

* 它在 `@context` 中包含 Linked Art 上下文文档引用
* 它在 `id` 中自文档化其 URI
* 它的 `type` 为 "LinguisticObject"
* 它有一个 `_label`，值为 "Gainsborough by Hayes"，供阅读 JSON 的人员使用
* 它被 `classified_as` 为 "Monograph"（专著），`id` 为 "aat:300060417"
* 它被 `identified_by` 为...
    * ...一个 `Name`，内容为 "Gainsborough: Paintings and Drawings"
    * ...一个 `Identifier`，内容为 "0714816396"，被 `classified_as` 为 ISBN（"aat:300417443"）
* 它被 `referred_to_by` 为一个声明...
    * ... `content` 为 "A thorough analysis of the artist's life and work"（对艺术家生活和作品的彻底分析）
    * ...被 `classified_as` 为摘要（"aat:"）
* 它有一个 `language` 为英语（"aat:300388277"）
* 它 `about` Gainsborough，一个 `id` 为 "ulan:500115200" 的个人
* 它被 `created_by` 一个创建...
    * ...由 John Hayes `carried_out_by`（执行），一个个人
* 它被 `used_for` 一个活动...
    * ...被 `classified_as` 为出版（"aat:300054686"）
    * ... `took_place_at`（发生在）纽约
    * ...由 Phaidon `carried_out_by`（执行），一个群体

```crom
top = vocab.MonographText(ident="auto int-per-segment", label="Gainsborough by Hayes")
top.identified_by = vocab.PrimaryName(content="Gainsborough: Paintings and Drawings")
top.identified_by = vocab.IsbnIdentifier(content="0714816396")
top.referred_to_by = vocab.Abstract(content="A thorough analysis of the artist's life and work")
top.language = vocab.instances['english']
top.about = model.Person(ident="http://vocab.getty.edu/ulan/500115200", label="Gainsborough, Thomas")
pub = vocab.Publishing()
pub.carried_out_by = model.Group(label="Phaidon")
pub.took_place_at = model.Place(label="New York")
ts = model.TimeSpan()
ts._label = "1975"
ts.begin_of_the_begin = "1975-01-01T00:00:00Z"
ts.end_of_the_end = "1975-12-31T23:59:59Z"
pub.timespan = ts
top.used_for = pub
cre = model.Creation()
cre.carried_out_by = model.Person(label="Hayes, John")
top.created_by = cre
```
