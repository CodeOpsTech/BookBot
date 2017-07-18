import ast
import json
import unicodedata
import base64

def elicit_intent(message, image_url, title):
	return {
		'dialogAction' : {
		'type' : 'ElicitIntent',
		'message' : message,
            'responseCard' : {
                'version' : 1,
                'contentType' : 'application/vnd.amazonaws.card.generic',
                'genericAttachments' : [
                    {
                        'title' : title,
                        'imageUrl' : image_url,
                        'buttons' : [
                            {
                                'text' : 'More options',
                                'value' : 'view more'
                            },
                            {
                                'text' : 'Reviews',
                                'value' : 'reviews?'
                            },
                            {
                                'text' : 'Pages',
                                'value' : 'pages??'
                            }
                            ]
                        
                    }
                    ]
                
            }    
        
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
        message = {'contentType': 'PlainText', 'content': """{}""".format(data[0]['publisher'])}
        return elicit_intent(message, data[0]['image_url'], data[0]['title'])
    except:
        message = {'contentType': 'PlainText', 'content': """:-O Oops I forgot what we were talking about. How about these trending ones?"""}
        return elicit(message)
