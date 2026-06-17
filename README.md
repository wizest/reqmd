# Markdown for requirements (ReqMd)

이 저장소는 요구사항을 Markdown으로 작성하기 위한 문서 형식인 `ReqMd`를 정의하고 설명합니다.

ReqMd는 별도의 Markdown 확장 문법을 만들지 않고, 일반 Markdown 위에 요구사항 문서화 규칙을 얹는 방식입니다. Markdown의 heading, link, YAML code block만 사용해 요구사항 섹션, 속성, 색인, 추적 관계를 표현합니다. 요구사항 섹션은 식별자 링크로 시작하고, 식별자 색인(`@.md`)과 도움자 색인(`=.md`)을 통해 시스템 요구사항, 소프트웨어 요구사항, 설계, 테스트 항목 사이의 추적성을 관리합니다.

또한 이 저장소는 ReqMd를 실제 agent coding 환경에서 다룰 수 있도록 Codex/Claude용 agent skill 구현을 함께 제공합니다. 즉, 저장소의 주 목적은 ReqMd 형식 자체를 정의하고 설명하는 것이며, agent skill은 그 형식을 작성, 수정, 검증, 분석하기 위한 실행 가능한 구현입니다.

## 주요 구성

```plaintext
.
├── .codex/skills/reqmd/      # Codex용 ReqMd skill
├── claude/reqmd/             # Claude용 ReqMd skill
└── reqmd/                    # ReqMd 설명 문서와 예제 요구사항 세트
```

- `reqmd/markdown_for_requirements.md`: ReqMd의 핵심 Markdown 작성 규칙을 설명합니다.
- `reqmd/quick_start.md`: ReqMd 문서를 빠르게 작성하기 위한 시작 절차를 설명합니다.
- `reqmd/reqmd.md`: ReqMd 자체를 ReqMd 요구사항 형식으로 정리한 문서입니다.
- `reqmd/reqmd-lsp.md`: ReqMd LSP 관련 문서입니다.
- `reqmd/example/`: `Brake Lamp Controller` 예제 요구사항 세트입니다.
- `.codex/skills/reqmd/SKILL.md`: Codex가 ReqMd 문서를 다룰 때 따르는 스킬 진입점입니다.
- `.codex/skills/reqmd/references/`: 문법, 워크플로, 판단 규칙, 검증 기준, 예제 문서가 들어 있습니다.
- `.codex/skills/reqmd/scripts/validate_reqmd.py`: ReqMd 문서와 색인을 검증합니다.
- `.codex/skills/reqmd/scripts/update_index.py`: 요구사항 문서에서 누락된 색인 섹션을 보강합니다.
- `claude/reqmd/`: Claude 환경에서 사용할 수 있는 동일 성격의 스킬 패키지입니다.

## ReqMd 핵심 규칙

- 요구사항 섹션은 `## [REQ_ID](@)`처럼 식별자 링크로 시작합니다.
- 요구사항 식별자는 `SCREAMING_SNAKE_CASE`를 사용합니다.
- 일반 도움자는 `snake_case`를 사용합니다.
- 구현 도움자는 `[=ActualName](=)`처럼 `=`로 시작하며 실제 코드, 모델, 포트 이름을 보존합니다.
- 요구사항 본문은 EARS(Easy Approach to Requirements Syntax) 스타일로 조건과 기대 동작을 명확히 씁니다.
- YAML 속성 블록은 요구사항 섹션 안에만 작성합니다.
- `@.md`는 식별자 색인, `=.md`는 도움자 색인입니다.
- 색인 파일에는 heading과 link list만 두며 YAML 속성을 넣지 않습니다.

## Agent Skill

ReqMd는 사람이 직접 작성할 수 있는 Markdown 문서 형식이지만, 색인과 추적 관계를 일관되게 유지하려면 반복 작업이 생깁니다. 이 저장소의 agent skill은 그 반복 작업을 자동화하고, agent가 ReqMd 규칙을 지키며 문서를 편집하도록 돕습니다.

제공하는 skill은 다음 작업을 다룹니다.

