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

이 문서에서 사용하는 용어는 다음 의미로 고정합니다:

- `요구사항 문서`: 요구사항 본문을 담은 일반 Markdown 파일입니다. 예: `SwReq.md`.
- `요구사항 경로`: 하나 이상의 요구사항 문서와 색인 파일을 함께 두는 디렉토리입니다.
- `식별자`: 하나의 요구사항을 가리키는 고유 이름입니다.
- `도움자`: 요구사항 본문에서 추적해야 하는 대상, 개념, 신호, 함수, 상태, 테스트 관찰값을 가리키는 이름입니다.
- `색인 파일`: 요구사항 경로마다 둘 수 있는 `@.md`, `=.md` 파일입니다.
- `링크 대상 @`: Markdown 링크에서 `@.md` 파일을 의미하는 축약 대상입니다. 예를 들어 `[REQ_001](@)`는 현재 요구사항 경로의 `@.md`에 있는 `REQ_001` 항목을 가리킵니다.
- `링크 대상 =`: Markdown 링크에서 `=.md` 파일을 의미하는 축약 대상입니다. 예를 들어 `[speed](=)`는 현재 요구사항 경로의 `=.md`에 있는 `speed` 항목을 가리킵니다.

ReqMd는 다음 표준 규칙을 기준으로 검증할 수 있어야 합니다:

- 식별자 이름은 정규식 `[A-Z][A-Z0-9_]*`을 따릅니다.
- 도움자 이름은 정규식 `[A-Za-z_][A-Za-z0-9_]*`을 따릅니다.
- `[REQ](@)`는 현재 요구사항 경로의 `@.md` 색인 엔트리 참조입니다.
- `[REQ](path/@)`는 `path/@.md` 색인 엔트리 참조입니다.
- `[name](=)`는 현재 요구사항 경로의 `=.md` 색인 엔트리 참조입니다.
- `[name](path/=)`는 `path/=.md` 색인 엔트리 참조입니다.
- 관계와 연결은 색인 섹션의 링크 목록으로 기록하며, 역방향 관계는 도구가 계산합니다.
- 문법 검증은 구조와 링크의 정합성을 확인하고, 품질 검증은 요구사항 문장의 명확성과 검증 가능성을 확인합니다.

ReqMd 문서를 작성하는 규칙은 다음과 같습니다:

- 요구사항은 하나의 `식별자`를 가진 하나의 **섹션**으로 구성됩니다.
- 요구사항은 **여러** 개의 `도움자`와 `속성자`를 포함할 수 있습니다.
- 요구사항의 섹션 **제목**은 반드시 식별자로 시작해야 합니다.
- 요구사항의 식별자간 **관계** 정보는 `식별자 색인`에 기술합니다.
- 요구사항의 도움자 간 **연결** 정보는 `도움자 색인`에 기술합니다.
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

`식별자(Identifier)`는 요구사항 하나를 고유하게 가리키는 이름입니다. Markdown 문법을 활용하여 특수 링크 대상 `@`을 링크합니다.
링크 대상 `@`은 현재 요구사항 경로의 `@.md` 식별자 색인을 의미합니다.

식별자는 다음과 같은 형식으로 구성됩니다:

- 기본 형식: `[identifier](@)`
- 상세 형식: `[identifier](pathto/@#fragment "description")`

이 형식에서 `[identifier](pathto/@#fragment "description")`는 Markdown 링크 문법을 활용하여 요구사항을 식별합니다.

각 요소의 의미는 다음과 같습니다:

- `identifier`: 해당 요구사항 경로 안에서 요구사항을 가리키는 유일한 문자열입니다.
- `pathto/`: 다른 요구사항 경로의 색인을 가리키는 상대 경로입니다. `pathto/@`는 `pathto/@.md`의 식별자 색인을 의미합니다. `pathto`는 식별자 이름 충돌을 방지하고, 식별자를 요구사항 계층별로 구조화할 때 사용합니다.
- `#fragment`: 색인 파일 안의 특정 섹션 위치를 지정합니다. 생략할 수 있으나, 자동화 도구가 색인을 갱신할 때는 가능한 실제 섹션 앵커로 보강합니다.
- `"description"`: 식별자를 설명하는 문자열입니다.

