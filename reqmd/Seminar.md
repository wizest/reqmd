---
marp: true
# theme: gaia
# _class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: 'SW팀 세미나, 김상훈 책임 2024-6-14'
---

# Markdown, ReqIF 표준을 활용한 요구사항 개발환경
 
- Markdown 요구사항 문서형식 제안: 식별자와 도움자의 정의와 활용
- Markdown → ReqIF 문서형식의 변환과 응용 사례 연구
 
---
 
## 모두를 위한 범용 환경
 
*무슨 기능이 제공되는가* 보다 *어떻게 사용하는가* 가 핵심이다
 
- 인프라 구축에 힘빼지 말자.
- 돈이 없어도 어떻게든 시작할 수 있어야
- 널리 사용되는 것, 표준을 활용하자
- 환경의 유지 보수를 걱정하고 싶지 않다.
- 범용 도구를 채택하자
- 양질의 공개강의, 서적을 활용하자
 
---
 
## 문서도 코드 처럼
 
기술 문서의 본질은 *서식*이 아니라 *내용*이다
 
- 글를 쓰고 읽기 위해 꼭 특별한 도구가 필요해야 하나?
- 글 쓰는 것과 코딩 하는 것이 본질적으로 다른가?
- 글을 잘 쓰고, 잘 열람하고, 잘 편집 하는 것이 기본에 충실해야 한다
- 문서관리(RM)와 코드관리(CM) 가 다를 필요가 있을까?
 
---
 
## Markdown
 
- .md 확장자를 가진 ***그냥*** 텍스트 파일
- 사람과 컴퓨터가 동시에 친화적인 문법
 
| ![h:300](seminar-image-0.png) | ![h:300](seminar-image-1.png) |
| ----------------------------- | ----------------------------- |
|                               |                               |
 
---
 
## 요구사항 문서의 특징
 
- 관계와 추적성
  - 요구사항간 관계를 기술할 수 있고, 그것을 부분집합으로 추출한다
 
- 추상적 표현과 구체적 표현
  - 추상적으로 기술한 대상이 어떻게 구체화 되는지 보인다
 
- 개별 요구사항의 속성
  - 요구사항의 속성에 따라 검색/필터링 할 수 있다
 
---
 
## 요구사항 문서를 위한 Markdown → ReqMD
 
Markdown 문법을 요구사항 문서에 맞도록 사용법을 제안 → **ReqMD** 라고 부르자
 
- **식별자**: **관계(Relation)** 의 추적을 위한 Link 문법의 활용
- **도움자**: 추상적 표현과 구체적 표현의 **연결(Mapping)** 위한 Link 문법의 활용
- **속성자**: 요구사항의 **속성(Attribute)** 표현을 위한 Autolink 분법의 활용
- **색인**: 관계, 연결, 속성를 기술하는 특별한 파일
  - **식별자색인**: 관계와 속성을 기술하는 특별한 파일 **@.md**
  - **도움자색인**: 추상과 구상을 연결하는 특별한 파일 **=.md**
 
> 새로운 문법을 추가하지 않아, 범용 도구를 그대로 사용할 수 있게 하자
 
---
 
- 하나의 요구사항은 하나의 section을 구성한다.
- 요구사항은 여러개의 여러개의 **식별자** , **도움자** , **속성자** 를 포함할 수 있다.
- 요구사항의 section 제목은 반드시 **식별자** 로 시작한다.
- 요구사항은 subsection 으로 자식 요구사항 들을 포함할 수 있다.
- 요구사항의 **관계**와 **속성** 정보는 **식별자색인** 의 해당 **식별자** section에 기술한다.
- **도움자** 간 **연결** 정보는 **도움자색인** 의 해당 **도움자** section에 기술한다.
 
> 요구사항의 관계, 연결, 속성은 본문과 분리하여, 색인에 작성한다
> **색인** 은 **도구**에 의해 가공될 수 있다. (통계, 색인, 검색, 요약, 번역 등)
 
