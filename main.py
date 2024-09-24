from fastapi import FastAPI
from src.scrapers import article, product, image, general, event
from schemas.models import ArticleData, ProductData, ImageData, GeneralData, EventData
from pydantic import HttpUrl

app = FastAPI()


@app.get("/article", response_model=ArticleData)
async def extract_article(url: HttpUrl):
    return article.extract_article(url)


@app.get("/product", response_model=ProductData)
async def extract_product(url: HttpUrl):
    return product.extract_product(url)


@app.get("/images", response_model=ImageData)
async def extract_images(url: HttpUrl):
    return image.extract_images(url)


@app.get("/general", response_model=GeneralData)
async def extract_general(url: HttpUrl):
    return general.extract_general(url)


@app.get("/event", response_model=EventData)
async def extract_event(url: HttpUrl):
    return event.extract_event(url)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
