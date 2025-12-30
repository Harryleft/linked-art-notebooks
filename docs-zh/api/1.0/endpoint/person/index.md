---
title: "Linked Art API：个人"
up_href: "/api/1.0/endpoint/"
up_label: "Linked Art API 1.0 端点"
-----




## 简介

个人 API 是获取在世或已故人物描述的方法。这将包括艺术家和收藏家，也包括对或使用艺术品执行其专业活动的博物馆工作人员，如策展人或保护员。个人模型具有中等复杂度，具有许多熟悉的属性和模式，加上一些更特定的字段。这产生了一个中等复杂度的 API，如果所有字段都有值，可能会导致相当长的 JSON 响应。

关于个人数据用法的更多信息，请参阅[个人模型](/model/actor/)描述。


## 属性定义

通过个人端点解析实体会得到一个包含单个 JSON 对象的 JSON-LD 文档，该对象具有以下属性。

### 个人的属性

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `@context`        | string, array | 必需    | 值必须是[Linked Art 上下文](../../json-ld/)的 URI，作为字符串 `"https://linked.art/ns/v1/linked-art.json"` 或数组，其中 URI 是最后一个条目以允许[扩展](../../json-ld/extensions) |
| `id`              | string        | 必需    | 值必须是个人表示可以[解析](../../protocol/)的 HTTP(S) URI |
| `type`            | string        | 必需    | 个人的类，必须是值 `"Person"` |
| `_label`          | string        | 推荐    | 个人的人类可读标签，面向开发者 |
| `classified_as`   | array         | 推荐    | JSON 对象数组，每个对象都是个人的分类，必须遵循[类型](../../shared/type/)的要求 |
| `identified_by`   | array         | 推荐    | JSON 对象数组，每个对象都是个人的名称，必须遵循[名称](../../shared/name/)的要求，或个人的标识符，必须遵循[标识符](../../shared/identifier/)的要求 |
| `referred_to_by`  | array         | 可选    | JSON 对象数组，每个对象都是关于个人的人类可读声明，必须遵循[声明](../../shared/statement/)的要求 |
| `equivalent`      | array         | 可选    | JSON 对象数组，每个对象都是对当前个人外部身份和描述的[引用](../../shared/reference) |
| `representation`  | array         | 可选    | JSON 对象数组，每个对象都是对代表当前个人的[视觉作品](../visual_work)的引用，必须遵循[引用](../../shared/reference/)的要求 |
| `member_of`       | array         | 可选    | JSON 对象数组，每个对象都是当前个人成员的集合，必须遵循对**[群体](../group/)**的[引用](../../shared/reference/)的要求 |
| `subject_of`      | array         | 可选    | JSON 对象数组，每个对象都是对[文本作品](../textual_work/)的引用，其内容聚焦于当前个人，必须遵循[引用](../../shared/reference/)的要求 |
| `attributed_by`   | array         | 可选    | JSON 对象数组，每个对象都是将当前个人与另一个实体相关联的[关系分配](../../shared/assignment/) |
| `contact_point` | array | 可选 | JSON 对象数组，每个对象都是个人可联系到的地址，必须遵循[标识符](../../shared/identifier)的要求 |
| `residence` | array | 可选 | 个人关联的地点，必须遵循对[地点](../place/)的[引用](../../shared/reference/)的要求 |
| `carried_out` | array | 可选 | JSON 对象数组，每个对象代表个人的专业活动，遵循[活动](../../shared/activity)的要求 |
| `participated_in` | array | 可选 | JSON 对象数组，每个对象代表个人参与但不负责的活动或事件，遵循[活动](../../shared/activity)的要求 |
| `born` | json object | 可选 | 表示个人出生的 JSON 对象，遵循[出生](../../shared/activity)的要求 |
| `died` | json object | 可选 | 表示个人死亡的 JSON 对象，遵循[死亡](../../shared/activity)的要求 |

### 属性图

> ![diagram](person_properties.png){:.diagram_img width="600px"}

### JSON 模式

请参阅[模式文档](../../schema_docs/person)和[模式本身](../../schema/person.json)


### 引用属性

个人实例通常作为以下属性的对象出现，除了上述自引用属性。此列表并非详尽无遗，而是旨在涵盖其他端点可能引用个人的可能情况。

