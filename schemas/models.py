from typing import List, Optional
from pydantic import BaseModel, HttpUrl
from datetime import datetime

class ArticleData(BaseModel):
    title: str
    content: str
    author: Optional[str] = None
    date: Optional[str] = None

class ProductData(BaseModel):
    name: str
    price: Optional[str] = None
    description: Optional[str] = None

class ImageData(BaseModel):
    url: str
    alt: Optional[str] = None

class GeneralData(BaseModel):
    title: str
    meta_description: Optional[str] = None
    h1_tags: List[str]
    links: List[HttpUrl]

class EventData(BaseModel):
    name: str
    date: Optional[datetime] = None
    location: Optional[str] = None
    description: Optional[str] = None
    organizer: Optional[str] = None
    url: str