from utils import get_soup
from schemas.models import ArticleData


def extract_article(url: str) -> ArticleData:
    soup = get_soup(url)

    title = soup.find("h1").text.strip() if soup.find("h1") else "No title found"
    content = " ".join([p.text for p in soup.find_all("p")])
    author = soup.find("meta", {"name": "author"})
    author = author["content"] if author else None
    date = soup.find("meta", {"property": "article:published_time"})
    date = date["content"] if date else None

    return ArticleData(title=title, content=content, author=author, date=date)