| 属性名称              | 源端点 | 描述 |
|----------------------------|-----------------|-------------|
| `carried_out_by`           | 所有             | 个人执行的活动 |
| `current_owner`            | [对象](../physical_object/) | 个人拥有的对象 |
| `current_custodian`        | [对象](../physical_object/) | 个人保管的对象 |
| `current_permanent_custodian` | [对象](../physical_object/) | 通常由群体保管的对象 |
| `represents`               | [视觉作品](../visual_work/)     | 代表个人的图像内容（`representation` 的反向） |
| `about`                    | [文本作品](../textual_work/)    | 关于个人的文本内容 |
| `transferred_custody_to`   | [流传历史](../provenance_activity/)      | 将对象保管权转移给个人的活动 |
| `transferred_custody_from` | [流传历史](../provenance_activity/)      | 将对象保管权从个人转移出去的活动 |
| `transferred_title_to`     | [流传历史](../provenance_activity/)      | 将对象所有权转移给个人的活动 |
| `transferred_title_from`   | [流传历史](../provenance_activity/)      | 将对象所有权从个人转移出去的活动 |
| `paid_to`                  | [流传历史](../provenance_activity/)      | 从其他人向个人支付款项的活动 |
| `paid_from`                | [流传历史](../provenance_activity/)      | 从个人向其他人支付款项的活动 |


## 示例


艺术家伦勃朗的个人条目的 JSON 可能如下所示。

* 它在 `@context` 中包含 Linked Art 上下文引用
* 它在 `id` 中自文档化其 URI
* 它的 `type` 为 "Person"
* 它有一个 `_label`，值为 "Rembrandt"，供阅读 JSON 的人员使用
* 它有一个 `classified_as` 属性，包含...
    * ...男性，依次被 `classified_as` 为性别
    * ...荷兰人，依次被 `classified_as` 为国籍
* 它有一个 `identified_by` 属性，包含他的全名 "Rembrandt Harmenszoon van Rijn" 的 `Name`
* 它有一个 `referred_to_by` 声明，`classified_as` 为传记
* 它有一个 `born` 属性表示他的出生，包含 `timespan` 和 `took_place_at` 中的位置。
* 它有一个 `died` 属性表示他的死亡，包含 `timespan` 和 `took_place_at` 中的位置。
* 它有一个 `carried_out` 表示他的专业活动，同样包含 `timespan` 和 `took_place_at` 属性，还有 `classified_as` 为专业活动
* 它有一个 `equivalent` 等同于他的 ULAN 身份
* 它有一个 `residence` 包含对他居住地点的引用
* 它有一个 `contact_point` 用于他以前的街道地址

```crom
top = model.Person(ident="auto int-per-segment", label="Rembrandt")
n = model.Name(content="Rembrandt Harmenszoon van Rijn")
top.identified_by = n
b = model.Birth(label="Birth of Rembrandt")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1606-07-15T00:00:00Z"
ts.end_of_the_end = "1606-07-16T00:00:00Z"
b.timespan = ts
p = model.Place(label="Leiden")
b.took_place_at = p
top.born = b

d = model.Death(label="Death of Rembrandt")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1669-10-04T00:00:00Z"
ts.end_of_the_end = "1669-10-05T00:00:00Z"
d.timespan = ts
p = model.Place(label="Amsterdam")
d.took_place_at = p
top.died = d

top.referred_to_by = vocab.BiographyStatement(
	content="Rembrandt was a Dutch draughtsman, painter and printmaker.")

top.classified_as = vocab.instances['male']
top.classified_as = vocab.instances['dutch nationality']

act = vocab.Active(label="Active Dates")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1631-01-01T00:00:00Z"
ts.end_of_the_end = "1669-10-05T00:00:00Z"
act.timespan = ts
act.took_place_at = p
top.carried_out = act

top.residence = model.Place(label="Nieuwe Doelenstraat")
top.contact_point = vocab.StreetAddress(content="Jodenbreestraat 4, 1011NK Amsterdam")
top.equivalent = model.Person(ident="http://vocab.getty.edu/ulan/500011051", label="Rembrandt")


```
