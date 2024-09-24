from utils import get_soup
from schemas.models import ImageData
from urllib.parse import urljoin
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_images(url: str) -> list[ImageData]:
    soup = get_soup(url)
    base_url = url
    
    images = []
    for img in soup.find_all('img'):
        src = img.get('src')
        alt = img.get('alt')
        
        if src:
            try:
                # Convert relative URLs to absolute URLs
                full_url = urljoin(base_url, src)
                image_data = ImageData(url=full_url, alt=alt)
                images.append(image_data)
                logger.info(f"Added image: {image_data}")
            except Exception as e:
                logger.error(f"Error processing image {src}: {str(e)}")
        else:
            logger.warning(f"Found img tag without src attribute: {img}")
    
    logger.info(f"Extracted {len(images)} images from {url}")
    return images