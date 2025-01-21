import requests

# URL du serveur où envoyer la requête
url = "http://127.0.0.1:8000/fishin/messages"  # Remplace par l'URL de ton serveur

# Chaîne de caractères à envoyer
data = {
    "message": "Bonjour, voici une chaîne de caractères !"
}

try:
    # Envoi de la requête POST
    response = requests.post(url, json=data)
    
    # Vérification du statut de la réponse
    if response.status_code == 200:
        print("Succès ! Réponse du serveur :", response.json())
    else:
        print(f"Erreur {response.status_code} : {response.text}")
except requests.exceptions.RequestException as e:
    print("Une erreur est survenue :", e)