`pathto/`, `#fragment`, `"description"` 요소는 선택적으로 생략할 수 있으며, 다음과 같은 다양한 형태로 사용될 수 있습니다:

- `[identifier](@)`
- `[identifier](pathto/@)`
- `[identifier](@#fragment)`
- `[identifier](@ "description")`

식별자 이름은 Markdown 표시 텍스트에 있는 `identifier`를 기준으로 합니다. 링크의 `pathto/`는 식별자의 범위를 정할 뿐, 식별자 이름의 일부가 아닙니다. 예를 들어 `[GLD_INIT](sw/@)`와 `[GLD_INIT](sys/@)`는 이름은 같지만 서로 다른 요구사항 경로의 식별자를 가리킵니다.

표준 식별자 이름은 `[A-Z][A-Z0-9_]*` 정규식을 따릅니다. 소문자, 공백, 하이픈, 마침표는 식별자 이름에 사용하지 않습니다. 외부 도구에서 가져온 식별자가 이 규칙을 따르지 않으면 원문 값은 속성자로 보존하고, ReqMd 식별자는 표준 형식으로 별도 부여합니다.



### 도움자 (Helper)

`도움자(Helper)`는 추상적인 표현과 구체적인 표현 간의 연결을 표현하는 이름입니다. Markdown 문법을 활용하여 특수 링크 대상 `=`을 링크합니다.
링크 대상 `=`은 현재 요구사항 경로의 `=.md` 도움자 색인을 의미합니다. 

도움자는 다음과 같은 형식으로 구성됩니다:

- 기본 형식: `[helper](=)`
- 상세 형식: `[helper](pathto/=#fragment "description")`

이 형식에서 `[helper](pathto/=#fragment "description")`는 Markdown 링크 문법을 활용하여 연결하고자 하는 대상을 표현합니다. 

각 요소의 의미는 다음과 같습니다:

- `helper`: 해당 요구사항 경로 안에서 특정 대상을 가리키는 고유한 문자열입니다.
- `pathto/`: 다른 요구사항 경로의 색인을 가리키는 상대 경로입니다. `pathto/=`는 `pathto/=.md`의 도움자 색인을 의미합니다. `pathto`는 도움자 이름 충돌을 방지하고, 도움자를 요구사항 계층별로 구조화할 때 사용합니다.
- `#fragment`: 색인 파일 안의 특정 섹션 위치를 지정합니다. 생략할 수 있으나, 자동화 도구가 색인을 갱신할 때는 가능한 실제 섹션 앵커로 보강합니다.
- `"description"`: 도움자를 설명하는 문자열입니다.

`pathto/`, `#fragment`, `"description"` 요소는 선택적으로 생략할 수 있으며 다양한 형태로 사용될 수 있습니다:

- `[helper](=)`
- `[helper](path/=)`
- `[helper](=#fragment)`
- `[helper](= "description")`

도움자 이름은 Markdown 표시 텍스트에 있는 `helper`를 기준으로 합니다. 링크의 `pathto/`는 도움자의 범위를 정할 뿐, 도움자 이름의 일부가 아닙니다.

표준 도움자 이름은 `[A-Za-z_][A-Za-z0-9_]*` 정규식을 따릅니다. 코드, 모델, 테스트에 실제 이름이 있으면 가능한 그 이름을 그대로 사용합니다. 표시 이름에 공백이나 단위 설명이 필요하면 링크 설명(`"description"`)이나 속성자를 사용합니다.


### 속성자 (Attribute)

`속성자`는 사용자 변수를 명시하기 위해 Markdown 코드블록을 사용하여 YAML 형식으로 정의됩니다. 이 변수들은 해당 요구사항의 식별자 내에서 유효합니다. 한 요구사항 내에서 속성자를 여러 번 나누어 배치할 수 있으며, 요구사항 본문에 기록된 속성자와 이와 관련된 식별자 색인에 있는 속성자는 같은 수준으로 취급됩니다. 단일 식별자에 연결된 모든 속성자는 하나로 합쳐집니다.

속성자는 다음과 같은 형식으로 작성됩니다:

``````markdown
```yaml
Attribute1: Value1
Attribute2: Value2
Attribute3: Value3
Attribute4: Value4
```
``````

속성자를 병합할 때 같은 키가 여러 번 나오면 다음 규칙을 적용합니다:

- 값이 모두 같으면 하나의 속성으로 취급합니다.
- 값이 다르면 문서 본문의 값을 우선합니다.
- 색인 파일의 값은 본문에 없는 메타정보를 보완하는 용도로 사용합니다.
- 같은 키에 여러 값이 필요한 경우 YAML 배열을 사용합니다.

예:

```yaml
Keyword:
  - startup
  - safety
```


### 식별자 색인 (`@.md` 파일)

`식별자 색인` 은 Markdown 파일로 작성되며, 각 식별자에 대한 관계(relationship) 정보를 표현합니다. 식별자 색인은 요구사항의 식별자와 관련된 모든 정보를 포함하며, 요구사항 간의 관계를 명확히 하기 위해 사용됩니다. 

식별자 색인은 다음과 같은 형식으로 작성됩니다:

````markdown
## [식별자](@)

- [원문](요구사항이 기술된 문서)
- [관계있는 식별자1](@)
- [관계있는 식별자2](pathto/@)

```yaml
UserField1: Value1
UserField2: Value2

```
````

식별자 색인 섹션에 포함된 링크는 현재 섹션의 식별자와 관계가 있는 항목입니다. 관계의 종류는 링크 대상의 경로, 문서 위치, 주변 설명, 프로젝트 맥락으로 해석합니다. 색인 파일은 기본적으로 관계 타입을 강제하지 않습니다.

예:

```markdown
## [SW_GLD_INIT](@)

- [SYS_GLD_STARTUP](../sys/@)
- [SWQT_GLD_INIT_001](../swqt/@)
```

식별자 간의 관계 맥락은 경로를 활용하여 구분합니다. 예를 들어 `sysrq`, `swrq`, `swit`, `swqt`, `sysqt` 같은 요구사항 경로를 사용하면 현재 식별자가 시스템 요구사항, 소프트웨어 요구사항, 통합 테스트, 소프트웨어 테스트 중 어떤 항목과 연결되는지 추론할 수 있습니다.

양방향 추적이 필요한 경우에도 문서에는 한 방향의 링크만 기록할 수 있습니다. 반대 방향 관계는 도구가 색인 전체를 분석하여 계산합니다. 프로젝트에서 양방향 명시를 요구할 수는 있지만, 이 경우 두 방향의 불일치를 검증 대상으로 봅니다.

식별자 색인 섹션에 포함된 속성자는 식별자가 특정하는 요구사항을 범위로 한 사용자 정의 변수입니다. 요구사항에서 기술한 속성자와 동일한 효과를 가지며, 요구사항에 대한 메타정보를 시스템적으로 처리하고자 할 때 유용합니다.


### 도움자 색인 (`=.md` 파일)

`도움자 색인` 은 Markdown 파일로 작성되며, 각 도움자에 대한 연결(mapping) 정보를 표현합니다. 도움자 색인은 요구사항의 도움자와 관련된 모든 정보를 포함하며, 도움자 간 연결을 명확히 하기 위해 사용됩니다. 

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

도움자 색인 섹션에 포함된 링크는 현재 섹션의 도움자와 연결된 항목입니다. 연결의 종류는 링크 대상의 경로, 문서 위치, 주변 설명, 프로젝트 맥락으로 해석합니다. 색인 파일은 기본적으로 연결 타입을 강제하지 않습니다.

예:

```markdown
## [position_lever_delayed](=)

- [LeverPositionDelayed](../design/=)
- [actual_lever_position](../test/=)
```

도움자 간의 연결 맥락은 경로를 활용하여 구분합니다. 예를 들어 `design`, `code`, `test`, `swqt` 같은 경로를 사용하면 현재 도움자가 설계 항목, 코드 항목, 테스트 관찰값 중 어떤 항목과 연결되는지 추론할 수 있습니다.

도움자 연결도 문서에는 한 방향의 링크만 기록할 수 있으며, 역방향 연결은 도구가 색인 전체를 분석하여 계산합니다. 양방향을 모두 기록하는 프로젝트에서는 양쪽 링크가 서로 일치하는지 검증해야 합니다.

도움자 색인 섹션에 포함된 속성자는 도움자를 범위로 한 사용자 정의 변수입니다. 도움자에 대한 메타정보를 시스템적으로 처리하고자 할 때 유용합니다.


