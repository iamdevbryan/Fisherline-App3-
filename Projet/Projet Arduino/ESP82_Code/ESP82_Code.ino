#include <ESP8266WiFi.h>

const char* ssid = "BLANC";  
const char* password = "AZERTYUIOP";  
const char* serveur_ip = "192.168.137.36";  // Remplace par l'IP du serveur ESP32
const uint16_t port = 80;

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);
    
    Serial.print("Connexion à Wi-Fi");
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    
    Serial.println("\nConnecté !");
}

void loop() {
    WiFiClient client;
    if (client.connect(serveur_ip, port)) {
        Serial.println("Connexion au serveur réussie !");
        client.println("Hello ESP32 !");
        client.stop();
    } else {
        Serial.println("Connexion échouée !");
    }
    
    delay(2000);  // Attente avant le prochain envoi
}
