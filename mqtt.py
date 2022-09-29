################################################################################
# mqtt.py: User friendly MQTT implementation via the class MQTT and a few
#          private callback routines.
################################################################################
import paho.mqtt.client as mqtt

class MQTT:
   """
   MQTT: User friendly MQTT implementation for easy publishing and subscribing.

         - __client: Private MQTT client object.
   """

   def __init__(self, host = "broker.hivemq.com"):
      """
      __init__: Creates new MQTT object and connects to specified host.

                - host: The broker/host to connect to (default = "broker.hivemq.com"). 
      """
      import time

      # Creating new MQTT client:
      self.__client = mqtt.Client()

      # Sets function pointers to point at callback routines:
      self.__client.on_connect = _client_on_connect
      self.__client.on_disconnect = _client_on_disconnect
      self.__client.on_message = _client_on_message

      # Connecting client to specified host:
      self.__client.connect(host)
      # If the connection does not start immediately, reconnection is made:
      if not self.__client.is_connected():
         self.__client.reconnect()

      # Starting MQTT thread:
      self.__client.loop_start()

      # Wait one second for connecting to finish:
      time.sleep(1)
      return

   def __del__(self):
      """
      __del__: Disconnects MQTT client and stopping MQTT thread.
      """
      # Terminating MQTT thread:
      self.__client.loop_stop()
      # Disconnecting from host:
      self.__client.disconnect()
      return

   def publish(self, topic, message, qos = 1):
      """
      publish: Publishes message to specified topic. The program is stalled
               until the message has been published.

               - topic  : The topic the message is going to be sent to.
               - message: The message to send as text (string).
               - qos    : Quality Of Service (default = 1, guarantees that
                          that the message is received, but sometimes two
                          messages might be sent by mistake).
      """
      # Receives MQTT info object to be able to wait for publish:
      msg = self.__client.publish(topic, message, qos)
      # Waiting until the message is published:
      msg.wait_for_publish()
      return

   def subscribe(self, topic, qos = 1):
      """
      subscribe: Subscribes to specified topic. When a message is received, the
                 message is printed in the terminal.

                 - topic  : The topic for subscription.
                 - qos    : Quality Of Service (default = 1, guarantees that
                            that the message is received, but sometimes two
                            messages might be sent by mistake).
      """
      self.__client.subscribe(topic, qos)
      return

   def unsubscribe(self, topic):
      """
      unsubscribe: Unsubscribes from specified topic.

                   - topic: The topic to unsubscribe.
      """
      self.__client.unsubscribe(topic)
      return

   def disconnect(self):
      """
      disconnect: Terminates MQTT thread and disconnects from host.
      """
      self.__client.loop_stop()
      self.__client.disconnect()
      return

def _client_on_connect(client, data, flags, return_code):
   """
   _client_on_connnect: Callback routine which gets called when trying to
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

def _client_on_disconnect(client, data, return_code):
   """
   _client_on_disconnnect: Callback routine which gets called when disconnecting
                           from a host. If the disconnection succeeded, the return
                           code is 0, otherwise if an unexpected disconnection
                           occured, the return code is equal to 1.

                           - client     : The MQTT client that's trying to connect.
                           - data       : User data (not used).
                           - return_code: Indicates connection status (0 = success).
   """
   if return_code:
      print("Unexpected disconnection from host \"" + str(client._host) + "\"!")
   else:
      print("Successful disconnection from host \"" + str(client._host) + "\"!")
   return 

def _client_on_message(client, data, message):
   """
   _client_on_message: Callback routine which gets called then a message is received
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
