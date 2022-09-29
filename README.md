# Anteckningar-2022-09-29
Implementering av MQTT i Python (del II). Skapande av användarvänlig MQTT-klass.

Filen repetition.py utgör repetition av innehållet från föregående lektion. Här implementeras ett MQTT-objekt som fungerar 
både som klient och server via biblioteket paho-mqtt. Meddelanden matas in från terminalen och publiceras till en blank rad matas in.
Mottagna meddelanden skrivs ut i terminalen.

Filen mqtt.py innehåller en egenskapad mycket användarvänlig MQTT-klass. som bygger på paho-mqtt. I filen main.py testas denna klass
via ett objekt som agerar både server och klient. Även här matas meddelanden in från terminalen tills en blank rad matas in och
mottagna meddelanden skrivs ut i terminalen.
