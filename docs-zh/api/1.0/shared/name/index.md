---
title: "Linked Art API：名称结构"
up_href: "/api/1.0/shared/"
up_label: "Linked Art API 1.0 共享数据结构"
-----




## 简介

名称是赋予某个实体的语言标签，在所有端点中表示为通用的 JSON 结构。

名称在模型文档的[基础模式](/model/base/#types-and-classifications)中有描述，几乎所有类都有示例。

## 属性定义

### 名称的属性

| 属性名称     | 数据类型      | 要求 | 描述 |
|-------------------|---------------|-------------|-------------|
| `id`              | string        | 可选    | 如果存在，值必须是标识名称的 URI，可以从中检索名称的表示 |
| `type`            | string        | 必需    | 名称的类，必须是值 `"Name"` |
| `_label`          | string        | 可选    | 人类可读标签，面向开发者 |
| `_complete`       | boolean       | 可选    | 非语义。如果存在带有 URI 的 `id` 属性，并且在该 URI 的表示中有更多关于名称的信息可用，则 `_complete` 必须存在且值为 `false`，以通知消费应用程序可能需要检索它 |
| `content`         | string        | 必需    | 名称的字符串形式 |
| `classified_as`   | array         | 推荐    | JSON 对象数组，每个对象都是名称的进一步分类，必须遵循[类型](../类型/)的要求 |
| `language`        | array         | 推荐    | JSON 对象数组，每个对象都是名称内容中存在的语言，必须遵循[语言](../类型/)的要求 |
| `part`            | array         | 可选    | JSON 对象数组，每个对象都是当前名称的一部分，必须遵循这些名称要求 |
| `identified_by`   | array         | 可选    | JSON 对象数组，每个对象都是此名称的名称，遵循名称模式 |
| `referred_to_by`  | array         | 可选    | JSON 对象数组，每个对象要么是对引用名称的[文本作品](../../端点/textual_work/)的引用，要么是关于名称的嵌入[声明](../声明/) |
| `assigned_by`     | array         | 可选    | JSON 对象数组，每个对象都是名称的分配，必须遵循[分配](../分配/)的要求 |

### 属性图

> ![diagram](name_properties.png){:.diagram_img width="600px"}


### 引用属性

名称实例通常作为以下属性的对象出现。此列表并非详尽无遗，而是旨在涵盖可能的情况。

| 属性名称   | 源类      | 描述 |
|-----------------|-------------------|-------------|
| `identified_by` | 所有               | 名称用于通过 identified_by 为实体提供识别标签。 |

（这就是全部！）

## 示例

一个对象被赋予名称 "Hacha (Ceremonial Axe)"，并注明原始形式为 'hacha'。

* 它在 `id` 中给出了一个 URI（标识名称本身，而不是对象）
* 它的 `type` 为 "Name"
* 它被 `classified_as` 为主要名称，`id` 为 _aat:300404670_，`type` 为 "Type"
* 它的 `content` 为 "Hacha (Ceremonial Axe)"
* 它有一个显示标签为 "Assigned Title"
* 它被 `referred_to_by` 为一个声明，`type` 为 "LinguisticObject"，`classified_as` 为注释，`id` 为 _aat:300027200_，`content` 为 "Title was originally ..."（标题最初为...）
* 它有英语语言，`id` 为 _aat:300388277_，`type` 为 "Language"，以及西班牙语语言，`id` 为 _aat:300389311_，`type` 为 "Language"
* 它有一个特定的 `part`，...
    * ...也有一个 `type` 为 "Name"
    * ...被 `classified_as` 为副标题，`id` 为 _aat:300312006_
    * ... `content` 为 "Ceremonial Axe"
    * ...以及英语语言，如上。

```crom
top = model.HumanMadeObject(ident="auto int-per-segment")
n = vocab.PrimaryName(content="Hacha (Ceremonial Axe)")
n.language = vocab.instances['spanish']
n.language = vocab.instances['english']
top.identified_by = n
st = vocab.Subtitle(content="Ceremonial Axe")
st.language = vocab.instances['english']
n.part = st
n.identified_by = vocab.DisplayName(content="Assigned Title")
n.referred_to_by = vocab.Note(content="Title was originally given as 'hacha'")
```


## 未来考虑

* 如[标识符](../标识符/)所述的分配可以很容易地为名称添加，但尚未提出用例。
