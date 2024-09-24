# Web Scraper API

This project is a simple web scraping API built with FastAPI. It provides endpoints for extracting article data, product information, images, and general page data from websites.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/Jasshporwal/WEBSCRAPER_Diffbot.git
   cd WEBSCRAPER_Diffbot
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   uvicorn main:app --reload
   ```

The server will start running on `http://localhost:8000`.

## API Endpoints

- `/article?url=<url>`: Extract article data
- `/product?url=<url>`: Extract product data
- `/images?url=<url>`: Extract images from a page
- `/general?url=<url>`: Extract general page data



