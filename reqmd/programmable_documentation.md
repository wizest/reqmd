# 프로그래머블 문서 작성 시스템 (ProDoc)

Programmable Documentation System `ProDoc`은 Markdown 문서의 frontmatter를 선언적 설정으로 활용하여, 에이전트형 인공지능이 문서를 작성하고 검증하며, 문서 간 추적성과 변경 사항 전파를 수행하도록 하는 시스템입니다.
즉, 문서에 포함된 메타데이터가 에이전트의 작성 방식과 동작 기준을 결정하고, 에이전트는 이를 바탕으로 문서의 목적과 형식에 맞게 내용을 생성하고 관리합니다.

ProDoc은 ReqMd 위에서 동작하는 시스템입니다. ProDoc으로 작성되는 문서, 그 문서가 참조하는 요구사항과 지식, 그리고 변경 사항을 전파할 대상 문서는 ReqMd 형식으로 작성된 문서입니다.

> programmable = agent behavior is configurable by document metadata

문서의 frontmatter에는 다음 내용을 기술합니다.

- 문서의 요구사항: 에이전트가 작성해야 할 문서의 유형과 특징을 정의합니다.
- 참조할 도메인 지식: 에이전트가 문서를 작성할 때 참고해야 할 문서를 정의합니다.
- 영향을 주는 문서: 현재 문서가 어떤 문서에 영향을 주는지 정의합니다.
  - 영향 대상 문서가 계층 구조를 가지는 경우, 현재 문서와의 상하위 관계를 정의합니다.
  - 현재 문서와 영향 대상 문서 사이의 추적성 설정 방식을 정의합니다.

ProDoc frontmatter 예제:

```yaml
---
reqmd_prodoc:
  requirement_refs:
    - reqmd/example-aspice:       # Path to ReqMd identifier index
      - SWE_3_BP_1                # Identifier
      - WP_04_05                  
  knowledge_paths:
    - reqmd/example-aspice        # Path to ReqMd identifier index
  propagation_docs:
    lateral:
      - path/to/lateral1.md
      - path/to/lateral2.md
    upstream:
      - path/to/upstream.md
    downstream:
      - path/to/downstream.md
---
```

## Requirements

## Knowledge

## Propagation

lateral:

upstream:

downstream:
