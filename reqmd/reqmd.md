# ReqMd Requirements

이 문서는 `markdown_for_requirements.md`의 내용을 ReqMd 형식으로 재구성한 요구사항 문서입니다.
ReqMd 자체의 문서 구조, 링크 문법, 색인 규칙, 검증 규칙, skill 구성 기준을 EARS 스타일의 요구사항 문장으로 기술합니다.

## [REQMD_DOCUMENT_MODEL](@) ReqMd 문서 모델

- ReqMd는 일반 Markdown 문서에 [identifier](=), [helper](=), [attribute](=), [index_file](=) 규칙을 적용하여 요구사항을 추적할 수 있어야 합니다.
- ReqMd는 별도의 Markdown 확장 문법을 정의하지 않고 Markdown heading, link, fenced code block을 사용해야 합니다.
- 요구사항 경로가 존재하는 경우, ReqMd는 해당 경로에 요구사항 문서와 `@.md`, `=.md` 색인 파일을 함께 둘 수 있어야 합니다.

### [REQMD_SECTION_TYPES](@) 섹션 종류

- ReqMd 문서를 해석할 때, ReqMd는 [requirement_section](=)과 [general_section](=)을 구분해야 합니다.
- Markdown heading이 [identifier](=)로 시작하는 경우, ReqMd는 해당 섹션을 [requirement_section](=)으로 취급해야 합니다.
- Markdown heading이 [identifier](=)로 시작하지 않는 경우, ReqMd는 해당 섹션을 [general_section](=)으로 취급해야 합니다.
- 섹션이 [general_section](=)인 경우, ReqMd는 해당 섹션을 요구사항으로 취급하지 않아야 하며 [identifier_index](=), [helper_index](=), 추적성 계산 대상에서 제외해야 합니다.

### [REQMD_REQUIREMENT_SECTION_STRUCTURE](@) 요구사항 섹션 구조

- 섹션이 [requirement_section](=)인 경우, ReqMd는 해당 섹션을 [requirement_header](=), 선택적 [requirement_attributes](=), [requirement_body](=), 선택적 [child_requirements](=)로 구성해야 합니다.
- [requirement_header](=)를 작성할 때, ReqMd는 Markdown heading depth, [identifier](=), 선택적 부제목을 포함해야 합니다.
- [requirement_body](=)를 작성할 때, ReqMd는 EARS 규칙을 적용하여 요구사항의 의도, 조건, 기대 결과를 Markdown으로 표현해야 합니다.
- 하위 요구사항을 작성할 때, ReqMd는 상위 요구사항보다 더 깊은 Markdown heading depth를 사용해야 합니다.

## [REQMD_IDENTIFIER_SYNTAX](@) 식별자 문법

- ReqMd는 하나의 [identifier](=)가 하나의 [requirement_section](=)을 고유하게 가리키도록 해야 합니다.
- [identifier](=)를 작성할 때, ReqMd는 `SCREAMING_SNAKE_CASE`를 사용해야 하며 정규식 `[A-Z][A-Z0-9_]*`을 만족해야 합니다.
- 요구사항 제목을 작성할 때, ReqMd는 `[IDENTIFIER](@)` 또는 `[IDENTIFIER](path/@)` 형식으로 시작해야 합니다.
- [identifier](=) 이름을 판단할 때, ReqMd는 Markdown link 표시 텍스트를 기준으로 판단해야 하며 `path/`를 이름의 일부로 취급하지 않아야 합니다.
- [identifier](=)가 삭제된 경우, ReqMd는 해당 [identifier](=)를 재사용하지 않아야 합니다.

### [REQMD_IDENTIFIER_LINK_TARGET](@) 식별자 링크 대상

- [identifier](=)가 `[IDENTIFIER](@)` 형식인 경우, ReqMd는 현재 요구사항 경로의 [identifier_index](=)를 참조해야 합니다.
- [identifier](=)가 `[IDENTIFIER](path/@)` 형식인 경우, ReqMd는 다른 요구사항 경로의 [identifier_index](=)를 참조해야 합니다.
- 요구사항 본문에 [identifier](=) 링크를 작성할 때, ReqMd는 fragment 생략을 허용해야 합니다.
- 색인 파일 안에 [identifier](=) 링크를 작성할 때, ReqMd는 대상 색인 섹션으로 이동할 수 있도록 fragment를 포함해야 합니다.

