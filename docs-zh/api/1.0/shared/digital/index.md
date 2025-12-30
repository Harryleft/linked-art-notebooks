---
title: "Linked Art API: 数字引用结构"
up_href: "/api/1.0/shared/"
up_label: "Linked Art API 1.0 共享数据结构"
---




## 简介

在核心实体的描述中，需要包含许多对外部数字资源的引用，包括实体的图像或关于实体的网页。这些引用可以通过描述各种文本作品、视觉作品和数字对象的单独记录来管理，但是在作品描绘或描述的记录中嵌入必要的信息更容易且更可用。因此，这是通用模式的一个特定嵌入案例，当有关涉及的资源的更多信息时仍可使用。

这是一个复杂的共享结构，因为它涉及嵌套的 JSON 对象而不是单一层级。第一层是嵌入的文本或视觉作品，然后引用嵌入的数字对象。


## 属性定义

### 嵌入作品的属性

| 属性名称          | 数据类型      | 要求        | 描述 |
|-------------------|---------------|-------------|-------------|
| `id`              | string        | 可选        | 如果存在，值必须是标识作品的 URI，可以从该 URI 检索其表示 |
| `type`            | string        | 必需        | 作品的类，必须是值 `"VisualItem"` 或 `"LinguisticObject"`|
| `_label`          | string        | 可选        | 易读标签，面向开发人员 |
| `_complete`       | boolean       | 可选        | 非语义。如果存在带有 URI 的 `id` 属性，并且从该 URI 的表示中可以获得关于作品的更多信息，那么 `_complete` 必须存在，值为 `false`，以通知消费应用程序它可能想要检索它 |
| `classified_as`   | array         | 可选 | json 对象数组，每个都是作品的进一步分类，必须遵循 [类型](../type/) 的要求 |
| `identified_by`   | array         | 可选        | json 对象数组，每个都是作品的名称，遵循 [名称](../name/) 模式 |
| `referred_to_by`  | array         | 可选        | json 对象数组，每个都是关于作品的嵌入 [陈述](../statement/) |
| `digitally_shown_by` | array | 必需 * | 仅当 `type` 是 `"VisualItem"` 时使用。json 对象数组，每个都是如下所述的 DigitalObject |
| `digitally_carried_by` | array | 必需 * | 仅当 `type` 是 `"LinguisticObject"` 时使用。json 对象数组，每个都是如下所述的 DigitalObject |
| `language` | array | 可选 | 仅当 `type` 是 `"LinguisticObject"` 时使用。json 对象数组，每个都是文本所使用的语言，必须遵循 [语言](../../shared/type) 的要求 |

* \* 请注意，根据作品的类别，必须恰好存在 `digitally_shown_by` 和 `digitally_carried_by` 之一

### 嵌入数字对象的属性

| 属性名称          | 数据类型      | 要求        | 描述 |
|-------------------|---------------|-------------|-------------|
| `id`              | string        | 可选        | 如果存在，值必须是标识数字对象的 URI，可以从该 URI 检索其表示 |
| `type`            | string        | 必需        | 数字对象的类，必须是值 `"DigitalObject"` |
| `_label`          | string        | 可选        | 易读标签，面向开发人员 |
| `_complete`       | boolean       | 可选        | 非语义。如果存在带有 URI 的 `id` 属性，并且从该 URI 的表示中可以获得关于数字对象的更多信息，那么 `_complete` 必须存在，值为 `false`，以通知消费应用程序它可能想要检索它 |
| `classified_as`   | array         | 可选 | json 对象数组，每个都是数字对象的进一步分类，必须遵循 [类型](../type/) 的要求 |
| `identified_by`   | array         | 可选        | json 对象数组，每个都是数字对象的名称，遵循 [名称](../name/) 模式 |
| `referred_to_by`  | array         | 可选        | json 对象数组，每个都是关于数字对象的嵌入 [陈述](../statement/) |
| `format`          | string        | 推荐        | 数字对象格式的媒体类型 |
| `conforms_to`     | array         | 可选        | json 对象数组，每个都是数字对象遵循的标准，必须遵循 [类型](../type/) 的要求 |
| `created_by`      | json object   | 可选        | 数字对象的创建活动，必须遵循 [活动](../activity/) 的要求 |
| `timespan`        | json object   | 可选        | 描述数字对象存在时间的 json 对象，必须遵循 [时间范围](../timespan/) 的要求 |
| `access_point` | array | 可选 | json 对象数组，每个只有两个属性：`id` 包含可以检索描述的数字对象表示的 URI，`type` 具有值 `"DigitalObject"`。两者都是必需的 |
| `digitally_available_via` | array | 可选| json 对象数组，每个都是数字服务结构，在[数字对象](../../endpoint/digital_object)文档中定义 |
| `format` | string | 可选 | 描述的数字对象的媒体类型，例如 "image/jpeg" |
| `conforms_to` | array | 可选 | json 对象数组，每个都是当前数字对象遵循的外部规范的[引用](../../shared/reference/)。引用的 `type` 值必须是 `"InformationObject"` |


### 属性图

> ![图](digital_ref_properties.png){:.diagram_img width="600px"}


### 传入属性

名称实例通常作为以下属性的对象被找到。此列表并不详尽，但旨在涵盖可能的情况。

| 属性名称   | 源类     | 描述 |
|-----------------|------------------|-------------|
| `representation`| 所有              | 当作品是视觉项目时。 |
| `subject_of`    | 所有              | 当作品是语言对象时。 |


## 示例

对象在 https://example.org/objects/1 有主页，该页面承载英文文本。


```crom
top = model.HumanMadeObject(ident="auto int-per-segment")
top.identified_by = vocab.PrimaryName(content="Object")
lo = model.LinguisticObject()
lo.language = vocab.instances['english']
wp = vocab.WebPage()
lo.digitally_carried_by = wp
wp.access_point = model.DigitalObject(ident="https://example.org/objects/1")
wp.identified_by = vocab.PrimaryName(content="Home page for Object")
top.subject_of = lo
``` |