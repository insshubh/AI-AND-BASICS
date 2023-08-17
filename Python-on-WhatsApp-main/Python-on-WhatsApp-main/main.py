
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import src.services as services


app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg.startswith('service'):
        code = incoming_msg.lstrip('service')
        output = "ODD_check /n IsPrime /n Factors /n Multiples "
        msg.body(output)
        return str(resp)

    incoming_msg = incoming_msg.lower()

    if 'your name' in incoming_msg:
        output = 'I am your BOT Friend'

    elif 'date' in incoming_msg:
        output = services.get_date()

    elif 'time' in incoming_msg:
        output = services.get_time()

    elif 'joke' in incoming_msg:
        output = services.get_joke()

    elif 'quote' in incoming_msg:
        output = services.get_quote()

    else:
        api_key = services.fetch_apikey('wolfram-alpha')
        if api_key == None:
            output = 'Wolfram alpha api key needed'
        else:
            output = services.chatbot(api_key, incoming_msg)

    msg.body(output)
    return str(resp)


if __name__ == '__main__':
    app.run()
