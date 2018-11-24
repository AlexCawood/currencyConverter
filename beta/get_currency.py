#currency converter
import requests
from bs4 import BeautifulSoup 
class currency():
        def get_anycurr(curr1,curr2):
                try:
                        url = 'https://www.google.com/finance?q=' + curr1+curr2
                        resp = requests.get(url)
                        html = resp.text
                        soup = BeautifulSoup(html, "html.parser")
                        handling_results = []
                        for exch in soup.find_all(class_ ="bld"):
                                handling_results.append(exch.string)
                        exch_full_string = handling_results[0]
                        exchange_rate = exch_full_string[0:7]
                        return float(exchange_rate)
                except:
                        return 'no connection "she\'s not the one :\'("'
        print(get_anycurr('cny','eur'))

