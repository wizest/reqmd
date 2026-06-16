# 요구사항을 기술하는 Markdown 문법

`ReqMd`는 요구 사항을 작성하기 위한 Markdown 문법과 해당 문법으로 작성된 문서를 의미합니다.

ReqMd 문법은 다음과 같은 주요 요소들로 구성됩니다:

- `식별자`: 요구사항 간의 **관계**를 추적하기 위해 Markdown 링크 문법을 활용합니다.
- `도움자`: 추상적인 표현과 구체적인 표현을 **연결**하기 위해 링크 Markdown 문법을 활용합니다.
- `속성자`: 요구사항의 속성을 정의하기 위해 Markdown 코드블록 문법을 활용합니다.
- `색인`: 요구사항 간의 관계와 도움자 간 연결을 기술하기 위한 특정 이름의 파일을 활용합니다. 두 가지 색인이 있습니다:
   - `식별자 색인`: 요구사항 간의 관계를 기술하는 파일로, 파일명은 `@.md`입니다.
   - `도움자 색인`: 추상적인 표현과 구체적인 표현을 연결하는 정보를 담은 파일로, 파일명은 `=.md`입니다.

> 식별자, 도움자, 속성자, 색인을 위해 Markdown 문법을 추가로 확장하지 않아 
> 기존의 범용 Markdown 도구를 그대로 사용할 수 있습니다.

이 문서에서 사용하는 용어는 다음 의미로 고정합니다:

- `요구사항 문서`: 요구사항 섹션(RequirementSection)과 일반 섹션(GeneralSection)을 담은 일반 Markdown 파일입니다. 예: `SwReq.md`.
- `요구사항 경로`: 하나 이상의 요구사항 문서와 색인 파일을 함께 두는 디렉토리입니다.
- `식별자`: 하나의 요구사항을 가리키는 고유 이름입니다.
- `도움자`: 요구사항 본문(RequirementBody)에서 추적해야 하는 대상, 개념, 신호, 함수, 상태, 테스트 관찰값을 가리키는 이름입니다.
- `색인 파일`: 요구사항 경로마다 둘 수 있는 `@.md`, `=.md` 파일입니다. 색인 파일은 링크 목록만 포함하며 YAML 속성자를 작성하지 않습니다.
- `링크 대상 @`: Markdown 링크에서 `@.md` 파일을 의미하는 축약 대상입니다. 예를 들어 `[REQ_001](@)`는 현재 요구사항 경로의 `@.md`에 있는 `REQ_001` 항목을 가리킵니다.
- `링크 대상 =`: Markdown 링크에서 `=.md` 파일을 의미하는 축약 대상입니다. 예를 들어 `[speed](=)`는 현재 요구사항 경로의 `=.md`에 있는 `speed` 항목을 가리킵니다.
- `요구사항 섹션(RequirementSection)`: 식별자(Identifier)로 시작하는 요구사항 작성 단위입니다.
- `일반 섹션(GeneralSection)`: 식별자로 시작하지 않는 일반 Markdown 섹션입니다. 색인 생성과 추적성 계산의 대상이 아닙니다.
- `요구사항 제목(RequirementHeader)`: Markdown 제목 깊이, 식별자, 선택적 부제목으로 구성되는 요구사항 섹션의 제목입니다.
- `요구사항 본문(RequirementBody)`: 요구사항의 의도, 조건, 기대 결과를 Markdown으로 작성하는 본문입니다.
- `요구사항 속성(RequirementAttributes)`: 요구사항 섹션 안에 작성하는 YAML 속성 블록입니다.
- `자식 요구사항(ChildRequirements)`: 상위 요구사항 섹션보다 더 깊은 제목 깊이로 작성하는 하위 요구사항 섹션입니다.
- `일반 섹션 제목(GeneralHeader)`: 식별자로 시작하지 않는 일반 섹션의 제목입니다.
- `일반 섹션 본문(GeneralBody)`: 색인 대상이 아닌 설명, 주석, 배경 정보를 Markdown으로 작성하는 본문입니다.

ReqMd는 다음 표준 규칙을 기준으로 검증할 수 있어야 합니다:

- 식별자 이름은 `SCREAMING_SNAKE_CASE`를 사용하며 정규식 `[A-Z][A-Z0-9_]*`을 따릅니다.
- 도움자 이름은 기본적으로 `snake_case`를 사용하며 정규식 `[a-z][a-z0-9_]*`을 따릅니다.
- 표시 텍스트가 `=`로 시작하는 도움자는 SW 구현에 사용한 실제 변수, 신호, 포트, 모델 요소를 특정하는 구현 도움자입니다. 구현 도움자는 `snake_case` 규칙을 따르지 않아도 됩니다.
- `[REQ](@)`는 현재 요구사항 경로의 `@.md` 색인 엔트리 참조입니다.
- `[REQ](path/@)`는 `path/@.md` 색인 엔트리 참조입니다.
- `[name](=)`는 현재 요구사항 경로의 `=.md` 색인 엔트리 참조입니다.
- `[name](path/=)`는 `path/=.md` 색인 엔트리 참조입니다.
- `@.md`, `=.md` 색인 파일 안의 링크는 반드시 fragment를 포함합니다. 색인 파일에는 두 종류의 fragment가 있습니다.
  - 색인 섹션 제목의 링크는 원문 요구사항 또는 원문 도움자 섹션을 가리킵니다. 이 fragment는 원문 heading의 표시 텍스트 전체를 반영합니다. 예: `## [SW_BLC_CONTROL](@) 브레이크 램프 제어 소프트웨어` -> `SwReq.md#sw_blc_control-브레이크-램프-제어-소프트웨어`
  - 색인 섹션 본문 목록의 링크는 다른 색인 섹션을 가리킵니다. 이 fragment는 대상 색인 heading의 표시 텍스트를 반영합니다. 예: `## [SYS_BLC_CONTROL](SysReq.md#sys_blc_control-브레이크-램프-제어-시스템)` -> `../sys/@#sys_blc_control`
  - 도움자도 같은 방식입니다. 예: `## [brake_lamp_request](SwDesign.md#brake_lamp_request-브레이크-램프-요청)` -> `=#brake_lamp_request`
  - fragment는 링크 텍스트가 아니라 최종 표시되는 heading 텍스트를 기준으로 VS Code가 이해하는 Markdown heading anchor 형식으로 작성합니다.
