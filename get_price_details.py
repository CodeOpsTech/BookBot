import ast
import json
import unicodedata
import base64

def elicit_intent(message):
	return {
		'dialogAction' : {
		'type' : 'ElicitIntent',
		'message' : message,
		}
	}

def lambda_handler(event, context):
    print event
    session_attributes = event['sessionAttributes']['data']
    decoded = base64.b64decode(session_attributes)
    print 'decoded', decoded
    data = json.loads(decoded)
    message = {'contentType': 'PlainText', 'content': """It would cost around ${}""".format(data[0]['price'])}
    return elicit_intent(message)
  