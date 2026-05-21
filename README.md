# F&F CN · Claude Code Workshop

F&F 중국법인 PROCESS AX TEAM 운영 Claude Code 교육자료. 120분, 7개 챕터로 '나만의 대시보드'를 직접 만들어보는 워크숍.

## 진입

브라우저로 `cn_claude_edu.html` 또는 사이트 루트(`/`) 방문 시 자동 리다이렉트.

## 콘텐츠 구성

| 챕터 | 시간 | 내용 |
| --- | --- | --- |
| 00 Opening | 0–10' | 첫 실행 점검 + 결과물 데모 |
| 01 Use Case | 10–25' | F&F 한국 사례(KARINA·FnCo) + 5대 메커니즘 |
| 02 PLAN | 25–40' | 5단계 워크시트 + 시나리오 + 예시 프롬프트 |
| 03 Skill 빠른 투어 | 40–55' | 4대 공식 Skill + AI 시그니처 회피 4가지 전략 + Apple.com 디자인 시스템 |
| 04 Hands-on ① | 55–95' | 데이터 → 대시보드 구현 |
| 05 Hands-on ② | 95–110' | 배포 + 보고서 PPT 자동 생성 |
| 06 Deploy | 110–120' | DCS AI MCP로 사내 배포 |

## 실습 데이터

`MLB_China_LastWeek_Channel_Sales_2026wk19_EN.xlsx` — Tmall / Douyin 주간 매출 샘플.
페이지 상단의 **실습자료 받기** 버튼 또는 footer 링크로 다운로드.

## 정적 자산

- `KARINA_EDITION_VOL2_GLMKT_UNIFIED AI DASHBOARD (1)/` — KARINA EDITION VOL.2 판매전략 분석
- `fnco_if_ceo-main/` — FnCo IF CEO Report
- `planmode/` — Plan Mode 화면 흐름 (VS Code / 터미널)
- `gpt images/` — 5가지 메커니즘 일러스트 (Skills · Plugins · Memory · MCP · Hooks)
- `images_fin/` — 기본 AI 디자인 예시
- `awesome_design/` — awesome-design-md 갤러리
- `ppt/` — PPT 자동 생성 결과
- `deploy/` — DCS AI 배포 화면

## 배포

Vercel 정적 호스팅 권장. 별도 빌드 단계 없음 — 정적 파일 그대로 배포.

```bash
# Vercel CLI로 즉시 배포
vercel deploy --prod
```

또는 GitHub repo를 Vercel에 연결하면 자동 배포.

## 운영

- 작성: F&F 중국법인 PROCESS AX TEAM
- 문의: hyoeun28@fnfcorp.com
