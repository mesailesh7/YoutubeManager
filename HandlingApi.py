# import requests
#
#
# def fetch_random_joke():
#     url = 'https://api.freeapi.app/api/v1/public/randomjokes/joke/random'
#     response = requests.get(url)
#     data =  response.json()
#
#     if data["success"] == True and "data" in data:
#         joke_data = data["data"]
#         jokes = joke_data["content"]
#         return jokes
#     else:
#         raise Exception("No jokes found")
#
#
#
#
# def main():
#     try:
#         jokes = fetch_random_joke()
#         print(f"jokes: {jokes}")
#     except Exception as e:
#         print(str(e))
#
# if __name__ == '__main__':
#     main()
#
from shlex import quote

import requests

def fetch_random_quotes():
    url = 'https://api.freeapi.app/api/v1/public/quotes?page=1&limit=10&query=human'
    response = requests.get(url)
    data = response.json()

    if data["success"] == True and "data" in data:
        quotes_data = data["data"]["data"]
        quotes_list = []
        for quote in quotes_data:
            quote_info = {
                "author": quote["author"],
                "quote": quote["content"],
                "dateAdded": quote["dateAdded"]
            }
            quotes_list.append(quote_info)
        return quotes_list
    else:
        raise Exception("Something went wrong")


def main():
    try:
        quotes_list = fetch_random_quotes()
        for quote in quotes_list:
            print(f"Author: {quote['author']}\nQuote: {quote['quote']}\nDate Added: {quote['dateAdded']}\n")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()





