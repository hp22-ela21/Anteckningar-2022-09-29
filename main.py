################################################################################
# main.py: Implementing user friendly custom made MQTT class for publishing
#          and subscribing to a specified topic.
################################################################################
from mqtt import MQTT # Imports the user friendly MQTT class from the mqtt module.

def main():
   """
   main: Publishing and subscribing to topic "python/mqtt/1" by using a
         single MQTT object, used as both a client and a server. Messaged are
         entered from the terminal and published until a blank line is entered.
   """
   # Creates a MQTT client, connects to default host "broker.hivemq.com":
   client1 = MQTT()
   # Subscribes to topic "python/mqtt/1":
   client1.subscribe(topic = "python/mqtt/1")

   while True:
      # Reads message from terminal:
      s = input("Enter a message to publish or a blank line to finish:\n")
      print() # Blank line.

      # If a message was entered it gets published to toic "python/mqtt/1":
      if s:
         client1.publish(topic = "python/mqtt/1", message = s)
      # If a blank line was entered we disconnect from the host and break the loop:
      else:
         client1.disconnect()
         break

   print("Bye!\n")
   return

################################################################################
# If this is the startup file, the main function is called to start the program.
################################################################################
if __name__ == "__main__":
   main()