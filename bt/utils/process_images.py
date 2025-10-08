from pathlib import Path
from PIL import Image
from os import listdir, makedirs, remove
from bt.settings import ROOT_DIR, COVER_ART_FOLDER
from bt.utils.logging import logging

output_folder = COVER_ART_FOLDER / "cover_art_post"


def resize_image(cover_art: Path, width=300, height=450) -> Path:
    makedirs(output_folder, exist_ok=True)
    output_path = output_folder / cover_art.name
    if Path(output_path).exists():
        return output_path.relative_to(ROOT_DIR)

    img = Image.open(cover_art)
    original_width, original_height = img.size

    scale_w = width / original_width
    scale_h = height / original_height
    scale = max(scale_w, scale_h)

    new_size = (int(original_width * scale), int(original_height * scale))
    img = img.resize(new_size)

    crop = (width, height)
    left = round((img.size[0] - crop[0]) / 2)
    top = round((img.size[1] - crop[1]) / 2)
    img = img.crop((left, top, crop[0] + left, crop[1] + top))

    logging.info(f"Resized image size: {img.size}")
    img.save(output_path)

    _clean_post_folder(COVER_ART_FOLDER, output_folder)

    return output_path.relative_to(ROOT_DIR)


def _clean_post_folder(trusted_dir: Path, untrusted_dir: Path):
    active_cover_art = listdir(trusted_dir)

    for item in listdir(untrusted_dir):
        if item not in active_cover_art:
            logging.warning(f"Removed {item}")
            remove(Path(untrusted_dir) / item)


if __name__ == "__main__":
    _clean_post_folder(COVER_ART_FOLDER, output_folder)
