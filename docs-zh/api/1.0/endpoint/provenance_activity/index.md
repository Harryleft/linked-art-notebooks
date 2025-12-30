---
title: "Linked Art API：流传历史活动"
up_href: "/api/1.0/endpoint/"
up_label: "Linked Art API 1.0 端点"
---




## 简介

流传历史活动 API 是获取...描述的方法。该 API 的复杂度高于平均水平，具有许多熟悉的属性和模式，但也有一系列传达较高级别活动部分的类，每个类都有自己的独特属性。

## 属性定义

通过流传历史活动端点解析实体会得到一个包含单个 JSON 对象的 JSON-LD 文档，该对象具有以下属性。

### 流传历史活动的属性

顶级活动具有以下属性。

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `@context`        | string, array | 必需    | 值必须是[Linked Art 上下文](../../json-ld/)的 URI，作为字符串 `"https://linked.art/ns/v1/linked-art.json"` 或数组，其中 URI 是最后一个条目以允许[扩展](../../json-ld/extensions) |
| `id`              | string        | 必需    | 值必须是事件表示可以[解析](../../protocol/)的 HTTP(S) URI |
| `type`            | string        | 必需    | 事件的类，必须是值 `"Event"` 或值 `"Activity"` |
| `_label`          | string        | 推荐    | 事件的人类可读标签，面向开发者 |
| `classified_as`   | array         | 必需    | JSON 对象数组，每个对象都是事件的分类，必须遵循[类型](../../shared/type/)的要求 |
| `identified_by`   | array         | 推荐    | JSON 对象数组，每个对象都是事件的名称/标题，必须遵循[名称](../../shared/name/)的要求，或事件的标识符，必须遵循[标识符](../../shared/identifier/)的要求 |
| `referred_to_by`  | array         | 可选    | JSON 对象数组，每个对象都是关于事件的人类可读声明，必须遵循[声明](../../shared/statement/)的要求 |
| `equivalent`      | array         | 可选    | JSON 对象数组，每个对象都是对当前事件的外部身份和描述的[引用](../../shared/reference) |
| `representation`  | array         | 可选    | JSON 对象数组，每个对象都是对代表当前事件的[视觉作品](../visual_work)的引用，必须遵循[引用](../../shared/reference/)的要求 |
| `member_of`       | array         | 可选    | JSON 对象数组，每个对象都是当前事件是其成员的集合，必须遵循对集合的[引用](../../shared/reference/)的要求 |
| `subject_of`      | array         | 可选    | JSON 对象数组，每个对象都是对[文本作品](../textual_work/)的引用，其内容聚焦于当前事件，必须遵循[引用](../../shared/reference/)的要求 |
| `attributed_by`   | array         | 可选    | JSON 对象数组，每个对象都是将当前事件与另一个实体相关联的[关系分配](../../shared/assignment/) |
| `part_of` | array | 可选 | JSON 对象数组，每个对象都是对当前事件所属的另一个事件的[引用](../../shared/reference/) |
| `timespan`        | json object   | 推荐    | 记录事件发生时间的 JSON 对象，必须遵循[时间段](../../shared/timespan/)的要求|
| `during`          | array         | 可选    | JSON 对象数组，每个对象都是对流传历史活动发生的[时期](../event/)的[引用](../../shared/reference) |
| `before`          | array         | 可选    | JSON 对象数组，每个对象都是对此事件发生之前的时期、事件或活动的[引用](../../shared/reference) |
| `after`          | array         | 可选    | JSON 对象数组，每个对象都是对此事件发生之后的时期、事件或活动的[引用](../../shared/reference) |
| `took_place_at`   | array         | 可选    | JSON 对象数组，每个对象都是对事件发生的[地点](../place/)的[引用](../../shared/reference/) |
| `caused_by`       | array         | 可选    | JSON 对象数组，每个对象都是对导致事件发生的[事件](../event/)的[引用](../../shared/reference/) |
| `influenced_by`   | array         | 可选    | JSON 对象数组，每个对象都是对以某种显著方式影响事件的实体的[引用](../../shared/reference/) |
| `carried_out_by`  | array         | 可选    | JSON 对象数组，每个对象都是对执行活动的[个人](../person/)或[群体](../group/)的[引用](../../shared/reference/) |
| `participant`  | array         | 可选    | JSON 对象数组，每个对象都是对参与活动但未执行活动的[个人](../person/)或[群体](../group/)的[引用](../../shared/reference/) |
| `used_specific_object` | array    | 可选    | JSON 对象数组，每个对象都是对在执行活动中起作用的实体的[引用](../../shared/reference) |
| `part` | array | 必需 | 活动组成的更详细的变化，如下所述|


