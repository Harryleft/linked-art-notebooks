---
title: "Linked Art API 1.0 关系"
up_href: "/api/1.0/"
up_label: "Linked Art API 1.0"
---

## 简介

本节记录了 Linked Art API 1.0 中使用的关系类型。这些关系定义了实体之间如何相互连接，是构建复杂文化遗产描述的基础。

## 关系类型

Linked Art 使用标准的关系类型来连接不同的实体。这些关系基于 CIDOC-CRM 本体，并扩展以支持艺术品的特定需求。

### 主要关系类别

* **创建关系**：连接艺术品与其创作者、创作过程等
* **所有权关系**：连接艺术品与其所有者、收藏历史等
* **物理关系**：连接物理对象与其材料、尺寸、位置等
* **概念关系**：连接概念作品与其表现形式、主题等
* **时间关系**：连接事件与时间范围
* **地点关系**：连接活动与发生的地点

## HAL 链接


### 物理对象 (Object)

  * [activityUsedObject](activityUsedObject)：返回使用该对象的活动。
  * [conceptInfluencedByObject](conceptInfluencedByObject)：返回受该对象影响的概念。
  * [objectPartOfObject](objectPartOfObject)：返回属于该对象一部分的对象。
  * [objectProductionInfluencedByObject](objectProductionInfluencedByObject)：返回其创作受该对象影响的对象。
  * [workAboutObject](workAboutObject)：返回关于或以该对象为主题的作品。
  * [workAboutOrRepresentsObject](workAboutOrRepresentsObject)：返回关于或代表该对象的作品。
  * [workRepresentsObject](workRepresentsObject)：返回代表或描绘该对象的视觉作品。

### 作品 (Work)

  * [activityUsedWork](activityUsedWork)：返回使用该作品的活动。
  * [conceptInfluencedByWork](conceptInfluencedByWork)：返回受该作品影响的概念。
  * [objectCarriesWork](objectCarriesWork)：返回承载该语言作品的物理对象。
  * [objectProductionInfluencedByWork](objectProductionInfluencedByWork)：返回其创作受该作品影响的对象。
  * [objectShowsWork](objectShowsWork)：返回显示该视觉作品的对象。
  * [workAboutOrRepresentsWork](workAboutOrRepresentsWork)：返回关于或代表该作品的作品。
  * [workAboutWork](workAboutWork)：返回关于或以该作品为主题的作品。
  * [workPartOfWork](workPartOfWork)：返回属于该作品一部分的作品。
  * [workRepresentsWork](workRepresentsWork)：返回代表或描绘该作品的作品。

### 行动者 (Agent)

  * [activityCarriedOutByAgent](activityCarriedOutByAgent)：返回由该个人或群体执行的活动。
  * [activityParticipantAgent](activityParticipantAgent)：返回该个人或群体参与但未直接执行的活动。
  * [agentMemberOfGroup](agentMemberOfGroup)：返回属于该群体成员的个人或群体。
  * [conceptInfluencedByAgent](conceptInfluencedByAgent)：返回受该个人或群体影响的概念。
  * [groupFoundedByAgent](groupFoundedByAgent)：返回由该个人或群体创建的群体。
  * [objectCuratedByAgent](objectCuratedByAgent)：返回由该个人或群体策展、照管或以其他方式保管的对象。
  * [objectEncounteredByAgent](objectEncounteredByAgent)：返回由该个人或群体发现或遭遇的对象。
  * [objectOwnedByAgent](objectOwnedByAgent)：返回由该个人或群体拥有的对象。
  * [objectProducedByAgent](objectProducedByAgent)：返回由该个人或群体（全部或部分）生产的对象。
  * [objectProductionInfluencedByAgent](objectProductionInfluencedByAgent)：返回其创作受该个人或群体影响的对象。
  * [setCreatedByAgent](setCreatedByAgent)：返回由该个人或群体（全部或部分）创建的集合或收藏。
  * [workAboutAgent](workAboutAgent)：返回关于或以该个人或群体为主题的作品。
  * [workAboutOrRepresentsAgent](workAboutOrRepresentsAgent)：返回关于或描绘该个人或群体的作品。
  * [workCreatedByAgent](workCreatedByAgent)：返回由该个人或群体（全部或部分）创作的作品。
  * [workPublishedByAgent](workPublishedByAgent)：返回由该个人或群体出版的作品。
  * [workRepresentsAgent](workRepresentsAgent)：返回代表或描绘该个人或群体的视觉作品。

### 地点 (Place)

  * [activityTookPlaceAtPlace](activityTookPlaceAtPlace)：返回在该地点发生的活动。
  * [agentActiveAtPlace](agentActiveAtPlace)：返回在该地点活跃的个人或群体。
  * [agentBornOrFormedAtPlace](agentBornOrFormedAtPlace)：返回在该地点出生或成立的个人或群体。
  * [agentDiedOrDissolvedAtPlace](agentDiedOrDissolvedAtPlace)：返回在该地点去世或解散的个人或群体。
  * [agentResidentAtPlace](agentResidentAtPlace)：返回在该地点居住或曾居住的个人或群体。
  * [conceptInfluencedByPlace](conceptInfluencedByPlace)：返回其创作受该地点影响的概念。
  * [groupActiveAtPlace](groupActiveAtPlace)：返回在该地点活跃的群体。
  * [groupDissolvedAtPlace](groupDissolvedAtPlace)：返回在该地点解散的群体。
  * [groupFormedAtPlace](groupFormedAtPlace)：返回在该地点成立的群体。
  * [objectCurrentPlace](objectCurrentPlace)：返回据系统所知目前位于该地点的对象。
  * [objectEncounteredAtPlace](objectEncounteredAtPlace)：返回在该地点遭遇的对象。
  * [objectProducedAtPlace](objectProducedAtPlace)：返回在该地点（全部或部分）生产的对象。
  * [objectProductionInfluencedByPlace](objectProductionInfluencedByPlace)：返回其创作受该地点影响的对象。
  * [personActiveAtPlace](personActiveAtPlace)：返回在该地点活跃的个人。
  * [personBornAtPlace](personBornAtPlace)：返回在该地点出生的个人。
  * [personDiedAtPlace](personDiedAtPlace)：返回在该地点去世的个人。
  * [placePartOfPlace](placePartOfPlace)：返回属于该地点一部分的地点。
  * [setCreatedAtPlace](setCreatedAtPlace)：返回在该地点创建的集合。
  * [workAboutOrRepresentsPlace](workAboutOrRepresentsPlace)：返回关于或描绘该地点的作品。
  * [workAboutPlace](workAboutPlace)：返回关于或以该地点为主题的作品。
  * [workCreatedAtPlace](workCreatedAtPlace)：返回在该地点（全部或部分）创作的作品。
  * [workPublishedAtPlace](workPublishedAtPlace)：返回在该地点出版的作品。
  * [workRepresentsPlace](workRepresentsPlace)：返回代表或描绘该地点的视觉作品。

