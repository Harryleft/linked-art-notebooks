---
title: "Linked Art API：集合"
up_href: "/api/1.0/endpoint/"
up_label: "Linked Art API 1.0 端点"
-----




## 简介

集合 API 是获取集合描述的方法，包括藏品集合、系列、展览集合或任何其他可识别的对象集合。集合模型具有中等复杂度，具有许多熟悉的属性和模式，以及描述集合成员关系的字段。

关于集合数据用法的更多信息，请参阅[集合模型](/model/collection/)描述。


## 属性定义

通过集合端点解析实体会得到一个包含单个 JSON 对象的 JSON-LD 文档，该对象具有以下属性。

### 集合的属性

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `@context`        | string, array | 必需    | 值必须是[Linked Art 上下文](../../json-ld/)的 URI，作为字符串 `"https://linked.art/ns/v1/linked-art.json"` 或数组，其中 URI 是最后一个条目以允许[扩展](../../json-ld/extensions) |
| `id`              | string        | 必需    | 值必须是集合表示可以[解析](../../protocol/)的 HTTP(S) URI |
| `type`            | string        | 必需    | 集合的类，必须是值 `"Set"` |
| `_label`          | string        | 推荐    | 集合的人类可读标签，面向开发者 |
| `classified_as`   | array         | 推荐    | JSON 对象数组，每个对象都是集合的分类，必须遵循[类型](../../shared/type/)的要求 |
| `identified_by`   | array         | 推荐    | JSON 对象数组，每个对象都是集合的名称，必须遵循[名称](../../shared/name/)的要求，或集合的标识符，必须遵循[标识符](../../shared/identifier/)的要求 |
| `referred_to_by`  | array         | 可选    | JSON 对象数组，每个对象都是关于集合的人类可读声明，必须遵循[声明](../../shared/statement/)的要求 |
| `equivalent`      | array         | 可选    | JSON 对象数组，每个对象都是对当前集合外部身份和描述的[引用](../../shared/reference) |
| `representation`  | array         | 可选    | JSON 对象数组，每个对象都是对代表当前集合的[视觉作品](../visual_work)的引用，必须遵循[引用](../../shared/reference/)的要求 |
| `member_of`       | array         | 可选    | JSON 对象数组，每个对象都是当前集合成员的另一个集合，必须遵循对集合的[引用](../../shared/reference/)的要求 |
| `subject_of`      | array         | 可选    | JSON 对象数组，每个对象都是对[文本作品](../textual_work/)的引用，其内容聚焦于当前集合，必须遵循[引用](../../shared/reference/)的要求 |
| `attributed_by`   | array         | 可选    | JSON 对象数组，每个对象都是将当前集合与另一个实体相关联的[关系分配](../../shared/assignment/) |
| `dimension`       | array | 可选 | JSON 对象数组，每个对象都是当前集合的[维度](../../shared/dimension)，如成员总数 |
| `about`           | array | 可选 | JSON 对象数组，每个对象都是对此集合主要关于或作为主题的任何类型的另一个实体的[引用](../../shared/reference) |
| `members_exemplified_by` | array | 可选 | JSON 对象数组，每个对象要么是遵循 Linked Art API 端点之一的模式的嵌入结构，要么是对任何 Linked Art 资源的引用 |
| `members_contained_by` | array | 可选 | JSON 对象数组，每个对象都是对保存或包含当前集合的（物理）成员的[物理对象](../physical_object/)的引用 |
| `created_by`      | json object | 可选 | 表示集合创建的 JSON 对象，遵循[创建](../../shared/activity)的要求 |
| `used_for`        | array | 可选 | JSON 对象数组，每个对象都是出版（或类似活动），遵循[活动](../../shared/activity)的要求 |


### 属性图

> ![diagram](set_properties.png){:.diagram_img width="600px"}

### JSON 模式

请参阅[模式文档](../../schema_docs/set)和[模式本身](../../schema/set.json)

请注意，`members_exemplified_by` 属性只能进行最小程度的验证。


### 引用属性

集合实例通常作为以下属性的对象出现，除了上述自引用属性。此列表并非详尽无遗，而是旨在涵盖其他端点可能引用集合的可能情况。

| 属性名称              | 源端点 | 描述 |
|----------------------------|-----------------|-------------|
| `member_of`                | 所有             | 除个人或群体之外的实体可以是集合的成员。（个人和群体是群体的成员） |
| `used_specific_object`     | [事件](../event/) | [事件](../事件/)可以使用事物集合，例如展览或拍卖拍品中的对象集合 |


## 示例

大都会艺术博物馆收藏的集合条目的 JSON 可能如下所示。

* 它在 `@context` 中包含 Linked Art 上下文文档引用
* 它在 `id` 中自文档化其 URI
* 它的 `type` 为 "Set"
* 它有一个 `_label`，值为 "Collection of the Met"，供阅读 JSON 的人员使用
* 它被 `classified_as` 为一个 "Collection"（收藏），`id` 为 "aat:300025976"
* 它被 `identified_by` 为一个 `Name`，内容为 "Art Collection of the Metropolitan Museum of Art"
* 它被 `referred_to_by` 为一个声明...
    * ... `content` 为 "Over 2 million works ..."（超过 200 万件作品...）
    * ...被 `classified_as` 为描述（"aat:300435416"）
* 它被 `created_by` 一个创建...
    * ...在 "1870-04-13T00:00:00Z" 和 "1870-04-13T23:59:59Z" 之间的 `timespan`（时间段）内


```crom
top = vocab.CollectionSet(ident="auto int-per-segment", label="Collection of the Met")
n = model.Name(content="Art Collection of the Metropolitan Museum of Art")
top.identified_by = n
top.referred_to_by = vocab.Description(content="Over 2 million works, divided into 17 curatorial departments")
cre = model.Creation()
ts = model.TimeSpan()
ts._label = "April 13th, 1870"
ts.begin_of_the_begin = "1870-04-13T00:00:00Z"
ts.end_of_the_end = "1870-04-13T23:59:59Z"
cre.timespan = ts
top.created_by = cre
```

