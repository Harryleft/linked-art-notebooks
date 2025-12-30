---
title: "Linked Art API 视觉作品"
---




## 简介

视觉作品 API 是获取图像内容描述的方法，如绘画和二维艺术品、雕塑和三维艺术品或数字图像的外观。视觉作品模型具有中等复杂度，具有许多熟悉的属性和模式，以及几个添加来描述视觉作品与其他实体之间关系的属性。

关于视觉作品数据用法的更多信息，请参阅[对象相关性模型](/model/object/aboutness/)描述。


## 属性定义

通过视觉作品端点解析实体会得到一个包含单个 JSON 对象的 JSON-LD 文档，该对象具有以下属性。

### 视觉作品的属性

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `@context`        | string, array | 必需    | 值必须是[Linked Art 上下文](../../json-ld/)的 URI，作为字符串 `"https://linked.art/ns/v1/linked-art.json"` 或数组，其中 URI 是最后一个条目以允许[扩展](../../json-ld/extensions) |
| `id`              | string        | 必需    | 值必须是视觉作品表示可以[解析](../../protocol/)的 HTTP(S) URI |
| `type`            | string        | 必需    | 视觉作品的类，必须是值 `"VisualItem"` |
| `_label`          | string        | 推荐    | 视觉作品的人类可读标签，面向开发者 |
| `classified_as`   | array         | 推荐    | JSON 对象数组，每个对象都是视觉作品的分类，必须遵循[类型](../../shared/type/)的要求 |
| `identified_by`   | array         | 推荐    | JSON 对象数组，每个对象都是视觉作品的名称/标题，必须遵循[名称](../../shared/name/)的要求，或视觉作品的标识符，必须遵循[标识符](../../shared/identifier/)的要求 |
| `referred_to_by`  | array         | 可选    | JSON 对象数组，每个对象都是关于视觉作品的人类可读声明，必须遵循[声明](../../shared/statement/)的要求 |
| `equivalent`      | array         | 可选    | JSON 对象数组，每个对象都是对当前视觉作品外部身份和描述的[引用](../../shared/reference) |
| `member_of`       | array         | 可选    | JSON 对象数组，每个对象都是当前视觉作品成员的集合，必须遵循对集合的[引用](../../shared/reference/)的要求 |
| `subject_of`      | array         | 可选    | JSON 对象数组，每个对象都是对[文本作品](../textual_work/)的引用，其内容聚焦于当前视觉作品，必须遵循[引用](../../shared/reference/)的要求 |
| `attributed_by`   | array         | 可选    | JSON 对象数组，每个对象都是将当前视觉作品与另一个实体相关联的[关系分配](../../shared/assignment/) |
| `dimension` | array | 可选 | JSON 对象数组，每个对象都是当前视觉作品的[维度](../../shared/dimension)，如抽象高度或宽度 |
| `part_of` | array | 可选 | JSON 对象数组，每个对象都是对当前视觉作品所属的另一个视觉作品或[文本作品](../textual_work/)的[引用](../../shared/reference/) |
| `conceptually_part_of` | array | 可选 | JSON 对象数组，每个对象都是对当前作品概念上所属的[抽象作品](../abstract_work/)的[引用](../../shared/reference/) |
| `about` | array | 可选 | JSON 对象数组，每个对象都是对此文本主要关于的任何类型的另一个实体的[引用](../../shared/reference/) |
| `represents` | array | 可选 | JSON 对象数组，每个对象都是对此视觉作品代表或描绘的任何类型的另一个实体的[引用](../../shared/reference/) |
| `represents_instance_of_type` | array | 可选 | JSON 对象数组，每个对象都是此视觉作品代表或描绘的实体类型，但个人不为人知，必须遵循[类型](../../shared/type/)的要求 |
| `subject_to` | array | 可选 | JSON 对象数组，每个对象都是对知识产权作品持有的[权利](../../shared/right) |
| `created_by` | json object | 可选 | 表示图像创建的 JSON 对象，遵循[创建](../../shared/activity)的要求 |
| `used_for` | array | 可选 | JSON 对象数组，每个对象都是出版活动，遵循[活动](../../shared/activity)的要求 |

### 属性图

> ![diagram](image_properties.png){:.diagram_img width="600px"}

### JSON 模式

请参阅[模式文档](../../schema_docs/image)和[模式本身](../../schema/image.json)


### 引用属性

视觉作品实例通常作为以下属性的对象出现，除了上述自引用属性。此列表并非详尽无遗，而是旨在涵盖其他端点可能引用图像内容的可能情况。

| 属性名称              | 源端点 | 描述 |
|----------------------------|-----------------|-------------|
| `representation`           | 所有             | 实体可以用视觉内容表示，换句话说，描绘它们的图像的内容。 |
| `shows`                    | [物理对象](../physical_object/) | 物理对象可以显示视觉内容 |
| `digitally_shows`          | [数字对象](../digital_object/) | 数字对象同样可以数字显示视觉内容 |


## 示例

Miro 的 "The Farm" 的视觉内容的视觉作品条目的 JSON 可能如下所示。

* 它在 `@context` 中包含 Linked Art 上下文文档引用
* 它在 `id` 中自文档化其 URI
* 它的 `type` 为 "VisualItem"
* 它有一个 `_label`，值为 "Appearance of Miro's The Farm"，供阅读 JSON 的人员使用
* 它被 `classified_as` 为 "Cubist"（立体派），`id` 为 "aat:300021495"，依次被 `classified_as` 为风格（"aat:300015646"）
* 它被 `identified_by` 为一个 `Name`，内容为 "Appearance of The Farm"
* 它被 `referred_to_by` 为一个声明...
    * ... `content` 为 "A brilliant amalgamation of an intense ..."（一种强烈的精彩融合...）
    * ...被 `classified_as` 为描述（"aat:300435416"）
* 它 `represents`（代表）一个地点，Mont-roig del Camp
* 它 `represents_instance_of_type`（代表...类型的实例）树（"aat:300132410"），意味着有一棵树被描绘，但树除了内容之外没有单独的身份
* 它被 `created_by` 一个创建...
    * ...由 Miro `carried_out_by`（执行）
    * ...有一个 `timespan`（时间段），在 "1921-01-01" 和 "1922-12-31" 之间

```crom
top = model.VisualItem(ident="auto int-per-segment", label="Appearance of Miro's The Farm")
n = model.Name(content="Appearance of The Farm")
top.identified_by = n
c = model.Type(ident="http://vocab.getty.edu/aat/300021495", label="Cubist")
c.classified_as = model.Type(ident="http://vocab.getty.edu/aat/300015646", label="Style")
top.classified_as = c
top.referred_to_by = vocab.Description(content="A brilliant amalgamation of an intense, even primitive, realism with the formal vocabulary of cubism.")
top.represents = model.Place(ident="http://vocab.getty.edu/tgn/7300934", label="Mont-roig del Camp")
top.represents_instance_of_type = model.Type(ident="http://vocab.getty.edu/aat/300132410", label="Tree")
top.shown_by = model.HumanMadeObject(ident="https://www.nga.gov/collection/art-object-69660", label="The Farm")
cre = model.Creation()
cre.carried_out_by = model.Person(ident="http://vocab.getty.edu/ulan/500014094", label="Miro")
ts = model.TimeSpan(label="1921-1922")
ts.begin_of_the_begin = "1921-01-01T00:00:00Z"
ts.end_of_the_end = "1922-12-31T23:59:59Z"
cre.timespan = ts
top.created_by = cre
```
