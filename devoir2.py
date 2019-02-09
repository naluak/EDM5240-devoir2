#coding: utf-8

import json
import csv
import requests

entete = {
	"User-Agent":"Stéphanie Prévost - 438-777-4252",
	"From":"stephanie-prevost@hotmail.ca"
}

fichier = "banq.csv"

baseurl="http://collections.banq.qc.ca/api/service-notice?handle=52327/"
# req = requests.get(baseurl+str(1386),headers=entete)

f2 = open(fichier,"a")
banq = csv.writer(f2)

for numberX in range(1000,2001): #monter à 2001 après les tests
	# print(numberX)
	url = baseurl + str(numberX)
	req = requests.get(url,headers=entete)
	req.status_code
	if req.status_code == 200:
		
		lainfo = req.json()
		# print(json.dumps(lainfo, indent=4, sort_keys=True))

		if lainfo["type"] == "audio":
			infos=[]
			infos.append(lainfo["titre"])
			infos.append(lainfo["createurs"][0])
			infos.append(lainfo["dateCreation"])
			infos.append(lainfo["descriptionMat"])
			if "url" in lainfo["bitstreams"] ["racine"] ["fils"] [0] ["formats"] [0]:
				infos.append(lainfo["bitstreams"] ["racine"] ["fils"] [0] ["formats"] [0] ["url"])
			else: infos.append("url inconnu")
			print(infos, numberX)
			print("$"*80)
			
		# 	assert isinstance(lainfo["url"], str), numberX + "n'est pas un string"
			
			banq.writerow(infos)