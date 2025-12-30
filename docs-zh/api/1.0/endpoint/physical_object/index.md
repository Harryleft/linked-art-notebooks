---
title: "Linked Art API：物理对象"
up_href: "/api/1.0/endpoint/"
up_label: "Linked Art API 1.0 端点"
---




## 简介

物理对象 API 是获取物理对象描述的方法，如绘画、雕塑、手稿或其他有形艺术品。承载艺术品内容的物理对象是任何 Linked Art 信息系统的核心部分，因此描述可能具有大量字段和数据。这产生了一组相对较长的关系和属性，但它们遵循典型的模式和构造。

关于物理对象数据的更多信息，请参阅[对象模型](/model/object/)描述。


### 物理对象的属性


| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `@context`        | string, array | 必需    | 值必须是[Linked Art 上下文](../../json-ld/)的 URI，作为字符串 `"https://linked.art/ns/v1/linked-art.json"` 或数组，其中 URI 是最后一个条目以允许[扩展](../../json-ld/extensions) |
| `id`              | string        | 必需    | 值必须是对象表示可以[解析](../../protocol/)的 HTTP(S) URI |
| `type`            | string        | 必需    | 对象的类，必须是值 `"HumanMadeObject"` |
| `_label`          | string        | 推荐    | 对象的人类可读标签，面向开发者 |
| `classified_as`   | array         | 推荐    | JSON 对象数组，每个对象都是对象的分类，必须遵循[类型](../../shared/type/)的要求 |
| `identified_by`   | array         | 推荐    | JSON 对象数组，每个对象都是对象的名称/标题，必须遵循[名称](../../shared/name/)的要求，或对象的标识符，必须遵循[标识符](../../shared/identifier/)的要求 |
| `referred_to_by`  | array         | 可选    | JSON 对象数组，每个对象都是关于对象的人类可读声明，必须遵循[声明](../../shared/statement/)的要求 |
| `equivalent`      | array         | 可选    | JSON 对象数组，每个对象都是对当前对象外部身份和描述的[引用](../../shared/reference) |
| `representation`  | array         | 可选    | JSON 对象数组，每个对象都是对代表当前对象的[视觉作品](../visual_work)的引用，必须遵循[引用](../../shared/reference/)的要求 |
| `member_of`       | array         | 可选    | JSON 对象数组，每个对象都是当前对象成员的集合，必须遵循对集合的[引用](../../shared/reference/)的要求 |
| `subject_of`      | array         | 可选    | JSON 对象数组，每个对象都是对[文本作品](../textual_work/)的引用，其内容聚焦于当前对象，必须遵循[引用](../../shared/reference/)的要求 |
| `attributed_by`   | array         | 可选    | JSON 对象数组，每个对象都是将当前对象与另一个实体相关联的[关系分配](../../shared/assignment/) |
| `part_of` | array | 可选 | JSON 对象数组，每个对象都是对当前对象所属的另一个物理对象的[引用](../../shared/reference/) |
| `dimension` | array | 可选 | JSON 对象数组，每个对象都是当前对象的[维度](../../shared/dimension)，如高度或宽度 |
| `made_of` | array | 可选 | JSON 对象数组，每个对象都是构成对象的材料的[引用](../../shared/reference)，必须遵循[材料](../../shared/type)的要求 |
| `current_owner` | array | 可选 | JSON 对象数组，每个对象都是目前拥有对象的[个人](../person/)或[群体](../group/)的[引用](../../shared/reference/) |
| `current_custodian` | array | 可选 | JSON 对象数组，每个对象都是目前保管对象的[个人](../person/)或[群体](../group/)的[引用](../../shared/reference/) |
| `current_permanent_custodian` | array | 可选 | JSON 对象数组，每个对象都是通常保管对象的[个人](../person/)或[群体](../group/)的[引用](../../shared/reference/)，但可能当前时间不是 |
| `current_location` | json object | 可选 | 对象当前所在位置的[地点](../place/)的[引用](../../shared/reference/)的 JSON 对象 |
| `current_permanent_location` | json object | 可选 | 对象通常所在位置的[地点](../place/)的[引用](../../shared/reference/)的 JSON 对象，但可能当前时间不是 |
| `held_or_supported_by` | json object | 可选 | 支撑、包含或支持当前对象的另一个物理对象的[引用](../../shared/reference)的 JSON 对象 |
| `carries` | array | 可选 | JSON 对象数组，每个对象都是此对象承载其文本的[文本作品](../textual_work/)的[引用](../../shared/reference/) |
| `shows` | array | 可选 | JSON 对象数组，每个对象都是此对象显示其再现的[视觉作品](../visual_work/)的[引用](../../shared/reference/) |
| `used_for`    | array | 可选 | JSON 对象数组，每个对象代表对象在其中起重要作用但没有自己身份的活动，遵循[活动](../../shared/activity)的要求 |
| `produced_by` | json object | 可选 | 表示对象生产的 JSON 对象，遵循[生产](../../shared/activity)的要求 |
| `destroyed_by` | json object | 可选 | 表示对象毁坏的 JSON 对象，遵循[毁坏](../../shared/activity)的要求 |
| `removed_by` | array | 可选 | JSON 对象数组，每个对象代表将当前对象从其先前所属的较大对象中移除，遵循[部分移除](../../shared/activity)的要求 |
| `modified_by` | array | 可选 | JSON 对象数组，每个对象代表对对象的物理修改，如保护处理，遵循[修改](../../shared/activity)的要求 |
| `encountered_by` | array | 可选 | JSON 对象数组，每个对象代表某个行动者与当前对象的遭遇，通常当收藏家"发现"对象时，遵循[遭遇](../../shared/activity)的要求 |
| `changed_ownership_through` | array | 可选 | JSON 对象数组，每个对象代表某个行动者从另一个行动者那里获得对象，遵循[流传历史活动](../provenance_activity/)端点描述中给出的`获得`的要求，并在下面总结 |