#### 必需分类

为了确定活动是流传历史活动，而不是更一般的事件或活动（后者将遵循[事件](../event/) API），活动必须具有 `classified_as` 条目，其 `id` 为 `"http://vocab.getty.edu/aat/300055863"`。

```crom
top = vocab.ProvenanceEntry(ident="auto int-per-segment", label="Provenance Activity")
```


### 所有部分的属性

`part` 属性中的每个活动都可以具有下表中的属性。不同类型的活动有自己的 `type` 和其他属性，这些在以下小节中定义。

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `id`              | string        | 可选    | 如果存在，值必须是标识流传历史部分活动的 URI |
| `type`            | string        | 必需    | 部分的类，必须是下面小节中给出的值 |
| `_label`          | string        | 推荐    | 流传历史部分的人类可读标签，面向开发者 |
| `identified_by`   | array         | 推荐    | JSON 对象数组，每个对象都是流传历史部分的名称，必须遵循[名称](../../shared/name/)的要求，或部分的标识符，必须遵循[标识符](../../shared/identifier/)的要求 |
| `classified_as`   | array         | 推荐    | JSON 对象数组，每个对象都是流传历史部分的进一步分类，必须遵循[类型](../../shared/type/)的要求 |
| `referred_to_by`  | array         | 可选    | JSON 对象数组，每个对象都是关于部分的嵌入式[声明](../../shared/statement/) |
| `timespan`        | json object   | 推荐    | 记录部分发生时间的 JSON 对象，必须遵循[时间段](../../shared/timespan/)的要求|
| `during`          | array         | 可选    | JSON 对象数组，每个对象都是对部分活动发生的[时期](../event/)的[引用](../../shared/reference) |
| `took_place_at`   | array         | 可选    | JSON 对象数组，每个对象都是对部分活动发生的[地点](../place/)的[引用](../../shared/reference/) |
| `influenced_by`   | array         | 可选    | JSON 对象数组，每个对象都是对以某种显著方式影响部分活动但未执行它的实体的[引用](../../shared/reference/) |
| `carried_out_by`  | array         | 可选    | JSON 对象数组，每个对象都是对执行部分活动的[个人](../person/)或[群体](../group/)的[引用](../../shared/reference/) |
| `participant`  | array         | 可选    | JSON 对象数组，每个对象都是对参与部分活动但未执行它的[个人](../person/)或[群体](../group/)的[引用](../../shared/reference/) |
| `used_specific_object` | array    | 可选    | JSON 对象数组，每个对象都是对在执行部分活动中起作用的实体的[引用](../../shared/reference) |

#### 部分：获得的属性

作为获得的部分具有以下附加属性。

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `type`            | string        | 必需    | 部分的类，必须是值 `"Acquisition"` |
| `transferred_title_of`   | array | 必需 | JSON 对象数组，每个对象都是所有权转移的[对象](../physical_object/)的[引用](../../shared/reference) |
| `transferred_title_from` | array       | 可选 | JSON 对象数组，每个对象都是对[个人](../person/)或[群体](../group/)的[引用](../../shared/reference)，每个都是对象的前所有者，对象的所有权从其转移 |
| `transferred_title_to`   | array       | 可选 | JSON 对象数组，每个对象都是对[个人](../person/)或[群体](../group/)的[引用](../../shared/reference)，每个都是对象的所有权转移给的新所有者之一 |


#### 部分：支付的属性

作为支付的部分具有以下附加属性。

| 属性名称     | 数据类型    | 要求 | 描述 |
|-------------------|-------------|-------------|-------------|
| `type`            | string      | 必需 | 部分的类，必须是值 `"Payment"` |
| `paid_amount`     | json object | 可选 | 编码转移金额的[货币金额](../../shared/money/)结构 |
| `paid_from`       | array       | 可选 | JSON 对象数组，每个对象都是对提供部分货币金额的[个人](../person/)或[群体](../group/)的[引用](../../shared/reference) |
| `paid_to`         | array       | 可选 | JSON 对象数组，每个对象都是对接收部分货币金额的[个人](../person/)或[群体](../group/)的[引用](../../shared/reference) |

