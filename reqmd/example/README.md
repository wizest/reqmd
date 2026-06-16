# Brake Lamp Controller ReqMd Example

이 예제는 차량용 `Brake Lamp Controller`를 가정한 ReqMd 문서 세트입니다.

```plaintext
example/
  sys/    # System requirements
  sw/     # Software requirements
  swdd/   # Software detailed design
  swqt/   # Software qualification test requirements
```

각 경로는 요구사항 문서, `@.md` 식별자 색인, `=.md` 도움자 색인을 포함합니다. 식별자는 `SCREAMING_SNAKE_CASE`, 도움자는 `snake_case`를 사용합니다.

요구사항 본문은 EARS(Easy Approach to Requirements Syntax) 규칙을 적용하여 작성합니다. 조건, 사건, 상태, 옵션, 예외가 있는 요구사항은 해당 조건을 문장 앞에 두고 기대 응답을 뒤에 명확히 적습니다.

요구사항 문서에는 두 종류의 섹션이 있습니다.

- 요구사항 섹션(RequirementSection): `[IDENTIFIER](@)`로 시작하며 `@.md`, `=.md` 색인의 대상입니다.
- 일반 섹션(GeneralSection): 식별자로 시작하지 않는 설명 섹션이며 색인 대상이 아닙니다.

색인 파일의 섹션 제목은 원문 섹션으로 이동하는 fragment를 포함하고, 색인 본문 목록은 대상 색인 섹션으로 이동하는 fragment를 포함합니다.

