import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException

def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch the URL")
    return BeautifulSoup(response.content, 'html.parser')