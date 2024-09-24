from utils import get_soup
from schemas.models import ImageData

def extract_images(url: str) -> list[ImageData]:
    soup = get_soup(url)
    
    images = []
    for img in soup.find_all('img'):
        src = img.get('src')
        if src and src.startswith('http'):
            images.append(ImageData(url=src, alt=img.get('alt')))
    
    return images