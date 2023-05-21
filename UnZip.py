from zipfile import ZipFile as z
def unzip(file : str):
  with z(file, 'r') as f:
    f.extractall()
unzip('.zip')
