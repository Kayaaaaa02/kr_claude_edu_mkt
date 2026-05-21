"""
Gemini API를 활용한 프로필 이미지 스타일 변환 스크립트
- 참조 이미지(송예린 대리님.png) 스타일로 다른 이미지들을 변환합니다.
- 모델: gemini-2.0-flash-exp (이미지 생성/편집 지원)
"""

import os
import sys
import base64
import glob
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
MODEL_ID = "gemini-3-pro-image-preview"  # 이미지 생성/편집 지원 모델
IMAGE_DIR = Path(__file__).parent / "이미지"
OUTPUT_DIR = Path(__file__).parent / "이미지_결과"
REFERENCE_IMAGE = IMAGE_DIR / "송예린 대리님.png"

# 스타일 변환 프롬프트
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


def load_image_as_bytes(image_path: Path) -> bytes:
    """이미지 파일을 바이트로 읽기"""
    with open(image_path, "rb") as f:
        return f.read()


def save_image(image_data: bytes, output_path: Path) -> None:
    """이미지 데이터를 파일로 저장"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(image_data)
    print(f"  저장 완료: {output_path}")


def edit_single_image(client, image_path: Path, output_path: Path) -> bool:
    """단일 이미지를 스타일 변환"""
    print(f"\n처리 중: {image_path.name}")

    try:
        # 원본 이미지 로드
        image_bytes = load_image_as_bytes(image_path)

        # 참조 이미지 로드
        ref_bytes = load_image_as_bytes(REFERENCE_IMAGE)

        # Gemini API 호출 - 참조 이미지 + 원본 이미지 + 프롬프트
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[
                types.Content(
                    parts=[
                        types.Part.from_text(
                            text=f"참조 이미지의 스타일(배경, 조명, 톤)을 참고하여 "
                            f"두 번째 이미지를 같은 스타일로 변환해주세요.\n\n{STYLE_PROMPT}"
                        ),
                        types.Part.from_bytes(data=ref_bytes, mime_type="image/png"),
                        types.Part.from_bytes(data=image_bytes, mime_type="image/png"),
                    ]
                )
            ],
            config=types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"],
            ),
        )

        # 응답에서 이미지 추출
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                save_image(part.inline_data.data, output_path)
                return True

        print(f"  경고: {image_path.name} - 이미지가 응답에 포함되지 않았습니다.")
        if response.candidates[0].content.parts:
            for part in response.candidates[0].content.parts:
                if part.text:
                    print(f"  응답 텍스트: {part.text[:200]}")
        return False

    except Exception as e:
        print(f"  오류: {image_path.name} - {e}")
        return False


def main():
    # API 키 확인
    if not API_KEY:
        print("오류: GEMINI_API_KEY 환경변수를 설정해주세요.")
        print("  Windows: set GEMINI_API_KEY=your-api-key-here")
        print("  또는 스크립트 상단의 API_KEY 변수에 직접 입력")
        sys.exit(1)

    # 참조 이미지 확인
    if not REFERENCE_IMAGE.exists():
        print(f"오류: 참조 이미지를 찾을 수 없습니다: {REFERENCE_IMAGE}")
        sys.exit(1)

    # Gemini 클라이언트 초기화
    client = genai.Client(api_key=API_KEY)

    # 처리할 이미지 목록 (참조 이미지 제외)
    image_files = sorted(IMAGE_DIR.glob("*.png"))
    target_files = [f for f in image_files if f.name != REFERENCE_IMAGE.name]

    if not target_files:
        print("처리할 이미지가 없습니다.")
        sys.exit(0)

    print(f"참조 이미지: {REFERENCE_IMAGE.name}")
    print(f"처리 대상: {len(target_files)}개 이미지")
    print(f"출력 폴더: {OUTPUT_DIR}")
    print("=" * 50)

    # 전체 이미지 처리
    success_count = 0
    fail_count = 0

    for image_path in target_files:
        output_path = OUTPUT_DIR / image_path.name
        if edit_single_image(client, image_path, output_path):
            success_count += 1
        else:
            fail_count += 1

    # 결과 요약
    print("\n" + "=" * 50)
    print(f"처리 완료: 성공 {success_count}개 / 실패 {fail_count}개")
    print(f"결과 폴더: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
