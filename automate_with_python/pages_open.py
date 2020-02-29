#! python3
#  Open several links from Google search

import bs4, requests, sys, webbrowser

print('Googling....')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')
links = soup.select('.r a')  # select links with search results - they belong to 'r' CSS class
page_number = min(5, len(links))
for i in range(page_number):
    webbrowser.open('http://google.com' + links[i].get('href'))