### 获得的附加属性

[活动](../../shared/activity)的属性可用于获得，以及以下属性：

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `transferred_title_from` | array       | 可选 | JSON 对象数组，每个对象都是[个人](../person/)或[群体](../group/)的[引用](../../shared/reference)，每个都是对象的先前所有者，对象的所有权从他们转移。**仅在 `type` 为 `"Acquisition"` 时可用** |
| `transferred_title_to`   | array       | 可选 | JSON 对象数组，每个对象都是[个人](../person/)或[群体](../group/)的[引用](../../shared/reference)，每个都是对象所有权转移给的新所有者之一。**仅在 `type` 为 `"Acquisition"` 时可用** |

### 属性图

> ![diagram](object_properties.png){:.diagram_img width="600px"}

### JSON 模式

请参阅[模式文档](../../schema_docs/object)和[模式本身](../../schema/object.json)


### 引用属性

物理对象实例通常作为以下属性的对象出现，除了上述自引用属性。此列表并非详尽无遗，而是旨在涵盖其他端点可能引用物理对象的可能情况。

| 属性名称              | 源端点 | 描述 |
|----------------------------|-----------------|-------------|
| `used_specific_object`     | 所有             | 可以使用特定物理对象作为仪器、工具或其他组成部分（如印刷照片中的底片）来执行各种活动 |
| `influenced_by`            | 所有             | 各种活动受物理对象影响，如副本的灵感 |
| `transferred_title_of`     | [流传历史](../provenance_activity/) | 对象的所有权可以在流传历史活动中转移 |
| `transferred_custody_of`   | [流传历史](../provenance_activity/) | 对象的保管权也可以转移 |
| `moved`                    | [流传历史](../provenance_activity/) | 对象可以在位置之间移动 |
| `applies_to`               | [流传历史](../provenance_activity/) | 权利可以适用于对象 |
| `carried_by`               | [文本作品](../textual_work/)      | 文本作品由对象承载 |
| `shown_by`                 | [视觉作品](../textual_work/)       | 视觉作品由对象显示 |

## 示例

蒙娜丽莎的物理对象条目的 JSON 可能如下所示。

* 它在 `@context` 中包含 Linked Art 上下文文档引用
* 它在 `id` 中自文档化其 URI
* 它的 `type` 为 "HumanMadeObject"
* 它有一个 `_label`，值为 "Mona Lisa"，供阅读 JSON 的人员使用
* 它被 `classified_as` 为...
    * ...一个"Painting"（绘画），`id` 为 "aat:300033618"，依次被分类为"Type of Work"（作品类型）（"aat:300435443"）
    * ...一个"Work of Art"（艺术品），`id` 为 "aat:300111159"
