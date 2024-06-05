from serpapi import GoogleSearch
import os

api_key = os.getenv("SERPER_API_KEY")
params = {
    "api_key": api_key,
    "engine": "google",
    "q": "Coffee",
    "location": "Austin, Texas, United States",
    "google_domain": "google.com",
    "gl": "us",
    "hl": "en"
}

search = GoogleSearch(params)
results = search.get_dict()
print(results)
print('that was it bbbbbb')