#### 部分：保管权转移的属性

作为保管权转移的部分具有以下附加属性。

| 属性名称     | 数据类型       | 要求 | 描述 |
|-------------------|----------------|-------------|-------------|
| `type`            | string         | 必需    | 部分的类，必须是值 `"TransferOfCustody"` |
| `transferred_custody_of`   | array | 必需    | JSON 对象数组，每个对象都是保管权转移的[对象](../physical_object/)的[引用](../../shared/reference) |
| `transferred_custody_from` | array | 可选    | JSON 对象数组，每个对象都是对[个人](../person/)或[群体](../group/)的[引用](../../shared/reference)，每个都是对象的前保管人，对象的保管权从其转移|
| `transferred_custody_to`   | array | 可选    | JSON 对象数组，每个对象都是对[个人](../person/)或[群体](../group/)的[引用](../../shared/reference)，每个都是对象的前保管人，对象的保管权从其转移|

#### 部分：相遇的属性

作为相遇的部分具有以下附加属性。

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `type`            | string        | 必需    | 部分的类，必须是值 `"Encounter"` |
| `encountered`     | array         | 必需    | JSON 对象数组，每个对象都是被相遇的[对象](../object/)的[引用](../../shared/reference) |

#### 部分：权利获得的属性

作为权利获得的部分具有以下附加属性。

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `type`            | string        | 必需    | 部分的类，必须是值 `"RightAcquisition"` |
| `establishes`     | array         | 必需    | JSON 对象数组，每个对象都是 `Right` 结构，如下所述 |
| `invalidates`     | array         | 可选    | JSON 对象数组，每个对象都是 `Right` 结构，如下所述 |

#### 部分：移动的属性

作为移动的部分具有以下附加属性。

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `type`            | string        | 必需    | 部分的类，必须是值 `"Move"` |
| `moved`           | array         | 必需    | JSON 对象数组，每个对象都是被此活动移动的[对象](../object)的[引用](../../shared/reference) |
| `moved_from`      | json object   | 可选    | 对所有对象移动来源的[地点](../place/)的[引用](../../shared/reference/) |
| `moved_to`        | json object   | 可选    | 对所有对象移动到的[地点](../place/)的[引用](../../shared/reference/) |


#### 部分：承诺的属性

作为承诺的部分具有以下附加属性。

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `type`            | string        | 必需    | 部分的类，必须是值 `"Activity"` |
| `classified_as`   | array         | 必需    | JSON 对象数组，每个对象都是创作或出版的进一步分类，必须遵循[类型](../../shared/type/)的要求，并且数组中的一个条目必须具有值为 "http://vocab.getty.edu/aat/300435599" 的 `id`，以便将此活动区分为承诺 |

#### 部分：转移的属性

作为未知类型的转移的部分具有以下附加属性。

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `type`            | string        | 必需    | 部分的类，必须是值 `"Transfer"` |
| `transferred`   | array | 必需 | JSON 对象数组，每个对象都是以某种方式转移的[对象](../object/)的[引用](../../shared/reference) |
| `transferred_from` | array       | 可选 | JSON 对象数组，每个对象都是对对象转移自的[个人](../person/)或[群体](../group/)的[引用](../../shared/reference) |
| `transferred_to`   | array       | 可选 | JSON 对象数组，每个对象都是对对象转移给的对象的[个人](../person/)或[群体](../group/)的[引用](../../shared/reference) |