---
 
## 요구사항 예제
 
```console
sw/@.md                           ⇐ 식별자색인
  /=.md                           ⇐ 도움자색인
  /SwReq1.md                      ⇐ 이 파일을 편집하고 있다고 가정
  /SwReq2.md
  /...
```
 
```markdown
# [GLD_INIT](@) Initialization
 
- GLD shall initialize [position_lever_delayed](=) with [macro_lever_position_0](=)
- GLD shall initialize [count_time](=) as deactivated at the beginning of each time step.
...
 
## Acceptance criteria
 
- [position_lever_delayed](=) is equal to [macro_lever_position_0](=) at the first time step.
- [count_time](=) is deactivated at the beginning of each time step as the component is running
...

```
 
---
 
## 식별자 `[identifier](@)`
 
`[identifier](path/@#fragment "description")`
: Markdown Link 문법으로 요구사항 **관계**의 출발점(source)과 도착점(target) 을 표현함
 
- `path/` 는 요구사항이 저장된 file path 이며, 여러 요구사항 문서를 구조화 한다.
- `identifier` 는 path 범위에서 요구사항을 가리키는 유일한 문자열이다.
- `#fragment` 는 색인의 특정 위치를 가리킨다.
- `"description"` 은 identifier를 설명하는 문자열이다.
- `path/`, `#fragment`, `"description"`은 생략할 수 있다.
  - `[id](@)`, `[id](path/@)`, `[id](@#fragment)`, `[id](@ "desc")`
 
---
 
## 속성자 `<attribute:Value>`

`<attribute:value>`
: Markdown 의 Autolink 문법으로 요구사항 **속성** 을 표현함
 
- `attribute` 와 `value` 는 띄워쓰기 하지 않으며 특수 문자를 포함하지 않는다.
- 요구사항의 속성은 정형화된 field 또는 parameter 를 가리킨다.
- 여러개의 value 입력은 `,` 으로 기술한다
 
> #### 기본 속성
> 
> - Type : Container, Informational, Functionl 중 하나의 값 → `<Type:Functional>`
> - Keyword : 키워드 자유기술 → `<Keyword:Keyword1,Keyword2>`
 


---
 
## `@.md` 파일에서 관계와 속성 표현하기
 
```console
sys/@.md
    /SysReq1.md
    /SysReq2.md
sw/@.md                           ⇐ 이 파일을 편집하고 있다고 가정할 때
    /SwReq1.md                      
swqt/@.md
    /SwqtReq1.md
```
 
```markdown
# SourceIdent                     ⇐ 식별자를 section 제목으로 함
 
Relation                          ⇐ sw/SwReq1.md 에 [SourceIdent](@) 요구사항에 대한 관계를 표현
  - [TargetIdent1](../sys/@)      ⇐ (SourceIdent → TargetIdent1 of sys/) 관계를 표현
  - [TargetIdent2](../swqt/@)     ⇐ (SourceIdent → TargetIdent2 of swqt/) 관계를 표현
  - [TargetIdent3](@)             ⇐ (SourceIdent → TargetIdent3 of sw/) 관계를 표현
 
Attribute
  - <Type:Functional>             ⇐ GLD_INIT 요구사항은 Type 가 Functional 임
  - <Keyword:aaaa,bbbb>           ⇐ GLD_INIT 요구사항은 keyword 가 aaaa,bbbb 임
```
 
---
 
## 도움자 `[helper](=)`
 
`[helper](path/=#fragment "description")`
: Markdown Link 문법으로 **연결** 하고자 하는 추상적 또는 구체적 대상을 표현함
 
