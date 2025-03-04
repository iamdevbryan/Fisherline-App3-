  
var alerte = document.querySelector(".alert-container");
var alerte_false = document.querySelector(".alert-false-container");

var close = document.querySelector(".close")
close.addEventListener('click', ()=>{
    alerte.style.visibility = "hidden"
})

var close_false = document.querySelector(".close-false")
close_false.addEventListener('click', ()=>{
    alerte_false.style.visibility = "hidden"
})

var modified_id = document.querySelector(".id-number h2");
console.log(modified_id);

function showAlert(){

    const donnees = {
        requete: "Votre message ici"
    };

    fetch('http://127.0.0.1:8000/fishin/alert/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(donnees),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erreur HTTP ! Statut : ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Réponse de l\'API :', data);
            if (data.reponse === 0) {
                console.log("rien à signaler");
            } else {
                if(data.reponse.statut==="Verified"){
                    console.log("Alerte détectée, Id :", data.reponse.id);
                    modified_id.innerHTML = data.reponse;
                    alerte.style.visibility = 'visible';
                }else{
                    console.log("bateau illégal");
                    if(alerte.style.visibility != 'visible'){
                        console.log("surement unen erreur");
                        alerte_false.style.visibility = 'visible';
                    }
                }
              
            }
        })
        .catch(error => {
            console.error('Erreur :', error);
        });
}

 
setInterval(showAlert, 3000);

  