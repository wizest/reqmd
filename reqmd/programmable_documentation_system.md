# 프로그래머블 문서 작성 시스템 (ProDoc)

Programmable Documentation System `ProDoc`은 Markdown 문서의 frontmatter를 선언적 설정으로 활용하여, 에이전트형 인공지능이 문서를 작성하고 검증하며, 문서 간 추적성과 변경 사항의 전파를 수행하도록 하는 시스템입니다.
즉, 문서에 포함된 메타데이터가 에이전트의 작성 방식과 동작 기준을 결정하며, 에이전트는 이를 바탕으로 문서의 목적과 형식에 맞게 내용을 생성하고 관리합니다.

> programmable = agent behavior is configurable by document metadata

문서의 frontmatter는 에이전트가 문서를 작성·검증·전파하기 위해 참조하는 선언적 설정 영역입니다. 여기에는 문서의 요구사항, 참조해야 할 도메인 지식, 준수해야 할 작성 규칙, 관련 문서와의 계층 및 추적 관계, 작성 후 전파 대상, 그리고 통과해야 할 검증 기준을 기술합니다. 에이전트는 이 정보를 기반으로 현재 문서의 역할을 해석하고, 적절한 형식으로 내용을 작성하며, 관련 문서와의 추적성을 유지하고, 필요한 후속 문서로 변경 사항을 전파합니다.

문서의 frontmatter에는 다음 내용을 기술합니다.

- 문서의 요구사항: Agent가 작성해야 할 문서의 유형과 특징을 정의합니다.
- 포함하는 도메인 지식: Agent가 문서를 작성할 때 참고해야 할 전문 지식을 정의합니다.
- 작성 규칙: Agent가 준수해야 할 문서 형식과 작성 규칙을 정의합니다. 예: ReqMd
- 영향을 주는 문서: 현재 문서가 어떤 문서에 영향을 주는지 정의합니다.
  - 영향 대상 문서가 계층 구조를 가지는 경우, 현재 문서와의 상하위 관계를 정의합니다.
  - 현재 문서와 영향 대상 문서 간의 추적성을 어떻게 설정할지 정의합니다.
- 검증 기준: 문서가 통과해야 할 검사 항목을 정의합니다.

ProDoc frontmatter 예제:

```yaml
---
reqmd_prodoc:
  requirement_refs: 
    - reqmd/example-aspice:       # Path of ReqMd Identifier index
      - SWE_3_BP_1                # ID for Specify the static aspects of the detailed design
      - WP_04_05                  # ID for software_detailed_design
  knowledge_paths:
    - reqmd/example-aspice        # Path of ReqMd Identifier index
  propagation_docs:
    lateral:
      - pathto/lateral1.md
      - pathto/lateral2.md
    upstream:
      - pathto/upstream.md
    downstream:
      - pathto/downstream.md
---
```

## Requirements

## Knowledge

## Propagation

lateral:

upstream:

downstream:
