# Markdown for requirements (ReqMd)

이 저장소는 요구사항을 Markdown으로 작성하기 위한 문서 형식인 `ReqMd`를 정의하고 설명합니다.

ReqMd는 일반 Markdown의 heading, link, YAML code block을 사용해 요구사항 섹션, 속성, 색인, 추적 관계를 표현합니다. 별도의 Markdown 확장 문법을 만들지 않고, Markdown 문서 안에서 요구사항을 일관되게 작성하고 추적할 수 있도록 하는 것이 목적입니다.

자세한 문법과 작성 규칙은 [`reqmd/markdown_for_requirements.md`](reqmd/markdown_for_requirements.md)를 참고하세요.

## 구성

```plaintext
.
├── reqmd/                    # ReqMd 설명 문서와 예제 요구사항 세트
├── .codex/skills/reqmd/      # Codex용 ReqMd agent skill
└── claude/reqmd/             # Claude용 ReqMd agent skill
```

- `reqmd/markdown_for_requirements.md`: ReqMd의 핵심 문법과 작성 규칙
- `reqmd/quick_start.md`: 빠른 시작 문서
- `reqmd/example/`: `Brake Lamp Controller` 예제 요구사항 세트
- `.codex/skills/reqmd/`: Codex가 ReqMd 문서를 작성, 수정, 검증, 분석하기 위한 skill 구현
- `claude/reqmd/`: Claude 환경용 skill 구현

## Agent Skill

이 저장소는 ReqMd 형식을 정의하는 것에 더해, agent coding 환경에서 ReqMd 문서를 다룰 수 있도록 Codex/Claude용 skill도 함께 제공합니다.

skill은 요구사항 섹션 작성, `@.md`/`=.md` 색인 갱신, fragment 링크 검증, 영향 분석 같은 반복 작업을 돕습니다. skill의 세부 동작 기준은 `.codex/skills/reqmd/`와 `claude/reqmd/` 아래 문서를 참고하세요.

## 라이선스

이 저장소는 MIT License로 배포됩니다. 자세한 내용은 [`LICENSE`](LICENSE)를 참고하세요.

---

# Markdown for requirements (ReqMd) - English

This repository defines and explains `ReqMd`, a document format for writing requirements in Markdown.

ReqMd uses ordinary Markdown headings, links, and YAML code blocks to represent requirement sections, attributes, indexes, and traceability relationships. It does not introduce a separate Markdown extension. Its purpose is to make requirements authoring and traceability consistent inside Markdown documents.

For the detailed syntax and authoring rules, see [`reqmd/markdown_for_requirements.md`](reqmd/markdown_for_requirements.md).

## Structure

```plaintext
.
├── reqmd/                    # ReqMd documentation and example requirement set
├── .codex/skills/reqmd/      # ReqMd agent skill for Codex
└── claude/reqmd/             # ReqMd agent skill for Claude
```

- `reqmd/markdown_for_requirements.md`: Core ReqMd syntax and authoring rules
- `reqmd/quick_start.md`: Quick-start guide
- `reqmd/example/`: Example requirement set for a `Brake Lamp Controller`
- `.codex/skills/reqmd/`: Skill implementation for authoring, editing, validating, and analyzing ReqMd documents with Codex
- `claude/reqmd/`: Skill implementation for Claude environments

## Agent Skill

In addition to defining the ReqMd format, this repository provides Codex/Claude skills for working with ReqMd documents in agent coding environments.

The skills help with repeated work such as authoring requirement sections, updating `@.md`/`=.md` indexes, validating fragment links, and analyzing impact. See the documents under `.codex/skills/reqmd/` and `claude/reqmd/` for skill-specific details.

## License

This repository is distributed under the MIT License. See [`LICENSE`](LICENSE) for details.