## 구조

### 문서 구조

ReqMd 문서의 문서 구조를 McKeeman Form으로 표현하면 다음과 같습니다. 이 구조는 요구사항 문서의 일관성을 유지하고, 다양한 요구사항을 명확하게 표현하도록 돕기 위해 설계되었습니다. 

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
  RequirementHeader newline RequirementBody newline ChildRequirements
  RequirementHeader newline RequirementAttributes newline RequirementBody newline ChildRequirements

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

ChildRequirements
  Requirement
  Requirement newline ChildRequirements
```

위 구조에서 `RequirementDepth`는 Markdown 제목 깊이입니다. 부모 요구사항이 `##`이면 자식 요구사항은 `###`처럼 더 깊은 제목으로 작성합니다. 같은 깊이의 다음 요구사항이 나오면 이전 요구사항 섹션은 종료됩니다.

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
- `@.md`: 식별자 색인 파일로, 해당 경로의 요구사항 식별자에 대한 관계와 속성을 포함합니다.
- `=.md`: 도움자 색인 파일로, 해당 경로의 도움자에 대한 연결과 속성을 포함합니다.


## Agentic Coding 활용을 위한 작성 원칙

ReqMd 문서는 사람이 읽는 요구사항 문서이면서, 동시에 agentic coding 도구가 요구사항을 검색, 수정, 검증, 추적할 수 있는 구조화된 입력입니다. 따라서 문서는 자연어 설명만 충분한 상태가 아니라, 에이전트가 기계적으로 판단할 수 있는 단서를 함께 포함해야 합니다.

### 에이전트가 수행할 수 있어야 하는 작업

ReqMd 기반 skill은 다음 작업을 안정적으로 수행할 수 있어야 합니다:

- 새 요구사항 문서를 ReqMd 형식으로 작성합니다.
- 기존 요구사항에서 식별자, 도움자, 속성자를 추출합니다.
- 요구사항 본문과 `@.md`, `=.md` 색인 사이의 불일치를 찾습니다.
- 상위 요구사항, 하위 요구사항, 테스트, 설계 항목 사이의 추적 관계를 갱신합니다.
- 속성자 값을 기준으로 요구사항을 분류, 필터링, 요약합니다.
- 요구사항 변경이 관련 요구사항과 테스트 케이스에 미치는 영향을 분석합니다.

### 작성 단위

요구사항 하나는 하나의 식별자 섹션으로 작성합니다. 에이전트가 섹션 경계를 안정적으로 찾을 수 있도록 다음 규칙을 지킵니다:

- 섹션 제목은 항상 `[IDENTIFIER](@)` 형식으로 시작합니다.
- 같은 경로 안에서 식별자 이름은 중복하지 않습니다.
- 제목의 식별자 뒤에는 사람이 읽기 쉬운 짧은 제목을 붙일 수 있습니다.
- 요구사항 본문에는 요구사항의 의도, 조건, 기대 결과를 명확히 적습니다.
- 여러 요구사항을 한 문장에 섞지 않습니다. 독립적으로 검증해야 하는 내용은 별도 식별자로 분리합니다.

예:

````markdown
## [GLD_INIT](@) 초기화

```yaml
Type: Functional
Status: Draft
Variant: Evo
```

- GLD는 첫 번째 시간 단계에서 [position_lever_delayed](=)를 [macro_lever_position_0](=)으로 초기화해야 합니다.
- GLD는 컴포넌트 실행 중 각 시간 단계의 시작 시 [count_time](=)을 비활성화해야 합니다.
````

### 식별자 작성 규칙

식별자는 요구사항 추적의 기준이므로 사람이 보기 쉽고 변경에 강해야 합니다.

- 대문자 영문, 숫자, 밑줄(`_`)을 기본 문자로 사용합니다.
- 의미 있는 접두사를 사용합니다. 예: `SYS_`, `SWRQ_`, `SWQT_`, `TC_`.
- 문서 제목이나 자연어 문장이 바뀌어도 식별자는 가능한 유지합니다.
- 삭제된 식별자는 재사용하지 않습니다.
- 이름 충돌 가능성이 있으면 경로를 활용합니다. 예: `[GLD_INIT](sw/@)`, `[GLD_INIT](sys/@)`.

