################################################################################
# repeition.py: Repetition regarding usage of the paho-mqtt library.
################################################################################
import paho.mqtt.client as mqtt 

def client_on_connect(client, data, flags, return_code):
   """
   client_on_connnect: Callback routine which gets called when trying to
                       connect to a host. If the connection succeeded, the
                       return code is 0, otherwise the return code is 1.

                       - client     : The MQTT client that's trying to connect.
                       - data       : User data (not used).
                       - flags      : Status flags (not used).
                       - return_code: Indicates connection status (0 = success).
   """
   if return_code:
      print("Could not connect to host \"" + str(client._host) + "\"!\n")
   else:
      print("Successfully connected to host \"" + str(client._host) + "\"!\n")
   return

def client_on_disconnect(client, data, return_code):
   """
   client_on_disconnnect: Callback routine which gets called when disconnecting
                          from a host. If the disconnection succeeded, the return
                          code is 0, otherwise if an unexpected disconnection
                          occured, the return code is equal to 1.

                          - client     : The MQTT client that's trying to connect.
                          - data       : User data (not used).
                          - return_code: Indicates connection status (0 = success).
   """
   if return_code:
      print("Unexpected disconnection from host \"" + str(client._host) + "\"!\n")
   else:
      print("Successful disconnection from host \"" + str(client._host) + "\"!\n")
   return 

def client_on_message(client, data, message):
   """
   client_on_message: Callback routine which gets called then a message is received
                      from a subscribed topic. The message is received by the payload
                      parameter of input argument message, while the topic it was received
                      from is received by the topic parameter of the samt input argument.
                      The message first gets decoded from binary form into UTF-8
                      and stored in a local string named s.

                      - client : The MQTT client that acts as the server (subscriber).
                      - data   : User data (not used).
                      - message: Contains the message in binary form and the topic it
                                 was received from.
   """
   s = message.payload.decode("utf-8")
   print("Received message \"" + str(s) + "\" from topic \"" + str(message.topic) + "\"!\n")
   return

def main():
   """
   main: Using a MQTT object as both client and server. Messages are entered from the
         terminal until a blank line is finished.
   """
   import time # Imports time module for using the sleep function (delay).

   # Creating a MQTT client object:
   client1 = mqtt.Client()

   # Connecting function pointers to callback routines:
   client1.on_connect = client_on_connect
   client1.on_disconnect = client_on_disconnect
   client1.on_message = client_on_message

   # Connect the client to host "broker.hivemq.com":
   client1.connect(host = "broker.hivemq.com")
   # If the client does not connect immediately, reconnect:
   if not client1.is_connected():
      client1.reconnect()

   # Starting MQTT thread:
   client1.loop_start()

   # Waits one second before starting main program:
   time.sleep(1)

   # Subscribes to topic "python/mqtt/erik":
   client1.subscribe(topic = "python/mqtt/erik", qos = 1)

   while True:
      # Reads message from the terminal, stores in a string:
      s = input("Enter a message to publish or a blank line to finish:\n")
      print() # Adds a blank line.

      if s: # If s contains any characters, it's published as a message.
         # We publish the message and wait until the message has been published.
         msg = client1.publish(topic = "python/mqtt/erik", payload = s, qos = 1)
         msg.wait_for_publish()
      else:
         # Stop MQTT thread and disconnect from host.
         client1.loop_stop()
         client1.disconnect()
   print("Bye!\n")
   return 

################################################################################
# If this is the startup file, the main function is called to start the program.
################################################################################
if __name__ == "__main__":
   main()