"""
지정된 인물만 이미지_결과2 폴더에 변환하는 스크립트
인물 변형 절대 금지 - 배경/조명만 수정
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("google-genai 패키지가 설치되어 있지 않습니다.")
    sys.exit(1)

API_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL_ID = "gemini-3-pro-image-preview"
IMAGE_DIR = Path(__file__).parent / "이미지"
OUTPUT_DIR = Path(__file__).parent / "이미지_결과2"
REFERENCE_IMAGE = IMAGE_DIR / "송예린 대리님.png"

# 변환 대상 목록: (원본 파일명, 출력 파일명)
TARGETS = [
    ("국준호 차장님.png", "국준호 차장님2.png"),
    ("김수현 과장님.png", "김수현 과장님.png"),
    ("김협 담당님.png", "김협 담당님.png"),
    ("김효은 대리님.png", "김효은 대리님.png"),
    ("송예린 대리님.png", "송예린 대리님.png"),
    ("정진주 과장님.png", "정진주 과장님.png"),
    ("서해니 과장님.png", "서해니 과장님.png"),
]

STYLE_PROMPT = """두 번째 이미지의 인물 사진을 보정해주세요.

[최우선 규칙 - 절대 변경 금지 - 이 규칙을 어기면 안 됩니다]
- 인물의 얼굴을 절대 변경하지 마세요: 얼굴형, 눈 모양, 눈 크기, 코, 입, 이마, 턱선, 광대뼈, 쌍꺼풀 유무
- 인물의 피부색을 절대 변경하지 마세요
- 인물의 머리카락 색상, 길이, 스타일을 절대 변경하지 마세요
- 인물의 체형, 어깨 너비를 절대 변경하지 마세요
- 인물의 표정을 절대 변경하지 마세요
- 인물의 포즈를 절대 변경하지 마세요
- 인물을 새로 그리지 마세요. 원본 픽셀을 최대한 보존하세요.

[변경할 부분 - 이것만 수정하세요]
- 배경만 깔끔한 흰색으로 교체
- 조명을 부드러운 스튜디오 조명처럼 자연스럽게 보정
- 화질이 낮으면 선명하게 업스케일링
- 전체 사진의 비율은 3:4로 조정

이 작업은 포토샵에서 배경만 제거하고 흰색으로 교체하는 것과 동일합니다.
인물 자체는 한 픽셀도 변형하지 마세요.
"""


def main():
    if not API_KEY:
        print("오류: GEMINI_API_KEY 환경변수를 설정해주세요.")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    client = genai.Client(api_key=API_KEY)
    ref_bytes = REFERENCE_IMAGE.read_bytes()

    print(f"총 {len(TARGETS)}장 처리 시작")
    print("=" * 50)

    success = 0
    fail = 0

    for src_name, out_name in TARGETS:
        src_path = IMAGE_DIR / src_name
        out_path = OUTPUT_DIR / out_name

        if not src_path.exists():
            print(f"\n건너뜀: {src_name} (파일 없음)")
            fail += 1
            continue

        print(f"\n처리 중: {src_name} → {out_name}")
        img_bytes = src_path.read_bytes()

        try:
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=[
                    types.Content(
                        parts=[
                            types.Part.from_text(
                                text=f"참조 이미지의 스타일(배경, 조명)만 참고하세요. "
                                f"두 번째 이미지의 인물은 절대 변형하지 마세요.\n\n{STYLE_PROMPT}"
                            ),
                            types.Part.from_bytes(data=ref_bytes, mime_type="image/png"),
                            types.Part.from_bytes(data=img_bytes, mime_type="image/png"),
                        ]
                    )
                ],
                config=types.GenerateContentConfig(
                    response_modalities=["TEXT", "IMAGE"],
                ),
            )

            saved = False
            for part in response.candidates[0].content.parts:
                if part.inline_data is not None:
                    out_path.write_bytes(part.inline_data.data)
                    print(f"  저장 완료: {out_path}")
                    success += 1
                    saved = True
                    break
            if not saved:
                print(f"  경고: 이미지 응답 없음")
                fail += 1

        except Exception as e:
            print(f"  오류: {e}")
            fail += 1

    print("\n" + "=" * 50)
    print(f"완료: 성공 {success}개 / 실패 {fail}개")
    print(f"결과 폴더: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
