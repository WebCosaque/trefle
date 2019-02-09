# trefle 4chan files downloader.

import requests
import random
import urllib.request
import pyprind
import time,datetime,os
from hurry.filesize import size, si
from bs4 import BeautifulSoup

from pyfiglet import Figlet
custom_fig = Figlet(font='ogre')
print(custom_fig.renderText('trefle'))

url = input('Thread URL: ')
folder = input('Name of the folder (leave blank for an automated name) :')
if folder == '':
    folder = str(time.time()) + "/"
else:
    folder = folder + "/"
thread_source = requests.get(url)
thread = thread_source.text
soup = BeautifulSoup(thread,'html.parser')
os.makedirs(str(folder), exist_ok=True)
print('Files will be saved in', folder)

for link in soup.findAll('a', {'class': 'fileThumb'}):
    imageUrl = 'https:' + link.get('href')
    imageName = imageUrl[-5:]
    print(imageUrl)
    name = time.time()
    full_name = str(name) + imageName
    path_name = str(folder) + str(full_name)
    urllib.request.urlretrieve(imageUrl, path_name)

print('Done')
