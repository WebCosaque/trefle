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
thread_source = requests.get(url)
thread = thread_source.text
soup = BeautifulSoup(thread,'html.parser')
folder = str(time.time()) + "/"
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

folderSize = size(sum(os.path.getsize(f) for f in os.listdir(str(folder)) if os.path.isfile(f)), system=si)
test = os.path.getsize(folder)
print(test)
print(folderSize, 'downloaded in folder', folder)
print('Done')
