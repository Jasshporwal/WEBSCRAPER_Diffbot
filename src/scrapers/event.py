from typing import Optional
from utils import get_soup
from schemas.models import EventData
from datetime import datetime
import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_event(url: str) -> EventData:
    soup = get_soup(url)
    
    name = extract_name(soup)
    date = extract_date(soup)
    location = extract_location(soup)
    description = extract_description(soup)
    organizer = extract_organizer(soup)
    
    event = EventData(
        name=name,
        date=date,
        location=location,
        description=description,
        organizer=organizer,
        url=url
    )
    
    logger.info(f"Extracted event: {event}")
    return event

def extract_name(soup: BeautifulSoup) -> str:
    name = soup.find('h1')
    return name.text.strip() if name else "Event name not found"

def extract_date(soup: BeautifulSoup) -> Optional[datetime]:
    date_tag = soup.find('time') or soup.find(class_=['date', 'event-date'])
    if date_tag and date_tag.get('datetime'):
        try:
            return datetime.fromisoformat(date_tag['datetime'])
        except ValueError:
            logger.warning(f"Could not parse date: {date_tag['datetime']}")
    return None

def extract_location(soup: BeautifulSoup) -> Optional[str]:
    location = soup.find(class_=['location', 'event-location', 'venue'])
    return location.text.strip() if location else None

def extract_description(soup: BeautifulSoup) -> Optional[str]:
    description = soup.find(class_=['description', 'event-description'])
    return description.text.strip() if description else None

def extract_organizer(soup: BeautifulSoup) -> Optional[str]:
    organizer = soup.find(class_=['organizer', 'event-organizer'])
    return organizer.text.strip() if organizer else None