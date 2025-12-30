---
title: "Linked Art API：地点"
up_href: "/api/1.0/endpoint/"
up_label: "Linked Art API 1.0 端点"
-----




## 简介

地点 API 是获取地点描述的方法，包括城市、建筑物、具体房间或地理区域。地点模型具有中等复杂度，具有许多熟悉的属性和模式，以及描述地理坐标、层级关系等的字段。这产生了一个中等复杂度的 API。

关于地点用法的更多信息，请参阅[地点模型](/model/place/)描述。

## 属性定义

通过地点端点解析实体会得到一个包含单个 JSON 对象的 JSON-LD 文档，该对象具有以下属性。

### 地点的属性

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `@context`        | string, array | 必需    | 值必须是[Linked Art 上下文](../../json-ld/)的 URI，作为字符串 `"https://linked.art/ns/v1/linked-art.json"` 或数组，其中 URI 是最后一个条目以允许[扩展](../../json-ld/extensions) |
| `id`              | string        | 必需    | 值必须是地点表示可以[解析](../../protocol/)的 HTTP(S) URI |
| `type`            | string        | 必需    | 地点的类，必须是值 `"Place"` |
| `_label`          | string        | 推荐    | 地点的人类可读标签，面向开发者 |
| `classified_as`   | array         | 推荐    | JSON 对象数组，每个对象都是地点的分类，必须遵循[类型](../../shared/type/)的要求 |
| `identified_by`   | array         | 推荐    | JSON 对象数组，每个对象都是地点的名称，必须遵循[名称](../../shared/name/)的要求，或地点的标识符，必须遵循[标识符](../../shared/identifier/)的要求 |
| `referred_to_by`  | array         | 可选    | JSON 对象数组，每个对象都是关于地点的人类可读声明，必须遵循[声明](../../shared/statement/)的要求 |
| `equivalent`      | array         | 可选    | JSON 对象数组，每个对象都是对当前地点外部身份和描述的[引用](../../shared/reference) |
| `representation`  | array         | 可选    | JSON 对象数组，每个对象都是对代表当前地点的[视觉作品](../visual_work)的引用，必须遵循[引用](../../shared/reference/)的要求 |
| `member_of`       | array         | 可选    | JSON 对象数组，每个对象都是对当前地点成员的[集合](../set/)的引用，必须遵循[引用](../../shared/reference/)的要求 |
| `subject_of`      | array         | 可选    | JSON 对象数组，每个对象都是对[文本作品](../textual_work/)的引用，其内容聚焦于当前地点，必须遵循[引用](../../shared/reference/)的要求 |
| `attributed_by`   | array         | 可选    | JSON 对象数组，每个对象都是将当前地点与另一个实体相关联的[关系分配](../../shared/assignment/) |
| `part_of`         | array         | 可选    | JSON 对象数组，每个对象都是当前地点所属的地点，必须遵循对地点的[引用](../../shared/reference/)的要求 |
| `defined_by`      | string        | 可选    | 包含地点几何形状的 [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) 表示的字符串 |


### 属性图

> ![diagram](place_properties.png){:.diagram_img width="600px"}

### JSON 模式

请参阅[模式文档](../../schema_docs/place)和[模式本身](../../schema/place.json)


### 引用属性

地点实例通常作为以下属性的对象出现，除了上述自引用属性。此列表并非详尽无遗，而是旨在涵盖其他端点可能引用地点的可能情况。

| 属性名称      | 源端点 | 描述 |
|--------------------|-----------------|-------------|
| `took_place_at`    | 所有 | 所有事件和活动都可以在地点发生，这出现在大多数端点中，如个人出生的位置或标识符分配的位置 |
| `current_location` | [对象](../physical_object/) | 对象的当前位置记录在对象 API 中 |
| `current_permanent_location` | [物理对象](../physical_object/) | 对象的通常位置也记录在对象 API 中 |
| `moved_from`       | [流传历史](../provenance_activity/) | 在流传历史活动中，对象可以在 `移动` 活动中从一个地点移动... |
| `moved_to`         | [流传历史](../provenance_activity/) | ...到另一个地点 |
| `residence`        | [个人](../person/)、[群体](../group/) | 个人和群体有他们居住或曾居住过的地点 |


## 示例

洛杉矶城市的地点条目的 JSON 可能如下所示。

* 它在 `@context` 中包含 Linked Art 上下文文档引用
* 它在 `id` 中自文档化其 URI
* 它的 `type` 为 "Place"
* 它有一个 `_label`，值为 "Los Angeles"，供阅读 JSON 的人员使用
* 它被 `classified_as` 为一个城市，`id` 为 _aat:300008389_，`type` 为类型，以及一个标签。
* 它被 `identified_by` 为一个 `Name`，`content` 为 "Los Angeles"
* 它被 `identified_by` 为一个 `Identifier`，`content` 为 "06-44000"
* 它被 `defined_by` 为一个特定的 WKT 多边形
* 它被 `referred_to_by` 为一个 `LinguisticObject`，被 `classified_as` 为描述（_aat:300435416_），`content` 为 "Los Angeles is the largest city in California"（洛杉矶是加利福尼亚州最大的城市）
* 它 `part_of` 另一个 `Place`，即加利福尼亚州
* 它是前 10 大美国城市 `Set` 的 `member_of`
* 它等同于 TGN 条目


```crom
top = vocab.City(ident="auto int-per-segment", label="Los Angeles")
top.identified_by = model.Name(content="Los Angeles")
top.identified_by = model.Identifier(content="06-44000")
top.referred_to_by = vocab.Description(content="Los Angeles is the largest city in California")
top.defined_by = "POLYGON((-118.574 34.185,-117.558 34.185,-117.5585 33.512,-118.574 33.512,-118.5745 34.185))"
top.part_of = model.Place(label="California")
top.member_of = model.Set(label="Top 10 Cities in USA")
top.equivalent = model.Place(ident="http://vocab.getty.edu/tgn/7023900", label="Los Angeles")
```


### 引用示例

一个[物理对象](../physical_object/)通过 `current_location` 和创建位置引用两个地点。

```crom
top = model.HumanMadeObject(ident="auto int-per-segment",label="Van Gogh Painting")
top.current_location = model.Place(label="Rijksmuseum Gallery")
top.produced_by = model.Production(label="Production of Painting")
top.produced_by.took_place_at = model.Place(label="Amsterdam")
```