## [REQMD_HELPER_SYNTAX](@) 도움자 문법

- ReqMd는 [helper](=)를 요구사항, 설계, 테스트, 구현에서 같은 대상이나 개념을 연결하는 이름으로 사용해야 합니다.
- 일반 [helper](=)를 작성할 때, ReqMd는 `snake_case`를 사용해야 하며 정규식 `[a-z][a-z0-9_]*`을 만족해야 합니다.
- [helper](=)가 `[helper](=)` 형식인 경우, ReqMd는 현재 요구사항 경로의 [helper_index](=)를 참조해야 합니다.
- [helper](=)가 `[helper](path/=)` 형식인 경우, ReqMd는 다른 요구사항 경로의 [helper_index](=)를 참조해야 합니다.
- [helper](=) 이름을 판단할 때, ReqMd는 Markdown link 표시 텍스트를 기준으로 판단해야 하며 `path/`를 이름의 일부로 취급하지 않아야 합니다.

### [REQMD_IMPLEMENTATION_HELPER](@) 구현 도움자

- 구현 [helper](=)를 작성할 때, ReqMd는 표시 텍스트를 `=`로 시작해야 합니다.
- 구현 [helper](=)를 작성할 때, ReqMd는 실제 코드 변수, 모델 포트, 데이터 사전 항목, 생성 심볼 이름을 보존해야 합니다.
- 구현 [helper](=)가 `=`로 시작하는 경우, ReqMd는 `=` 뒤의 문자열에 일반 [helper](=) naming convention을 강제하지 않아야 합니다.
- 구현 [helper](=)와 개념 [helper](=)가 같은 대상을 가리키는 경우, ReqMd는 [helper_index](=)에서 두 [helper](=)를 연결할 수 있어야 합니다.

## [REQMD_ATTRIBUTE_SYNTAX](@) 속성자 문법

- ReqMd는 [attribute](=)를 요구사항을 분류하고 필터링하기 위한 YAML code block으로 사용해야 합니다.
- [attribute](=)를 작성할 때, ReqMd는 [requirement_section](=) 안의 [requirement_attributes](=) 위치에 작성해야 합니다.
- [attribute](=)의 필드 이름을 정의할 때, ReqMd는 프로젝트 안에서 일관된 이름을 사용해야 합니다.
- 같은 [requirement_section](=) 안에서 같은 key와 같은 값을 가진 [attribute](=)가 반복되는 경우, ReqMd는 해당 항목을 하나의 속성으로 취급해야 합니다.
- 같은 key에 여러 값이 필요한 경우, ReqMd는 YAML 배열을 사용해야 합니다.
- 대상 파일이 `@.md` 또는 `=.md`인 경우, ReqMd는 YAML code block을 작성하지 않아야 합니다.

### [REQMD_RECOMMENDED_ATTRIBUTES](@) 권장 속성자

- 요구사항 분류 정보가 필요한 경우, ReqMd는 `Type`, `Status`, `Priority`, `Source`, `Verification`, `Variant`, `Owner` 속성을 사용할 수 있어야 합니다.
- 동일한 의미의 속성을 작성할 때, ReqMd는 `Owner`, `Assignee`, `Responsible`처럼 여러 이름을 혼용하지 않아야 합니다.
- 사람이 관리해야 하는 요구사항 상태, 우선순위, 검증 방법이 있는 경우, ReqMd는 해당 정보를 색인이 아니라 [requirement_attributes](=)에 작성해야 합니다.

## [REQMD_IDENTIFIER_INDEX](@) 식별자 색인