- 관계와 연결은 색인 섹션의 링크 목록으로 기록하며, 역방향 관계는 도구가 계산합니다.
- 문법 검증은 구조와 링크의 정합성을 확인하고, 품질 검증은 요구사항 문장의 명확성과 검증 가능성을 확인합니다.

ReqMd 문서를 작성하는 규칙은 다음과 같습니다:

- 요구사항 섹션(RequirementSection)은 하나의 `식별자(Identifier)`를 가진 하나의 **섹션**으로 구성됩니다.
- 요구사항 섹션은 **여러** 개의 `도움자(Helper)`와 `속성자(Attribute)`를 포함할 수 있습니다.
- 요구사항 제목(RequirementHeader)은 반드시 식별자로 시작해야 합니다.
- 일반 섹션(GeneralSection)은 식별자로 시작하지 않으며 `@.md`, `=.md` 색인의 대상이 아닙니다.
- 요구사항의 식별자간 **관계** 정보는 `식별자 색인`에 기술합니다.
- 요구사항의 도움자 간 **연결** 정보는 `도움자 색인`에 기술합니다.
- 요구사항은 **계층** 구조를 가질 수 있으며, 자식 요구사항은 섹션의 서브 섹션으로 구성합니다.

> 요구사항의 관계 및 연결 정보는 본문에서 분리하여 색인에 작성하는 것이 중요합니다. 
> 이러한 색인은 통계, 검색, 요약, 번역 등 다양한 목적으로 활용될 수 있습니다.

아래는 이러한 방법으로 작성된 요구사항 문서의 예시입니다:

````markdown
## [SW_BRAKE_LAMP_REQUEST](@) 브레이크 램프 요청

```yaml 
Type: Functional
Status: Draft
Verification: Test
```

- 제동 제어기는 [brake_pedal_status](=)가 눌림 상태이면 [brake_lamp_request](=)를 활성화해야 합니다.
- 제동 제어기는 [brake_pedal_status](=)가 해제 상태이면 [brake_lamp_request](=)를 비활성화해야 합니다.
````
- 식별자: SW_BRAKE_LAMP_REQUEST
- 도움자: brake_pedal_status,brake_lamp_request
- 속성자: Type,Status,Verification


## 문법

### 식별자 (Identifier)

`식별자(Identifier)`는 요구사항 섹션(RequirementSection) 하나를 고유하게 가리키는 이름입니다. Markdown 문법을 활용하여 특수 링크 대상 `@`을 링크합니다.
링크 대상 `@`은 현재 요구사항 경로의 `@.md` 식별자 색인을 의미합니다.

식별자는 다음과 같은 형식으로 구성됩니다:

- 기본 형식: `[identifier](@)`
- 상세 형식: `[identifier](pathto/@#fragment "description")`

이 형식에서 `[identifier](pathto/@#fragment "description")`는 Markdown 링크 문법을 활용하여 요구사항을 식별합니다.

각 요소의 의미는 다음과 같습니다:

- `identifier`: 해당 요구사항 경로 안에서 요구사항을 가리키는 유일한 문자열입니다.
- `pathto/`: 다른 요구사항 경로의 색인을 가리키는 상대 경로입니다. `pathto/@`는 `pathto/@.md`의 식별자 색인을 의미합니다. `pathto`는 식별자 이름 충돌을 방지하고, 식별자를 요구사항 계층별로 구조화할 때 사용합니다.
- `#fragment`: 색인 파일 안의 특정 섹션 위치를 지정합니다. 요구사항 본문(RequirementBody)에서는 생략할 수 있으나, `@.md` 색인 파일 안에서는 반드시 작성합니다. 색인 본문 목록의 fragment는 대상 색인 섹션 heading의 표시 텍스트를 반영한 VS Code 호환 anchor 문자열이어야 합니다.
- `"description"`: 식별자를 설명하는 문자열입니다.

`pathto/`, `#fragment`, `"description"` 요소는 선택적으로 생략할 수 있으며, 다음과 같은 다양한 형태로 사용될 수 있습니다:

- `[identifier](@)`
- `[identifier](pathto/@)`
- `[identifier](@#fragment)`
- `[identifier](@ "description")`

식별자 이름은 Markdown 표시 텍스트에 있는 `identifier`를 기준으로 합니다. 링크의 `pathto/`는 식별자의 범위를 정할 뿐, 식별자 이름의 일부가 아닙니다. 예를 들어 `[BRAKE_LAMP_REQUEST](sw/@)`와 `[BRAKE_LAMP_REQUEST](sys/@)`는 이름은 같지만 서로 다른 요구사항 경로의 식별자를 가리킵니다.

색인 파일 안에서는 `[identifier](@)` 또는 `[identifier](pathto/@)`처럼 파일만 가리키는 링크를 사용하지 않습니다. 같은 색인 파일의 다른 색인 섹션은 `[identifier](@#fragment)`로, 다른 경로의 색인 섹션은 `[identifier](pathto/@#fragment)`로 작성합니다. 이때 fragment는 **대상 색인 섹션 heading**의 표시 텍스트를 반영한 VS Code 호환 anchor 문자열이어야 합니다. 예를 들어 대상 색인 섹션이 `## [SYS_BLC_CONTROL](SysReq.md#sys_blc_control-브레이크-램프-제어-시스템)`이면 목록 링크는 `[SYS_BLC_CONTROL](../sys/@#sys_blc_control)`처럼 작성합니다.

