import bs4, requests

def getEbayPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#prcIsum')
    return elems[0].text.strip()


price = getEbayPrice('https://www.ebay.com/itm/Dune-Mass-Market-Paperback-By-Herbert-Frank-GOOD/264627984337?epid=109089518&_trkparms=ispr%3D1&hash=item3d9d0e97d1:g:-JgAAOSwg0FgTKlY&amdata=enc%3AAQAFAAACYBaobrjLl8XobRIiIML1V4Imu%252Fn%252BzU5L90Z278x5ickkXKoKcbeZcOrOku%252BoOBl%252BSwh7vN%252BE%252FvwnBMNW5GXsTRoH0ZhlJzGtOhLo2YmZ9CCWLR268VQy%252FWkL38uPEmz%252FqjVK%252Fub2zFKjnPeeAKI36ZWTSowliAeqIgQzYWUx95s0oIzqpHbo4onMmJgzuRRWFRLJ%252BQDWBiq6v3w%252FQ8jA5NjyBdCStCmf3Lx%252FzRjWvRdG%252BpFyqh1XEOHMoyZkRwP9lupJGCOSve4%252FAIfJhJpA6HvJdk0NulCn39MkH7rR%252BWtlHsXuXqxhY2Y%252F%252BmaXZRqj6PB3b3twHo2e7sU8d%252BHb5FibubiCxbDhji7FAcLPgQ2xnP%252FQJRZh%252Fzf5d6ATIUAsZCo%252BlxOkR%252B%252FdN60kTN%252FZReV2RQK07mAws%252Bht6EJGcppBjXdx7rZCsMPFSkk13JHAEaX3Xpz7XTNjU0mPhbQLGnmzb%252FK02Ti4tICekaBOOB76rJz%252FOLjLgdvVPOJHyKBOca2I8mwdtAXSPRF%252BjGh1BXkMTo0r8PZAVT2c7usUJ2Cr8dCyrgasdPzb%252B71NTg%252FmGQBQ8BakhtddIznfOywR6bOyoxCtOetSi8F0%252FYcFjAqyTMPc99ypbkyDhpCJztArKTvqlKRvCSxRsddG%252Fyi%252BwHTJGdo25RqO0t5U7v2N%252BP6LKwj8xVgj6GsRJ8NA3LM2rquyXLGf64tlj%252FDLLs4gqCTkHUARYlekj0w%252Fy5ZAt%252B8xGKQ%252FV8rz2Da0kxkopda07VCzXwBvedeM2mk1vAruZ1ik95rIH2zvJbQ1aICENhh9%7Ccksum%3A264627984337d9f7290c107740a68b0ddc14251d67ad%7Campid%3APL_CLK%7Cclp%3A2334524')
print('The price is ' + price)
