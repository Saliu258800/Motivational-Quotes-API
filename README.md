Quotes API Documentation

Base URL: https://motivational-quotes-api-haah.onrender.com

ENDPOINTS

	1. Get all Quotes
	URL: /quotes
	Method: GET
	Description: Returns all quotes available

	Example(Request): GET /quotes/json
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


	3. Get only the words by the authors
	URL: /quotes/sayings
	Method: GET
	Description: Returns all the sayings of the available authors


	4. Get the authors by name
	URL: /quotes/authors/json
	Method: GET
	Description: Retrieves all the names of the authors


	5. To generate a random quote from the Quotes
	URl: /api/random/json
	Method: GET
	Description: generates and returns a random quote

	Example(Response):
						{
						  "data": {
						    "random quote": {
						      "text": "Talk is cheap. Show me the code",
						      "author": "Linus Torvalds"
						    }
						  }
						}



ERRORS:
	
	Invalid index or index < 0 or > number of quotes:
			returns {
					  "detail": "quote unavailable"
					}
	Example(Request): GET /quotes/8
			(Response):
						{
	  						"detail": "quote unavailable"
						}


	Some the API request routes returns both HTML response and JSON response. So when requesting for such API, Exception would be raised if wrong format is requested. eg.  /api/quotes/<format> where format: json or html

					/api/quotes/json returns JSON response where as 
					/api/quotes/html returns HTML response

				Invalid request: /api/quotes/hello instead of hello being html or json returns
								{
									"detail": "Invalid format: '/hello'. request must be '/html' or '/json' to process"
								}

	The html format was added to routes for direct integration via HTMX for UI testing of the APIs

	The HTML response can be used but it is advisable to use HTMX to request for it as the response might have HTMX content in it and use JavaScript to request for the JSON response data