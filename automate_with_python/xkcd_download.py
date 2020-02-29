#! python3
#  Download every single XKCD comic (task for test)

import bs4, requests, os

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)  # exist_ok prevents from exception if folder already exists

while url.endswith('#') == False:  # first link ends with '#'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    check_image_link = soup.select('#comic img')

    if not check_image_link:
        print('Cannot find the image')
    else:
        image_link = check_image_link[0].get('src')

    # downloading the image
    print('Downloading image {0} from {1}'.format(image_link, url))
    # saving image in previously created folder
    image_file = open(os.path.join('xkcd', os.path.basename(image_link)), 'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    url = 'http://xkcd.com' + soup.select('.comicNav a')[1].get('href')  # set url of previous image