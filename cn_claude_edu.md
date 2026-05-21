### 📌 강의 요약

- "데이터 → 기획 → 대시보드(http 배포) or 보고서 PPT"까지 **한 흐름으로 연결**
- 사전과제 제거 → **현장에서 동일한 실습 시나리오 4종** 제공
- **PPT 자동 생성** 파트 포함 (Anthropic 공식 `pptx` skill 활용)
- 최신 Skill / 기능 반영 (`frontend-design`, Subagent 등)
- 청중 가정: Claude Code 설치는 했으나 거의 안 써본 입문 수준
- 진행 언어: 한국어 주, 채널명·UI 용어 첫 등장 시 중문 병기

---

### 🗂 강의 Index (총 120분)

| 시간 | 파트 | 내용 |
| --- | --- | --- |
| 0–10' | 0. Opening | 첫 실행 점검 + 결과물 데모 + 오늘 만들 것 미리보기 |
| 10–25' | 1. Use Case | F&CO 사례 2건 + 핵심 Skill 개념 |
| 25–40' | 2. 설계 프레임워크 | 5단계 PLAN 워크시트 + 시나리오 4종 |
| 40–55' | 3. 핵심 Skill 투어 | frontend-design, pptx, xlsx 등 |
| 55–95' | 4. 핸즈온 ① | 데이터 → 기획 → 대시보드 만들기 |
| 95–110' | 5. 핸즈온 ② | 대시보드 → 보고서 PPT 자동 생성 |
| 110–120' | 6. 배포 + 클로징 | Vercel 1-click 배포 + Q&A |

---

### **0부. Opening (10분)**

**0-A. 첫 실행 점검 (3분) — 입문자 케어**

핸즈온 시작 전에 모두가 같은 출발선에 있는지 확인:

- [ ] 터미널에서 `claude` 입력 → 정상 실행되는가
- [ ] `/plugin marketplace add obra/superpowers-marketplace` 명령어가 인식되는가
- [ ] `./sample_data/` 폴더 안에 시나리오 4종 CSV가 보이는가
- [ ] 사내 망/VPN/프록시 환경에서 Claude Code가 외부 호출 가능한가

> 💡 *막히는 사람은 보조강사가 1:1 케어. 이 3분 동안 해결 안 되면 강사가 실행 환경 빌려줘서 옆자리 셰어로 진행.*

**0-B. 오늘 만들고 갈 결과물 라이브 데모 (3분)**

- 매출 대시보드 화면(天猫·抖音 데이터) → 클릭 한 번에 임원 보고용 PPT까지 자동 생성되는 흐름

**0-C. F&CO 국내 사례 빠르게 시연 (2분)**

- 개발 워크플로우 자동화
- 보고서 HTML 생성 워크플로우

**0-D. 오늘의 약속 (2분)**

- "퇴근할 때 각자 ① 본인 대시보드 1개 + ② 자동 생성된 보고서 PPT 1개를 들고 나간다"
- 2시간 로드맵 1장

---

### **1부. Use Case + Claude Code 핵심 개념 (15분)**

**1-1. F&CO 국내 사례 (8분)**

- **개발 워크플로우 자동화** : Before/After + 시간 절감 수치
- **CEO Report, 보고서 : PPT → HTML**
    1. F&CO 보고자료 (Tribe 테스트건)

        [hooking_dna.html](attachment:854a9a89-256a-4fe6-b1c1-571cafbf0f38:hooking_dna.html)

        https://tribe2deep.vercel.app/

    2. 글로벌 마케팅팀 보고자료 CEO REPORT

        [KARINA_EDITION_VOL2_UNIFIED_DASHBOARD.html](attachment:c1ca5ab3-6665-4db2-9bc3-d88f0232e3fe:KARINA_EDITION_VOL2_UNIFIED_DASHBOARD.html)

    3. F&CO 인플루언서 대시보드 보고 자료 CEO REPORT

        [fnco_if_ceo-main.zip](attachment:cba4778f-4453-4cae-bbbc-dd7f8bc6e7ae:fnco_if_ceo-main.zip)

        [ceoreport.html](attachment:80527079-6a92-4853-8356-3de162bd08d2:ceoreport.html)

