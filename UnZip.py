from zipfile import ZipFile as z
def unzip(file : str):
  with z(file, 'r') as f:
    f.extractall()

from os import rename as r
from os.path import isdir
name="MyHtml-Emergency1"
if not isdir('pkg'):
    unzip(name+'.zip')
    r(name,'pkg')