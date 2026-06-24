# Requirements as Markdown

이 저장소는 Markdown으로 요구사항과 문서 추적성을 관리하기 위한 두 가지 형식을 정의합니다.

## Markdown for Requirements (ReqMd)

ReqMd는 일반 Markdown의 heading, link, YAML code block을 사용합니다. 별도의 Markdown 확장 문법을 만들지 않고, 요구사항 본문과 `@.md`/`=.md` 색인을 일관되게 작성하고 검증하는 것이 목적입니다.

## Programmable Documentation (ProDoc)

ProDoc은 문서의 YAML frontmatter에 `reqmd_prodoc`을 선언해 에이전트가 어떤 요구사항을 만족해야 하는지, 어떤 지식 파일을 참고해야 하는지, 어떤 문서로 변경을 전파해야 하는지 알 수 있게 합니다. ProDoc 문서 자체도 일반 Markdown이며, 필요할 때 ReqMd 요구사항과 색인을 참조합니다.

## 문서

- [`reqmd/markdown_for_requirements.md`](reqmd/markdown_for_requirements.md): ReqMd 핵심 문법과 작성 규칙
- [`reqmd/quick_start.md`](reqmd/quick_start.md): ReqMd 빠른 시작
- [`reqmd/programmable_documentation.md`](reqmd/programmable_documentation.md): ProDoc 개념, frontmatter, propagation 규칙
- [`reqmd/example/`](reqmd/example/): Brake Lamp Controller ReqMd 예제
- [`reqmd/example-aspice/`](reqmd/example-aspice/): ASPICE 기반 ReqMd 요구사항 예제
- [`reqmd/example-project/`](reqmd/example-project/): ProDoc 기반 프로젝트 문서 예제

## 구성

```plaintext
.
├── reqmd/                    # ReqMd/ProDoc 설명 문서와 예제
├── reqmd/example/            # Brake Lamp Controller ReqMd 예제
├── reqmd/example-aspice/     # ASPICE 기반 ReqMd 요구사항 예제
├── reqmd/example-project/    # ProDoc 기반 프로젝트 문서 예제
├── .codex/skills/reqmd/      # Codex용 ReqMd agent skill
├── .codex/skills/prodoc/     # Codex용 ProDoc agent skill
├── claude/reqmd/             # Claude용 ReqMd agent skill
└── claude/prodoc/            # Claude용 ProDoc agent skill
```

## Agent Skill

이 저장소는 ReqMd와 ProDoc을 agent coding 환경에서 다룰 수 있도록 Codex/Claude용 skill을 함께 제공합니다.

ReqMd skill은 다음 작업을 돕습니다.

- 요구사항 섹션 작성 및 수정
- `@.md` identifier index와 `=.md` helper index 갱신
- Markdown fragment link 검증
- 요구사항 traceability와 영향 분석

ProDoc skill은 다음 작업을 돕습니다.

- `reqmd_prodoc` frontmatter 작성 및 검증
- `requirement_refs`에 따른 문서 내용 준수 확인
- `knowledge_files`를 참고한 문서 작성
- `propagation_docs`에 따른 lateral/upstream/downstream 영향 분석과 전파
- 전파 과정에서 필요한 ReqMd 색인 갱신

## 라이선스

이 저장소는 MIT License로 배포됩니다. 자세한 내용은 [LICENSE](LICENSE)를 참고하세요.