- `path/` 는 요구사항이 저장된 file path 이며, 여러 요구사항 문서를 구조화 한다.
- `helper` 는 path 범위에서 추상적 또는 구체적 대상을 가리키는 유일한 문자열이다.
- `#fragment` 는 색인의 특정 위치를 가리킨다.
- `"description"` 은 helper를 설명하는 문자열이다.
- `path/`, `#fragment`, `"description"`은 생략할 수 있다.
  - `[help](=)`, `[help](path/=)`, `[help](=#fragment)`, `[help](= "desc")`
 
---
 
## `=.md` 파일에서 추상과 구상의 연결하기
 
```console
sys/=.md
    /SysReq1.md
sw/=.md                             ⇐ 이 파일을 편집하고 있다고 가정할 때
    /SwReq1.md                      
```
 
sw/=.md 파일에서
 
```markdown
# SourceHelper                      ⇐ 도움자를 section 제목으로 함
 
Mapping                             ⇐ 도움자 [SourceHelper](=) 에 대한 연결을 표현
  - [TargetHelper1](../sys/=)       ⇐ (SourceHelper → TargetHelper1 of sys/) 연결을 표현
  - [TargetHelper2](=)              ⇐ (SourceHelper → TargetHelper2 of sw/) 연결을 표현
 
Relation                            ⇐ 도움자와 관계한 식별자, 도구에 의해 자동 작성 가능
  - [ReqIdent1](@)                  ⇐ (ReqIdent1 in sw/) 요구사항에 SourceHelper가 언급됨
  - [ReqIdent2](../sys/@)           ⇐ (ReqIdent2 in sys/) 요구사항에 SourceHelper가 언급됨

```
 
---

 

## 요구사항 템플릿은 어떻게 정할까
 
<style scoped>{ font-size: 20px; }</style>
 
VW AQ 의 Work product
 
<style scoped>table { font-size: 15px; }</style>
 
| 유형 | Requirement                 | Design                                  | Testsuite                   |
| ---- | --------------------------- | --------------------------------------- | --------------------------- |
| 종류 | L2 (PTC)                    | System architecture design (Word or EA) | L2 (PTC)                    |
|      | L4                          | SW architecture design (Word or EA)     | L4                          |
|      | L5                          | Detail design (Simulink)                | L4                          |
| 항목 | ![h:200](seminar-item1.png) | 개발도구에 의존                         | ![h:200](seminar-item2.png) |


MATLAB Requirement editor
 
- Index, ID, Summary, Implemented, Type : Container, Functional, Informational
- Keywords, SID, CreatedOn, CreatedBy, ModifiedOn, SynchronizedOn, ModifiedBy, Revision, Verified,- Description, Rationale
 
---
 
## 미래에는
 
색인 파일 자동 갱신 도구
 
- 식별자, 도움자를 제목으로 하는 section 생성
- 관계, 연결 정보의
  - 유효성 검사
  - fragment 갱신: `[Ident](@)` → `[Ident](path/@#fragment "desc")` 로 변경
 
검색 도구
 
- 관계, 연결 정보로 관련 요구사항을 출력 → 영향성 분석도구
- 속성에 따른 요구사항 필터링 도구

---

## Markdown 으로 기술한 요구사항을 어떻게 상세 개발할까?
 
업무흐름: Markdown ⇔ ReqIF 간 상호 변환
 
1. 요구사항을 Markdown으로 작성한다.
2. Markdown 요구사항 문서를 ReqIF 로 변환한다.
3. ReqIF 를 지원하는 개발도구에 Import 하여 상세 개발한다.
4. 개발도구에서 관계 정보가 갱신된 ReqIF 를 export한다.
5. ReqIF 를 요구사항 Markdown 으로 변환하고, 기존의 markdown에 반영한다.
 
ReqIF 표준포멧으로 요구사항을 확보하기만 하면
 
- 개발도구 연동을 위한 커스텀 개발을 배제 → 시간이 지날수록 *더 좋은* 도구가 생김
- 요구사항의 migration 이 준비된 상태 → 필요하다면 ALM *갈아타기* 좋아
- MATLAB requirement toolbox 사용 → 요구사항 기반 개발을 *명시적*으로 수행
 