**1-2. Claude Code의 4대 확장 메커니즘 (7분) — 짧고 굵게**

2026년 현재 Claude Code의 핵심은 4개 시스템입니다:

| 메커니즘 | 한 줄 설명 | 오늘 워크숍에서 |
| --- | --- | --- |
| **Skills** | 특정 작업을 잘하게 만드는 지침서 (markdown) | ✅ 메인 활용 |
| **Subagents** | 별도 컨텍스트에서 작업하는 전문 에이전트 | ✅ 일부 활용 |
| **MCP** | 외부 데이터/도구 연결 (DB, Slack, Figma 등) | 🔍 개념만 |
| **Hooks** | 작업 전후 자동 실행 트리거 | 🔍 개념만 |

> 💡 *"오늘은 Skills를 마스터하면 됩니다. 나머지는 다음 단계."* 라고 명확히 정리.

---

### **2부. 설계 프레임워크 — PLAN부터 시작하기 (15분)**

워크숍 결과물의 퀄리티를 좌우하는 가장 중요한 파트.

**🎯 5단계 PLAN 워크시트 (실제 인쇄/PDF로 배포)**

```
1️⃣ 목적
   "누가 / 언제 / 어떤 의사결정을 위해 보는가?"
   예: 마케팅팀장이 매주 월요일 캠페인 ROI 점검

2️⃣ 데이터
   - 어떤 데이터? (매출/마케팅/재고/VOC)
   - 어디서? (Excel, Tmall(天猫) API, Douyin(抖音) API, JD(京东), 사내 ERP)
   - 형태? (CSV/Excel/JSON)

3️⃣ 화면 스케치 (손그림 OK)
   - 한 화면에 들어갈 핵심 지표 3-5개
   - 차트 타입 (막대/라인/지도)

4️⃣ 보고서 형식
   - PPT? HTML? 엑셀?
   - 누구에게 전달?

5️⃣ 배포
   - 본인 PC에서만? URL로 공유?
```

### 2-1. 간단하게 plan 짜는 3가지 방법

**방법 1. Claude Code 빌트인 Plan Mode**

- VS Code 확장 프로그램으로 Claude Code 설치 후 즉시 사용 가능
- `Shift+Tab` 두 번 → Plan Mode 진입. 디자인 승인 전까지 코드 작성 안 함

![image.png](attachment:1155f990-37fe-416f-879b-56b1eaee9e9c:image.png)

![image.png](attachment:c1e2675a-23c8-4c50-b244-2979a436fa49:image.png)

**방법 2. Superpowers의 `brainstorming` skill**

- GitHub: https://github.com/obra/superpowers (Jesse Vincent 제작, 476,000+ 설치)
- 작동 방식:
    - "철의 법칙(Iron Law)" — 디자인 승인 전에는 절대 코드 작성 안 함
    - **한 번에 한 질문씩** 소크라테스식으로 묻기 (객관식 우선)
    - 항상 2-3가지 대안 제시
    - YAGNI 원칙으로 불필요한 기능 제거
    - 최종적으로 design 문서 생성 → 승인 후에만 진행
- 설치:

    ```bash
    /plugin marketplace add obra/superpowers-marketplace
    /plugin install superpowers@superpowers-marketplace
    ```

- **오늘 쓸 핵심 흐름 3개**: `brainstorming` → `writing-plans` → `execute-plan`
    - `brainstorming` : 아이디어를 디자인 문서로 다듬기
    - `writing-plans` : 디자인을 2-5분짜리 작은 task로 분해, 각 task에 정확한 파일 경로/검증 단계 포함
    - `execute-plan` : 분해된 task를 순차 실행

![image.png](attachment:32f48a43-962b-4bea-9d3b-06ef2d9fa814:image.png)

