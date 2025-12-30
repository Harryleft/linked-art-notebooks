---
title: "Linked Art API：群体"
up_href: "/api/1.0/endpoint/"
up_label: "Linked Art API 1.0 端点"
---




## 简介

群体 API 是获取人群和/或子群组描述的方法，如家庭、组织、公司、部门或任何其他可识别的行动者集合。群体模型具有中等复杂度，具有许多熟悉的属性和模式，加上一些更特定的字段。这产生了一个中等复杂度的 API，与[个人 API](../person/) 非常相似，如果所有字段都有值，可能会导致相当长的 JSON 响应。

关于群体数据用法的更多信息，请参阅[群体模型](/model/actor/)描述。


## 属性定义

通过群体端点解析实体会得到一个包含单个 JSON 对象的 JSON-LD 文档，该对象具有以下属性。

### 群体的属性

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `@context`        | string, array | 必需    | 值必须是[Linked Art 上下文](../../json-ld/)的 URI，作为字符串 `"https://linked.art/ns/v1/linked-art.json"` 或数组，其中 URI 是最后一个条目以允许[扩展](../../json-ld/extensions) |
| `id`              | string        | 必需    | 值必须是群体表示可以[解析](../../protocol/)的 HTTP(S) URI |
| `type`            | string        | 必需    | 群体的类，必须是值 `"Group"` |
| `_label`          | string        | 推荐    | 群体的人类可读标签，面向开发者 |
| `classified_as`   | array         | 推荐    | JSON 对象数组，每个对象都是群体的分类，必须遵循[类型](../../shared/type/)的要求 |
| `identified_by`   | array         | 推荐    | JSON 对象数组，每个对象都是群体的名称，必须遵循[名称](../../shared/name/)的要求，或群体的标识符，必须遵循[标识符](../../shared/identifier/)的要求 |
| `referred_to_by`  | array         | 可选    | JSON 对象数组，每个对象都是关于群体的人类可读声明，必须遵循[声明](../../shared/statement/)的要求 |
| `equivalent`      | array         | 可选    | JSON 对象数组，每个对象都是对当前群体外部身份和描述的[引用](../../shared/reference) |
| `representation`  | array         | 可选    | JSON 对象数组，每个对象都是对代表当前群体的[视觉作品](../visual_work)的引用，必须遵循[引用](../../shared/reference/)的要求 |
| `member_of`       | array         | 可选    | JSON 对象数组，每个对象都是当前群体成员的集合，必须遵循对**[群体](../group/)**的[引用](../../shared/reference/)的要求 |
| `subject_of`      | array         | 可选    | JSON 对象数组，每个对象都是对[文本作品](../textual_work/)的引用，其内容聚焦于当前群体，必须遵循[引用](../../shared/reference/)的要求 |
| `attributed_by`   | array         | 可选    | JSON 对象数组，每个对象都是将当前群体与另一个实体相关联的[关系分配](../../shared/assignment/) |
| `contact_point` | array | 可选 | JSON 对象数组，每个对象都是群体可联系到的地址，必须遵循[标识符](../../shared/identifier)的要求 |
| `residence` | array | 可选 | 群体关联的地点，必须遵循对[地点](../place/)的[引用](../../shared/reference/)的要求 |
| `carried_out` | array | 可选 | JSON 对象数组，每个对象代表群体的专业活动，遵循[活动](../../shared/activity)的要求 |
| `participated_in` | array | 可选 | JSON 对象数组，每个对象代表群体参与但不负责的活动或事件，遵循[活动](../../shared/activity)的要求 |
| `formed_by` | json object | 可选 | 表示群体形成的 JSON 对象，遵循[形成](../../shared/activity)的要求 |
| `dissolved_by` | json object | 可选 | 表示群体解散的 JSON 对象，遵循[解散](../../shared/activity)的要求 |

### 属性图

> ![diagram](group_properties.png){:.diagram_img width="600px"}

### JSON 模式

请参阅[模式文档](../../schema_docs/group)和[模式本身](../../schema/group.json)


### 引用属性

群体实例通常作为以下属性的对象出现，除了上述自引用属性。此列表并非详尽无遗，而是旨在涵盖其他端点可能引用群体的可能情况。

