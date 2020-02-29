#! python3
#  Download every single XKCD comic - multithreaded version

import bs4, requests, os, threading, time

#url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)  # exist_ok prevents from exception if folder already exists

def download_xkcd(start, end):
    for url_number in range(start, end):
        res = requests.get('http://xkcd.com/' + str(url_number))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'lxml')
        check_image_link = soup.select('#comic img')

        if not check_image_link:
            print('Cannot find the image')
        else:
            image_link = check_image_link[0].get('src')

        # downloading the image
        print('Downloading image {0}...'.format(image_link))
        #time.sleep(1)
        # saving image in previously created folder
        image_file = open(os.path.join('xkcd', os.path.basename(image_link)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

download_threads = [] # keep all threads objects
for i in range(1, 100, 10): # creates 10 threads, 1000 - number of total images downloaded
    download_thread = threading.Thread(target=download_xkcd, args=(i, i+9))  # creating thread object
    download_threads.append(download_thread)
    download_thread.start()  # running download_thread function

for download_thread in download_threads:
    download_thread.join()  # Waiting until all threads are finished
print("Done")