표준 식별자 이름은 `SCREAMING_SNAKE_CASE`를 사용하며 `[A-Z][A-Z0-9_]*` 정규식을 따릅니다. 소문자, 공백, 하이픈, 마침표는 식별자 이름에 사용하지 않습니다. 외부 도구에서 가져온 식별자가 이 규칙을 따르지 않으면 원문 값은 속성자로 보존하고, ReqMd 식별자는 표준 형식으로 별도 부여합니다.



### 도움자 (Helper)

`도움자(Helper)`는 추상적인 표현과 구체적인 표현 간의 연결을 표현하는 이름입니다. Markdown 문법을 활용하여 특수 링크 대상 `=`을 링크합니다.
링크 대상 `=`은 현재 요구사항 경로의 `=.md` 도움자 색인을 의미합니다. 

도움자는 다음과 같은 형식으로 구성됩니다:

- 기본 형식: `[helper](=)`
- 상세 형식: `[helper](pathto/=#fragment "description")`

이 형식에서 `[helper](pathto/=#fragment "description")`는 Markdown 링크 문법을 활용하여 연결하고자 하는 대상을 표현합니다. 

각 요소의 의미는 다음과 같습니다:

- `helper`: 해당 요구사항 경로 안에서 특정 대상을 가리키는 고유한 문자열입니다. 일반 도움자는 `snake_case`를 사용하고, SW 구현에 사용한 실제 변수나 모델 요소를 직접 가리키는 구현 도움자는 표시 텍스트가 `=`로 시작합니다.
- `pathto/`: 다른 요구사항 경로의 색인을 가리키는 상대 경로입니다. `pathto/=`는 `pathto/=.md`의 도움자 색인을 의미합니다. `pathto`는 도움자 이름 충돌을 방지하고, 도움자를 요구사항 계층별로 구조화할 때 사용합니다.
- `#fragment`: 색인 파일 안의 특정 섹션 위치를 지정합니다. 요구사항 본문(RequirementBody)에서는 생략할 수 있으나, `=.md` 색인 파일 안에서는 반드시 작성합니다. 색인 본문 목록의 fragment는 대상 색인 섹션 heading의 표시 텍스트를 반영한 VS Code 호환 anchor 문자열이어야 합니다.
- `"description"`: 도움자를 설명하는 문자열입니다.

`pathto/`, `#fragment`, `"description"` 요소는 선택적으로 생략할 수 있으며 다양한 형태로 사용될 수 있습니다:

- `[helper](=)`
- `[helper](path/=)`
- `[helper](=#fragment)`
- `[helper](= "description")`

도움자 이름은 Markdown 표시 텍스트에 있는 `helper`를 기준으로 합니다. 링크의 `pathto/`는 도움자의 범위를 정할 뿐, 도움자 이름의 일부가 아닙니다.

색인 파일 안에서는 `[helper](=)` 또는 `[helper](path/=)`처럼 파일만 가리키는 링크를 사용하지 않습니다. 같은 색인 파일의 다른 색인 섹션은 `[helper](=#fragment)`로, 다른 경로의 색인 섹션은 `[helper](path/=#fragment)`로 작성합니다. 이때 fragment는 **대상 색인 섹션 heading**의 표시 텍스트를 반영한 VS Code 호환 anchor 문자열이어야 합니다. 예를 들어 대상 색인 섹션이 `## [brake_lamp_request_signal](SwDesign.md#brake_lamp_request_signal-브레이크-램프-신호)`이면 목록 링크는 `[brake_lamp_request_signal](../swdd/=#brake_lamp_request_signal)`처럼 작성합니다. 구현 도움자도 같은 규칙을 따르며, 실제 구현 이름과 heading anchor를 함께 보존합니다.

표준 도움자 이름은 `snake_case`를 사용하며 `[a-z][a-z0-9_]*` 정규식을 따릅니다. 다만 실제 SW 구현 변수, 코드 심볼, 모델 포트, 데이터 사전 항목처럼 원래 이름을 보존해야 하는 대상은 표시 텍스트가 `=`로 시작하는 구현 도움자로 작성합니다. 구현 도움자는 첫 글자 `=` 뒤의 문자열에 대해 ReqMd naming convention을 강제하지 않습니다.

예:

- `[brake_lamp_request](=)`: 요구사항과 설계 사이에서 공유하는 개념적 도움자입니다.
- `[=BrakeLampReq](=)`: SW 구현에서 사용하는 실제 변수 또는 모델 신호를 특정하는 구현 도움자입니다.

구현 도움자는 개념적 도움자와 `=.md`에서 연결합니다.


### 속성자 (Attribute)

`속성자(Attribute)`는 사용자 변수를 명시하기 위해 Markdown 코드블록을 사용하여 YAML 형식으로 정의됩니다. 이 변수들은 해당 요구사항 섹션의 식별자 내에서 유효합니다. 속성자는 요구사항 속성(RequirementAttributes)으로 요구사항 섹션 안에만 작성합니다. 일반 섹션과 `@.md`, `=.md` 색인 파일에는 YAML 속성자를 작성하지 않습니다.

속성자는 다음과 같은 형식으로 작성됩니다:

``````markdown
```yaml
Attribute1: Value1
Attribute2: Value2
Attribute3: Value3
Attribute4: Value4
```
``````

한 요구사항 섹션(RequirementSection) 안에서 속성자가 여러 번 나오고 같은 키가 반복되면 다음 규칙을 적용합니다:

- 값이 모두 같으면 하나의 속성으로 취급합니다.
- 값이 다르면 문서 본문의 값을 우선합니다.
- 같은 키에 여러 값이 필요한 경우 YAML 배열을 사용합니다.

