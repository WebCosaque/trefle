# trefle, 4chan files downloader.

import requests
import urllib.request
import time, datetime, os
from hurry.filesize import size, alternative
from bs4 import BeautifulSoup
from pyfiglet import Figlet
from colorama import init
init()
from colorama import Fore, Back, Style

customFig = Figlet(font='ogre')
print(Back.GREEN + customFig.renderText('trefle'))

print(Fore.WHITE + Back.GREEN + 'A tool to download all media files from a 4chan(nel).org thread.')
print(Style.RESET_ALL)


url = input('Thread URL: ')
folder = input('Name of the folder (leave blank for an automated name) :')

if folder == '':
    folder = str(time.time()) + "/"
else:
    folder = folder + "/"

os.makedirs(str(folder), exist_ok=True)
print('Files will be saved in', folder)

threadSource = requests.get(url)
thread = threadSource.text
soup = BeautifulSoup(thread,'html.parser')

for link in soup.findAll('a', {'class': 'fileThumb'}):
    imageUrl = 'https:' + link.get('href')
    imageName = imageUrl[-5:]
    print(imageUrl)
    name = time.time()
    fullName = str(name) + imageName
    pathName = str(folder) + str(fullName)
    urllib.request.urlretrieve(imageUrl, pathName)

totalSize = 0
for path, dirs, files in os.walk(folder):
    for f in files:
        fp = os.path.join(path, f)
        totalSize += os.path.getsize(fp)
print(Back.CYAN + size(totalSize, system=alternative), 'downloaded, files have been saved in', folder)
print(Style.RESET_ALL)
print(Fore.WHITE + Back.GREEN + 'Success !')
print(Style.RESET_ALL)
