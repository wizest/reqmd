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
- `@.md`: 요구사항 식별자 간 관계와 속성을 기록하는 색인입니다.
- `=.md`: 도움자 간 연결과 속성을 기록하는 색인입니다.

## 2. 요구사항 작성하기

요구사항 하나는 하나의 Markdown 섹션으로 작성합니다. 섹션 제목은 반드시 식별자 링크로 시작합니다.

````markdown
# Software Requirements

## [GLD_INIT](@) 초기화

```yaml
Type: Functional
Status: Draft
Verification: Test
Variant: Common
```

- GLD는 첫 번째 시간 단계에서 [position_lever_delayed](=)를 [macro_lever_position_0](=)으로 초기화해야 합니다.
- GLD는 컴포넌트 실행 중 각 시간 단계의 시작 시 [count_time](=)을 비활성화해야 합니다.
````

기본 규칙:

- `[GLD_INIT](@)`는 요구사항 식별자입니다.
- `[position_lever_delayed](=)` 같은 링크는 도움자입니다.
- `yaml` 코드블록은 요구사항 속성자입니다.
- 검증 가능한 동작이 여러 개면 요구사항을 나누는 것을 우선합니다.
- 식별자 이름은 `[A-Z][A-Z0-9_]*` 형식을 사용합니다.
- 도움자 이름은 `[A-Za-z_][A-Za-z0-9_]*` 형식을 사용합니다.

## 3. 식별자 색인 작성하기

`@.md`에는 요구사항 식별자별 관계와 본문 위치를 적습니다.

````markdown
# Identifier Index

## [GLD_INIT](@)

- [원문](SwReq.md#GLD_INIT)
- [SYS_GLD_STARTUP](../sys/@)
- [SWQT_GLD_INIT_001](../swqt/@)

```yaml
Type: Functional
Status: Draft
Verification: Test
```
````

처음에는 `원문` 링크만 있어도 됩니다. 상위 요구사항, 하위 요구사항, 테스트 케이스가 생기면 관련 식별자 링크를 목록에 추가합니다. 관계의 의미는 경로와 주변 맥락으로 이해합니다.

관계는 한 방향만 기록해도 됩니다. 반대 방향 관계는 도구가 색인 전체를 분석하여 계산할 수 있어야 합니다.

## 4. 도움자 색인 작성하기

`=.md`에는 요구사항 본문에 나온 도움자별 연결 정보를 적습니다.

````markdown
# Helper Index

## [position_lever_delayed](=)

- [원문](SwReq.md#GLD_INIT)
- [LeverPositionDelayed](../design/=)

```yaml
Kind: Signal
Unit: enum
```

## [macro_lever_position_0](=)

- [원문](SwReq.md#GLD_INIT)

```yaml
Kind: Constant
Unit: enum
```

## [count_time](=)

- [원문](SwReq.md#GLD_INIT)

```yaml
Kind: Timer
Unit: tick
```
````

처음에는 도움자 이름과 원문 링크만 작성해도 됩니다. 설계 모델, 코드, 테스트 관찰값과 연결할 대상이 생기면 관련 도움자 링크를 목록에 추가합니다. 연결의 의미는 경로와 주변 맥락으로 이해합니다.

## 5. 작성 후 확인하기

요구사항을 작성하거나 수정한 뒤에는 다음을 확인합니다.

- 모든 요구사항 제목이 `[IDENTIFIER](@)`로 시작하는가?
- 식별자 이름이 `[A-Z][A-Z0-9_]*` 형식인가?
- 도움자 이름이 `[A-Za-z_][A-Za-z0-9_]*` 형식인가?
- 같은 요구사항 경로 안에서 식별자가 중복되지 않는가?
- 본문에 나온 주요 도움자가 `=.md`에 있는가?
- `@.md`의 원문 링크가 실제 요구사항 섹션을 가리키는가?
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
## [REQ_ID](@)

- [원문](Document.md#REQ_ID)
```

`=.md`:

```markdown
## [target](=)

- [원문](Document.md#REQ_ID)
```

## 7. 다음 단계

ReqMd 문서가 늘어나면 다음 기준을 적용합니다.

- 요구사항 종류와 상태 값은 프로젝트 안에서 고정합니다.
- 상위 요구사항, 소프트웨어 요구사항, 테스트 요구사항은 경로를 나누어 관리합니다.
- 관계 종류가 중요하면 경로와 파일 배치를 먼저 명확히 합니다.
- 반복 검증이 필요하면 `@.md`, `=.md`, YAML, 중복 식별자를 검사하는 스크립트를 둡니다.