- [identifier_index](=)를 작성할 때, ReqMd는 파일 이름을 `@.md`로 지정해야 합니다.
- [identifier_index](=)를 작성할 때, ReqMd는 요구사항 간 관계를 링크 목록으로 기록해야 합니다.
- [identifier_index](=)를 작성할 때, ReqMd는 각 요구사항에서 사용한 [helper](=)를 링크 목록에 함께 기록해야 합니다.
- [identifier_index](=) 섹션 제목을 작성할 때, ReqMd는 원문 [requirement_section](=)으로 이동하는 링크를 사용해야 합니다.
- [identifier_index](=) 섹션 본문 목록을 작성할 때, ReqMd는 관계있는 다른 [identifier](=)의 색인 섹션으로 이동하는 링크를 사용해야 합니다.
- [identifier_index](=) 섹션 본문 목록을 작성할 때, ReqMd는 해당 요구사항에서 사용한 [helper](=)의 색인 섹션으로 이동하는 링크를 사용할 수 있어야 합니다.
- [identifier_index](=)를 해석할 때, ReqMd는 관계 타입을 강제하지 않아야 하며 관계 의미를 경로와 주변 맥락으로 해석할 수 있어야 합니다.

### [REQMD_HELPER_INDEX](@) 도움자 색인

- [helper_index](=)를 작성할 때, ReqMd는 파일 이름을 `=.md`로 지정해야 합니다.
- [helper_index](=)를 작성할 때, ReqMd는 도움자 간 연결을 링크 목록으로 기록해야 합니다.
- [helper_index](=)를 작성할 때, ReqMd는 각 [helper](=)를 사용한 [identifier](=)를 링크 목록에 함께 기록해야 합니다.
- [helper_index](=) 섹션 제목을 작성할 때, ReqMd는 링크 없이 [helper](=) 이름만 사용해야 합니다.
- [helper_index](=) 섹션 제목을 작성할 때, ReqMd는 하나의 원문 도움자 위치로 이동하는 링크를 사용하지 않아야 합니다.
- [helper_index](=) 섹션 본문 목록을 작성할 때, ReqMd는 연결되는 다른 [helper](=)의 색인 섹션으로 이동하는 링크를 사용해야 합니다.
- [helper_index](=) 섹션 본문 목록을 작성할 때, ReqMd는 해당 [helper](=)를 사용한 [identifier](=)의 색인 섹션으로 이동하는 링크를 사용할 수 있어야 합니다.
- [helper_index](=)를 해석할 때, ReqMd는 연결 타입을 강제하지 않아야 하며 연결 의미를 경로와 주변 맥락으로 해석할 수 있어야 합니다.

### [REQMD_INDEX_FRAGMENT_RULES](@) 색인 fragment 규칙

- 색인 파일 안에 링크를 작성할 때, ReqMd는 bare link `@`, `=`, `path/@`, `path/=`를 사용하지 않아야 합니다.
- [identifier_index](=) 섹션 제목의 원문 fragment를 작성할 때, ReqMd는 원문 Markdown heading의 최종 표시 텍스트를 기준으로 작성해야 합니다.
- [helper_index](=) 섹션 제목의 fragment를 계산할 때, ReqMd는 링크 없는 도움자 이름을 기준으로 작성해야 합니다.
- 색인 섹션 본문 목록의 fragment를 작성할 때, ReqMd는 대상 색인 섹션 heading의 표시 텍스트를 기준으로 작성해야 합니다.
- fragment를 작성할 때, ReqMd는 VS Code가 이해하는 Markdown heading anchor 형식과 호환되도록 작성해야 합니다.

## [REQMD_TRACEABILITY_MODEL](@) 추적성 모델

- ReqMd는 요구사항 관계와 도움자 연결을 본문 밖의 색인에 기록해야 합니다.
- 문서에 한 방향 링크만 기록된 경우, ReqMd는 도구가 역방향 관계를 계산할 수 있도록 해야 합니다.
- 프로젝트가 양방향 링크를 모두 기록하는 경우, ReqMd는 양쪽 색인 내용의 불일치를 검증 대상으로 취급해야 합니다.
- 요구사항 변경 영향을 분석할 때, ReqMd는 [identifier_index](=)와 [helper_index](=)를 함께 분석하여 요구사항, 설계, 테스트, 구현 도움자로 나누어 보고할 수 있어야 합니다.

