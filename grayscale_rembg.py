"""
단일 이미지 흑백 변환 + 배경 제거 스크립트
사용법: python grayscale_rembg.py "이미지_결과/김협 담당님.png"
옵션: --output-dir, --contrast, --brightness, --sharpness
"""

import argparse
import sys
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance
from rembg import remove
import io


def process_image(
    image_path: Path,
    output_path: Path,
    contrast: float = 1.2,
    brightness: float = 1.05,
    sharpness: float = 1.1,
) -> None:
    """배경 제거 + 흑백 변환 + 톤 보정"""
    print(f"처리 중: {image_path.name}")

    # 1. 배경 제거
    print("  배경 제거 중...")
    img_bytes = image_path.read_bytes()
    result_bytes = remove(img_bytes)
    img = Image.open(io.BytesIO(result_bytes)).convert("RGBA")

    # 2. 흑백 변환 (알파 채널 유지)
    print("  흑백 변환 중...")
    r, g, b, a = img.split()
    gray = ImageOps.grayscale(img.convert("RGB"))
    img = Image.merge("RGBA", (gray, gray, gray, a))

    # 3. 톤 보정 (RGB 채널만, 알파 유지)
    print(f"  톤 보정 중... (대비={contrast}, 밝기={brightness}, 선명도={sharpness})")
    rgb = img.convert("RGB")
    rgb = ImageEnhance.Contrast(rgb).enhance(contrast)
    rgb = ImageEnhance.Brightness(rgb).enhance(brightness)
    rgb = ImageEnhance.Sharpness(rgb).enhance(sharpness)
    r, g, b = rgb.split()
    img = Image.merge("RGBA", (r, g, b, a))

    # 4. 저장
    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path, "PNG")
    print(f"  저장 완료: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="이미지 흑백 변환 + 배경 제거")
    parser.add_argument("image", help="입력 이미지 경로")
    parser.add_argument("--output-dir", default="이미지_흑백", help="출력 폴더 (기본: 이미지_흑백)")
    parser.add_argument("--contrast", type=float, default=1.2, help="대비 (기본: 1.2)")
    parser.add_argument("--brightness", type=float, default=1.05, help="밝기 (기본: 1.05)")
    parser.add_argument("--sharpness", type=float, default=1.1, help="선명도 (기본: 1.1)")
    args = parser.parse_args()

    input_path = Path(args.image)
    if not input_path.is_absolute():
        input_path = Path(__file__).parent / input_path

    if not input_path.exists():
        print(f"오류: 파일을 찾을 수 없습니다: {input_path}")
        sys.exit(1)

    output_dir = Path(__file__).parent / args.output_dir
    output_path = output_dir / input_path.name

    process_image(input_path, output_path, args.contrast, args.brightness, args.sharpness)


if __name__ == "__main__":
    main()