| 属性名称              | 源端点 | 描述 |
|----------------------------|-----------------|-------------|
| `member_of`                | [个人](../person/)、[群体](../group/)   | 属于当前群体成员的个人记录在个人记录中 |
| `carried_out_by`           | 所有             | 群体执行的活动 |
| `current_owner`            | [对象](../physical_object/) | 群体拥有的对象 |
| `current_custodian`        | [对象](../physical_object/) | 群体保管的对象 |
| `current_permanent_custodian` | [对象](../physical_object/) | 通常由群体保管的对象 |
| `represents`               | [视觉作品](../visual_work/)     | 代表群体的图像内容（`representation` 的反向） |
| `about`                    | [文本作品](../textual_work/)    | 关于群体的文本内容 |
| `transferred_custody_to`   | [流传历史](../provenance_activity/)     | 将对象保管权转移给群体的活动 |
| `transferred_custody_from` | [流传历史](../provenance_activity/)     | 将对象保管权从群体转移出去的活动 |
| `transferred_title_to`     | [流传历史](../provenance_activity/)     | 将对象所有权转移给群体的活动 |
| `transferred_title_from`   | [流传历史](../provenance_activity/)     | 将对象所有权从群体转移出去的活动 |
| `paid_to`                  | [流传历史](../provenance_activity/)     | 从其他人向群体支付款项的活动 |
| `paid_from`                | [流传历史](../provenance_activity/)    | 从群体向其他人支付款项的活动 |


## 示例

Camden Town 群体的群体条目的 JSON 可能如下所示。

* 它在 `@context` 中包含 Linked Art 上下文文档引用
* 它在 `id` 中自文档化其 URI
* 它的 `type` 为 "Group"
* 它有一个 `_label`，值为 "Camden Town Group"，供阅读 JSON 的人员使用
* 它被 `classified_as` 为...
    * ...一个"Society"（协会），`id` 为 "aat:300026009"
    * ... "British"（英国），`id` 为 "aat:300111159"，元类型为 "Nationality"（国籍），`id` 为 "aat:300379842"
* 它被 `identified_by` 为一个 `Name`，内容为 "Camden Town Group"，`language` 为英语（"aat:300388277"）
* 它被 `referred_to_by` 为一个声明...
    * ... `content` 为 "A group of British painters formed in 1911 ..."（一群于 1911 年成立的英国画家...）
    * ...被 `classified_as` 为传记（"aat:300435422"）
* 它 `carried_out` 其专业活动...
    * ...在 "1911-01-01" 和 "1913-12-31" 之间的 `timespan`（时间段）内
* 它被 `attributed_by` 为一个 "AttributeAssignment"（属性分配）关系
    * ...到 London Group（伦敦群体），`id` 为 "ulan:500117319"
* 它有一个 `residence`（居住地）为 London（伦敦）
* 它 `equivalent`（等同于）ULAN 条目 `"ulan:500117318"`
* 它被 `formed_by` 一个形成...
    * ... `took_place_at`（发生在）伦敦
    * ...在 "1911-01-01" 和 "1911-12-31" 之间的 `timespan`（时间段）内
* 它被 `dissolved_by` 一个解散...
    * ...再次 `took_place_at`（发生在）伦敦
    * ...在 "1913-01-01" 和 "1913-12-31" 之间的 `timespan`（时间段）内

```crom
top = model.Group(ident="auto int-per-segment", label="Camden Town Group")
n = model.Name(content="Camden Town Group")
n.language = model.Language(ident="http://vocab.getty.edu/aat/300388277", label="English")
top.identified_by = n

top.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300026009", label="Society")
top.classified_as = vocab.instances['british nationality']

b = model.Formation(label="Formation of the Group")
ts = model.TimeSpan()
ts._label = "1911"
ts.begin_of_the_begin = "1911-01-01T00:00:00Z"
ts.end_of_the_end = "1911-12-31T23:59:59Z"
b.timespan = ts
p = model.Place(label="London")
b.took_place_at = p
top.formed_by = b

d = model.Dissolution(label="Dissolution of the Group")
ts = model.TimeSpan()
ts._label = "1913"
ts.begin_of_the_begin = "1913-01-01T00:00:00Z"
ts.end_of_the_end = "1913-12-31T23:59:59Z"
d.timespan = ts
d.took_place_at = p
top.dissolved_by = d

top.referred_to_by = vocab.BiographyStatement(
	content="A group of British painters formed in 1911; although it only lasted two years, its name is used in a broader sense to characterize a particular strain of British painting from about 1905 to 1920.")

act = vocab.Active(label="Active Dates")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1911-01-01T00:00:00Z"
ts.end_of_the_end = "1913-12-31T23:59:59Z"
act.timespan = ts
top.carried_out = act

top.residence = p
top.equivalent = model.Group(ident="http://vocab.getty.edu/ulan/500117318", label="Camden Town Group")

aa = model.AttributeAssignment(label="Related Group")
aa.assigned = model.Group(ident="http://vocab.getty.edu/ulan/500117319", label="London Group")
top.attributed_by = aa

```
