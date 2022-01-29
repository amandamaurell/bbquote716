import re
import requests


def get_quote():
    url = 'https://movie-quote-api.herokuapp.com/v1/quote/'
    response = requests.get(url).json()
    return f"quote: {response['quote']}, role:{response['role']}!"

if __name__ == '__main__':
    print(get_quote())
