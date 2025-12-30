---
title: "Linked Art API：事件"
up_href: "/api/1.0/endpoint/"
up_label: "Linked Art API 1.0 端点"
-----




## 简介

事件 API 是获取时间段、事件或活动描述的方法，这些时间段、事件或活动不直接与其他实体相关联，也不是流传历史活动或展览，但仍然是以某种方式与艺术品相关的值得注意的事件。例如可能包括烧毁博物馆从而造成许多艺术品毁坏的火灾、研究艺术品某些方面的项目，或对象被创建的命名时期。虽然这些是不同的类，但在此用法中它们如此相似，以至于从 API 的角度来看它们被组合到单个端点中。事件 API 具有中等复杂度，具有许多其他端点的熟悉属性和模式，以及嵌入式事件熟悉的事件和活动属性。

## 属性定义

通过事件端点解析实体会得到一个包含单个 JSON 对象的 JSON-LD 文档，该对象具有以下属性。

### 事件的属性

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `@context`        | string, array | 必需    | 值必须是[Linked Art 上下文](../../json-ld/)的 URI，作为字符串 `"https://linked.art/ns/v1/linked-art.json"` 或数组，其中 URI 是最后一个条目以允许[扩展](../../json-ld/extensions) |
| `id`              | string        | 必需    | 值必须是事件表示可以[解析](../../protocol/)的 HTTP(S) URI |
| `type`            | string        | 必需    | 事件的类，必须是值 `"Period"`、`"Event"` 或 `"Activity"` |
| `_label`          | string        | 推荐    | 事件的人类可读标签，面向开发者 |
| `classified_as`   | array         | 推荐    | JSON 对象数组，每个对象都是事件的分类，必须遵循[类型](../../shared/type/)的要求 |
| `identified_by`   | array         | 推荐    | JSON 对象数组，每个对象都是事件的名称/标题，必须遵循[名称](../../shared/name/)的要求，或事件的标识符，必须遵循[标识符](../../shared/identifier/)的要求 |
| `referred_to_by`  | array         | 可选    | JSON 对象数组，每个对象都是关于事件的人类可读声明，必须遵循[声明](../../shared/statement/)的要求 |
| `equivalent`      | array         | 可选    | JSON 对象数组，每个对象都是对当前事件外部身份和描述的[引用](../../shared/reference) |
| `representation`  | array         | 可选    | JSON 对象数组，每个对象都是对代表当前事件的[视觉作品](../visual_work)的引用，必须遵循[引用](../../shared/reference/)的要求 |
| `member_of`       | array         | 可选    | JSON 对象数组，每个对象都是当前事件成员的集合，必须遵循对集合的[引用](../../shared/reference/)的要求 |
| `subject_of`      | array         | 可选    | JSON 对象数组，每个对象都是对[文本作品](../textual_work/)的引用，其内容聚焦于当前事件，必须遵循[引用](../../shared/reference/)的要求 |
| `attributed_by`   | array         | 可选    | JSON 对象数组，每个对象都是将当前事件与另一个实体相关联的[关系分配](../../shared/assignment/) |
| `part_of` | array | 可选 | JSON 对象数组，每个对象都是对当前事件直接所属的另一个事件的[引用](../../shared/reference/) |
| `timespan`        | json object   | 推荐    | 记录事件发生时间的 JSON 对象，必须遵循[时间段](../../shared/timespan/)的要求 |
| `during`          | array         | 可选    | JSON 对象数组，每个对象都是对发生此事件的广泛[时期](../event/)的[引用](../../shared/reference) |
| `before`          | array         | 可选    | JSON 对象数组，每个对象都是对此事件发生之前的时期、事件或活动的[引用](../../shared/reference) |
| `after`          | array         | 可选    | JSON 对象数组，每个对象都是对此事件发生之后的时期、事件或活动的[引用](../../shared/reference) |
| `took_place_at`   | array         | 可选    | JSON 对象数组，每个对象都是对事件发生的[地点](../place/)的[引用](../../shared/reference/) |
| `caused_by`       | array         | 可选    | JSON 对象数组，每个对象都是对导致此事件发生的另一个事件的[引用](../../shared/reference/)。**仅在 `type` 为 `"Event"` 或 `"Activity"` 时可用** |
| `influenced_by`   | array         | 可选    | JSON 对象数组，每个对象都是对以某种显著方式影响事件的实体的[引用](../../shared/reference/)。**仅在 `type` 为 `"Activity"` 时可用** |
| `carried_out_by`  | array         | 可选    | JSON 对象数组，每个对象都是对执行活动的[个人](../person/)或[群体](../group/)的[引用](../../shared/reference/)。**仅在 `type` 为 `"Activity"` 时可用** |
| `participant`  | array         | 可选    | JSON 对象数组，每个对象都是对参与事件但未执行事件的[个人](../person/)或[群体](../group/)的[引用](../../shared/reference/)。**仅在 `type` 为 "Event" 或 "Activity" 时可用** |
| `used_specific_object` | array    | 可选    | JSON 对象数组，每个对象都是对在执行活动中起重要作用的实体的[引用](../../shared/reference/)。**仅在 `type` 为 `"Activity"` 时可用** |
| `technique` | array | 可选 | JSON 对象数组，每个对象都是活动中使用的技术，必须遵循[类型](../../shared/type)的要求。**仅在 `type` 为 `"Activity"` 时可用** |

