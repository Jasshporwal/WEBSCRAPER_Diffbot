from utils import get_soup
from schemas.models import ImageData
from urllib.parse import urljoin

def extract_images(url: str) -> list[ImageData]:
    soup = get_soup(url)
    images = []

    for img in soup.find_all('img'):
        src = img.get('src')
        if src and not src.startswith('http'):
            src = urljoin(url, src)
        if src:  # Ensure src is valid before appending
            alt = img.get('alt')  # Get the alt attribute
            images.append(ImageData(url=src, alt=alt))

    return images
