# F&F CN Claude Code Workshop Script - Korean + English

> 기준 파일 / Source file: `cn_claude_edu.html`  
> 목적 / Purpose: 같은 페이지 흐름을 한국어와 영어로 함께 확인하는 발표 대본  
> 구성 / Format: 각 섹션별 한국어 대본 후 영어 대본 배치

---

## 0. 상단 내비게이션 / Top Navigation

**페이지 영역 / Page Area:** Top Navigation  
**HTML 기준 / HTML Reference:** `<header class="top-nav">`  
**화면 표시 / Visible Section:** F&F · CN 로고, 강의 개요, 설계 프레임워크, 시나리오 A, 핸즈온, 배포, Korean/English 버튼

### KR

안녕하세요. 오늘은 F&F China 구성원분들을 대상으로 Claude Code를 활용한 실무형 대시보드 제작 워크숍을 진행하겠습니다.

상단 메뉴를 보시면 오늘 과정의 큰 흐름을 확인하실 수 있습니다. 강의 개요에서 전체 진행 순서를 먼저 보고, 설계 프레임워크에서 어떤 방식으로 결과물을 기획할지 정리한 뒤, 시나리오 A를 기준으로 실제 핸즈온을 진행합니다. 이후 보고서 PPT 생성과 DCS AI 기반 사내 배포까지 연결하겠습니다.

### EN

Good morning, everyone. Today we will run a practical Claude Code workshop for the F&F China team, focused on building a business-ready dashboard from data and extending that output into a report workflow.

The top navigation shows the overall structure of today's session. We will begin with the workshop overview, move into the planning framework, work through Scenario A, complete the hands-on build, and then connect the output to PowerPoint reporting and internal deployment through DCS AI.

---

## 1. 히어로 오프닝 / Hero Opening

**페이지 영역 / Page Area:** Hero  
**HTML 기준 / HTML Reference:** `<section class="hero">`  
**화면 표시 / Visible Section:** “나만의 대시보드를 만들어보다” / “Build Your Own Dashboard”

### KR

오늘 워크숍의 핵심 메시지는 한 문장으로 정리할 수 있습니다.

데이터에서 화면으로, 그리고 보고서까지 이어지는 하나의 업무 흐름을 직접 만들어보는 것입니다.

우리가 오늘 만들 것은 단순한 예제 페이지가 아닙니다. 실제 업무에서 매주 반복되는 데이터 확인, 성과 분석, 보고서 작성, 공유 과정을 Claude Code로 어떻게 줄일 수 있는지 체험하는 실습형 결과물입니다.

### EN

The core message of today's workshop is simple.

We will build one connected workflow from data, to dashboard, to business report.

What we are creating today is not just a sample page. It is a practical workflow that reflects real recurring work: checking data, reviewing performance, building a clear screen, preparing a report, and sharing the result with the organization.

---

## 2. 핵심 지표 요약 / Key Metrics Summary

**페이지 영역 / Page Area:** Stat Strip  
**HTML 기준 / HTML Reference:** `<div class="stat-strip">`  
**화면 표시 / Visible Section:** 120분, 1종 시나리오, 2개 결과물, 5단계 PLAN

### KR

오늘 과정은 약 120분으로 설계되어 있습니다.

진행 방식은 하나의 핸즈온 시나리오를 깊게 따라가는 구조입니다. 여러 주제를 얕게 보는 대신, 하나의 실제 업무 흐름을 끝까지 완성하는 데 집중하겠습니다.

결과물은 두 가지입니다. 첫 번째는 대시보드입니다. 두 번째는 그 대시보드의 핵심 내용을 기반으로 만든 보고용 PPT입니다.

### EN

Today's workshop is designed as a 120-minute practical session.

We will not cover many disconnected topics at a shallow level. Instead, we will follow one hands-on scenario deeply and complete the end-to-end workflow.

There are two target outputs. The first is a dashboard. The second is a PowerPoint report generated from the core insights in that dashboard.

---

## 3. 전체 진행 순서 / Run-of-Show

**페이지 영역 / Page Area:** Run-of-Show  
**HTML 기준 / HTML Reference:** `<section class="block" id="ros">`  
**화면 표시 / Visible Section:** “120분, 7개 챕터로 한 흐름으로 연결”

### KR

전체 흐름을 먼저 보겠습니다.

오늘은 7개 챕터로 진행됩니다. Opening에서는 실행 환경을 점검하고 오늘 만들 결과물을 확인합니다. Use Case에서는 F&F 한국 사례와 Claude Code의 핵심 확장 개념을 짧게 보겠습니다.

