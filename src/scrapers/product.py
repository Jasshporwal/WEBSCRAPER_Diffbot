import re
from utils import get_soup
from schemas.models import ProductData

def extract_product(url: str) -> ProductData:
    soup = get_soup(url)
    
    name = soup.find('h1').text.strip() if soup.find('h1') else "No product name found"
    price = soup.find('span', {'class': re.compile('price')})
    price = price.text.strip() if price else None
    description = soup.find('div', {'class': re.compile('description')})
    description = description.text.strip() if description else None

    return ProductData(name=name, price=price, description=description)