### 도움자 작성 규칙

도움자는 요구사항 본문 안의 대상, 개념, 신호, 함수, 상태, 테스트 관찰값을 연결하기 위한 이름입니다.

- 도움자는 요구사항의 구현 또는 검증에서 다시 찾아야 하는 대상을 표시합니다.
- 같은 개념에는 같은 도움자 이름을 반복해서 사용합니다.
- 추상 표현과 구체 표현의 연결은 본문에 길게 설명하지 않고 `=.md`에 기록합니다.
- 코드, 모델, 테스트에서 실제 이름이 있는 대상은 가능한 실제 이름을 도움자로 사용합니다.

예:

```markdown
- [requested_gear](=)가 `P`이면 [parking_lock_command](=)는 활성화되어야 합니다.
```

### 속성자 작성 규칙

속성자는 에이전트가 요구사항을 분류하고 필터링하는 기준입니다. YAML 코드블록으로 작성하며, 필드 이름은 프로젝트 안에서 일관되게 유지합니다.

권장 기본 속성은 다음과 같습니다:

```yaml
Type: Functional
Status: Draft
Priority: Must
Source: Stakeholder
Verification: Test
Variant: Common
Owner: TeamName
```

필드 의미:

- `Type`: 요구사항 종류입니다. 예: `Container`, `Functional`, `Informational`, `Constraint`, `TestCase`.
- `Status`: 작성 상태입니다. 예: `Draft`, `Review`, `Approved`, `Deprecated`.
- `Priority`: 구현 또는 검증 우선순위입니다. 예: `Must`, `Should`, `May`.
- `Source`: 요구사항 출처입니다. 예: 상위 문서, 고객 요구, 표준, 이슈 번호.
- `Verification`: 검증 방법입니다. 예: `Review`, `Analysis`, `Test`, `Inspection`.
- `Variant`: 적용 대상 variant입니다.
- `Owner`: 담당 조직 또는 담당자입니다.

프로젝트별 속성자를 추가할 수 있지만, 동일한 의미의 필드를 여러 이름으로 만들지 않습니다. 예를 들어 `Owner`, `Assignee`, `Responsible`을 혼용하지 않습니다.

### 색인 작성 규칙

색인은 본문 밖에서 관계와 연결을 관리하기 위한 파일입니다. 에이전트가 색인을 자동 갱신할 수 있도록 색인 구조는 단순하고 반복 가능해야 합니다.

`@.md`의 각 섹션은 하나의 식별자를 기준으로 작성합니다:

````markdown
## [GLD_INIT](@)

