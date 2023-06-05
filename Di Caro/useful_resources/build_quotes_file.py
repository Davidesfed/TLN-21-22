from requests import get
from bs4 import BeautifulSoup

def get_from_phrases():
    url = 'https://www.phrases.org.uk/meanings/phrases-and-sayings-list.html'
    response = get(url)
    html_phrases = BeautifulSoup(response.text, 'html.parser')
    quotes = html_phrases.find_all('p', class_ = 'phrase-list')
    size = len(quotes)
    quotes = [quotes[i].text for i in range(size)]
    return quotes

def get_from_ef():
    def remove_backslash_char(string):
        return string[6:]

    url = 'https://www.ef.edu/english-resources/english-idioms/'
    response = get(url)
    html_ef = BeautifulSoup(response.text, 'html.parser')
    quotes = html_ef.select('tr td:nth-of-type(1)')
    size = len(quotes)
    quotes = [quotes[i].text for i in range(size)]
    quotes = [remove_backslash_char(x) for x in quotes]
    return quotes

def save_to_file():
    with open('common_saying.txt', 'w', encoding='utf-8') as f:
        quotes = set()
        quotes.update(get_from_ef())
        quotes.update(get_from_phrases())
        for item in quotes:
            f.write('%s\n' % item)
        print('Done')

save_to_file()
#print(get_from_phrases())