### 权利的属性

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `id`              | string        | 可选    | 如果存在，值必须是标识权利的 URI |
| `type`            | string        | 必需    | 权利的类，必须是值 `"Right"` |
| `_label`          | string        | 推荐    | 权利的人类可读标签，面向开发者 |
| `identified_by`   | array         | 推荐    | JSON 对象数组，每个对象都是权利的名称，必须遵循[名称](../../shared/name/)的要求，或权利的标识符，必须遵循[标识符](../../shared/identifier/)的要求 |
| `classified_as`   | array         | 推荐    | JSON 对象数组，每个对象都是权利的进一步分类，必须遵循[类型](../../shared/type/)的要求 |
| `referred_to_by`  | array         | 可选    | JSON 对象数组，每个对象都是关于权利的嵌入式[声明](../statement/) |
| `dimension`       | array         | 可选    | JSON 对象数组，每个对象都是[维度](../../shared/dimension/)结构 |
| `possessed_by`    | array         | 可选    | JSON 对象数组，每个对象都是对拥有权利的[个人](../person/)或[群体](../group/)的[引用](../../shared/reference) |
| `applies_to`      | array         | 可选    | JSON 对象数组，每个对象都是对权利适用的[对象](../object)的[引用](../../shared/reference) |
| `part`            | array         | 可选    | JSON 对象数组，每个对象都是权利，必须遵循权利定义的要求 |


### 属性图

> ![diagram](provenance_properties.png){:.diagram_img width="600px"}

### JSON 模式

请参阅[模式文档](../../schema_docs/provenance)和[模式本身](../../schema/provenance.json)


### 传入属性

流传历史活动在当前 API 集中没有传入引用，而是链接到许多不同的实体。


## 示例

描述 1820 年在拍卖会上购买对象的流传历史活动的 JSON 可能如下所示。

* 它在 `@context` 中有 Linked Art 上下文文档引用
* 它在 `id` 中自文档化其 URI
* 它的 `type` 为 "Activity"
* 它具有值为 "St George from Simpson to Adams" 的 `_label`，供阅读 JSON 的人员使用
* 它被 `classified_as` 为"流传历史条目"，其 `id` 为 "aat:300055863"
* 它被 `identified_by` ...
    * ... `Name`，内容为 "Purchase of Lot 0055a, Durer's St George and the Dragon"
    * ... 和 `Identifier`，内容为 "0055a"
* 它的时间段在 "1820-03-09T00:00:00Z" 和 "1820-03-09T23:59:59Z" 之间
* 它在伦敦 `took_place_at`
* 它使用拍卖批次的 `used_specific_object`，该批次是一个将对象作为成员的集合
* 它由两个 `part` 条目组成：
    * 一个获得...
        * ... 对象的 `transferred_title_of`
        * ... 从名为 Simpson（卖方）的个人 `transferred_title_from`
        * ... 和转移给名为 Adams（买方）的个人 `transferred_title_to`
    * 一个支付...
        * ... `paid_amount` 为 8.8 英镑（"aat:300411998"）
        * ... 从 Adams `paid_from`
        * ... 给 Simpson `paid_to`

```crom
top = vocab.ProvenanceEntry(ident="auto int-per-segment", label="St George from Simpson to Adams")
top.identified_by = model.Name(content="Purchase of Lot 0055a, Durer's St George and the Dragon")
top.identified_by = model.Identifier(content="0055a")
ts = model.TimeSpan(label="1820 Mar 09")
ts.begin_of_the_begin = "1820-03-09T00:00:00Z"
ts.end_of_the_end = "1820-03-09T23:59:59Z"
top.timespan = ts
top.carried_out_by = model.Group(ident="http://vocab.getty.edu/ulan/500451765", label="Edward Foster & Son")
top.took_place_at = model.Place(ident="http://vocab.getty.edu/tgn/7011781", label="London")
top.caused_by = model.Activity(ident="http://example.org/auction/Br1908/0055", label="Auction of Lot 0055")
top.used_specific_object = model.Set(ident="http://example.org/set/Br1908/0055", label="Set of Objects for Lot 0055")

what = model.HumanMadeObject(ident="http://example.museum/object/1", label="St George and the Dragon")
buyer = model.Person(ident="http://example.museum/person/1", label="Adams")
seller = model.Person(ident="http://example.museum/person/2", label="Simpson")
amnt = model.MonetaryAmount(label="8.8 pounds")
amnt.value = 8.8
amnt.currency = vocab.instances['gb pounds']

acq = model.Acquisition()
top.part = acq
pay = model.Payment()
top.part = pay

acq.transferred_title_of = what
acq.transferred_title_from = seller
acq.transferred_title_to = buyer
pay.paid_amount = amnt
pay.paid_from = buyer
pay.paid_to = seller

```