- 요구사항 섹션 작성과 수정
- `@.md`, `=.md` 색인 갱신
- identifier, helper, YAML 속성, fragment 링크 검증
- 요구사항, 설계, 테스트, 구현 helper 간 영향 분석
- 불확실한 추적 링크 검토 항목 보고

## 예제 문서

예제 문서는 `reqmd/example` 아래에 있습니다.

```plaintext
reqmd/example/
├── sys/    # System requirements
├── sw/     # Software requirements
├── swdd/   # Software detailed design
└── swqt/   # Software qualification test requirements
```

각 경로는 요구사항 문서와 함께 `@.md`, `=.md` 색인을 포함합니다. 예제의 자세한 설명은 `reqmd/example/README.md`를 참고하세요.

## 검증

프로젝트 루트에서 다음 명령으로 ReqMd 예제를 검증할 수 있습니다.

```powershell
python .codex\skills\reqmd\scripts\validate_reqmd.py reqmd\example
```

특정 요구사항 루트만 검증하려면 마지막 인자만 바꿉니다.

```powershell
python .codex\skills\reqmd\scripts\validate_reqmd.py reqmd\example\sw
```

## 색인 보강

요구사항 문서에서 누락된 `@.md`, `=.md` 색인 섹션을 추가하려면 다음 명령을 사용합니다.

```powershell
python .codex\skills\reqmd\scripts\update_index.py reqmd\example
```

스크립트는 기존 의미 링크를 완전히 판단하지 않습니다. 실행 후 변경된 색인을 검토하는 흐름을 권장합니다.

## 문서 작성 흐름

1. 요구사항 문서를 둘 위치를 정합니다.
2. 안정적인 `SCREAMING_SNAKE_CASE` 식별자를 만듭니다.
3. `[IDENTIFIER](@)`로 시작하는 요구사항 섹션을 추가합니다.
4. 검증 가능한 동작이나 제약을 EARS 스타일로 작성합니다.
5. 본문에 등장하는 주요 개념, 신호, 상태, 설계 항목, 테스트 값을 도움자 링크로 연결합니다.
6. 필요한 YAML 속성을 요구사항 섹션 안에 추가합니다.
7. `@.md`, `=.md` 색인을 갱신합니다.
8. 검증 스크립트로 문법과 색인 링크를 확인합니다.

## 참고 문서

- `reqmd/markdown_for_requirements.md`: 요구사항 작성을 위한 Markdown 규칙
- `reqmd/quick_start.md`: ReqMd 빠른 시작 문서
- `reqmd/reqmd.md`: ReqMd 자체 요구사항 문서
- `reqmd/reqmd-lsp.md`: ReqMd LSP 관련 문서
- `.codex/skills/reqmd/references/syntax.md`: 스킬이 사용하는 문법 기준
- `.codex/skills/reqmd/references/workflows.md`: 스킬이 사용하는 작업 절차

## 라이선스

이 저장소는 MIT License로 배포됩니다. 자세한 내용은 `LICENSE`를 참고하세요.

---

This repository defines and explains `ReqMd`, a document format for writing requirements in Markdown.

ReqMd does not introduce a separate Markdown extension. Instead, it adds requirements-documentation conventions on top of ordinary Markdown. It uses only Markdown headings, links, and YAML code blocks to represent requirement sections, attributes, indexes, and traceability relationships. Requirement sections start with identifier links, and identifier indexes (`@.md`) plus helper indexes (`=.md`) manage traceability across system requirements, software requirements, design, and test items.

This repository also provides Codex/Claude agent skill implementations so ReqMd can be used in practical agent coding environments. In other words, the main purpose of this repository is to define and explain the ReqMd format itself, while the agent skills are executable implementations for authoring, editing, validating, and analyzing that format.

## Project Structure

```plaintext
.
├── .codex/skills/reqmd/      # ReqMd skill for Codex
├── claude/reqmd/             # ReqMd skill for Claude
└── reqmd/                    # ReqMd documentation and example requirement set
```

