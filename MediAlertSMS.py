import schedule
import vonage
import time
import os
#BY ELKHHARAZ ABDERRAHIM
# Configuration des informations d'authentification
VONAGE_API_KEY = os.environ.get("VONAGE_API_KEY")
VONAGE_API_SECRET = os.environ.get("VONAGE_API_SECRET")

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)
sms = vonage.Sms(client)

# Liste des numéros de téléphone
phone_numbers = ['212664352206', '212664352207', '212664352208']  # Ajoutez vos numéros de téléphone ici

def send_message_to_numbers():
    try:
        message = 'Time to take your medication'
        
        for number in phone_numbers:
            response = sms.send_message({
                'from': 'Vonage APIs',
                'to': number,
                'text': message
            })

            # Vérification de la réponse
            if response['messages'][0]['status'] == '0':
                print(f"Message sent to {number} successfully")
            else:
                print(f"Failed to send message to {number}")
    except Exception as e:
        print(f'An error occurred: {e}')

# Planification de la tâche
schedule.every().day.at("16:43").do(send_message_to_numbers)
schedule.every().day.at("12:00").do(send_message_to_numbers)
schedule.every().day.at("18:00").do(send_message_to_numbers)

while True:
    schedule.run_pending()
    time.sleep(1)
