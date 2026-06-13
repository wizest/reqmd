# 요구사항을 기술하는 Markdown 문법 소개

`ReqMd`는 요구 사항을 작성하기 위한 Markdown 문법과 해당 문법으로 작성된 문서를 가리킵니다.
이 문서는 본문이 설명하는 구조를 따르는 여러 개의 파일로 구성됩니다.

이 문서를 기술하는 문법은 다음과 같은 주요 요소들을 포함합니다:

1. **식별자**: 관계(Relation)의 추적을 위해 링크(link) 문법을 활용합니다. 이를 통해 요구사항 간의 관계를 명확히 할 수 있습니다.
2. **도움자**: 추상적 표현과 구체적 표현 간의 연결(mapping)을 위해 링크 문법을 사용합니다. 이는 요구사항의 이해를 돕는 역할을 합니다.
3. **속성자**: 요구사항의 속성(Attribute)을 표현하기 위해 자동 링크(Autolink) 기능을 활용합니다. 이는 요구사항의 상세 정보를 더하는 데 유용합니다.
4. **색인**: 요구사항의 관계, 연결, 속성을 기술하기 위한 특별한 파일이 필요합니다. 이를 위해 두 가지 색인을 제안합니다:
   - **식별자색인**: 관계와 속성을 기술하는 파일로, 이름은 **@.md**입니다.
   - **도움자색인**: 추상과 구상을 연결하는 정보를 담는 파일로, 이름은 **=.md**입니다.

> 새로운 문법을 추가하지 않음으로써 사용자는 기존의 범용 도구를 그대로 사용할 수 있습니다.

이 문서를 작성하는 규칙은 다음과 같습니다:

- 각 요구사항은 하나의 섹션으로 구성됩니다.
- 요구사항 섹션은 여러 개의 식별자, 도움자, 속성자를 포함할 수 있습니다.
- 각 요구사항의 섹션 제목은 반드시 식별자로 시작해야 합니다.
- 요구사항은 하위 요구사항을 포함할 수 있는 서브섹션으로 구성될 수 있습니다.
- 요구사항의 관계와 속성 정보는 해당 식별자 섹션이 포함된 **식별자색인**에 기술되어야 합니다.
- 도움자 간의 연결 정보는 **도움자색인**의 해당 도움자 섹션에 기록되어야 합니다.

> 요구사항의 관계, 연결, 속성 정보는 본문과 분리하여 색인에 작성하는 것이 중요합니다. 이러한 색인은 통계, 색인, 검색, 요약, 번역 등의 다양한 목적으로 가공될 수 있습니다.


위와 같은 방법으로 요구사항을 기술한 문서 예제 입니다.

 
```markdown
## [GLD_INIT](@) Initialization
 
- GLD shall initialize [position_lever_delayed](=) with [macro_lever_position_0](=)
- GLD shall initialize [count_time](=) as deactivated at the beginning of each time step.
...
 
### Acceptance criteria
 
- [position_lever_delayed](=) is equal to [macro_lever_position_0](=) at the first time step.
- [count_time](=) is deactivated at the beginning of each time step as the component is running
...

```


## 문서 구조

ReqMd 문서의 개별 파일 구조를 McKeeman Form 으로 표현하면 다음과 같습니다.
이 문서 구조는 요구 사항 문서화의 일관성을 높이고, 다양한 요구 사항을 명확하게 표현할 수 있도록 돕기 위해 설계되었습니다. 마크다운 형식의 사용은 가독성을 증가시키며, YAML 속성 정의는 추가적인 메타데이터를 제공하여 요구 사항을 보다 세부적으로 기술할 수 있게 합니다.