- `reqmd/markdown_for_requirements.md`: Explains the core Markdown authoring rules for ReqMd.
- `reqmd/quick_start.md`: Explains the quick-start workflow for writing ReqMd documents.
- `reqmd/reqmd.md`: Describes ReqMd itself in ReqMd requirement format.
- `reqmd/reqmd-lsp.md`: Documents ReqMd LSP-related ideas.
- `reqmd/example/`: Example requirement set for a `Brake Lamp Controller`.
- `.codex/skills/reqmd/SKILL.md`: Entry point for the Codex skill used when working with ReqMd documents.
- `.codex/skills/reqmd/references/`: Syntax, workflow, decision-rule, validation, and example references.
- `.codex/skills/reqmd/scripts/validate_reqmd.py`: Validates ReqMd documents and indexes.
- `.codex/skills/reqmd/scripts/update_index.py`: Adds missing index sections inferred from requirement documents.
- `claude/reqmd/`: Equivalent skill package for Claude environments.

## Core ReqMd Rules

- Requirement sections start with identifier links such as `## [REQ_ID](@)`.
- Requirement identifiers use `SCREAMING_SNAKE_CASE`.
- General helpers use `snake_case`.
- Implementation helpers start with `=`, for example `[=ActualName](=)`, and preserve actual code, model, or port names.
- Requirement bodies use EARS (Easy Approach to Requirements Syntax) style to express conditions and expected behavior clearly.
- YAML attribute blocks are written only inside requirement sections.
- `@.md` is the identifier index, and `=.md` is the helper index.
- Index files contain only headings and link lists. They do not contain YAML attributes.

## Agent Skill

ReqMd is a Markdown format that people can write directly, but keeping indexes and traceability relationships consistent creates repeated work. The agent skills in this repository automate that repeated work and help agents edit documents while following ReqMd rules.

The provided skills cover:

- Authoring and editing requirement sections
- Updating `@.md` and `=.md` indexes
- Validating identifiers, helpers, YAML attributes, and fragment links
- Analyzing impact across requirements, design, tests, and implementation helpers
- Reporting uncertain traceability links as review items

## Example Documents

Example documents are under `reqmd/example`.

```plaintext
reqmd/example/
├── sys/    # System requirements
├── sw/     # Software requirements
├── swdd/   # Software detailed design
└── swqt/   # Software qualification test requirements
```

Each path contains a requirement document plus `@.md` and `=.md` index files. See `reqmd/example/README.md` for more details.

## Validation

From the project root, run the following command to validate the ReqMd example:

```powershell
python .codex\skills\reqmd\scripts\validate_reqmd.py reqmd\example
```

To validate only a specific requirement root, change the last argument.

```powershell
python .codex\skills\reqmd\scripts\validate_reqmd.py reqmd\example\sw
```

## Index Update

To add missing `@.md` and `=.md` index sections inferred from requirement documents, run:

```powershell
python .codex\skills\reqmd\scripts\update_index.py reqmd\example
```

The script does not fully judge existing semantic links. Review changed indexes after running it.

## Authoring Workflow

1. Choose where the requirement document should live.
2. Create a stable `SCREAMING_SNAKE_CASE` identifier.
3. Add a requirement section that starts with `[IDENTIFIER](@)`.
4. Write verifiable behavior or constraints in EARS style.
5. Link important concepts, signals, states, design items, and test values as helpers.
6. Add required YAML attributes inside the requirement section.
7. Update the `@.md` and `=.md` indexes.
8. Run the validation script to check syntax and index links.

## References

- `reqmd/markdown_for_requirements.md`: Markdown rules for writing requirements
- `reqmd/quick_start.md`: ReqMd quick-start guide
- `reqmd/reqmd.md`: ReqMd requirement document for ReqMd itself
- `reqmd/reqmd-lsp.md`: ReqMd LSP-related document
- `.codex/skills/reqmd/references/syntax.md`: Syntax rules used by the skill
- `.codex/skills/reqmd/references/workflows.md`: Workflows used by the skill

## License

This repository is distributed under the MIT License. See `LICENSE` for details.
