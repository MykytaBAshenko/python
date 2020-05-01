import requests
from bs4 import BeautifulSoup as BS

max_page = 2

pages = []

for x in range(1, max_page + 1):
    pages.append(requests.get('https://www.pornhub.com/video?page=' + str(x)))

for r in pages:
    html = BS(r.content, 'html.parser')

    for el in html.select('.thumbnail-info-wrapper'):
        title = el.select('span > a')
        if '/view_video.php?viewkey=' in title[0]['href']:
            print('<iframe src="https://rt.pornhub.com/embed/' + title[0]['href'].split('=')[1] + '" frameborder="0" width="560" height="340" scrolling="no" allowfullscreen=""></iframe>')
