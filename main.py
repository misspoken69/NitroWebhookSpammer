import string
import random
import time
import crayons
from discord_webhook import *

print("{}".format(crayons.green('This was made by Misspoken#1122! Not my fault if you get in trouble.')))

def send():
    webhook = DiscordWebhook(url=webhookurl, content="discord.gift/" + code) # First part of the generating.
    response = webhook.execute()

# SETTINGS
webhookurl = 'PUT YOUR WEBHOOK HERE' # Put your webhook here.

changewh = input("Do you want to change the webhook URL, say Y if you haven't changed it in the file else say N. (Y/N) > ")
if changewh == "y":
    webhookurl = input("You have chosen to change the web hook url, paste it here and press enter. > ")

amount = 0
amount = input("How many codes would you like to be sent to your server? ")
print("You have chose to send "+ amount +" codes.")


for x in range(1, int(amount) + 1):
    code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    send() # Makes strings and sends them.
    print("Code Sent: " + code + "Code Number: %d" % (x))
    time.sleep(1.65) # Cooldown because of rate limited.

print('\nAll the codes have been sent to your server!')
time.sleep(5)
