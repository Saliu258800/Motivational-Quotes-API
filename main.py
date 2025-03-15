from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from random import choice

app = FastAPI()

quotes = [
    {"text": "The only way to do a great work is to love what you do",
    "author": "Steve Jobs"},

    {"text": "Success is not final, failure is not fatal: it is the courage to continue that counts",
    "author": "Winston Churchill"},

    {"text": "Believe you can, and you are halfway there",
    "author": "Theodore Roosevelt"},

    {"text": "Talk is cheap. Show me the code",
    "author": "Linus Torvalds"},

    {"text": "First, solve the problem. Then, write the code",
    "author": "John Johnson"},

    {"text": "The function of a good software is to make the complex appear simple",
    "author": "Grady Booch"},

    {"text": "It does not matter how slowly you go as long as you do not stop",
    "author": "Confucius"},

    {"text": "Do what you can, with what you have, where you are",
    "author": "Theodore Roosevelt"},

    {"text": "Opportunities don't happen. You create them",
    "author": "Chris Grosser"},

    {"text": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand",
    "author": "Martin Fowler"},

    {"text": "Simplicity is the soul of efficiency",
    "author": "Austin Freeman"},

    {"text": "Code is like humor. When you have to explain it, it's bad",
    "author": "Cory House"},

    {"text": "The best way to predict the future is to create it",
    "author": "Peter Drucker"},

    {"text": "A journey of a thousand miles begins with a single step",
    "author": "Lao Tzu"},

    {"text": "Happiness depends on ourselves", 
    "author": "Aristotle"},

    {"text": "Knowledge is power",
    "author": "Francis Bacon"},

    {"text": "If you want to go fast, go alone. If you want go far, go together",
    "author": "African Proverb"}

    ] #quotes stored

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["GET"],
    allow_headers = ["*"],
)

templates = Jinja2Templates(directory="templates")

app.mount("/styles", StaticFiles(directory="static/styles"),
    name="styles")

app.mount("/scripts", StaticFiles(directory="static/scripts"),
    name="scripts")

app.mount("/images", StaticFiles(directory="static/images"),
    name="images")


@app.get("/api/quotes/visual", response_class=HTMLResponse)
async def display_quotes(request: Request):
    return templates.TemplateResponse("index.html",
{"request": request})

@app.get("/api/quotes/sayings")
def get_authors_sayings():
    sayings = [{"text": quote["text"]} for quote in quotes]
    data = {"data": {"sayings": sayings}}
    return JSONResponse(content=data, status_code=200)

@app.get("/api/random/{format}", response_class=HTMLResponse)
async def generate_random_quote(request:Request, format:str)->HTMLResponse:
    class Quotes:
        def random_quote(self)->dict:
            selected_quote = choice(quotes)
            return selected_quote

        def html_content(self)->HTMLResponse:
            _html_content = ''
            selected_quote = self.random_quote()
            text = selected_quote["text"]
            author = selected_quote["author"]
            _html_content = f''' 
                                    <h4>
                                        <img src="/images/quotes.svg" width="18" height="18">
                                        {text} <i>by {author}</i>
                                    </h4>
                             '''
            return _html_content

    quote = Quotes()

    if format.lower() == "json":
        content = {"data": {"random quote": quote.random_quote()}}
        return JSONResponse(content=content, status_code=200)
    if format.lower() == "html":
        return HTMLResponse(content=quote.html_content(), status_code=200)
    else:
        raise HTTPException(status_code=404, detail=f"Invalid format: '/{format}'. request must be '/html' or '/json' to process")

@app.get("/api/quotes/{format}") # send all quotes
async def get_quotes(format:str)->HTMLResponse:
    if format.lower() == "json":
        data = {"data": {"quotes": quotes}}
        return JSONResponse(content=data, status_code=200)
    if format.lower() == "html":
        html_content = '''<div class="quotes">
                          <h3>All Quotes</h3>
                          <ul>'''

        for quote in quotes:
            text = quote["text"]
            author = quote["author"]
            html_content += f'''<li>
                                <img src="/images/list-item.svg" width="16" height="16">
                                {text} by <span>{author}</span>
                            </li>'''
        html_content += '''</ul>
                          </div>
                          <div class="text-center custom-div">
                                <button class="btn btn-success" hx-get="/api/hide"
                                    hx-target="#all-quotes" hx-swap="innerHTML swap:0.5s">
                                        Hide
                                </button>
                            </div>
                        '''
        return HTMLResponse(content=html_content, status_code=200)

@app.get("/api/quotes/authors/{format}", response_class=HTMLResponse)
async def get_authors(format:str):
    authors = [{"author": quote["author"]} for quote in quotes]
    data = {"data": {"authors": authors}}
    if format.lower() == "json":
        return JSONResponse(content=data, status_code=200)
    if format.lower() == "html":
        _html_content = "".join(f'''
                                    <li>{quote["author"]}

                                    ''' for quote in quotes)
        container = f'''<ul class="authors-container">
                            <button hx-get='/api/hide' hx-target="#authors-receiver" hx-swap="innerHTML swap:0.5s">&times</button>
                            {_html_content}
                        </ul>'''
        return HTMLResponse(content=container, status_code=200)
    else:
        raise HTTPException(status_code=404, detail=f"Invalid format: '/{format}'. request must be '/html' or '/json' to process")

@app.get("/api/hide")
def hide_html_content():
    html_content = ""
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/api/quotes/{quote_index}") # allows to get a specific quote from the quotes storage
async def get_speific_quote(quote_index:int):
    quote_index = quote_index - 1
    if quote_index < 0 or quote_index >= len(quotes):
        raise HTTPException(status_code=404, detail="quote unavailable") #if index is out of range
    if quote_index >= 0 < len(quotes):
        data = {"data": {"quote": quotes[quote_index]}}
        return JSONResponse(content=data, status_code=200) # if index is in range

if __name__ == "__main__":
    print("server functioning successfully")