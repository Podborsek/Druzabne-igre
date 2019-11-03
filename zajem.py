import json
import re
import requests
import orodja

#neki = r"<meta name="title" content="(.*?)">.*{"gameid":\["(.*?)"\]"
#r"<div id='results_objectname\d+' style='z-index:1000;' onclick=''>.*?<a  href=\"(?P<href>\/boardgame\/(?P<id>\d+?)\/.*?)\"   >(?P<ime>.*?)<\/a>"

# Najprej moramo iz prvih petih strani dobiti seznam najpopularnejsih iger:
#for st in range(1,6):
#    orodja.shrani_spletno_stran("https://boardgamegeek.com/browse/boardgame/page/{}?sort=numvoters&sortdir=desc".format(st), "najigre_stran_{}".format(st))

vzorec_za_igre = re.compile(
    r"<div id='results_objectname\d+' style='z-index:1000;' onclick=''>.*?<a  href=\"(.*?)\"   >(?P<ime>.*?)<\/a>",
    flags=re.DOTALL
)


url_naslovi = []
for st in range(1,6):
    vsebina = orodja.vsebina_datoteke("najigre_stran_{}".format(st))
    url_naslovi += re.findall(vzorec_za_igre, vsebina)
    print(len(url_naslovi))
orodja.zapisi_json(url_naslovi, "url_naslovi.json")

