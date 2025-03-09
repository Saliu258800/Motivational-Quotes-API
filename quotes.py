from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

quotes = [
    {"text": "The only way to do a great work is to love what you do",
    "author": "Steve Jobs"},

    {"text": "Success is not final, failure is not fatal: it is the courage to",
    "author": "Winston Churchill"},

    {"text": "Believe you can, and you are halfway there",
    "author": "Theodore Roosevelt"},

    {"text": "Talk is cheap. Show me the code",
    "author": "Linus Torvalds"},

    {"text": "First, solve the problem. Then, write the code",
    "author": "John Johnson"},

    {"text": "the function of a good software is to make the complex appear simple",
    "author": "Grady Booch"},

    {"text": "It does not matter how slowly you go as long as you do not stop",
    "author": "Confucius"}

    ] #quotes stored

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["GET"],
    allow_headers = ["*"],
)

@app.get("/api/quotes") # send all quotes
async def get_quotes():
    data = {"data": {"quotes": quotes}}
    return JSONResponse(content=data, status_code=200)

@app.get("/api/quotes/text")
async def get_individual_text():
    for _ in range(len(quotes)):
        for text in quotes[_].items():
            data = {"data": {"authors quote": text}}
            return JSONResponse(content=data, status_code=200)

@app.get("/api/quotes/{quote_index}") # allows to get a specific quote from the quotes storage
async def get_speific_quote(quote_index:int=Path(...)):
    quote_index = quote_index - 1
    if quote_index < 0 or quote_index >= len(quotes):
        raise HTTPException(status_code=404, detail="quote unavailable")
    if quote_index >= 0 < len(quotes):
        data = {"data": {"quote": quotes[quote_index]}}
        return JSONResponse(content=data, status_code=200)


if __name__ == "__main__":
    print("server functioning successfully")