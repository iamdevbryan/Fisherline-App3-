  
  const alerte = document.querySelector(".alert-container")


function showAlert(){

    const donnees = {
        requete: "Votre message ici" // Remplacez par la valeur que vous voulez envoyer
    };

    fetch('http://127.0.0.1:8000/fishin/alert/', {
        method: 'POST',
         mode: 'no-cors',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(donnees),
    })
        .then(response => {
            if (!response.ok) {
                // Si le serveur retourne un statut d'erreur, on gère ici
                throw new Error(`Erreur HTTP ! Statut : ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Réponse de l\'API :', data);
            if (data.reponse === 0) {
                console.log("rien à signaler");
            } else {
                console.log("Alerte détectée, Id :", data.reponse);
            }
        })
        .catch(error => {
            console.error('Erreur :', error);
        });
}

 
setInterval(showAlert, 3000);

  