Quotes API Documentation

Base URL: https://api-name.com/api

ENDPOINTS

	1. Get all Quotes
	URL: /quotes
	Method: GET
	Description: Returns all quotes available

	Example(Request): GET /quotes
			(Response): 
						{
						  "data": {
						    "quotes": [
						      {
						        "text": "The only way to do a great work is to love what you do",
						        "author": "Steve Jobs"
						      },
						      {
						        "text": "Success is not final, failure is not fatal: it is the courage to",
						        "author": "Winston Churchill"
						      },
						      {
						        "text": "Believe you can, and you are halfway there",
						        "author": "Theodore Roosevelt"
						      },
						      {
						        "text": "Talk is cheap. Show me the code",
						        "author": "Linus Torvalds"
						      },
						      {"All other quotes available"}
						    ]
						  }
						}


	2. Get a specific Quote by index
	URL: /quotes/{id}
	Method: GET
	Description: Retrieves a quote based on the provided index

	Example (Request): GET /quotes/2
			(Response):
						{
						  "data": {
						    "quote": {
						      "text": "Success is not final, failure is not fatal: it is the courage to",
						      "author": "Winston Churchill"
						    }
						  }



ERRORS:
	
	Quotes Available = 7
	Invalid index or index < 0 or > 7:
			returns {
					  "detail": "quote unavailable"
					}
	Example(Request): GET /quotes/8
			(Response):
						{
	  						"detail": "quote unavailable"
						}