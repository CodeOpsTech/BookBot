import ast
import json
import unicodedata
import base64

def elicit_intent(message, image_url, title, book_url):
	return {
		'dialogAction' : {
		'type' : 'ElicitIntent',
		'message' : message,
            'responseCard' : {
                'version' : 1,
                'contentType' : 'application/vnd.amazonaws.card.generic',
                'attachmentLinkUrl' : book_url,
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
                                'text' : 'Pulisher',
                                'value' : 'publisher?'
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
        data = json.loads(decoded)
        message = {'contentType': 'PlainText', 'content': """Here is the cover pic for {}""".format(data[0]['title'])}
        return elicit_intent(message, data[0]['image_url'], data[0]['title'], data[0]['url'])
    except:
        message = {'contentType': 'PlainText', 'content': """:-O Oops I forgot what we were talking about. How about these trending ones?"""}
        return elicit(message)