* 它被 `identified_by` 为...
    * ...一个 `Name`，内容为 "Mona Lisa"，`language` 为英语（"aat:300388277"），`classified_as` 为主要名称（用于英语）
    * ...一个 `Name`，内容为 "La Joconde"，`language` 为法语（"aat:300388306"），`classified_as` 为主要名称（用于法语）
    * ...一个 `Name`，内容为 "La Gioconda"，`language` 为意大利语（"aat:300388474"），再次 `classified_as` 为主要名称（用于意大利语）
    * ...一个 `Identifier`，内容为 "INV. 779"，`classified_as` 为登记号（"aat:300312355"）
* 它被 `referred_to_by` 为一个声明...
    * ... `content` 为 "This portrait was doubtless started in Florence around 1503 ..."（这幅肖像无疑是在 1503 年左右在佛罗伦萨开始的...）
    * ...被 `classified_as` 为描述（"aat:300435416"）
* 它有两个 `dimension` 条目...
    * ...高度（"aat:300055644"）为 0.77 米（"aat:300379099"）
    * ...宽度（"aat:300055647"）为 0.53 米（"aat:300379099"）
* 它 `made_of` 两种材料...
    * ...杨木（"aat:300012363"）
    * ...和油画颜料（"aat:300015050"）
* 它 `equivalent`（等同于）Wikidata 实体 "Q12418"
* 它有一个 `current_owner` 为卢浮宫博物馆（一个群体）
* 它有一个 `current_location` 为博物馆中的画廊（一个地点）（这将是另一个地点，不是与群体相同的实体）
* 它 `shows` 非常著名的视觉内容
* 它被 `produced_by` 一个生产...
    * ...由列奥纳多·达·芬奇 `carried_out_by`（执行）
    * ... `took_place_at`（发生在）意大利佛罗伦萨
    * ...在 "1503-01-01" 和 "1506-12-31" 之间的 `timespan`（时间段）内发生

```crom
top = vocab.Painting(ident="auto int-per-segment", label="Mona Lisa", art=1)
en = vocab.PrimaryName(value="Mona Lisa")
en.language = vocab.instances['english']
it = vocab.PrimaryName(value="La Gioconda")
it.language = vocab.instances['italian']
fr = vocab.PrimaryName(value="La Joconde")
fr.language = vocab.instances['french']
top.identified_by = en
top.identified_by = fr
top.identified_by = it
top.identified_by = vocab.AccessionNumber(content="INV. 779")
top.referred_to_by = vocab.Description(content="This portrait was doubtless started in Florence around 1503. It is thought to be of Lisa Gherardini, wife of a Florentine cloth merchant ...")
top.equivalent = model.HumanMadeObject(ident="http://wikidata.org/entity/Q12418", label="Mona Lisa")
top.member_of = model.Set(ident="", label="Most expensive paintings in the world")
top.member_of = model.Set(ident="http://data.louvre.example/all_holdings", label="Holdings of the Louvre")

h = vocab.Height(value=0.77)
h.unit = vocab.instances['meters']
w = vocab.Width(value=0.53)
w.unit = vocab.instances['meters']
top.dimension = h
top.dimension = w
top.made_of = model.Material(ident="http://vocab.getty.edu/aat/300012363", label="Poplar (wood)")
top.made_of = model.Material(ident="http://vocab.getty.edu/aat/300015050", label="Oil Paint")

top.current_owner = model.Group(ident="http://louvre.fr/", label="The Louvre")
top.current_location = model.Place(ident="http://galleries.example/louvre/711", label="Room 711, Denon Wing, The Louvre, Paris")
top.shows = model.VisualItem(ident="http://data.louvre.example/visual/mona_lisa", label="Visual Work of the Mona Lisa")

prod = model.Production()
prod.carried_out_by = model.Person(ident="http://vocab.getty.edu/ulan/500010879", label="Leonardo da Vinci")
ts = model.TimeSpan()
ts.begin_of_the_begin = "1503-01-01T00:00:00Z"
ts.end_of_the_end = "1506-12-31T23:59:59Z"
ts.identified_by = vocab.DisplayName(content="1503-1506")
prod.timespan = ts
prod.took_place_at = model.Place(ident="http://vocab.getty.edu/tgn/7000457", label="Florence, Italy")
top.produced_by = prod
```

