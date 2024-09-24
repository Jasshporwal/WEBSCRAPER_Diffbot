import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_soup(url: str) -> BeautifulSoup:
    try:
        logger.info(f"Fetching URL: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        logger.info(f"Successfully fetched URL: {url}")
        return BeautifulSoup(response.content, "html.parser")
    except requests.RequestException as e:
        logger.error(f"Error fetching URL {url}: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Error fetching URL: {str(e)}")