이후 PLAN 단계에서 오늘 만들 대시보드를 설계하고, Skill 투어에서는 업무용으로 신뢰감 있는 대시보드를 만들기 위한 방법을 다룹니다. 핸즈온에서는 대시보드 구현, PPT 생성, Agent와 Hook 심화 개념, DCS AI 배포까지 연결하겠습니다.

### EN

Let us first review the full flow.

Today's session is organized into seven chapters. In Opening, we will check the environment and preview the outputs. In Use Case, we will briefly review F&F Korea examples and the core Claude Code mechanisms.

Then we will design the dashboard in the PLAN stage, learn how to improve business dashboard quality in the Skill Tour, and move through hands-on implementation, PPT generation, Agent and Hook concepts, and DCS AI deployment.

---

## 4. Opening: 세팅 확인하기 / Setup Check

**페이지 영역 / Page Area:** Chapter 00  
**HTML 기준 / HTML Reference:** `<section class="chapter-section" id="ch0">`  
**화면 표시 / Visible Section:** “처음 10분, 막힘 없이 핸즈온까지 진입”

### KR

먼저 실습 환경을 확인하겠습니다.

이 단계는 짧지만 중요합니다. 실제 실습에서 막히는 원인은 대부분 코드가 아니라 환경 설정입니다. 따라서 시작 전에 모두 같은 상태에서 출발할 수 있도록 기본 실행 여부를 확인하겠습니다.

터미널에서 `claude` 명령어가 정상적으로 실행되는지 확인해 주세요. 플러그인 설치 명령어가 인식되는지도 확인합니다. 또한 오늘 사용할 샘플 데이터인 `sample_data.xlsx` 파일이 준비되어 있는지 확인합니다.

### EN

We will begin by checking the practice environment.

This step is short, but it is important. In hands-on sessions, most early blockers are not caused by the code itself. They usually come from environment setup.

Please confirm that the `claude` command runs successfully from your terminal. Then confirm that the plugin marketplace command is recognized. Also confirm that `sample_data.xlsx` is available.

---

## 5. Use Case와 Claude Code 핵심 개념 / Use Case and Core Concepts

**페이지 영역 / Page Area:** Chapter 01  
**HTML 기준 / HTML Reference:** `<section class="chapter-section" id="ch1">`  
**화면 표시 / Visible Section:** “결과물 먼저, 개념은 짧게.”

### KR

이제 왜 이런 방식이 필요한지 실제 사례를 통해 보겠습니다.

F&F 한국에서는 이미 HTML 기반 보고서나 대시보드 형태의 결과물을 업무에 활용하고 있습니다. 기존에는 Excel에서 데이터를 정리하고, PPT로 복사하고, 다시 디자인을 다듬는 방식이 일반적이었습니다.

HTML 기반 대시보드는 이 흐름을 바꿉니다. 데이터, 화면, 보고서가 하나의 구조로 연결될 수 있고, 같은 패턴을 반복 업무에 재사용할 수 있습니다.

### EN

Now let us look at why this workflow matters through actual use cases.

F&F Korea is already using HTML-based reports and dashboards as business outputs. Traditionally, teams would organize data in Excel, copy content into PowerPoint, and then spend additional time adjusting the design.

HTML-based dashboards change that workflow. Data, screen, and report can be connected in one reusable structure.

---

## 6. PLAN 프레임워크 / PLAN Framework

**페이지 영역 / Page Area:** Chapter 02  
**HTML 기준 / HTML Reference:** `<section class="chapter-section" id="ch2">`  
**화면 표시 / Visible Section:** “5분 계획이 전체의 완성도를 좌우합니다.”

### KR

AI로 결과물을 만들 때 가장 흔한 실수는 바로 구현부터 요청하는 것입니다. 예를 들어 “매출 대시보드 만들어줘”라고만 하면 화면은 만들어질 수 있습니다. 하지만 그 화면이 누구를 위한 것인지, 어떤 의사결정을 지원하는지 반영되지 않을 수 있습니다.

그래서 오늘은 먼저 PLAN을 작성합니다. 목적, 데이터, 화면 스케치, 보고서 형식, 배포 방식까지 다섯 가지를 정리한 뒤 구현으로 넘어갑니다.

Plan Mode를 켜면 Claude가 바로 코드를 작성하지 않고 먼저 작업 계획을 보여줍니다. 사용자가 승인해야 실제 구현이 시작되므로 입문자에게 특히 안전한 방식입니다.

### EN

The most common mistake when using AI is asking it to implement immediately. If we simply say, “Build a sales dashboard,” Claude may generate a screen, but it may not reflect the business purpose or decision context.

That is why we start with PLAN. We define the objective, data, screen sketch, report format, and deployment method before implementation.

When Plan Mode is on, Claude does not write code immediately. It first shows the work plan, and implementation begins only after the user approves it.