- [원문](SwReq.md#GLD_INIT)
- [SYS_GLD_STARTUP](../sys/@)
- [SWQT_GLD_INIT_001](../swqt/@)

```yaml
Type: Functional
Status: Review
Verification: Test
```
````

`=.md`의 각 섹션은 하나의 도움자를 기준으로 작성합니다:

````markdown
## [position_lever_delayed](=)

- [원문](SwReq.md#GLD_INIT)
- [macro_lever_position_0](=)
- [LeverPositionDelayed](../design/=)

```yaml
Kind: Signal
Unit: enum
```
````

색인 섹션에 포함된 링크는 모두 현재 섹션의 식별자 또는 도움자와 관계가 있는 항목으로 해석합니다. 관계 종류는 기본 문법으로 강제하지 않으며, 경로와 주변 맥락으로 해석합니다.

예:

```markdown
## [GLD_INIT](@)

- [SYS_GLD_STARTUP](../sys/@)
- [SWQT_GLD_INIT_001](../swqt/@)
```

## 검증 규칙

ReqMd 문서를 수정한 뒤에는 문법 검증, 추적성 검증, 품질 검증을 분리해서 확인합니다. 문법 검증과 추적성 검증은 가능한 스크립트로 자동화하고, 품질 검증은 사람이 리뷰하거나 에이전트가 보조 검토합니다.

### 문법 검증

- 모든 요구사항 섹션 제목이 `[IDENTIFIER](@)` 또는 `[IDENTIFIER](path/@)`로 시작하는지 확인합니다.
- 모든 식별자 이름이 `[A-Z][A-Z0-9_]*` 정규식을 따르는지 확인합니다.
- 모든 도움자 링크가 `[helper](=)` 또는 `[helper](path/=)` 형식인지 확인합니다.
- 모든 도움자 이름이 `[A-Za-z_][A-Za-z0-9_]*` 정규식을 따르는지 확인합니다.
- YAML 코드블록이 올바른 YAML인지 확인합니다.
- 같은 경로 안에서 식별자 섹션이 중복되지 않는지 확인합니다.
- 같은 색인 파일 안에서 같은 식별자 또는 도움자 섹션이 중복되지 않는지 확인합니다.

### 추적성 검증

- 본문에 등장한 식별자가 `@.md`에 필요한 관계로 반영되었는지 확인합니다.
- 본문에 등장한 도움자가 `=.md`에 필요한 연결로 반영되었는지 확인합니다.
- `@.md` 또는 `=.md`의 원문 링크가 실제 문서 위치를 가리키는지 확인합니다.
- 상위 요구사항과 하위 요구사항의 관계가 기록된 한 방향 정보로부터 역방향까지 계산 가능한지 확인합니다.
- 요구사항과 테스트 케이스 사이의 관계가 끊기지 않았는지 확인합니다.
- 양방향 관계를 문서에 모두 기록하는 프로젝트에서는 양쪽 색인 내용이 서로 일치하는지 확인합니다.

### 품질 검증

- 하나의 요구사항이 하나의 검증 가능한 동작 또는 제약을 표현하는지 확인합니다.
- 모호한 표현을 줄입니다. 예: "적절히", "가능하면", "빠르게", "충분히".
- 수치 조건, 상태 조건, 예외 조건이 필요한 경우 본문에 명시합니다.
- 구현 상세가 요구사항을 불필요하게 제한하지 않는지 확인합니다.
- 속성자 필드 이름과 값이 프로젝트 규칙과 일치하는지 확인합니다.

## Agentic Coding Skill 초안 구조

이 문서를 기반으로 skill을 만들 때는 `SKILL.md`를 짧게 유지하고, 상세 문법과 예시는 reference 문서로 분리하는 것이 좋습니다.

권장 구조:

```plaintext
reqmd/
  SKILL.md
  references/
    syntax.md
    authoring-rules.md
    validation-checklist.md
    examples.md
  scripts/
    validate_reqmd.py
```

각 파일의 역할:

- `SKILL.md`: 언제 이 skill을 사용할지, 어떤 순서로 작업할지, 어떤 reference를 읽을지 안내합니다.
- `references/syntax.md`: 식별자, 도움자, 속성자, 색인 문법을 정의합니다.
- `references/authoring-rules.md`: 요구사항 작성 원칙과 프로젝트별 스타일 규칙을 둡니다.
- `references/validation-checklist.md`: 문법, 추적성, 품질 검증 체크리스트를 둡니다.
- `references/examples.md`: 좋은 예와 나쁜 예, 수정 예시를 둡니다.
- `scripts/validate_reqmd.py`: 반복 가능한 검증을 자동화합니다.

### Skill 작업 절차 초안

ReqMd skill은 다음 순서로 동작하도록 설계합니다:

1. 사용자의 요청이 작성, 수정, 검증, 추적성 분석 중 어디에 해당하는지 판단합니다.
2. 대상 경로의 `@.md`, `=.md`, 관련 요구사항 문서를 읽습니다.
3. 식별자, 도움자, 속성자 목록을 추출합니다.
4. 요청된 변경을 본문에 반영합니다.
5. 필요한 경우 `@.md`와 `=.md`를 함께 갱신합니다.
6. 문법 검증, 추적성 검증, 품질 검증을 수행합니다.
7. 변경된 요구사항, 갱신된 색인, 남은 검토 항목을 사용자에게 보고합니다.

### Skill trigger 예시

나중에 skill의 `description`에는 다음과 같은 사용 시점을 포함합니다:

- ReqMd 형식의 요구사항 문서를 작성하거나 수정할 때
- Markdown 요구사항에서 식별자, 도움자, 속성자를 추출할 때
- `@.md`와 `=.md` 색인을 생성하거나 갱신할 때
- 요구사항 간 추적성, 테스트 연결, 영향 범위를 분석할 때
- 요구사항 문서의 문법 오류, 중복 식별자, 끊어진 링크를 검증할 때