### 概念 (Concept)

  * [activityClassifiedAsConcept](activityClassifiedAsConcept)：返回被分类为该概念的活动。
  * [agentClassifiedAsConcept](agentClassifiedAsConcept)：返回被分类为该概念的个人或群体。
  * [conceptBroaderConcept](conceptBroaderConcept)：返回与该概念具有更广泛关系的概念（例如是更窄的概念）。
  * [conceptClassifiedAsConcept](conceptClassifiedAsConcept)：返回被分类为该概念的概念。
  * [conceptInfluencedByConcept](conceptInfluencedByConcept)：返回受该概念影响的概念。
  * [objectClassifiedAsConcept](objectClassifiedAsConcept)：返回被分类为该概念的对象。
  * [objectMadeOfMaterial](objectMadeOfMaterial)：返回由该材料制成的对象。
  * [objectProductionTechniqueConcept](objectProductionTechniqueConcept)：返回其创作技术为该概念的对象。
  * [placeClassifiedAsConcept](placeClassifiedAsConcept)：返回被分类为该概念的地点。
  * [setClassifiedAsConcept](setClassifiedAsConcept)：返回被分类为该概念的集合。
  * [workAboutConcept](workAboutConcept)：返回关于该概念的作品。
  * [workAboutOrRepresentsConcept](workAboutOrRepresentsConcept)：返回关于或描绘该概念的作品。
  * [workClassifiedAsConcept](workClassifiedAsConcept)：返回被分类为该概念的作品。
  * [workCreationTechniqueConcept](workCreationTechniqueConcept)：返回其创作技术为该概念的作品。
  * [workLanguageLanguage](workLanguageLanguage)：返回以该语言书写或使用该语言的作品。
  * [workRepresentsConcept](workRepresentsConcept)：返回代表或描绘该概念或其实例的视觉作品。

### 活动 (Activity)

  * [activityCausedByActivity](activityCausedByActivity)：返回由该事件或活动导致的活动。
  * [activityPartOfActivity](activityPartOfActivity)：返回属于该时期、事件或活动一部分的时期、事件或活动。
  * [conceptCreationCausedByActivity](conceptCreationCausedByActivity)：返回其创建由该事件或活动导致的概念。
  * [conceptInfluencedByActivity](conceptInfluencedByActivity)：返回受该时期、事件或活动影响的概念。
  * [objectDestructionCausedByActivity](objectDestructionCausedByActivity)：返回其毁坏由该事件或活动导致的对象。
  * [objectProductionCausedByActivity](objectProductionCausedByActivity)：返回其生产由该事件或活动导致的对象。
  * [personDeathCausedByActivity](personDeathCausedByActivity)：返回其死亡由该事件或活动导致的个人。
  * [setCreationCausedByActivity](setCreationCausedByActivity)：返回其创建由该事件或活动导致的集合。
  * [workAboutActivity](workAboutActivity)：返回关于或以该时期、事件或活动为主题的作品。
  * [workAboutOrRepresentsActivity](workAboutOrRepresentsActivity)：返回关于或代表该时期、事件或活动的作品。
  * [workCreationCausedByActivity](workCreationCausedByActivity)：返回其创建由该事件或活动导致的作品。
  * [workRepresentsActivity](workRepresentsActivity)：返回代表或描绘该时期、事件或活动的作品。

### 集合 (Set)

  * [activityUsedSet](activityUsedSet)：返回使用该集合的活动。
  * [conceptInfluencedBySet](conceptInfluencedBySet)：返回受该集合影响的概念。
  * [conceptMemberOfSet](conceptMemberOfSet)：返回属于该集合成员的概念。
  * [entityMemberOfSet](entityMemberOfSet)：返回属于该集合成员的实体。
  * [objectMemberOfSet](objectMemberOfSet)：返回属于该集合成员的对象。
  * [placeMemberOfSet](placeMemberOfSet)：返回属于该集合成员的地点。
  * [setMemberOfSet](setMemberOfSet)：返回属于该集合成员的集合。
  * [temporalMemberOfSet](temporalMemberOfSet)：返回属于该集合成员的时期、事件和活动。
  * [workAboutOrRepresentsSet](workAboutOrRepresentsSet)：返回关于或代表该集合的作品。
  * [workAboutSet](workAboutSet)：返回关于该集合的作品。
  * [workMemberOfSet](workMemberOfSet)：返回属于该集合成员的作品。
  * [workRepresentsSet](workRepresentsSet)：返回代表或描绘该集合的视觉作品。