## [REQMD_VALIDATION_RULES](@) 검증 규칙

- ReqMd 검증을 수행할 때, ReqMd는 문법 검증, 추적성 검증, 품질 검증으로 나누어 수행해야 합니다.
- 문법 검증을 수행할 때, ReqMd는 [requirement_header](=), [identifier](=), [helper](=), [attribute](=), 색인 링크 fragment, 색인 파일 YAML 금지를 확인해야 합니다.
- 추적성 검증을 수행할 때, ReqMd는 요구사항 본문에 등장한 주요 [identifier](=)와 [helper](=)가 색인에 반영되었는지 확인해야 합니다.
- 품질 검증을 수행할 때, ReqMd는 요구사항이 하나의 검증 가능한 동작 또는 제약을 표현하는지 확인해야 합니다.
- 품질 검증을 수행할 때, ReqMd는 [requirement_body](=)가 EARS 규칙에 따라 적용 조건과 기대 응답을 구분해 표현하는지 확인해야 합니다.
- 대상 섹션이 [general_section](=)인 경우, ReqMd는 해당 섹션을 [requirement_header](=) 검사, 색인 생성, 추적성 계산에서 제외해야 합니다.

### [REQMD_QUALITY_RULES](@) 품질 규칙

- 요구사항을 작성할 때, ReqMd는 모호한 표현을 줄여야 합니다.
- 검증에 수치 조건, 상태 조건, 예외 조건이 필요한 경우, ReqMd는 해당 조건을 [requirement_body](=)에 명시해야 합니다.
- 소프트웨어 요구사항을 작성할 때, ReqMd는 의도적인 제약이 아닌 구현 상세로 구현을 불필요하게 제한하지 않아야 합니다.

## [REQMD_AGENTIC_SKILL_STRUCTURE](@) Agentic Coding skill 구조

- ReqMd skill을 구성할 때, ReqMd는 `SKILL.md`를 짧게 유지하고 상세 문법과 예시는 reference 문서로 분리해야 합니다.
- ReqMd skill을 구성할 때, ReqMd는 `references/syntax.md`, `references/workflows.md`, `references/decision-rules.md`, `references/validation.md`, `references/examples.md`를 둘 수 있어야 합니다.
- 반복 가능한 검증과 색인 갱신이 필요한 경우, ReqMd skill은 `scripts/validate_reqmd.py`, `scripts/update_index.py`를 둘 수 있어야 합니다.

### [REQMD_AGENTIC_WORKFLOW](@) Agentic Coding 작업 절차

- 사용자 요청을 처리할 때, ReqMd skill은 요청을 작성, 수정, 검증, 추적성 분석 중 하나로 분류해야 합니다.
- ReqMd 작업을 시작할 때, ReqMd skill은 대상 요구사항 문서와 `@.md`, `=.md` 색인을 읽어야 합니다.
- [requirement_section](=)을 분석할 때, ReqMd skill은 [identifier](=), [helper](=), [attribute](=) 목록을 추출해야 합니다.
- 요구사항 본문을 수정한 경우, ReqMd skill은 필요한 경우 색인을 함께 갱신해야 합니다.
- ReqMd 작업을 완료할 때, ReqMd skill은 문법 검증, 추적성 검증, 품질 검증 결과와 남은 검토 항목을 보고해야 합니다.

## 용어 참고

이 일반 섹션은 요구사항이 아니며 색인 대상이 아닙니다.

- `RequirementSection`: 식별자로 시작하는 요구사항 작성 단위입니다.
- `GeneralSection`: 식별자로 시작하지 않는 일반 Markdown 섹션입니다.
- `RequirementHeader`: Markdown heading depth, 식별자, 선택적 부제목으로 구성되는 제목입니다.
- `RequirementBody`: EARS 규칙을 적용하여 요구사항의 의도, 조건, 기대 결과를 작성하는 본문입니다.
- `RequirementAttributes`: 요구사항 섹션 안에 작성하는 YAML 속성 블록입니다.