---

## 7. 추천 시나리오 / Recommended Scenario

**페이지 영역 / Page Area:** Scenario Section  
**HTML 기준 / HTML Reference:** `<section class="block" id="scenarios">`  
**화면 표시 / Visible Section:** “추천 시나리오, 이대로 따라가며 핸즈온.”

### KR

오늘의 추천 시나리오는 Tmall과 Douyin의 주간 매출 대시보드입니다.

이 시나리오는 패션 업계에서 자주 발생하는 업무 흐름과 연결됩니다. 채널별 매출을 확인하고, 전주 대비 성과를 보고, 어떤 상품과 카테고리가 성과를 만들었는지 빠르게 파악하는 것이 목적입니다.

핵심 지표는 전주 대비 증감률, 매출 기준 Top10 상품, 카테고리와 채널을 교차해서 보는 히트맵, 채널별 주간 매출 흐름입니다.

### EN

Today's recommended scenario is a weekly sales dashboard for Tmall and Douyin.

This reflects a common workflow in the fashion business: reviewing channel sales, checking week-over-week performance, and identifying which products and categories are driving results.

The core indicators are week-over-week growth, top 10 products by sales, category-by-channel heatmap, and weekly sales by channel.

---

## 8. Claude Code 핵심 개념 / Claude Code Concept Deep-Dive

**페이지 영역 / Page Area:** Concepts Deep-Dive  
**HTML 기준 / HTML Reference:** `<section class="chapter-section" id="ch2b">`

### KR

Skills는 업무 매뉴얼입니다. 특정 작업을 할 때 어떤 방식으로 접근해야 하는지 Claude에게 알려주는 지침입니다.

Plugins는 스킬 묶음 설치입니다. 여러 도구를 하나의 패키지처럼 설치해 사용할 수 있습니다.

Memory는 기억 노트, Hooks는 자동 트리거, MCP는 외부 시스템 연결선입니다. 오늘은 Skills와 Plugins를 직접 사용하고, 나머지는 다음 단계 자동화를 위한 개념으로 이해하겠습니다.

### EN

Skills are operating manuals. They tell Claude how to handle a certain type of work.

Plugins are bundled installations. They help install multiple skills or tools together.

Memory is a persistent note, Hooks are automation triggers, and MCP is the connection layer to external systems. Today, we will directly use Skills and Plugins, while understanding the others as preparation for advanced automation.

---

## 9. Skill 적용과 디자인 품질 / Applying Skills and Design Quality

**페이지 영역 / Page Area:** Chapter 03  
**HTML 기준 / HTML Reference:** `<section class="chapter-section" id="ch3">`

### KR

AI에게 별도 지시 없이 화면을 만들게 하면 비슷한 결과가 자주 나옵니다. 보라색 그라데이션, 둥근 카드, 과도한 그림자, 어디서 본 듯한 대시보드 레이아웃이 반복됩니다.

업무용 대시보드는 단순히 화려하면 안 됩니다. 매주 반복해서 볼 수 있어야 하고, 숫자와 차트가 명확해야 하며, 보고 받는 사람이 신뢰할 수 있어야 합니다.

그래서 오늘은 `frontend-design` skill을 활용합니다. 레퍼런스를 명확히 주고, 브랜드 톤을 정의하며, 피해야 할 예시와 따라야 할 예시를 함께 제공하겠습니다.

### EN

If we ask AI to design a dashboard without specific direction, the output often looks generic: purple gradients, rounded cards, excessive shadows, and familiar dashboard patterns.

A business dashboard should not only look polished. It should be reliable, readable, and suitable for repeated use.

That is why we use the `frontend-design` skill. We will provide concrete references, define the brand tone, and include both bad and good examples.

---

## 10. 핸즈온 1: 대시보드 구현 / Hands-on 1: Dashboard Implementation

**페이지 영역 / Page Area:** Chapter 04  
**HTML 기준 / HTML Reference:** `<section class="chapter-section" id="ch4">`

### KR

이제 실제 구현 단계입니다.

앞에서 만든 PLAN을 바탕으로 샘플 데이터를 분석하고, 대시보드를 HTML 단일 파일로 만들어봅니다.

진행 순서는 PLAN 확인, 데이터 확인과 첫 프롬프트 실행, 화면 구현과 다듬기, 품질 체크입니다. 처음 생성된 화면이 완벽하지 않아도 괜찮습니다. 레이아웃, 차트, 문구, 색상, 정보 우선순위를 조정하면서 완성도를 높이면 됩니다.

### EN

Now we move into implementation.

In this step, we will analyze the sample data and create a single-file HTML dashboard based on the PLAN we prepared earlier.

