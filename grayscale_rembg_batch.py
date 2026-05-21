"""
이미지_결과 폴더의 모든 이미지를 흑백 변환 + 배경 제거하는 일괄 처리 스크립트
"""

import argparse
import sys
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance
from rembg import remove
import io


def process_image(image_path, output_path, contrast=1.2, brightness=1.05, sharpness=1.1):
    print(f"  처리 중: {image_path.name}")
    img_bytes = image_path.read_bytes()
    result_bytes = remove(img_bytes)
    img = Image.open(io.BytesIO(result_bytes)).convert("RGBA")
    r, g, b, a = img.split()
    gray = ImageOps.grayscale(img.convert("RGB"))
    img = Image.merge("RGBA", (gray, gray, gray, a))
    rgb = img.convert("RGB")
    rgb = ImageEnhance.Contrast(rgb).enhance(contrast)
    rgb = ImageEnhance.Brightness(rgb).enhance(brightness)
    rgb = ImageEnhance.Sharpness(rgb).enhance(sharpness)
    r, g, b = rgb.split()
    img = Image.merge("RGBA", (r, g, b, a))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path, "PNG")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", default="이미지_결과")
    parser.add_argument("--output-dir", default="이미지_흑백")
    args = parser.parse_args()

    input_dir = Path(__file__).parent / args.input_dir
    output_dir = Path(__file__).parent / args.output_dir

    files = sorted(input_dir.glob("*.png"))
    if not files:
        print("처리할 이미지가 없습니다.")
        sys.exit(1)

    print(f"총 {len(files)}장 처리 시작\n")
    success = 0
    for f in files:
        try:
            process_image(f, output_dir / f.name)
            success += 1
        except Exception as e:
            print(f"  오류: {f.name} - {e}")

    print(f"\n완료: {success}/{len(files)}장")
    print(f"결과 폴더: {output_dir}")


if __name__ == "__main__":
    main()
