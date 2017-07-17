def elicit_intent(message):
    return {
        'dialogAction' : {
		'type' : 'ElicitIntent',
		'message' : message
		}
    }

def lambda_handler(event, context):
    message = {'contentType' : 'PlainText', 'content' : 'This feature is on the way :)! Please try out the available ones.'}
    return elicit_intent(message)