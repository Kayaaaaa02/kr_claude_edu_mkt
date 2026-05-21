"""
단일 이미지 스타일 변환 스크립트
- 특정 이미지 하나만 선택하여 변환할 때 사용합니다.
- 사용법: python gemini_image_edit_single.py "이미지\박봉섭 이사님.png"
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# .env 파일에서 환경변수 로드
load_dotenv(Path(__file__).parent / ".env")

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("google-genai 패키지가 설치되어 있지 않습니다.")
    print("설치 명령어: pip install google-genai")
    sys.exit(1)

# ─── 설정 ───────────────────────────────────────────────
API_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL_ID = "gemini-3-pro-image-preview"
IMAGE_DIR = Path(__file__).parent / "이미지"
OUTPUT_DIR = Path(__file__).parent / "이미지_결과"
REFERENCE_IMAGE = IMAGE_DIR / "송예린 대리님.png"

STYLE_PROMPT = """두 번째 이미지의 인물 사진을 보정해주세요.

[최우선 규칙 - 절대 변경 금지]
- 인물의 얼굴형, 눈, 코, 입, 이마, 턱선, 광대뼈 등 모든 얼굴 특징을 원본과 100% 동일하게 유지
- 피부색, 머리카락 색상, 머리 스타일을 원본 그대로 유지
- 체형, 어깨 너비를 원본 그대로 유지

[변경할 부분 - 배경과 조명만 수정]
- 배경만 깔끔한 흰색으로 교체
- 조명을 부드러운 스튜디오 조명처럼 보정
- 화질이 낮으면 선명하게 개선 (업스케일링)
- 전체 사진의 크기는 3:4 비율로 조정
- 정장을 착용한 사람의 이미지는 깔끔한 흰색 반팔티로 교체
- 몸은 측면을 바라보고 자연스럽게 고개는 정면을 바라보게 포즈 변경

이것은 포토샵의 배경 제거 + 흰색 배경 합성과 같은 작업입니다.
인물 자체를 새로 그리거나 변형하지 마세요. 원본 사진의 인물을 그대로 두고 배경과 조명만 바꿔주세요.
"""


def main():
    if len(sys.argv) < 2:
        print("사용법: python gemini_image_edit_single.py <이미지 경로>")
        print('예시: python gemini_image_edit_single.py "이미지\\박봉섭 이사님.png"')
        sys.exit(1)

    if not API_KEY:
        print("오류: GEMINI_API_KEY 환경변수를 설정해주세요.")
        print("  set GEMINI_API_KEY=your-api-key-here")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.is_absolute():
        input_path = Path(__file__).parent / input_path

    if not input_path.exists():
        print(f"오류: 파일을 찾을 수 없습니다: {input_path}")
        sys.exit(1)

    # 커스텀 프롬프트 (선택)
    custom_prompt = sys.argv[2] if len(sys.argv) > 2 else None

    client = genai.Client(api_key=API_KEY)

    print(f"원본 이미지: {input_path.name}")
    print(f"참조 이미지: {REFERENCE_IMAGE.name}")
    print("변환 중...")

    ref_bytes = REFERENCE_IMAGE.read_bytes()
    img_bytes = input_path.read_bytes()

    prompt = custom_prompt or (
        f"참조 이미지의 스타일(배경, 조명, 톤)을 참고하여 "
        f"두 번째 이미지를 같은 스타일로 변환해주세요.\n\n{STYLE_PROMPT}"
    )

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[
            types.Content(
                parts=[
                    types.Part.from_text(text=prompt),
                    types.Part.from_bytes(data=ref_bytes, mime_type="image/png"),
                    types.Part.from_bytes(data=img_bytes, mime_type="image/png"),
                ]
            )
        ],
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
        ),
    )

    # 결과 저장
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / input_path.name

    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            output_path.write_bytes(part.inline_data.data)
            print(f"저장 완료: {output_path}")
            return

        if part.text:
            print(f"응답 텍스트: {part.text[:300]}")

    print("경고: 이미지가 응답에 포함되지 않았습니다.")


if __name__ == "__main__":
    main()
