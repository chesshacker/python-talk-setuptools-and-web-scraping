import requests
from lxml import html

def main():
    url = 'http://store.apple.com/us/buy-watch/apple-watch-sport/38mm-silver-aluminum-case-white-sport-band' \
        '?product=MJ2T2LL/A&step=detail'
    page = requests.get(url)
    # living dangerously: not checking for errors at any point in this code
    tree = html.fromstring(page.text)
    price = tree.xpath('//span[@itemprop="price"]/text()')
    print price[0].strip()
