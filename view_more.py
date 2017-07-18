import logging
import json
import base64

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def elicit_intent(message, responsecards):
	return {
		'dialogAction' : {
		'type' : 'ElicitIntent',
		'message' : message,
		'responseCard' : {
			'version' : 1,
			'contentType' : 'application/vnd.amazonaws.card.generic',
			'genericAttachments' : responsecards
		
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
   
def create_response_cards(data, message):
	list = []
	print len(data)
	if len(data) != 1:
		for incrementor in range(1, len(data)):
			template = {}
			if len(data[incrementor]['title']) < 80:
				title = data[incrementor]['title']
			else:
				title = data[incrementor]['title'][:78]
				title = title + ".."
			template['title'] = title
			template['attachmentLinkUrl'] = data[incrementor]['url']
			template['imageUrl'] = data[incrementor]['image_url']
			list.append(template)
		return elicit_intent(message, list)
	else:
		message = {'contentType': 'PlainText', 'content': """Sorry! No more books for {} on Amazon""".format(data['incrementor']['title'])}
		return elicit(message)
	

def view_more(event):
    print event['sessionAttributes']
    try:
        session_attributes = event['sessionAttributes']['data']
        decoded = base64.b64decode(session_attributes)
        data = json.loads(decoded)
        message = {'contentType': 'PlainText', 'content': """Here are a few more options!"""}
        return create_response_cards(data, message)
    except TypeError:
        message = {'contentType': 'PlainText', 'content': """:-O Oops I forgot what we were talking about. How about these?"""}
        return elicit(message)


def lambda_handler(event, context):
    # TODO implement
    logger.debug('input: {}'.format(event))
    return view_more(event)