예:

```yaml
Keyword:
  - startup
  - safety
```


### 식별자 색인 (`@.md` 파일)

`식별자 색인` 은 Markdown 파일로 작성되며, 각 식별자에 대한 관계(relationship) 정보를 표현합니다. 식별자 색인은 요구사항 간의 관계를 명확히 하기 위해 사용됩니다. 속성의 원천 정보는 요구사항 속성(RequirementAttributes)에만 두고, 식별자 색인에는 YAML 속성자를 작성하지 않습니다.

식별자 색인은 다음과 같은 형식으로 작성됩니다:

````markdown
## [IDENTIFIER](SwReq.md#identifier-요구사항-제목)

- [RELATED_IDENTIFIER_1](@#related_identifier_1)
- [RELATED_IDENTIFIER_2](pathto/@#related_identifier_2)
````

식별자 색인 섹션 제목은 원래 요구사항 위치를 가리키는 링크로 작성합니다. 제목 링크는 **원문 요구사항 섹션(RequirementSection)**으로만 이동해야 합니다.

섹션 본문 목록에는 원문 링크를 반복하지 않습니다. 대신 현재 식별자와 관계가 있는 다른 식별자만 적고, 각 항목은 그 식별자의 **색인 섹션**을 가리켜야 합니다. 예를 들어 대상 색인 섹션 제목이 `## [SYS_BLC_CONTROL](SysReq.md#sys_blc_control-브레이크-램프-제어-시스템)`이면 목록 항목은 `[SYS_BLC_CONTROL](../sys/@#sys_blc_control)`처럼 해당 식별자의 색인 섹션을 가리킵니다.

즉, 식별자 색인에서는 `## [SW_BLC_CONTROL](SwReq.md#...)` 같은 **제목 링크**가 원문 섹션으로 이동하고, 목록의 `- [SYS_BLC_CONTROL](../sys/@#sys_blc_control)` 같은 **관계 링크**는 다른 식별자의 색인 섹션으로 이동합니다.

색인 파일 안에서 다른 색인 엔트리를 가리키는 링크는 반드시 fragment를 포함합니다. fragment는 대상 색인 섹션 heading의 표시 텍스트를 반영해야 하며, 관계의 종류는 링크 대상의 경로, 문서 위치, 주변 설명, 프로젝트 맥락으로 해석합니다. 색인 파일은 기본적으로 관계 타입을 강제하지 않습니다.

예:

```markdown
## [SW_BLC_CONTROL](SwReq.md#sw_blc_control-브레이크-램프-제어-소프트웨어)

- [SYS_BLC_CONTROL](../sys/@#sys_blc_control)
- [SWQT_BLC_PEDAL_ON_001](../swqt/@#swqt_blc_pedal_on_001)
```

식별자 간의 관계 맥락은 경로를 활용하여 구분합니다. 예를 들어 `sysrq`, `swrq`, `swit`, `swqt`, `sysqt` 같은 요구사항 경로를 사용하면 현재 식별자가 시스템 요구사항, 소프트웨어 요구사항, 통합 테스트, 소프트웨어 테스트 중 어떤 항목과 연결되는지 추론할 수 있습니다.

양방향 추적이 필요한 경우에도 문서에는 한 방향의 링크만 기록할 수 있습니다. 반대 방향 관계는 도구가 색인 전체를 분석하여 계산합니다. 프로젝트에서 양방향 명시를 요구할 수는 있지만, 이 경우 두 방향의 불일치를 검증 대상으로 봅니다.

식별자 색인은 자동 생성하거나 갱신할 수 있는 파생 정보로 취급합니다. 따라서 사람이 직접 관리해야 하는 상태, 우선순위, 검증 방법 같은 속성은 색인이 아니라 원문 요구사항 속성(RequirementAttributes)에 작성합니다.


### 도움자 색인 (`=.md` 파일)

`도움자 색인` 은 Markdown 파일로 작성되며, 각 도움자에 대한 연결(mapping) 정보를 표현합니다. 도움자 색인은 도움자 간 연결을 명확히 하기 위해 사용됩니다. 도움자에 대한 속성이나 정의가 필요하면 원문 요구사항 섹션(RequirementSection), 설계 문서, 테스트 문서 같은 본문에 작성하고, 도움자 색인에는 YAML 속성자를 작성하지 않습니다.

도움자 색인은 다음과 같은 형식으로 작성됩니다:


````markdown
## [helper](SwDesign.md#helper-도움자-제목)

- [connected_helper_1](=#connected_helper_1)
- [connected_helper_2](pathto/=#connected_helper_2)
````

도움자 색인 섹션 제목은 원래 도움자 위치를 가리키는 링크로 작성합니다. 제목 링크는 **원문 도움자의 단일 섹션**으로만 이동해야 합니다.

섹션 본문 목록에는 원문 링크를 반복하지 않습니다. 대신 현재 도움자와 연결되는 다른 도움자만 적고, 각 항목은 그 도움자의 **색인 섹션**을 가리켜야 합니다. 예를 들어 대상 색인 섹션 제목이 `## [brake_lamp_request_signal](SwDesign.md#brake_lamp_request_signal-브레이크-램프-신호)`이면 목록 항목은 `[brake_lamp_request_signal](../swdd/=#brake_lamp_request_signal)`처럼 해당 도움자의 색인 섹션을 가리킵니다.

즉, 도움자 색인에서는 `## [brake_lamp_request](SwDesign.md#...)` 같은 **제목 링크**가 원문 섹션으로 이동하고, 목록의 `- [brake_lamp_request_signal](../swdd/=#...)` 같은 **연결 링크**는 다른 도움자의 색인 섹션으로 이동합니다.

색인 파일 안에서 다른 색인 엔트리를 가리키는 링크는 반드시 fragment를 포함합니다. fragment는 대상 색인 섹션 heading의 표시 텍스트를 반영해야 하며, 연결의 종류는 링크 대상의 경로, 문서 위치, 주변 설명, 프로젝트 맥락으로 해석합니다. 색인 파일은 기본적으로 연결 타입을 강제하지 않습니다.

예:

```markdown
## [brake_lamp_request](SwDesign.md#brake_lamp_request-브레이크-램프-요청)

- [brake_lamp_request_signal](../swdd/=#brake_lamp_request_signal)
- [observed_brake_lamp_request](../swqt/=#observed_brake_lamp_request)
```

도움자 간의 연결 맥락은 경로를 활용하여 구분합니다. 예를 들어 `swdd`, `code`, `test`, `swqt` 같은 경로를 사용하면 현재 도움자가 소프트웨어 상세 설계 항목, 코드 항목, 테스트 관찰값 중 어떤 항목과 연결되는지 추론할 수 있습니다.

도움자 연결도 문서에는 한 방향의 링크만 기록할 수 있으며, 역방향 연결은 도구가 색인 전체를 분석하여 계산합니다. 양방향을 모두 기록하는 프로젝트에서는 양쪽 링크가 서로 일치하는지 검증해야 합니다.

도움자 색인은 자동 생성하거나 갱신할 수 있는 파생 정보로 취급합니다. 따라서 도움자의 종류, 단위, 값 범위 같은 메타정보는 색인이 아니라 해당 도움자가 설명되는 본문에 작성합니다.


## 구조

### 문서 구조

ReqMd 문서의 문서 구조를 McKeeman Form으로 표현하면 다음과 같습니다. 이 구조는 요구사항 섹션(RequirementSection)과 일반 섹션(GeneralSection)을 구분하여 요구사항 문서의 일관성을 유지하고, 다양한 요구사항과 설명 정보를 명확하게 표현하도록 돕기 위해 설계되었습니다.

```plaintext
ReqMd
  DocumentHeader newline Sections

DocumentHeader
  "# " RequirementDocumentName newline MarkdownDescription

RequirementDocumentName
  "<Requirement Document Name>"

MarkdownDescription
  "<Requirement description as markdown>"

Sections
  Section
  Section newline Sections

Section
  RequirementSection
  GeneralSection

RequirementSection
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
  RequirementSection
  RequirementSection newline ChildRequirements

GeneralSection
  GeneralHeader newline GeneralBody

GeneralHeader
  RequirementDepth GeneralTitle

GeneralTitle
  "<Markdown heading text that does not start with an Identifier>"

GeneralBody
  MarkdownDescription
```

위 구조에서 요구사항 섹션(RequirementSection)은 요구사항 제목(RequirementHeader), 요구사항 속성(RequirementAttributes), 요구사항 본문(RequirementBody), 자식 요구사항(ChildRequirements)으로 구성됩니다. 일반 섹션(GeneralSection)은 일반 섹션 제목(GeneralHeader)과 일반 섹션 본문(GeneralBody)으로 구성됩니다.

요구사항 제목(RequirementHeader)은 Markdown 제목 깊이(RequirementDepth), 식별자(Identifier), 선택적 부제목(SubTitle)으로 구성됩니다. 요구사항 본문(RequirementBody)은 요구사항의 의도, 조건, 기대 결과를 담는 Markdown 설명이며, 도움자(Helper)를 포함할 수 있습니다. 요구사항 속성(RequirementAttributes)은 YAML 코드블록으로 작성하는 속성자(Attribute) 목록입니다.

`RequirementDepth`는 Markdown 제목 깊이입니다. 부모 요구사항이 `##`이면 자식 요구사항(ChildRequirements)은 `###`처럼 더 깊은 제목으로 작성합니다. 같은 깊이의 다음 요구사항 섹션 또는 일반 섹션이 나오면 이전 요구사항 섹션은 종료됩니다. 일반 섹션은 식별자로 시작하지 않으며 색인 생성, 색인 검증, 추적성 계산의 대상이 아닙니다.

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
- `@.md`: 식별자 색인 파일로, 해당 경로의 요구사항 식별자에 대한 관계 링크만 포함합니다.
- `=.md`: 도움자 색인 파일로, 해당 경로의 도움자에 대한 연결 링크만 포함합니다.


## Agentic Coding 활용을 위한 작성 원칙

ReqMd 문서는 사람이 읽는 요구사항 문서이면서, 동시에 agentic coding 도구가 요구사항을 검색, 수정, 검증, 추적할 수 있는 구조화된 입력입니다. 따라서 문서는 자연어 설명만 충분한 상태가 아니라, 에이전트가 기계적으로 판단할 수 있는 단서를 함께 포함해야 합니다.

### 에이전트가 수행할 수 있어야 하는 작업

ReqMd 기반 skill은 다음 작업을 안정적으로 수행할 수 있어야 합니다:

- 새 요구사항 문서를 ReqMd 형식으로 작성합니다.
- 기존 요구사항 섹션(RequirementSection)에서 식별자, 도움자, 속성자를 추출합니다.
- 요구사항 본문(RequirementBody)과 `@.md`, `=.md` 색인 사이의 불일치를 찾습니다.
- 상위 요구사항, 하위 요구사항, 테스트, 설계 항목 사이의 추적 관계를 갱신합니다.
- 요구사항 추가, 수정, 삭제에 따라 관련 색인을 함께 갱신합니다.
- 요구사항 변경이 관련 요구사항, 설계 항목, 테스트 요구사항, 구현 도움자에 미치는 영향을 분석합니다.
- 개념 도움자와 구현 도움자(`=ActualVariable`)의 연결을 이용해 코드 또는 모델 심볼을 추적합니다.
- 속성자 값을 기준으로 요구사항을 분류, 필터링, 요약합니다.

### 작성 단위

요구사항 하나는 하나의 요구사항 섹션(RequirementSection)으로 작성합니다. 에이전트가 섹션 경계를 안정적으로 찾을 수 있도록 다음 규칙을 지킵니다:

- 요구사항 제목(RequirementHeader)은 항상 `[IDENTIFIER](@)` 형식으로 시작합니다.
- 같은 경로 안에서 식별자 이름은 중복하지 않습니다.
- 제목의 식별자 뒤에는 사람이 읽기 쉬운 짧은 제목을 붙일 수 있습니다.
- 요구사항 본문(RequirementBody)에는 요구사항의 의도, 조건, 기대 결과를 명확히 적습니다.
- 여러 요구사항을 한 문장에 섞지 않습니다. 독립적으로 검증해야 하는 내용은 별도 식별자로 분리합니다.
- 일반 섹션(GeneralSection)은 식별자로 시작하지 않으며 설명, 주석, 배경 정보처럼 색인 대상이 아닌 내용을 작성할 때 사용합니다.

예:

````markdown
## [SW_BRAKE_LAMP_REQUEST](@) 브레이크 램프 요청

```yaml
Type: Functional
Status: Draft
Verification: Test
```

- 제동 제어기는 [brake_pedal_status](=)가 눌림 상태이면 [brake_lamp_request](=)를 활성화해야 합니다.
- 제동 제어기는 [brake_pedal_status](=)가 해제 상태이면 [brake_lamp_request](=)를 비활성화해야 합니다.
````

### 식별자 작성 규칙

식별자는 요구사항 추적의 기준이므로 사람이 보기 쉽고 변경에 강해야 합니다.

- `SCREAMING_SNAKE_CASE`를 사용합니다.
- 대문자 영문, 숫자, 밑줄(`_`)을 기본 문자로 사용합니다.
- 의미 있는 접두사를 사용합니다. 예: `SYS_`, `SWRQ_`, `SWQT_`, `TC_`.
- 문서 제목이나 자연어 문장이 바뀌어도 식별자는 가능한 유지합니다.
- 삭제된 식별자는 재사용하지 않습니다.
- 이름 충돌 가능성이 있으면 경로를 활용합니다. 예: `[BRAKE_LAMP_REQUEST](sw/@)`, `[BRAKE_LAMP_REQUEST](sys/@)`.

### 도움자 작성 규칙

도움자(Helper)는 요구사항 본문(RequirementBody) 안의 대상, 개념, 신호, 함수, 상태, 테스트 관찰값을 연결하기 위한 이름입니다.

- `snake_case`를 사용합니다.
- SW 구현에 사용한 실제 변수, 포트, 모델 요소를 특정해야 하면 표시 텍스트가 `=`로 시작하는 구현 도움자를 사용합니다.
- 도움자는 요구사항의 구현 또는 검증에서 다시 찾아야 하는 대상을 표시합니다.
- 같은 개념에는 같은 도움자 이름을 반복해서 사용합니다.
- 추상 표현, 요구사항 표현, 구현 변수 사이의 연결은 본문에 길게 설명하지 않고 `=.md`에 기록합니다.

예:

```markdown
- [brake_pedal_status](=)가 눌림 상태이면 [brake_lamp_request](=)는 활성화되어야 합니다.
```

```markdown
## [=BrakeLampReq](SwDesign.md#swdd_blc_output_control-브레이크-램프-출력-제어)

- [brake_lamp_request](../sw/=#brake_lamp_request)
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

`@.md`의 각 섹션은 하나의 요구사항 섹션(RequirementSection) 식별자를 기준으로 작성합니다. 일반 섹션(GeneralSection)은 포함하지 않습니다:

````markdown
## [SW_BLC_CONTROL](SwReq.md#sw_blc_control-브레이크-램프-제어-소프트웨어)

- [SYS_BLC_CONTROL](../sys/@#sys_blc_control)
- [SWQT_BLC_PEDAL_ON_001](../swqt/@#swqt_blc_pedal_on_001)
````

`=.md`의 각 섹션은 하나의 요구사항 섹션(RequirementSection) 또는 다른 원문 섹션에서 설명되는 도움자를 기준으로 작성합니다. 일반 섹션(GeneralSection)에만 등장하는 도움자는 포함하지 않습니다:

````markdown
## [brake_lamp_request](SwDesign.md#brake_lamp_request-브레이크-램프-요청)

- [brake_lamp_request_signal](../swdd/=#brake_lamp_request_signal)
- [observed_brake_lamp_request](../swqt/=#observed_brake_lamp_request)

````

색인 섹션의 제목 링크는 원문 요구사항 또는 원문 도움자 섹션을 가리킵니다.

색인 섹션 본문의 목록 링크는 각 관계 항목의 **색인 섹션**을 가리킵니다. 따라서 본문 목록의 링크도 fragment를 반드시 포함해야 하며, 단순히 식별자나 도움자 이름만 가리키는 링크는 허용하지 않습니다.

색인 내부의 식별자/도움자 링크는 정의 섹션으로 바로 이동할 수 있도록 반드시 fragment를 포함합니다. fragment는 대상 색인 섹션의 heading 표시 텍스트를 반영해야 합니다. 관계 종류는 기본 문법으로 강제하지 않으며, 경로와 주변 맥락으로 해석합니다.

예:

```markdown
## [SW_BLC_CONTROL](SwReq.md#sw_blc_control-브레이크-램프-제어-소프트웨어)

- [SYS_BLC_CONTROL](../sys/@#sys_blc_control)
- [SWQT_BLC_PEDAL_ON_001](../swqt/@#swqt_blc_pedal_on_001)
```

## 검증 규칙

ReqMd 문서를 수정한 뒤에는 문법 검증, 추적성 검증, 품질 검증을 분리해서 확인합니다. 문법 검증과 추적성 검증은 가능한 스크립트로 자동화하고, 품질 검증은 사람이 리뷰하거나 에이전트가 보조 검토합니다.

### 문법 검증

- 모든 요구사항 제목(RequirementHeader)이 `[IDENTIFIER](@)` 또는 `[IDENTIFIER](path/@)`로 시작하는지 확인합니다. 일반 섹션(GeneralSection)은 이 검사 대상에서 제외합니다.
- 모든 식별자 이름이 `SCREAMING_SNAKE_CASE`와 `[A-Z][A-Z0-9_]*` 정규식을 따르는지 확인합니다.
- 모든 도움자 링크가 `[helper](=)` 또는 `[helper](path/=)` 형식인지 확인합니다.
- 일반 도움자 이름이 `snake_case`와 `[a-z][a-z0-9_]*` 정규식을 따르는지 확인합니다.
- 표시 텍스트가 `=`로 시작하는 구현 도움자는 첫 글자 `=` 뒤의 실제 구현 이름을 보존하며 일반 도움자 naming convention 검사에서 제외합니다.
- YAML 코드블록이 올바른 YAML인지 확인합니다.
- 같은 경로 안에서 요구사항 섹션(RequirementSection)의 식별자가 중복되지 않는지 확인합니다.
- 같은 색인 파일 안에서 같은 식별자 또는 도움자 색인 섹션이 중복되지 않는지 확인합니다.
- `@.md`, `=.md` 색인 파일에 YAML 코드블록이 없는지 확인합니다.
- `@.md`, `=.md` 색인 파일 안의 식별자/도움자 링크가 단순 `@`, `=`, `path/@`, `path/=`가 아니라 fragment를 포함한 `@#...`, `=#...`, `path/@#...`, `path/=#...` 형식인지 확인합니다.

### 추적성 검증

- 요구사항 본문(RequirementBody)에 등장한 식별자가 `@.md`에 필요한 관계로 반영되었는지 확인합니다.
- 요구사항 본문(RequirementBody)에 등장한 도움자가 `=.md`에 필요한 연결로 반영되었는지 확인합니다.
- `@.md` 또는 `=.md`의 제목 링크가 실제 원문 문서 위치와 원문 heading anchor를 정확히 가리키는지 확인합니다.
- 색인 섹션 본문 목록의 링크가 실제 대상 색인 섹션과 그 색인 heading anchor를 정확히 가리키는지 확인합니다.
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

Skill의 목적은 ReqMd 문법을 설명하는 것이 아니라, 에이전트가 요구사항 본문(RequirementBody)과 색인을 일관되게 읽고 수정하고 검증하도록 만드는 것입니다. 따라서 `SKILL.md`에는 긴 문법 설명보다 작업 절차, 판단 기준, 필요한 reference 선택 규칙을 우선 작성합니다.

권장 구조:

```plaintext
reqmd/
  SKILL.md
  references/
    syntax.md
    workflows.md
    decision-rules.md
    validation.md
    examples.md
  scripts/
    validate_reqmd.py
    update_index.py
```

각 파일의 역할:

- `SKILL.md`: 언제 이 skill을 사용할지, 어떤 순서로 작업할지, 어떤 reference를 읽을지 안내합니다.
- `references/syntax.md`: 식별자, 도움자, 속성자, 색인 문법을 정의합니다.
- `references/workflows.md`: 요구사항 추가, 수정, 삭제, 색인 갱신, 영향 분석 작업 절차를 둡니다.
- `references/decision-rules.md`: 애매한 상황에서 에이전트가 적용할 판단 기준을 둡니다.
- `references/validation.md`: 문법, 추적성, 품질 검증 체크리스트와 자동 검증 대상을 둡니다.
- `references/examples.md`: 좋은 예와 나쁜 예, 요청별 변경 전후 예시를 둡니다.
- `scripts/validate_reqmd.py`: 반복 가능한 검증을 자동화합니다.
- `scripts/update_index.py`: 요구사항 본문(RequirementBody)에서 식별자와 도움자를 추출해 색인을 생성하거나 보강합니다.

### Skill 작업 절차 초안

ReqMd skill은 모든 작업에서 다음 공통 절차를 따르도록 설계합니다:

1. 사용자의 요청이 작성, 수정, 검증, 추적성 분석 중 어디에 해당하는지 판단합니다.
2. 대상 경로의 `@.md`, `=.md`, 관련 요구사항 문서를 읽습니다.
3. 요구사항 섹션(RequirementSection)에서 식별자, 도움자, 속성자 목록을 추출합니다.
4. 요청된 변경을 요구사항 본문(RequirementBody)에 반영합니다.
5. 필요한 경우 `@.md`와 `=.md`를 함께 갱신합니다.
6. 문법 검증, 추적성 검증, 품질 검증을 수행합니다.
7. 변경된 요구사항, 갱신된 색인, 남은 검토 항목을 사용자에게 보고합니다.

작업별 세부 절차는 다음과 같이 분리합니다.

#### 새 요구사항 추가

1. 요구사항이 들어갈 요구사항 경로와 문서를 결정합니다.
2. 새 식별자를 `SCREAMING_SNAKE_CASE`로 부여합니다.
3. 요구사항 본문(RequirementBody)을 하나의 검증 가능한 동작 또는 제약으로 작성합니다.
4. 필요한 도움자를 `snake_case` 또는 구현 도움자 형식으로 작성합니다.
5. YAML 속성자를 요구사항 섹션 안의 요구사항 속성(RequirementAttributes)으로 작성합니다.
6. `@.md`에 새 식별자 색인 섹션을 만들고 섹션 제목에 원래 위치 링크를 둡니다.
7. 상위 요구사항, 설계, 테스트와의 관계가 있으면 fragment 포함 링크로 추가합니다.
8. `=.md`에 새 도움자 색인 섹션을 만들거나 기존 섹션을 보강합니다.

#### 기존 요구사항 수정

1. 수정 대상 식별자의 요구사항 섹션(RequirementSection)을 찾습니다.
2. 식별자 이름은 가능한 유지합니다.
3. 요구사항 본문(RequirementBody)에서 추가되거나 제거된 도움자를 추출합니다.
4. 변경된 도움자와 관계가 `=.md`에 반영되어 있는지 확인합니다.
5. 요구사항 의미가 크게 바뀌면 관련 테스트와 설계 링크의 영향 범위를 보고합니다.
6. 삭제된 관계는 즉시 제거하기보다, 불확실하면 검토 항목으로 남깁니다.

#### 색인 갱신

1. 요구사항 섹션(RequirementSection)에서 식별자 제목과 도움자 링크를 수집합니다.
2. 누락된 `@.md`, `=.md` 섹션을 생성합니다.
3. 섹션 제목에는 원래 위치 링크를 두고, 목록에는 실제 식별자 또는 도움자 문자열의 관계 링크만 작성합니다.
4. 색인 내부 링크는 반드시 `@#...`, `=#...`, `path/@#...`, `path/=#...` 형식으로 작성합니다.
5. 색인에는 YAML 속성자를 추가하지 않습니다.
6. 기존 링크의 의미가 불명확하면 삭제하지 말고 사용자에게 검토 항목으로 보고합니다.

#### 영향 범위 분석

1. 변경된 식별자와 도움자를 시작점으로 삼습니다.
2. `@.md`에서 상위 요구사항, 하위 요구사항, 설계, 테스트 링크를 수집합니다.
3. `=.md`에서 개념 도움자, 구현 도움자, 테스트 관찰값 연결을 수집합니다.
4. 역방향 링크는 색인 전체를 분석해 계산합니다.
5. 영향 대상은 요구사항, 설계, 테스트, 구현 도움자로 나누어 보고합니다.

### Skill 판단 기준

에이전트가 애매한 상황을 만났을 때는 다음 기준을 적용합니다:

- 요구사항 본문(RequirementBody)과 색인이 충돌하면 본문을 원천 정보로 보고 색인을 갱신 대상으로 봅니다.
- 속성자는 요구사항 속성(RequirementAttributes)의 YAML만 원천으로 인정하고, 색인에는 생성하지 않습니다.
- 관계 방향이 명확하지 않으면 현재 수정 중인 요구사항을 출발점으로 한 링크만 작성합니다.
- 반대 방향 관계는 문서에 강제로 추가하지 않고, 도구가 계산할 수 있는 정보로 둡니다.
- 동일한 개념의 도움자가 이미 있으면 새 이름을 만들기보다 기존 도움자를 재사용합니다.
- 실제 코드, 모델, 포트 이름을 보존해야 하면 `=ActualName` 구현 도움자를 사용합니다.
- 구현 도움자를 일반 `snake_case` 이름으로 바꾸지 않습니다.
- 삭제가 확실하지 않은 링크나 섹션은 임의로 제거하지 않고 검토 항목으로 보고합니다.

### 자동 검증 대상

Skill에는 최소한 다음 검증을 자동화하는 것이 좋습니다:

- 요구사항 제목(RequirementHeader)이 `[IDENTIFIER](@)` 또는 `[IDENTIFIER](path/@)`로 시작하는지 확인합니다.
- 식별자가 `SCREAMING_SNAKE_CASE` 규칙을 따르는지 확인합니다.
- 일반 도움자가 `snake_case` 규칙을 따르는지 확인합니다.
- 구현 도움자(`=ActualName`)가 일반 도움자 naming convention 검사에서 제외되는지 확인합니다.
- `@.md`, `=.md` 색인 파일에 YAML 코드블록이 없는지 확인합니다.
- 색인 내부 링크가 fragment 없는 `@`, `=`, `path/@`, `path/=`를 사용하지 않는지 확인합니다.
- 색인 내부 링크의 fragment가 실제 대상 색인 섹션에 존재하는지 확인합니다.
- 요구사항 본문(RequirementBody)에 등장한 식별자와 도움자가 색인에 반영되어 있는지 확인합니다.
- 색인의 제목 링크가 실제 원문 Markdown 섹션과 VS Code 호환 원문 heading anchor를 가리키는지 확인합니다.

### Skill 예제 보강 기준

`references/examples.md`에는 완성된 예제만 두지 말고, 사용자가 실제로 요청할 법한 작업 단위의 변경 전후 예시를 포함합니다:

- 새 소프트웨어 요구사항을 추가하는 예시
- 요구사항 본문(RequirementBody) 수정 후 `@.md`, `=.md`가 함께 바뀌는 예시
- 개념 도움자와 구현 도움자를 연결하는 예시
- 테스트 요구사항을 추가하고 소프트웨어 요구사항과 연결하는 예시
- 색인 링크에 fragment가 빠진 오류를 수정하는 예시
- 색인에 YAML 속성자가 잘못 들어간 오류를 제거하는 예시

각 예시는 사용자 요청, 변경 전 파일 일부, 변경 후 파일 일부, 검증 결과를 함께 보여주는 형태가 좋습니다.

### Skill trigger 예시

나중에 skill의 `description`에는 다음과 같은 사용 시점을 포함합니다:

- ReqMd 형식의 요구사항 문서를 작성하거나 수정할 때
- 요구사항 섹션(RequirementSection)에서 식별자, 도움자, 속성자를 추출할 때
- `@.md`와 `=.md` 색인을 생성하거나 갱신할 때
- 요구사항 간 추적성, 테스트 연결, 영향 범위를 분석할 때
- 요구사항 문서의 문법 오류, 중복 식별자, 끊어진 링크를 검증할 때