![image.png](attachment:c2cc729d-bd7e-4c31-a34c-1ee1f3dace0d:image.png)

![image.png](attachment:855de2ba-ae22-46d3-927c-45687e92329f:image.png)

**방법 3. Antigravity Awesome Skills 패키지**

- GitHub: https://github.com/sickn33/antigravity-awesome-skills
- 22,000+ stars, 1,234개 skill 통합 (`brainstorming`, `architecture`, `debugging-strategies`, `doc-coauthoring`, `create-pr` 등)
- 설치: `npx antigravity-awesome-skills --claude`

> 💡 **5분 실습**: PLAN 워크시트 1장 채우기 (아래 시나리오 4종 중 1개 선택). 짝과 1분씩 검증.

### 2-2. 패션 업계 예시 시나리오 4종 (실습 선택지)

이 4종 중 1개를 골라서 핸즈온 ①에서 본인 대시보드를 만듭니다. 샘플 데이터는 모두 `./sample_data/` 아래에 미리 배포되어 있습니다.

| 시나리오 | 한 줄 설명 | 핵심 지표 (예시) | 데이터 파일 |
| --- | --- | --- | --- |
| **A. Tmall/Douyin 주간 매출** | 채널×카테고리 매출 흐름 점검 | 채널별 주간 매출, 전주 대비 증감, Top10 상품 | `./sample_data/weekly_sales_tmall_douyin.csv` |
| **B. 재고 회전** | 카테고리별 재고일수·회전율 모니터링 | 재고일수, 회전율, 시즌 잔량, ABC 분석 | `./sample_data/inventory_turnover.csv` |
| **C. 마케팅 KPI** | 캠페인·KOL ROI 점검 | ROAS, 채널 ROI, KOL 참여율, 노출 대비 전환 | `./sample_data/marketing_kpi.csv` |
| **D. VOC 인사이트** | Tmall/小红书 리뷰 키워드·감성 분석 | 키워드 Top, 감성 비율, 카테고리별 불만 Top | `./sample_data/voc_reviews.csv` |

> 💡 *본인 회사 데이터 가져온 사람도 환영. 없으면 위 4종 중 선택.*

---

### **3부. 핵심 Skill 빠른 투어 (15분)**

오늘 쓸 Skill을 콕 집어서:

### **3-1. 4대 Anthropic 공식 Skill (5분)**

| Skill | 용도 | 패션 업무 적용 |
| --- | --- | --- |
| **frontend-design** | "AI스럽지 않은" UI 만들기 — 277K+ 설치, 가장 중요 | 모든 대시보드 |
| **pptx** | 임원 보고용 PPT 자동 생성 (HTML→PPTX) | 주간/월간 보고 |
| **xlsx** | 매출/재고 엑셀 데이터 분석 + 차트 | 데이터 전처리 |
| **docx / pdf** | 텍스트 보고서 자동화 | 분석 리포트 |

### **3-2. "AI스럽지 않게" 만드는 비법 (7분) — 핵심 강조**

핵심 인사이트:

> *"모델은 디자인 결정의 통계적 중심값을 학습. → 보라색 그라데이션, Inter 폰트, 둥근 카드 = AI 시그니처"*

**탈출 전략:**