<!--
<style scoped> blockquote{ font-size: 20px; }</style>
 
> 😯 변환을 위한 적절한 도구가 현재 없음. Markdown/XML parser를 이용하여 개발이 필요함 -->
---

## Requirements Interchange Format(ReqIF) 표준
 
- XML 형식의 개방적이고 비독점적인 교환 형식
 
<style>img[alt~="center"] {  display: block;   margin: 0 auto;}</style>
![h:500 center](seminar-reqif-exchange.png)
 
<!--
- 표준 특징
  - 계층적 구조 사양
  - 서식이 지정된 텍스트
  - 참조 바이너리 파일
  - 요구사항을 고유하게 식별
  - 속성을 요구 사항과 연결
  - 요구사항간 관계설정
  - 관계를 그룹화
  - 특정 정보에 대한 사용자 접근 제한
 
- 태그 속성
  - isSimplified: 도구가 값을 제대로 해석하지 못할 경우 true, 그외 false
    - xhtml 관련한 속성에 등장
    - true일 경우 단순화된 속성에 대한 원본 속성이 존재
-->
 
---

 
## ReqIF 파일의 구성
 
| ![h:400](seminar-reqif-0.png) | ![h:400](seminar-reqif-1.png) |
| ----------------------------- | ----------------------------- |


---
 
## MATLAB의 Requirement Toolbox 에 ReqIF를 Import 하기
 
<style scoped>table { font-size: 10px; }</style>
 
| ReqIF                             | Import                          | Requirement editor               |
| --------------------------------- | ------------------------------- | -------------------------------- |
| ![h:190](seminar-reqifexport.png) | ![h:190](seminar-reqimport.png) | ![h:190](seminar-reqtoolbox.png) |
 
<!-- ![](seminar-reqmdex.png) -->
 
<style scoped>blockquote { font-size: 15px; }</style>
 
> ### Requirements editor 에서 ReqIF 포멧으로 import, export 할 경우
> 
> - 요구사항간 link는 spec object type 이 `Requirement` 으로 정의됨
> - 모델과 관계한 link는 spec object type 이 `Simulink Object` 으로 정의됨
> - 모델과 요구사항에 대한 link 정보에 대해
>   - Export된 ReqIF에 모든 정보가 포함되어 있으나
>   - Import시 요구사항 간 link는 복원이 되나, 모델과 관계한 link는 복원이 되지 않는 문제가 있음
> - 시뮬링크에서 `요구사항-모델` 간 연결은 다음과 같은 url 로 표현된다.
>   - `http://127.0.0.1:31415/matlab/feval/rmiobjnavigate?arguments=[%22TodoListAsReq.slx%22,%22:1%22]`
>   - 위 문자열은 `[navURL,navLabel] = slreq.getExternalURL(myDesignItem)` 으로 얻는다.


<!-- Simulink 모델의 Relation
 
- Requirement Link Storage
- Requirements Management Interface (RMI)

-->
 
<!--
## MATLAB 요구사항 의 구성
 
