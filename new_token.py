import requests

import json

 

 

 

url = "https://entreprise.pole-emploi.fr/connexion/oauth2/access_token?realm=partenaire"

 

Leclient_id = "PAR_offreetdemandedecompe_1419c80c16f05e95859ad4a3ef8e5c1a85b845ec37c784a9a2301797b37ae787"

Leclient_secret = "5e720543fc0ceb46167a2f0678d095da6686abdb7be238bc2ba2ca82f3d6eebe"

 

 

payload='client_id=' + Leclient_id + '&client_secret=' + Leclient_secret + '&grant_type=client_credentials&scope=api_offresdemploiv2 o2dsoffre'

headers = {

  'Content-Type': 'application/x-www-form-urlencoded'

}

 

 

response = requests.request("POST", url, headers=headers, data=payload)

 

# Vérifiez si la requête a réussi

if response.status_code == 200:

    # Traitez la réponse ici

    # La réponse est disponible dans la variable response.json()

    data = response.json()

    print(data)

else:

    # Affichez un message d'erreur si la requête n'a pas réussi

    print("Erreur lors de la récupération des données "+str(response.status_code))

 

tk = json.loads(response.text)['access_token']

print(tk)

url = "https://api.pole-emploi.io/partenaire/offresdemploi/v2/offres/search"

 

payload={}

headers = {

  'Authorization': 'Bearer '+ str(tk)

}

 

 

 

response = requests.request("GET", url, headers=headers, data=payload)

 

# Vérifiez si la requête a réussi

if response.status_code == 200 or response.status_code == 206:

    # Traitez la réponse ici

    # La réponse est disponible dans la variable response.json()

    print(response.text)

else:

    # Affichez un message d'erreur si la requête n'a pas réussi

    print("Erreur lors de la récupération des données "+str(response.status_code))