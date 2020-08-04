import requests
from bs4 import BeautifulSoup

page = requests.get('https://wiki.rpcs3.net/index.php?title=Help:Game_Patches').content
soup = BeautifulSoup(page, 'lxml')
ver = soup.select_one('code:contains("Version:")').get_text()
f = open("patch.yml","w+")
f.write(str(ver) + "\n")
patches = soup.find_all('pre')
for i in range(len(patches)):
    f.write("\n")
    game_tmp = str(patches[i].contents)[2:-2]
    game_tmp = game_tmp.encode("raw_unicode_escape")
    game_tmp = game_tmp.decode("unicode_escape")
    f.write(game_tmp)
f.close()