from utils import get_soup
from schemas.models import GeneralData

def extract_general(url: str) -> GeneralData:
    soup = get_soup(url)
    
    title = soup.title.string if soup.title else "No title found"
    meta_description = soup.find('meta', {'name': 'description'})
    meta_description = meta_description['content'] if meta_description else None
    h1_tags = [h1.text for h1 in soup.find_all('h1')]
    links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('http')]

    return GeneralData(title=title, meta_description=meta_description, h1_tags=h1_tags, links=links)