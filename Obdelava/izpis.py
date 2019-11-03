import json
import re
import requests
import orodja

with open("igra_2.html") as dat:
    stran = dat.read()

izraz = re.compile(
    r'<meta name=\"title\" content=\"(?P<ime>.+?)\">.+?'
    r'{\"gameid\":\[\"(?P<id>.+?)\"\],.+?'
    r'\"yearpublished\":\"(?P<leto>\d+?)\",'
    r'\"minplayers\":\"(?P<minplay>\d+?)\",'
    r'\"maxplayers\":\"(?P<maxplay>\d+?)\",'
    r'\"minplaytime\":\"(?P<mintime>\d+?)\",'
    r'\"maxplaytime\":\"(?P<maxtime>\d+?)\",'
    r'\"minage\":\"(?P<minage>\d+?)\".+?'
    #r'\"boardgamecategory\":\[(.+?)\].+?'
    #r'\"boardgamemechanic\":\[(.+?)\].+?'
    r'\"ratingValue\": \"(?P<ocena>.+?)\".+?'
    r'\"reviewCount\": \"(?P<glasovi>\d+?)\"',
    flags=re.DOTALL
)

print(izraz.search(stran).groupdict())