```
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
  "## " Identifier
  "## " Identifier " " SubTitle

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

## 파일 구조

문서를 구성하는 여러개의 파일은 다음과 같이 구성됩니다.


```
RequirementRoot/
  RequirementCategory1/  # 요구사항 카테고리1
    Document1.md         # 요구사항 문서1
    Document2.md         # 요구사항 문서2
    Document3.md         # 요구사항 문서3
    DocumentN.md         # 요구사항 문서N
    @.md                 # 식별자 색인 파일
    =.md                 # 도움자 색인 파일

  RequirementCategory2/  # 요구사항 카테고리2
    Document1.md
    Document2.md
    Document3.md
    DocumentN.md
    @.md
    =.md

  ...

```

- RequirementRoot: 모든 요구사항 문서의 최상위 디렉토리입니다. 이 디렉토리 아래에 여러 카테고리로 요구사항 문서를 구성합니다.
- RequirementCategory1: 첫 번째 요구사항 카테고리를 나타내며, 이 카테고리에 관련된 모든 요구사항 문서를 포함합니다. 일반적으로 이곳에는 특정 주제나 기능에 대한 요구사항이 담긴 문서들이 위치합니다.
- Document1.md, Document2.md, Document3.md, DocumentN.md: 각각의 요구사항 문서입니다. 특정 기능이나 사항에 대해 자세한 설명, 요구사항, 테스트 케이스 등을 포함할 수 있습니다. 이러한 문서는 보통 버전 관리 및 수정 이력을 유지해야 합니다.
- @.md: 식별자 인덱스 파일로, 이 카테고리의 모든 문서에 대한 참조 및 링크를 포함합니다. 이를 통해 사용자는 각 식별자를 포함하는 문서로 빠르게 이동할 수 있습니다. 
- =.md: 도움자 인덱스 파일로, 이 카테고리의 모든 문서에 대한 참조 및 링크를 포함합니다. 이를 통해 사용자는 각 도움자를 포함하는 문서로 빠르게 이동할 수 있습니다. 



## 식별자 (Identifier)

<!--
Markdown 문법으로 특수 파일 `@`을 링크하는 문자열을 `식별자`라고 합니다. `@` 파일은 식별자의 색인 정보를 포함합니다.

- `[Identifier](@)`
- `[Identifier](pathto/@#fragment "description")`

 
`[identifier](path/@#fragment "description")`
: Markdown Link 문법으로 요구사항 **관계**의 출발점(source)과 도착점(target) 을 표현함
 
- `path/` 는 요구사항이 저장된 file path 이며, 여러 요구사항 문서를 구조화 한다.
- `identifier` 는 path 범위에서 요구사항을 가리키는 유일한 문자열이다.
- `#fragment` 는 색인의 특정 위치를 가리킨다.
- `"description"` 은 identifier를 설명하는 문자열이다.
- `path/`, `#fragment`, `"description"`은 생략할 수 있다.
  - `[id](@)`, `[id](path/@)`, `[id](@#fragment)`, `[id](@ "desc")`
-->


`식별자(Identifier)`는 Markdown 문법을 사용하여 특수 파일 `@`을 링크하는 문자열을 의미합니다. 이러한 `@` 파일은 식별자에 대한 색인 정보를 포함하고 있습니다. 

식별자는 다음과 같은 형식으로 구성됩니다:

- 기본 형식: `[Identifier](@)`
- 상세 형식: `[Identifier](pathto/@#fragment "description")`

이 형식에서 `[identifier](path/@#fragment "description")`는 Markdown 링크 문법을 활용하여 요구사항의 출발점(source)과 도착점(target)을 표현합니다. 각 요소를 살펴보면 다음과 같습니다:

- `path/`: 요구사항이 저장된 파일의 경로로, 여러 요구사항 문서를 구조화할 수 있습니다.
- `identifier`: 해당 경로 내에서 요구사항을 가리키는 유일한 문자열입니다.
- `#fragment`: 색인의 특정 위치를 지정합니다.
- `"description"`: 식별자를 설명하는 문자열입니다.

추가적으로, `path/`, `#fragment`, `"description"` 요소는 선택적으로 생략할 수 있으며, 다음과 같은 다양한 형태로 사용될 수 있습니다:

- `[id](@)`
- `[id](path/@)`
- `[id](@#fragment)`
- `[id](@ "desc")` 

이를 통해 요구사항 간의 관계를 효과적으로 명시할 수 있습니다.


## 도움자 (Helper)

<!--
Markdown 문법으로 특수 파일 `=`을 링크하는 문자열을 `도움자`라고 합니다. `=` 파일은 도움자의 색인 정보를 포함합니다.

- `[Helper](=)`
- `[Helper](pathto/=#fragment "description")`


`[helper](path/=#fragment "description")`
: Markdown Link 문법으로 **연결** 하고자 하는 추상적 또는 구체적 대상을 표현함
 
- `path/` 는 요구사항이 저장된 file path 이며, 여러 요구사항 문서를 구조화 한다.
- `helper` 는 path 범위에서 추상적 또는 구체적 대상을 가리키는 유일한 문자열이다.
- `#fragment` 는 색인의 특정 위치를 가리킨다.
- `"description"` 은 helper를 설명하는 문자열이다.
- `path/`, `#fragment`, `"description"`은 생략할 수 있다.
  - `[help](=)`, `[help](path/=)`, `[help](=#fragment)`, `[help](= "desc")` 
-->

`도움자`는 Markdown 문법을 활용하여 특수 파일 `=`을 링크하는 문자열로, 이 파일은 도움자에 대한 색인 정보를 포함하고 있습니다. 도움자는 다음과 같은 형식으로 구성됩니다:

- 기본 형식: `[Helper](=)`
- 상세 형식: `[Helper](pathto/=#fragment "description")`

이 형식에서 `[helper](path/=#fragment "description")`는 Markdown 링크 문법을 통해 연결하고자 하는 대상을 표현합니다. 각 요소는 다음을 의미합니다:

- `path/`: 요구사항이 저장된 파일의 경로로, 여러 요구사항 문서를 구조화하는 데 사용됩니다.
- `helper`: 해당 경로 내에서 특정 대상을 가리키는 고유한 문자열입니다.
- `#fragment`: 색인의 특정 위치를 지정합니다.
- `"description"`: 도움자를 설명하는 문자열입니다.

`path/`, `#fragment`, `"description"` 요소는 생략할 수 있으며 다양한 형태로 사용될 수 있습니다:

- `[help](=)`
- `[help](path/=)`
- `[help](=#fragment)`
- `[help](= "desc")`

이 구조를 통해 요구사항이나 정보 간의 관계를 효과적으로 명시할 수 있습니다.



## 속성자 (Attribute) 

<!--
Markdown 문법으로 `yaml` 형식으로 작성된 인용블록을 `속성자`라고 합니다. 속성자는 식별자 색인 또는 도움자 색인에서 사용합니다.


```yaml
Attribute1: Value1
Attribute2: Value2
Attribute3: Value3
    Attribute4: Value4
    Attribute4: Value4
```
-->

Markdown 문법을 활용하여 `yaml` 형식으로 작성된 인용블록을 `속성자`라고 합니다. 속성자는 식별자 색인이나 도움자 색인에서 활용됩니다. 속성자는 다음과 같은 형식으로 작성됩니다:

```yaml
Attribute1: Value1
Attribute2: Value2
Attribute3: Value3
Attribute4: Value4
```

이 형식은 다양한 속성과 그에 대한 값을 구조적으로 표현하는 데 유용합니다.



## 식별자 색인 파일 (`@.md` file)
 
```markdown
## [요구사항ID](@)

- [원문](요구사항이 기술된 문서)
- [연결된 식별자1](@)
- [연결된 식별자2](다른path/@)
```

## 도움자 색인 파일 (`=.md` file)
 

```markdown
## [요구사항ID](@)

- [원문](도움자가 기술된 문서)
- [연결된 도움자1](=)
- [연결된 도움자2](다른path/=)
```
