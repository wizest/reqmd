# ReqMd Quick Start

이 문서는 ReqMd를 처음 사용할 때 필요한 최소 작성 절차를 설명합니다. 상세 문법은 `MarkdownForRequirement.md`를 기준으로 합니다.

## 1. 요구사항 경로 만들기

요구사항을 모을 디렉토리를 하나 만들고, 그 안에 요구사항 문서와 두 색인 파일을 둡니다.

```plaintext
sw/
  SwReq.md
  @.md
  =.md
```

- `SwReq.md`: 요구사항 본문을 작성하는 문서입니다.
- `@.md`: 요구사항 식별자 간 관계 링크만 기록하는 색인입니다.
- `=.md`: 도움자 간 연결 링크만 기록하는 색인입니다.

## 2. 요구사항 작성하기

요구사항 하나는 하나의 Markdown 섹션으로 작성합니다. 섹션 제목은 반드시 식별자 링크로 시작합니다.

````markdown
# Software Requirements

## [SW_BRAKE_LAMP_REQUEST](@) 브레이크 램프 요청

```yaml
Type: Functional
Status: Draft
Verification: Test
Priority: Must
```

- 제동 제어기는 [brake_pedal_status](=)가 눌림 상태이면 [brake_lamp_request](=)를 활성화해야 합니다.
- 제동 제어기는 [brake_pedal_status](=)가 해제 상태이면 [brake_lamp_request](=)를 비활성화해야 합니다.
````

기본 규칙:

- `[SW_BRAKE_LAMP_REQUEST](@)`는 요구사항 식별자입니다.
- `[brake_pedal_status](=)` 같은 링크는 도움자입니다.
- `yaml` 코드블록은 요구사항 속성자입니다.
- 검증 가능한 동작이 여러 개면 요구사항을 나누는 것을 우선합니다.
- 식별자 이름은 `SCREAMING_SNAKE_CASE` 형식을 사용합니다.
- 도움자 이름은 `snake_case` 형식을 사용합니다.
- SW 구현 변수나 모델 신호를 직접 가리키는 도움자는 표시 텍스트가 `=`로 시작하며 naming convention을 강제하지 않습니다.

## 3. 식별자 색인 작성하기

`@.md`에는 요구사항 식별자별 관계와 본문 위치를 적습니다.

````markdown
# Identifier Index

## [SW_BRAKE_LAMP_REQUEST](@#SW_BRAKE_LAMP_REQUEST)

- [SW_BRAKE_LAMP_REQUEST](SwReq.md#SW_BRAKE_LAMP_REQUEST)
- [SYS_BRAKE_LAMP_CONTROL](../sys/@#SYS_BRAKE_LAMP_CONTROL)
- [SWQT_BRAKE_LAMP_REQUEST_001](../swqt/@#SWQT_BRAKE_LAMP_REQUEST_001)
````

처음에는 현재 식별자 문자열로 원문 문서를 가리키는 링크만 있어도 됩니다. 상위 요구사항, 하위 요구사항, 테스트 케이스가 생기면 관련 식별자 링크를 목록에 추가합니다. 색인 안의 식별자 링크는 `@#SW_BRAKE_LAMP_REQUEST`, `../sys/@#SYS_BRAKE_LAMP_CONTROL`처럼 반드시 섹션 fragment를 포함합니다. 관계의 의미는 경로와 주변 맥락으로 이해합니다.

관계는 한 방향만 기록해도 됩니다. 반대 방향 관계는 도구가 색인 전체를 분석하여 계산할 수 있어야 합니다.

## 4. 도움자 색인 작성하기

`=.md`에는 요구사항 본문에 나온 도움자별 연결 정보를 적습니다.

````markdown
# Helper Index

## [brake_pedal_status](=#brake_pedal_status)

- [brake_pedal_status](SwReq.md#SW_BRAKE_LAMP_REQUEST)
- [brake_pedal_input](../swdd/=#brake_pedal_input)
- [observed_brake_pedal_status](../swqt/=#observed_brake_pedal_status)

## [brake_lamp_request](=#brake_lamp_request)

- [brake_lamp_request](SwReq.md#SW_BRAKE_LAMP_REQUEST)
- [=BrakeLampReq](../swdd/=#=BrakeLampReq)
- [observed_brake_lamp_request](../swqt/=#observed_brake_lamp_request)
````

처음에는 현재 도움자 문자열로 원문 문서를 가리키는 링크만 작성해도 됩니다. 설계 모델, 코드, 테스트 관찰값과 연결할 대상이 생기면 관련 도움자 링크를 목록에 추가합니다. 색인 안의 도움자 링크는 `=#brake_lamp_request`, `../swdd/=#=BrakeLampReq`처럼 반드시 섹션 fragment를 포함합니다. 연결의 의미는 경로와 주변 맥락으로 이해합니다.

표시 텍스트가 `=`로 시작하는 도움자는 구현 변수를 직접 특정할 때 사용합니다.

```markdown
## [=BrakeLampReq](=#=BrakeLampReq)

- [=BrakeLampReq](SwDesign.md#SWDD_BLC_OUTPUT_CONTROL)
- [brake_lamp_request](../sw/=#brake_lamp_request)
```

## 5. 작성 후 확인하기

요구사항을 작성하거나 수정한 뒤에는 다음을 확인합니다.

- 모든 요구사항 제목이 `[IDENTIFIER](@)`로 시작하는가?
- 식별자 이름이 `SCREAMING_SNAKE_CASE` 형식인가?
- 도움자 이름이 `snake_case` 형식인가?
- 표시 텍스트가 `=`로 시작하는 도움자는 실제 구현 변수나 모델 요소를 특정하는가?
- 같은 요구사항 경로 안에서 식별자가 중복되지 않는가?
- 본문에 나온 주요 도움자가 `=.md`에 있는가?
- `@.md`의 원문 링크가 실제 요구사항 섹션을 가리키는가?
- `@.md`, `=.md` 안의 색인 링크가 `@#...`, `=#...`, `path/@#...`, `path/=#...`처럼 fragment를 포함하는가?
- YAML 코드블록이 올바른 YAML 형식인가?
- 요구사항 하나가 하나의 검증 가능한 동작 또는 제약을 표현하는가?

## 6. 최소 템플릿

새 요구사항을 빠르게 추가할 때는 아래 템플릿을 사용합니다.

````markdown
## [REQ_ID](@) 짧은 제목

```yaml
Type: Functional
Status: Draft
Priority: Must
Verification: Test
Variant: Common
```

- 시스템은 [target](=)을 조건에 따라 기대 상태로 만들어야 합니다.
````

`@.md`:

```markdown
## [REQ_ID](@#REQ_ID)

- [REQ_ID](Document.md#REQ_ID)
```

`=.md`:

```markdown
## [target](=#target)

- [target](Document.md#REQ_ID)
```

## 7. 다음 단계

ReqMd 문서가 늘어나면 다음 기준을 적용합니다.

- 요구사항 종류와 상태 값은 프로젝트 안에서 고정합니다.
- 상위 요구사항, 소프트웨어 요구사항, 테스트 요구사항은 경로를 나누어 관리합니다.
- 관계 종류가 중요하면 경로와 파일 배치를 먼저 명확히 합니다.
- 반복 검증이 필요하면 `@.md`, `=.md`, YAML, 중복 식별자를 검사하는 스크립트를 둡니다.