- Markdown 및 ReqIf 형식으로 기술하는 요구사항은 MATLAB requirements editor 가 지원하는 기본 항목을 대상으로 한다.
  - MATLAB requirements editor가 지원하는 기본 항목은 [Import, Update and Export Requirement](https://kr.mathworks.com/help/slrequirements/import-update-and-export-requirements.html?s_tid=CRUX_lftnav) 을 참고한다.
  - 상세 지원 항목은 MATLAB requirement editor 가 입출력하는 Generic 환경을 따른다.
  - RefIF 버전은 [1.2](https://www.omg.org/spec/ReqIF/1.2/About-ReqIF/)를 따른다.
    - `<REQ-IF  xmlns="http://www.omg.org/spec/ReqIF/20110401/reqif.xsd" xmlns:xhtml="http://www.w3.org/1999/xhtml">`
-->

---

 

## Simulink 에서 Relation
 
Requirement와 Requirement를 연결
![h:200 center](seminar-link0.png)
 
Simulink 또는 Testcase 와 Requirement 를 연결
![h:200 center](seminar-link1.png)
 
<!--
> 도구와 Workproduct
> - Simulink composer : SW Architecture Model
> - Simulink : SW Design Model
> - Test manager -->
 
<!-- ## Simulink requirements editor의 항목과 ReqIF 항목 간의 연결관계
 
<style scoped>table { font-size: 15px; }</style>
 
| MATLAB attribute | ReqIF types       |
| ---------------- | ----------------- |
| Summary          | ReqIF.ChapterName |
| Custom ID        | ReqIF.ForeignID   |
| Description      | ReqIF.Text        |
| CreatedBy        | CreatedBy         |
| CreatedOn        | CreatedOn         |
| Keywords         | Keywords          |
| ModifiedBy       | ModifiedBy        |
| ModifiedOn       | ModifiedOn        |
| Rationale        | Rationale         | -->
 
<!--
- Simulink가 excel 형식으로 import 하는 것
    - CustomID : 사용자가 입력한 ID
    - Summary : 요구사항의 한 줄 설명
    - Keywords
    - CreatedOn
    - CreatedBy
    - ModifiedOn
    - ModifiedBy
    - Description : 요구사항에 대한 상세 설명
    - Rationale        
 
- Simulink requirements editor에서 관리하는 항목이나 import 때 요청하지 않는 것
    - Index : 1, 1.1, 2 와 같이 목록의 순서와 계층구조
    - Type : Container, Functional, Informational 중 선택
    - Revision
 
- Simulink requirements editor의 Attributes
    - Index
    - ID
    - Summary
    - Implemented
    - Type : Container, Functional, Informational
    - Keywords
    - SID
    - CreatedOn
    - CreatedBy
    - ModifiedOn
    - SynchronizedOn
    - ModifiedBy
    - Revision
    - Verified
    - Description
    - Rationale        
-->
 
---
 
## 생각하기1 - 프로젝트를 한 권의 책으로
 
- CD/CI : 문서나 모델을 수정 -> Markdown, Book 자동갱신 -> 웹페이지 게시
- SW 배포시에 웹페이지 또는 pdf 형식의 책을 함께 제공
 
![h:400 center](seminar-mdbook.png)
 
---
 
## 생각하기2 - Feasiblility SW와 Production SW 의 개발

<style>img[alt~="center"] {  display: block;   margin: 0 auto;}</style>
![height:600 center](seminar-image-2.png)
 
<!--
- [A] Requirement 를 위한 Markdown 문서의 사양 정의 (확장자 = .req.md)
    - 사양대로 문서가 작성되었는지 Check 도구 필요
- [B] .req.md ó .reqif 변환기 개발
    - Simulink 내부와 외부간 연동
- [C] Simulink Model -> SW Requirement 생성기 개발 by 생성형 AI
    - Simulink/Stateflow Model -> Pseudo code 생성기 개발
    - Pseudo code -> SW Requirement 생성기 개발 by 생성형 AI
        - Python 코드 refactoring by AI (optional)
        - Python 코드에 대한 SW설명 by AI
- [D] Requirement 묶음 -> 상위 Requirement 생성기 개발 by 생성형 AI
- [E] Requirement 대응 Testcase 생성기 개발 by 생성형 AI
- [F] Requirement 묶음에서 Feature 추출기 개발 by 생성형 AI
- [G] 주어진 Feature 입력에 따라 Requirement 분류하는 도구 개발 by 생성형 AI
- [H] 자연어 ó 신호명 변환기 by 생성형 AI
- [I] Requirement markdown 문서 번역기 by 생성형 AI (optional)
-->

 

---

 

## 결론