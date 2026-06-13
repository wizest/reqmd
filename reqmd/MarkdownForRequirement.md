# 요구사항을 기술하는 Markdown 문법

`ReqMd`는 요구 사항을 작성하기 위한 Markdown 문법과 해당 문법으로 작성된 문서를 의미합니다.

ReqMd 문법은 다음과 같은 주요 요소들로 구성됩니다:

- `식별자`: 요구사항 간의 **관계**를 추적하기 위해 Markdown 링크 문법을 활용합니다.
- `도움자`: 추상적인 표현과 구체적인 표현을 **연결**하기 위해 링크 Markdown 문법을 활용합니다.
- `속성자`: 요구사항의 속성을 정의하기 위해 Markdown 코드블록 문법을 활용합니다.
- `색인`: 요구사항 간의 관계, 연결, 속성을 기술하기 위한 특정 이름의 파일을 활용합니다. 두 가지 색인이 있습니다:
   - `식별자 색인`: 요구사항 간의 관계와 속성을 기술하는 파일로, 파일명은 `@.md`입니다.
   - `도움자 색인`: 추상적인 표현과 구체적인 표현을 연결하는 정보를 담은 파일로, 파일명은 `=.md`입니다.

> 식별자, 도움자, 속성자, 색인을 위해 Markdown 문법을 추가로 확장하지 않아 
> 기존의 범용 Markdown 도구를 그대로 사용할 수 있습니다.

ReqMd 문서를 작성하는 규칙은 다음과 같습니다:

- 요구사항은 하나의 `식별자`를 가진 하나의 **섹션**으로 구성됩니다.
- 요구사항은 **여러** 개의 `도움자`와 `속성자`를 포함할 수 있습니다.
- 요구사항의 섹션 **제목**은 반드시 식별자로 시작해야 합니다.
- 요구사항의 식별자간 **관계** 정보는 `식별자 색인`에 기술합니다.
- 요구사항의 도움자간 **연결** 정보는 `도움자 색인`에 기술합니다.
- 요구사항은 **계층** 구조를 가질 수 있으며, 자식 요구사항은 섹션의 서브 섹션으로 구성합니다.

> 요구사항의 관계 및 연결 정보는 본문에서 분리하여 색인에 작성하는 것이 중요합니다. 
> 이러한 색인은 통계, 검색, 요약, 번역 등 다양한 목적으로 활용될 수 있습니다.

아래는 이러한 방법으로 작성된 요구사항 문서의 예시입니다:

````markdown
## [GLD_INIT](@) 초기화 

```yaml 
Variant: Evo
```

- GLD(Gear lever determination)는 [position_lever_delayed](=)를 [macro_lever_position_0](=)으로 초기화해야 합니다.
- GLD는 매 시간 단계의 시작 시 [count_time](=)을 비활성화 상태로 초기화해야 합니다.
- [position_lever_delayed](=)는 첫 번째 시간 단계에서 [macro_lever_position_0](=)과 동일해야 합니다.
- [count_time](=)은 컴포넌트가 실행될 때 매 시간 단계의 시작 시 비활성화되어야 합니다.
````
- 식별자: GLD_INIT
- 도움자: position_lever_delayed,macro_lever_position_0,count_time
- 속성자: Variant


## 문법

### 식별자 (Identifier)

`식별자(Identifier)`는 요구사항 간의 관계를 표현하며, Markdown 문법을 활용하여 특수 파일 `@`을 링크하는 문자열 입니다.
`@` 파일은 `식별자 색인`으로 식별자에 대한 색인 정보를 포함합니다.

식별자는 다음과 같은 형식으로 구성됩니다:

- 기본 형식: `[identifier](@)`
- 상세 형식: `[identifier](pathto/@#fragment "description")`

이 형식에서 `[identifier](pathto/@#fragment "description")`는 Markdown 링크 문법을 활용하여 요구사항을 식별합니다.

각 요소의 의미는 다음과 같습니다:

- `identifier`: 해당 경로 내에서 요구사항을 가리키는 유일한 문자열입니다.
- `pathto/`: 요구사항이 저장된 파일의 경로입니다. pathto는 식별자의 이름 충돌을 방지하고, 식별자를 구조화할 수 있습니다.
- `#fragment`: 색인의 특정 위치를 지정합니다. 기존 범용 markdown 도구와 호환성을 향상시킵니다.
- `"description"`: 식별자를 설명하는 문자열입니다.

`pathto/`, `#fragment`, `"description"` 요소는 선택적으로 생략할 수 있으며, 다음과 같은 다양한 형태로 사용될 수 있습니다:

- `[identifier](@)`
- `[identifier](pathto/@)`
- `[identifier](@#fragment)`
- `[identifier](@ "description")`



### 도움자 (Helper)

`도움자(Helper)`는 추상적인 표현과 구체적인 표현 간의 연결을 표현하며, Markdown 문법을 활용하여 특수 파일 `=`을 링크하는 문자열 입니다.
`=` 파일은 `도움자 색인`으로 도움자에 대한 색인 정보를 포함합니다. 

도움자는 다음과 같은 형식으로 구성됩니다:

- 기본 형식: `[helper](=)`
- 상세 형식: `[helper](pathto/=#fragment "description")`

이 형식에서 `[helper](pathto/=#fragment "description")`는 Markdown 링크 문법을 활용하여 연결하고자 하는 대상을 표현합니다. 

각 요소의 의미는 다음과 같습니다:

- `helper`: 해당 경로 내에서 특정 대상을 가리키는 고유한 문자열입니다.
- `pathto/`: 요구사항이 저장된 파일의 경로입니다. pathto는 도움자의 이름 충돌을 방지하고, 도움자를 구조화할 수 있습니다.
- `#fragment`: 색인의 특정 위치를 지정합니다. 기존 범용 markdown 도구와 호환성을 향상시킵니다.
- `"description"`: 도움자를 설명하는 문자열입니다.

`pathto/`, `#fragment`, `"description"` 요소는 선택적으로 생략할 수 있으며 다양한 형태로 사용될 수 있습니다:

- `[helper](=)`
- `[helper](path/=)`
- `[helper](=#fragment)`
- `[helper](= "description")`


### 속성자 (Attribute)

`속성자`는 사용자 변수를 명시하기 위해 Markdown 코드블록을 사용하여 YAML 형식으로 정의됩니다. 이 변수들은 해당 요구사항의 식별자 내에서 유효합니다. 한 요구사항 내에서 속성자를 여러 번 나누어 자유롭게 배치할 수 있으며, 요구사항에 기록된 속성자와 이와 관련된 식별자 색인에 있는 속성자는 같은 수준으로 취급됩니다. 단일 식별자에 연결된 모든 속성자는 하나로 합쳐집니다.

속성자는 다음과 같은 형식으로 작성됩니다:

``````markdown
```yaml
Attribute1: Value1
Attribute2: Value2
Attribute3: Value3
Attribute4: Value4
```
``````


### 식별자 색인 (`@.md` 파일)

`식별자 색인` 은 Markdown 파일로 작성되며, 각 식별자에 대한 관계(relationship) 정보를 표현합니다. 식별자 색인은 요구사항의 식별자와 관련된 모든 정보를 포함하며, 요구사항 간의 관계를 명확히 하기 위해 사용됩니다. 

식별자 색인은 다음과 같은 형식으로 작성됩니다:

````markdown
## [식별자](@)

- [원문](요구사항이 기술된 문서)
- [관계한 식별자1](@)
- [관계한 식별자2](pathto/@)

```yaml
UserField1: Value1
UserField2: Value2

```
````

식별자 색인 섹션에 포함된 모든 식별자는 서로 관계한 것입니다. 식별자 간의 구체적 관계는 pathto 를 활용하여 특정할 수 있습니다. 예를 들어 pathto 를 sysrq, swrq, swit, swqt, sysqt 가 되도록 파일의 경로를 설정하여 현재 식별자의 상위 또는 하위 요구사항 간 관계를 명시적으로 특정할 수 있습니다.

식별자 색인 색션에 포함된 속성자는 식별자가 특정하는 요구사항을 범위로 한 사용자 정의 변수입니다. 요구사항에서 기술한 속성자와 동일한 효과를 가지며, 요구사항에 대한 메타정보를 시스템적으로 처리하고자 할 떄 유용합니다.


