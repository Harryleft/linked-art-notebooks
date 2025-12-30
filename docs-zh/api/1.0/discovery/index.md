---
title: "Linked Art 发现 API"
up_href: "/api/1.0/"
up_label: "Linked Art API 1.0"
---



## 简介

Linked Art 数据并非存在于真空中，它也不试图定义与文化遗产数据所有可能的交互。相反，我们的范围是定义文化遗产物品的语义描述，以及重要的周围上下文信息，如人物、地点、概念和事件。本节记录了如何从其他 API 和基于 Web 的系统中引用 Linked Art 记录。


## HTML 中的数据可见性

为了确保像 Google 这样的搜索引擎获得尽可能多的信息，有一个从 Linked Art 到 [Schema.Org](https://schema.org/) 结构的映射。Schema.Org 可以作为 JSON-LD 或其他格式嵌入网页中，使搜索引擎能够将数据作为数据处理，而不仅仅是通过面向人类的 HTML。[映射](/cookbook/mappings/schema/) 不是版本化 API 的一部分，因为它会随着底层模式及其使用的变化而更新，这超出了我们的控制范围。

对于可能被给予网页而不是 JSON-LD 记录 URI 的客户端，为了数据的可见性，向它们提供数据的链接也很重要。这是通过 HTTP 响应中的[链接头](https://www.rfc-editor.org/rfc/rfc8288.html)（对于非浏览器客户端）和 HTML `head` 元素内（对于基于浏览器的客户端）完成的。这将允许客户端从面向人类用户的 HTML 视图直接转到更机器可理解的 JSON-LD 记录进行处理。

在对象网页的 HTTP 响应中，链接到 JSON-LD 记录的头如下所示：

```
Link: <https://example.com/data/object/1>;
        rel="describedby";
        type="application/ld+json;profile='https://linked.art/ns/v1/linked-art.json'"
```

在 HTML 的 `head` 元素中：

```XML
<head>
  <link rel="describedby" href="https://example.com/data/object/1"
        type="application/ld+json;profile='https://linked.art/ns/v1/linked-art.json'"/>
</head>
```

`head` 中的 `link` 元素必须存在，如果可能，HTTP 头也应该存在。页面必须只有一个指向 linked art 记录的链接，以避免混淆应该使用哪个链接。

请注意，这遵循[FAIR 标志配置文件](https://signposting.org/FAIR/)，因此任何遵循上述内容的 Linked Art 实现也将符合该规范。


## 收获

为了产生跨集合和跨机构的聚合服务或应用程序，必须能够以高效的方式找到所有记录，并与这些记录的任何更改保持同步。这是[IIIF 更改发现 API](https://iiif.io/api/discovery/)的目的。

为了使 Linked Art 记录类型可用，可以使用一个简短的上下文文档（[https://linked.art/ns/v1/record-types.json](https://linked.art/ns/v1/record-types.json)）作为扩展，如 IIIF API 的链接数据上下文和[扩展](https://iiif.io/api/discovery/1.0/#342-extensions)节中所述。

因此，响应中的上下文将是：

```json
{
  "@context": [
    "https://linked.art/ns/v1/record-types.json",
    "http://iiif.io/api/discovery/1/context.json"
  ]
}
```

这将允许以下更改条目出现在流中，而不是仅限于 IIIF 的 `type` 值。

```json
{
  "type": "Update",
  "object": {
    "id": "https://example.org/api/object/1",
    "type": "HumanMadeObject"
  }
}
```

否则，功能和语法完全按照 IIIF 规范的描述。