### 属性图

> ![diagram](event_properties.png){:.diagram_img width="600px"}

### JSON 模式

请参阅[模式文档](../../schema_docs/event)和[模式本身](../../schema/event.json)


### 引用属性

事件实例通常作为以下属性的对象出现，除了上述自引用属性。此列表并非详尽无遗，而是旨在涵盖其他端点可能引用事件的可能情况。

| 属性名称              | 源端点 | 描述 |
|----------------------------|-----------------|-------------|
| `part_of`                  | 所有             | 任何端点中的任何其他事件或活动都可以是更广泛的时期、事件或活动的 `part_of`。这意味着更广泛事件的空间和时间约束也适用于引用事件。 |


## 示例

描述 1820 年拍卖会的事件的 JSON 可能如下所示。

* 它在 `@context` 中包含 Linked Art 上下文文档引用
* 它在 `id` 中自文档化其 URI
* 它的 `type` 为 "Activity"（因为它由某个群体执行，因此不是事件或时期）
* 它有一个 `_label`，值为 "Foster Auction of March 1820"，供阅读 JSON 的人员使用
* 它被 `classified_as` 为 "Auction Event"（拍卖事件），`id` 为 "aat:300054751"
* 它被 `identified_by` 为...
    * ...一个 `Name`，内容为 "Edward Foster Auction of March 1820"
    * ...和一个 `Identifier`，内容为 "Br1908"，被 `classified_as` 为所有者分配的号码（"aat:300404621"）
* 它被 `referred_to_by` 为一个声明...
    * ... `content` 为 "Besides paintings, this sale ..."（除了绘画，此次销售...）
    * ...被 `classified_as` 为描述（"aat:300435416"）
* 它有一个 `timespan`（时间段）...
    * ...有一个显示标题，`content` 为 "1820 Mar 09"
    * ...有一个 `begin_of_the_begin`，值为 "1820-03-09T00:00:00Z"（3 月 9 日最早的可能时间）
    * ...有一个 `end_of_the_end`，值为 "1820-03-09T23:59:59Z"（3 月 9 日最晚的可能时间）
* 它 `took_place_at`（发生在）伦敦
* 它由群体 "Edward Foster & Son" `carried_out_by`（执行）
* 它 `used_specific_object`（使用特定对象）一个集合，包含所有拍卖拍品
* 它 `equivalent`（等同于）example.auction 处同一事件的另一个描述
* 它是销售目录文本的 `subject_of`


```crom
top = vocab.AuctionEvent(ident="auto int-per-segment", label="Foster Auction of March 1820")
top.identified_by = model.Name(content="Edward Foster Auction of March 1820")
top.identified_by = vocab.LocalNumber(content="Br1908")
top.carried_out_by = model.Group(ident="http://vocab.getty.edu/ulan/500451765", label="Edward Foster & Son")
top.took_place_at = model.Place(ident="http://vocab.getty.edu/tgn/7011781", label="London")
top.referred_to_by = vocab.Description(content="Besides paintings, this sale included a few lots with musical instruments and watches. The owners were a number of dealers who regularly consigned their wares to this auctioneer, despite the fact that the title page names \"A Gentleman\" as the owner.")
top.equivalent = model.Activity(ident="http://example.auction/past/foster/1820/03/1")
top.subject_of = model.LinguisticObject(ident="http://example.org/catalog/Br1908", label="Sales Catalog of Br-1908")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1820-03-09T00:00:00Z"
ts.end_of_the_end = "1820-03-09T23:59:59Z"
ts.identified_by = vocab.DisplayName(content="1820 Mar 09")
top.timespan = ts
top.used_specific_object = model.Set(ident="http://example.org/sets/Br1908", label="All Auction Lots of Br1908")
```
