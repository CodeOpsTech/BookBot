# -*- coding: utf-8 -*-
import json
import base64

def elicit_intent(message):
	return {
		'dialogAction' : {
		'type' : 'ElicitIntent',
		'message' : message
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
					'text' : 'python',
					'value' : 'show python book'
				}
			]
		}
		]
	}
		}
	}
	
def lambda_handler(event, context):
    # TODO implement
    print event
    try:
        session_attributes = event['sessionAttributes']['data']
        decoded = base64.b64decode(session_attributes)
        print 'decoded', decoded
        data = json.loads(decoded)
        print data[0]
        reviews = data[0]['reviews_url']
        message = {'contentType': 'PlainText', 'content': """You can find the reviews for {} at {} """.format(data[0]['title'], data[0]['reviews_url'])}
        return elicit_intent(message)
    except:
		message = {'contentType': 'PlainText', 'content': """Please select a book first. How about these to start with?"""}
		return elicit(message)