# ReqMd Quick Start

이 문서는 ReqMd를 처음 사용할 때 필요한 최소 작성 절차를 설명합니다. 상세 기준은 `markdown_for_requirements.md`를 따릅니다.

## 1. 요구사항 경로 만들기

요구사항 경로는 요구사항 문서와 두 색인 파일을 함께 두는 디렉토리입니다.

```plaintext
sw/
  SwReq.md
  @.md
  =.md
```

- `SwReq.md`: 요구사항 섹션(RequirementSection)과 일반 섹션(GeneralSection)을 담는 문서입니다.
- `@.md`: 식별자 관계를 기록하는 색인입니다.
- `=.md`: 도움자 연결을 기록하는 색인입니다.

색인 파일은 링크 목록만 포함합니다. YAML 속성자는 요구사항 섹션 안의 요구사항 속성(RequirementAttributes)에만 작성합니다.

## 2. 요구사항 섹션 작성하기

요구사항 하나는 하나의 요구사항 섹션으로 작성합니다. 요구사항 제목(RequirementHeader)은 식별자 링크로 시작합니다.

````markdown
# Software Requirements

## [SW_BRAKE_LAMP_REQUEST](@) 브레이크 램프 요청

```yaml
Type: Functional
Status: Draft
Priority: Must
Verification: Test
```

- 제동 제어기는 [brake_pedal_status](=)가 눌림 상태이면 [brake_lamp_request](=)를 활성화해야 합니다.
- 제동 제어기는 [brake_pedal_status](=)가 해제 상태이면 [brake_lamp_request](=)를 비활성화해야 합니다.

## 배경 설명

이 일반 섹션은 요구사항 식별자로 시작하지 않으므로 색인 대상이 아닙니다.
````

기본 규칙:

- 식별자는 `SCREAMING_SNAKE_CASE`를 사용합니다.
- 일반 도움자는 `snake_case`를 사용합니다.
- 구현 도움자는 `[=ActualName](=)`처럼 표시 텍스트를 `=`로 시작하고 실제 코드, 모델, 포트 이름을 보존합니다.
- 일반 섹션은 색인 생성, 색인 검증, 추적성 계산의 대상이 아닙니다.
- 검증 가능한 동작이 여러 개면 요구사항 섹션을 나눕니다.

## 3. 식별자 색인 작성하기

`@.md`에는 요구사항 식별자별 관계를 적습니다.

````markdown
# Identifier Index

## [SW_BRAKE_LAMP_REQUEST](SwReq.md#sw_brake_lamp_request-브레이크-램프-요청)

- [SYS_BLC_PEDAL_ON](../sys/@#sys_blc_pedal_on)
- [SWQT_BLC_PEDAL_ON_001](../swqt/@#swqt_blc_pedal_on_001)
````

색인 섹션 제목의 링크는 원문 요구사항 섹션으로 이동해야 합니다. 이때 fragment는 원문 heading 전체를 기준으로 작성합니다.

색인 섹션 본문의 목록 링크는 관계있는 식별자의 색인 섹션으로 이동해야 합니다. 목록 링크도 `@#sw_brake_lamp_request`, `../sys/@#sys_blc_pedal_on`처럼 대상 색인 heading 기준의 fragment를 포함합니다.

관계는 한 방향만 기록해도 됩니다. 반대 방향 관계는 도구가 색인 전체를 분석하여 계산할 수 있어야 합니다.

## 4. 도움자 색인 작성하기

`=.md`에는 요구사항 본문에 나온 도움자별 연결 정보를 적습니다.

````markdown
# Helper Index

## [brake_lamp_request](SwReq.md#sw_brake_lamp_request-브레이크-램프-요청)

- [=BrakeLampReq](../swdd/=#brakelampreq)
- [observed_brake_lamp_request](../swqt/=#observed_brake_lamp_request)
````

도움자 색인 섹션 제목의 링크는 원문 도움자 위치로 이동해야 합니다. 색인 섹션 본문의 목록 링크는 연결되는 도움자의 색인 섹션으로 이동해야 하며, `=#brake_lamp_request`, `../swdd/=#brakelampreq`처럼 fragment를 포함합니다.

## 5. 작성 후 확인하기

요구사항을 작성하거나 수정한 뒤에는 다음을 확인합니다.

- 요구사항 제목이 `[IDENTIFIER](@)` 또는 `[IDENTIFIER](path/@)`로 시작하는가?
- 일반 섹션이 색인 대상에서 제외되었는가?
- 식별자 이름이 `SCREAMING_SNAKE_CASE` 형식인가?
- 일반 도움자 이름이 `snake_case` 형식인가?
- 구현 도움자가 실제 구현 이름을 보존하는가?
- 같은 요구사항 경로 안에서 식별자가 중복되지 않는가?
- 요구사항 본문에 나온 주요 도움자가 `=.md`에 있는가?
- `@.md`, `=.md`의 제목 링크가 원문 섹션 fragment를 정확히 가리키는가?
- `@.md`, `=.md`의 목록 링크가 대상 색인 섹션 fragment를 정확히 가리키는가?
- 색인 파일에 YAML 코드블록이 없는가?
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
## [REQ_ID](Document.md#req_id-짧은-제목)

- [RELATED_REQ_ID](../related/@#related_req_id)
```

`=.md`:

```markdown
## [target](Document.md#req_id-짧은-제목)

- [mapped_target](../swdd/=#mapped_target)
```

## 7. 다음 단계

문서가 늘어나면 다음 기준을 적용합니다.

- 시스템 요구사항, 소프트웨어 요구사항, 설계, 테스트는 경로를 나누어 관리합니다.
- 관계 종류는 링크 속성보다 경로와 문서 배치로 드러나게 합니다.
- 반복 검증이 필요하면 `@.md`, `=.md`, YAML, 중복 식별자, fragment를 검사하는 스크립트를 둡니다.
