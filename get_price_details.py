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
	
def elicit(message):
	return {
		'dialogAction' : {
		'type' : 'ElicitIntent',
		'message' : message,
		'responseCard' : {
			'version' : 1,
			'contentType' : 'application/vnd.amazonaws.card.generic',
			'genericAttachments' : [
			{
				'title' : 'These are the trending technologies (as of TIOBE index)',
				'buttons' : [
				{
					'text' : 'Java',
					'value' : 'show java book'
				},
				{
					'text' : 'C',
					'value' : 'show C book'
				},
				{
					'text' : 'Python',
					'value' : 'show python book'
				}
			]
		}
		]
	}
		}
	}
   
def lambda_handler(event, context):
    print event
    try:
        session_attributes = event['sessionAttributes']['data']
        decoded = base64.b64decode(session_attributes)
        print 'decoded', decoded
        data = json.loads(decoded)
        message = {'contentType': 'PlainText', 'content': """It would cost around ${}""".format(data[0]['price'])}
        return elicit_intent(message)
    except:
        message = {'contentType': 'PlainText', 'content': """:-O Oops I forgot what we were talking about. How about these?"""}
        return elicit(message)
      