### 도움자 색인 (`=.md` 파일)

`도움자 색인` 은 Markdown 파일로 작성되며, 각 도움자에 대한 연결(mapping) 정보를 표현합니다. 도움자 색인은 요구사항의 도움자와 관련된 모든 정보를 포함하며, 도움자간 연결을 명확히 하기 위해 사용됩니다. 

도움자 색인은 다음과 같은 형식으로 작성됩니다:


````markdown
## [도움자](=)

- [원문](도움자가 기술된 문서)
- [연결된 도움자1](=)
- [연결된 도움자2](pathto/=)

```yaml
UserField1: Value1
UserField2: Value2
```
````

도움자 색인 섹션에 포함된 모든 도움자는 서로 연결된 것입니다. 도움자 간의 구체적 관계는 pathto 를 활용하여 특정할 수 있습니다. 예를 들어 pathto 를 sysrq, swrq, swit, swqt, sysqt 가 되도록 파일의 경로를 설정하여 현재 도움자의 상위 또는 하위 도움자 간 연결을 명시적으로 특정할 수 있습니다.

도움자 색인 색션에 포함된 속성자는 도움자의 범위로 한 사용자 정의 변수입니다. 도움자에 대한 메타정보를 시스템적으로 처리하고자 할 떄 유용합니다.


## 구조

### 문서 구조

ReqMd 문서의 파일 구조를 McKeeman Form으로 표현하면 다음과 같습니다. 이 구조는 요구사항 문서의 일관성을 유지하고, 다양한 요구사항을 명확하게 표현하도록 돕기 위해 설계되었습니다. 

```plaintext
ReqMd
  DocumentHeader newline Requirements

DocumentHeader
  "# " RequirementDocumentName newline MarkdownDescription

RequirementDocumentName
  "<Requirement Document Name>"

MarkdownDescription
  "<Requirement description as markdown>"

Requirements
  Requirement
  Requirement newline Requirements

Requirement
  RequirementHeader newline RequirementBody
  RequirementHeader newline RequirementAttributes newline RequirementBody

RequirementHeader
  RequirementDepth Identifier
  RequirementDepth Identifier " " SubTitle

RequirementDepth
   "<Depth of requirement as number of '#'> "
   
Identifier
  "<Unique identifier for the requirement in ReqMd syntax>"

SubTitle
  "<Subtitle>"

RequirementAttributes
  "```yaml" newline AttributeList "```" newline

AttributeList
  Attribute
  Attribute newline AttributeList

Attribute
  "<Attribute definition as yaml syntax in ReqMd syntax>"

RequirementBody
  MarkdownDescription
  MarkdownDescription Helper
  MarkdownDescription Helper MarkdownDescription

Helper
  "<Relation of symbols in ReqMd syntax>"
```

### 파일 구조

문서는 다음과 같은 파일 구조로 구성됩니다:

```plaintext
RequirementRoot/
  RequirementPath1/  # 요구사항 경로1
    Document1.md         # 요구사항 문서1
    Document2.md         # 요구사항 문서2
    Document3.md         # 요구사항 문서3
    DocumentN.md         # 요구사항 문서N
    @.md                 # 식별자 색인 파일
    =.md                 # 도움자 색인 파일

  RequirementPath2/  # 요구사항 경로2
    Document1.md
    Document2.md
    Document3.md
    DocumentN.md
    @.md
    =.md
```

- `RequirementRoot`: 모든 요구사항 문서의 최상위 디렉토리입니다. 이 디렉토리 아래에 여러 경로로 요구사항 문서를 구성합니다.
- `RequirementPath1`: 특정 주제나 기능에 대한 요구사항을 그룹화한 경로입니다.
- `Document1.md, Document2.md, Document3.md, DocumentN.md`: 각각의 요구사항 문서로, 특정 기능이나 사항에 대한 설명, 요구사항, 테스트 케이스 등을 포함합니다.
- `@.md`: 식별자 색인 파일로, 해당 경로의 모든 요구사항 문서에 `관계`를 포함합니다.
- `=.md`: 도움자 색인 파일로, 해당 경로의 모든 도움자에 대한 `연결`를 포함합니다.