The process is to confirm the PLAN, check the data and run the first prompt, build and refine the screen, and then perform a quality check. The first draft does not need to be perfect. We will improve it through iteration.

---

## 11. 핸즈온 2: 보고서 PPT 생성 / Hands-on 2: Report PPT Generation

**페이지 영역 / Page Area:** Chapter 05  
**HTML 기준 / HTML Reference:** `<section class="chapter-section" id="ch5">`

### KR

대시보드가 만들어졌다면 다음은 보고서화입니다.

업무에서는 대시보드만으로 끝나지 않는 경우가 많습니다. 임원 보고, 팀 공유, 월간 리뷰를 위해 PPT 형태가 필요한 경우가 많습니다.

`pptx` skill은 대시보드의 핵심 인사이트를 기반으로 보고용 PowerPoint를 만들 수 있도록 돕습니다. 또한 Agent와 Hook 개념을 이해하면 이후 반복 보고 업무를 자동화하는 방향으로 확장할 수 있습니다.

### EN

Once the dashboard is created, the next step is reporting.

In business workflows, a dashboard alone is often not enough. Teams frequently need a PowerPoint version for executive reporting, monthly reviews, or team sharing.

The `pptx` skill helps convert dashboard insights into presentation material. Understanding Agent and Hook concepts also prepares us to automate recurring reporting work later.

---

## 12. DCS AI 사내 배포 / DCS AI Internal Deployment

**페이지 영역 / Page Area:** Chapter 07  
**HTML 기준 / HTML Reference:** `<section class="chapter-section" id="ch7">`

### KR

마지막으로 결과물을 어떻게 공유하고 배포할지 보겠습니다.

DCS AI는 F&F 내부에서 운영하는 AI 인프라 및 도구 환경입니다. Claude Code와 MCP 방식으로 연결하면, Claude가 사내 리소스를 활용해 결과물을 업로드하거나 공유 링크를 생성할 수 있습니다.

로컬 HTML, 사내 인트라넷, 메신저나 메일 첨부 등 상황에 맞는 공유 방식을 선택할 수 있습니다. DCS AI를 사용하면 외부 서비스에 의존하지 않고 사내 보안 환경 안에서 결과물을 관리할 수 있습니다.

### EN

Finally, we will discuss how to share and deploy the output.

DCS AI is F&F's internal AI infrastructure and tool environment. When connected to Claude Code through MCP, Claude can use approved internal resources to upload outputs and generate internal sharing links.

Depending on the situation, you can use local HTML, the internal intranet, or messenger and email attachments. With DCS AI, outputs can be managed inside the company security boundary without relying on external services.

---

## 13. 세션 마무리 / Session Closing

**페이지 영역 / Page Area:** Final CTA  
**HTML 기준 / HTML Reference:** `<section class="cta-light">`

### KR

오늘 세션을 정리하겠습니다.

오늘 우리가 다룬 핵심은 세 가지입니다. 첫째, 바로 만들지 않고 PLAN부터 세운다는 점입니다. 둘째, 데이터와 목적, 보고 대상을 명확히 정의한다는 점입니다. 셋째, Claude Code의 Skills, pptx, DCS AI 배포 흐름을 활용해 대시보드와 보고서를 하나의 업무 흐름으로 연결한다는 점입니다.

오늘 실습을 통해 Claude Code를 단순한 코딩 도구가 아니라, 업무 자동화와 보고 품질을 높이는 실무 파트너로 활용하는 감각을 가져가시면 좋겠습니다.

### EN

Let us close the session by summarizing the key points.

There are three main takeaways from today. First, start with PLAN before asking AI to build. Second, define the data, purpose, and reporting audience clearly. Third, connect Claude Code Skills, pptx reporting, and DCS AI deployment into one practical workflow.

I hope today's session helps you see Claude Code not just as a coding tool, but as a practical partner for business automation and reporting quality.

---

## 14. 푸터 및 리소스 안내 / Footer and Resources

**페이지 영역 / Page Area:** Footer  
**HTML 기준 / HTML Reference:** `<footer>`

### KR

마지막으로 하단에는 오늘 강의에서 사용한 주요 리소스가 정리되어 있습니다.

Run-of-Show, Opening, PLAN, Skill Tour, Hands-on, DCS AI 배포 영역으로 바로 이동할 수 있습니다.

실습 이후 다시 복습하실 때는 오늘 만든 결과물과 함께 이 페이지를 참고하시면 됩니다.

### EN

At the bottom of the page, the key resources from today's session are organized for later reference.

You can jump back to Run-of-Show, Opening, PLAN, Skill Tour, Hands-on, and DCS AI deployment.

After the session, use this page together with your generated outputs as a reference for review and reuse.