1. **frontend-design skill 강제 활성화** — `/frontend-design` 명령어
2. **레퍼런스 명시** — `awesome-design-md`, [skills.sh](https://skills.sh/) 활용
3. **브랜드 톤 명시** — "우리 회사는 미니멀 / 클래식 / 스트리트" 등
4. **Bad vs Good 예시 주입** — 회피할 패턴을 직접 알려주기

**프롬프트 템플릿 (현장 배포):**

```
[데이터 파일] 을 활용해서 [목적]을 위한 대시보드를 만들어줘.

스타일 가이드:
- AI 기본 스타일(보라 그라데이션, Inter, 둥근 카드) 절대 금지
- 레퍼런스: [구체적 사이트/스타일]
- 브랜드 톤: [미니멀/럭셔리/캐주얼]
- 폰트: Noto Sans KR + Noto Sans SC 병기 (한·중 모두 깨지지 않게)
- 컬러: [HEX 코드 1-2개]

frontend-design skill을 적극 활용해줘.
```

### **3-3. 옵션 Skill 소개 (3분)**

- **vercel/web-design-guidelines** — UI 품질 자동 검사 (133K+ 설치)
- **vercel/one-click-deploy** — 1초 배포
- **superpowers** — 멀티 에이전트 워크플로우 (40K+ stars, 고급자용)

---

### **4부. 핸즈온 ① — 대시보드 구현 (40분)**

**Phase 1. PLAN 작성 (5분)**

- 2-2의 시나리오 A/B/C/D 중 1개 선택 → 워크시트 5단계 채우기
- 짝과 1분씩 검증

**Phase 2. 데이터 확인 + 첫 프롬프트 (10분)**

- 샘플 데이터 폴더(`./sample_data/`)에서 시나리오별 CSV 확인
- 시나리오별 프롬프트 템플릿 (본인이 고른 1개만 사용):

**시나리오 A — Tmall/Douyin 주간 매출 대시보드**

```
./sample_data/weekly_sales_tmall_douyin.csv 를 분석해서
"마케팅팀장이 매주 월요일 채널 ROI를 점검하기 위한"
주간 매출 대시보드를 HTML 단일 파일로 만들어줘.

핵심 지표 (3-5개):
- 채널별(天猫/抖音) 주간 매출 합계
- 전주 대비 증감률
- Top10 상품 (매출 기준)
- 카테고리×채널 히트맵

차트: 막대 + 라인 + 히트맵
스타일: AI 기본 스타일 금지, 미니멀, Noto Sans KR + Noto Sans SC
frontend-design skill, xlsx skill 활용
```

**시나리오 B — 재고 회전 대시보드**

```
./sample_data/inventory_turnover.csv 를 분석해서
"공급팀장이 매주 시즌 잔량과 회전율을 점검하기 위한"
재고 회전 대시보드를 HTML 단일 파일로 만들어줘.

핵심 지표:
- 카테고리별 재고일수
- 회전율(Turnover)
- 시즌 잔량 Top
- ABC 분석 (매출 기여도 vs 재고 비중)

차트: 막대 + 산점도 + 표
스타일: 클래식, 데이터 밀도 높은 표 강조, Noto Sans KR + Noto Sans SC
frontend-design skill, xlsx skill 활용
```

**시나리오 C — 마케팅 KPI 대시보드**

```
./sample_data/marketing_kpi.csv 를 분석해서
"마케팅팀이 주간으로 캠페인·KOL ROI를 점검하기 위한"
KPI 대시보드를 HTML 단일 파일로 만들어줘.

핵심 지표:
- 캠페인별 ROAS
- 채널별 ROI (天猫/抖音/小红书/JD)
- KOL Top10 참여율
- 노출 → 클릭 → 전환 퍼널

차트: KPI 카드 + 퍼널 + 막대
스타일: 캠페인 컬러풀하지만 절제, Noto Sans KR + Noto Sans SC
frontend-design skill, xlsx skill 활용
```

**시나리오 D — VOC 인사이트 대시보드**

```
./sample_data/voc_reviews.csv 를 분석해서
"상품기획팀이 매주 Tmall/小红书 리뷰 흐름을 점검하기 위한"
VOC 인사이트 대시보드를 HTML 단일 파일로 만들어줘.

핵심 지표:
- 키워드 Top20 (워드클라우드 또는 막대)
- 긍정/부정 감성 비율
- 카테고리별 불만 Top
- 주차별 키워드 트렌드

차트: 워드클라우드 + 도넛 + 라인
스타일: 텍스트 위주, 가독성 우선, Noto Sans KR + Noto Sans SC
frontend-design skill, xlsx skill 활용
```

**Phase 3. 화면 구현 + 다듬기 (20분)**

- 강사는 코치 역할 — 막힘 케어 동선:
    - **5분차 막힘** → 강사 1:1 케어
    - **10분차 막힘** → 보조강사 투입
    - **15분차 막힘** → 빠른 완수자 2-3명을 "보조 코치"로 지정해서 서로 도움
- 5분마다 체크인:
    - 5분차: 데이터 잘 읽혔는지?
    - 10분차: 첫 화면 떴는지?
    - 15분차: 디자인 다듬기 단계
    - 20분차: 마무리

**Phase 4. 품질 체크 (5분)**

- vercel/web-design-guidelines 적용해서 자가 검사
- 색상/폰트/레이아웃 미세 조정
- **중문 폰트 깨짐 점검** — 한자 글자 빠짐(豆腐 박스), Tmall=天猫 / Douyin=抖音 / 小红书 / 京东 표기 정상 렌더링 확인

> 💡 *이 Phase에서 빠른 완수자 2-3명을 "보조 코치"로 만드는 게 핵심.*

---

### **5부. 핸즈온 ② — 보고서 PPT 자동 생성 (15분)**

**개념 설명 (3분)**

- Anthropic 공식 **pptx skill** 작동 원리
    - HTML→PPTX 변환 (디자인 그대로)
    - 회사 템플릿 .pptx 첨부 → 마스터 슬라이드/폰트 그대로 사용
    - 차트는 편집 가능한 네이티브 PPT 차트로 생성
- 데이터/대시보드와 연동되는 "End-to-end 보고서 자동화" 흐름

**실습 (10분)**

방금 만든 대시보드 → 임원 보고용 PPT로 자동 변환:

```
프롬프트:
방금 만든 대시보드의 핵심 인사이트를 가지고
임원 보고용 PowerPoint를 만들어줘.

구성:
1. 표지 (타이틀, 날짜)
2. Executive Summary (3 bullet)
3. 핵심 지표 (네이티브 차트)
4. 채널별 상세 분석 (天猫/抖音/小红书/JD)
5. 다음 액션 제안

요구사항:
- pptx skill 사용
- [회사 템플릿 .pptx 첨부] 의 마스터 슬라이드 따라가기
- 차트는 편집 가능한 네이티브 차트로
- 폰트: 한글 Noto Sans KR + 중문 Noto Sans SC 둘 다 임베드 (豆腐 박스 방지)
```

**고급 팁 (2분)**

- 매주 자동 업데이트하려면? → Subagent + Hook 조합 개념 소개
- "다음 주에 데이터만 바꾸면 똑같이 만들어주는" 패턴

> 💡 *중국 법인 맥락: 천猫/抖音 채널 데이터, 중문 폰트 임베드, 简体 표기 일관성 필수.*

---

### **6부. 배포 + 클로징 (10분)**

**6-1. 배포 옵션 (5분)**

| 방법 | 시간 | 용도 |
| --- | --- | --- |
| **로컬 HTML** | 1초 | 본인만 보기 |
| **사내 인트라넷** | 정책 따름 | 보안 환경 |
| **Vercel 1-click** | 30초 | URL 공유, 외부 협업 |

**Vercel 1-click 데모:**

- `/deploy` 명령 한 번 → 30초 안에 공유 URL
- "Claim URL"로 본인 Vercel 계정에 이전 가능

**6-2. 우수 작품 발표 (3분)**

- "가장 실무 가까움" / "가장 디자인 좋음" / "가장 창의적" 1명씩
- 박수 + 본인 입으로 "프롬프트 어떻게 짰나" 30초 공유

**6-3. 클로징 (2분)**

- 5단계 프레임워크 재확인
- 다음 단계 가이드:
    - **이번 주**: 본인 실제 업무 데이터로 1개 더 만들기
    - **이번 달**: 팀에 공유하고 피드백
    - **다음 분기**: Subagent + MCP로 자동화 확장
- Q&A 채널 안내

---
