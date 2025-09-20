
import bs4 #importa a biblioteca beautifulSoup 4 
import requests #imposta a biblioteca requests

url = 'https://quotes.toscrape.com/' #grava o site quotes
quotes = requests.get(url) # importa o código do site 
soup = bs4.BeautifulSoup(quotes.text, 'html.parser') # coverte o quote em html

frases = soup.find_all('div', class_='quote')

for div in frase:
    texto = div.find('span', class_'text')