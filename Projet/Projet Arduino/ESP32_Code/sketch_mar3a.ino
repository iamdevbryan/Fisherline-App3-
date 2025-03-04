#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "BLANC";  // Remplace par ton SSID
const char* password = "AZERTYUIOP";  // Remplace par ton mot de passe

const char* server_url = "http://192.168.1.11:8000/fishin/messages/";  // URL Django

WiFiServer server(80);
String dernierMessage = "Aucun message reçu";  // Stocke le dernier message reçu (ID de l'ESP82)
unsigned long lastSendTime = 0;  // Gère l'intervalle de 5 sec
int trigPin = 5;  // Pin Trigger du HC-SR04
int echoPin = 18;  // Pin Echo du HC-SR04
long distance;
long seuil = 30;  // Distance seuil (en cm) pour détecter un mouvement
long seuilMin = 4;  // Distance minimale à prendre en compte
bool mouvementDetecte = false;  // Indicateur de détection de mouvement
unsigned long lastDetectionTime = 0;  // Temps de la dernière détection pour éviter l'envoi continu
unsigned long lastMessageTime = 0;  // Temps de la dernière réception du message de l'ESP82
unsigned long timeoutEsp82 = 10000;  // Délai d'attente (10 secondes) avant de réinitialiser l'ID si pas de message de l'ESP82

// Déclaration de la fonction sans argument par défaut dans la déclaration
void envoyerAuServeur(String message, String id);

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);
    
    Serial.print("Connexion à Wi-Fi");
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("\nWi-Fi connecté !");
    Serial.print("Adresse IP : ");
    Serial.println(WiFi.localIP());

    server.begin();
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
}

void loop() {
    WiFiClient client = server.available();  
    if (client) {
        Serial.println("Client connecté !");
        String requete = client.readStringUntil('\r');
        Serial.println("Message reçu de l'ESP82 : " + requete);
        client.flush();

        dernierMessage = requete;  // Mise à jour du dernier message (ID de l'ESP82)
        lastMessageTime = millis();  // Mise à jour du temps de réception du dernier message de l'ESP82
    }

    // Lecture de la distance du capteur ultrason
    distance = mesurerDistance();
    Serial.print("Distance mesurée : ");
    Serial.println(distance);

    // Vérifier que la distance est valide avant de continuer
    if (distance != -1) {
        // Vérification si la distance est inférieure au seuil (indiquant une intrusion)
        if (distance < seuil) {  // Si un mouvement est détecté
            if (!mouvementDetecte) {
                mouvementDetecte = true;
                lastDetectionTime = millis();  // Mise à jour du temps de détection
                Serial.println("Mouvement détecté !");
            }
        }

        // Envoi d'un message au serveur si un mouvement a été détecté et qu'il est temps d'envoyer
        if (mouvementDetecte && millis() - lastDetectionTime >= 500) {
            if (dernierMessage == "Aucun message reçu") {
                envoyerAuServeur("Intruder", "");  // Envoi "Intruder" si aucun message de l'ESP82
            } else {
                envoyerAuServeur("Verified", dernierMessage);  // Envoi "Verified" avec l'ID de l'ESP82
            }
            mouvementDetecte = false;  // Réinitialiser l'indicateur de mouvement après l'envoi
        }

    } else {
        Serial.println("Aucune distance valide détectée.");
    }

    // Si aucun message n'est reçu de l'ESP82 après un certain délai, réinitialiser l'ID
    if (millis() - lastMessageTime >= timeoutEsp82) {
        dernierMessage = "Aucun message reçu";  // Réinitialiser l'ID après le timeout
        Serial.println("ID de l'ESP82 réinitialisé après timeout.");
    }
}

long mesurerDistance() {
    // Envoie d'une impulsion pour obtenir la distance
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    long duration = pulseIn(echoPin, HIGH);
    long distance = (duration / 2) * 0.0344;  // Calcul de la distance en cm

    // Retourne -1 si la distance est invalide
    if (duration == 0 || distance < seuilMin) {
        return -1;  // Retourne -1 pour signaler une lecture invalide
    }

    return distance;
}

// Définition de la fonction sans argument par défaut
void envoyerAuServeur(String message, String id) {
    if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;
        http.begin(server_url);
        http.addHeader("Content-Type", "application/json");
            Serial.println("envoi du message au serveur.");

        // Envoi du message avec l'ID, si disponible
        String payload;
        if (id != "") {
            payload = "{\"message\": \"" + message + "\", \"id\": \"" + id + "\"}";
        } else {
            payload = "{\"message\": \"" + message + "\"}";
        }

        int httpResponseCode = http.POST(payload);

        Serial.print("Réponse serveur : ");
        Serial.println(httpResponseCode);
        
        if (httpResponseCode == 200) {  // Si le serveur répond correctement
            // Réinitialiser l'ID de l'ESP82 après une réponse réussie
            dernierMessage = "Aucun message reçu";  
            Serial.println("ID de l'ESP82 réinitialisé après réponse du serveur.");
        }

        http.end();
    } else {
        Serial.println("Wi-Fi déconnecté !");
    }
}
