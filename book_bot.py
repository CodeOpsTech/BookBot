import logging
import math
from amazon.api import AmazonAPI
import unicodedata
import base64
import json


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def get_slots(intent_request):
    return intent_request['currentIntent']['slots']

def build_validation_result(is_valid, violated_slot, message_content):
    if message_content is None:
        return {
            "isValid": is_valid,
            "violatedSlot": violated_slot,
        }

    return {
        'isValid': is_valid,
        'violatedSlot': violated_slot,
        'message': {'contentType': 'PlainText', 'content': message_content}
    }

	
def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }

    return response
	
# function to validate the title entered as a technical one
def is_valid_category(ancestor):
	list = ['Computers & Technology', 'Business Technology', 'Certification', 'Computer Science', 'Databases & Big Data', 'Digital Audio, Video & Photography' , 'Games & Strategy Guides', 'Graphics & Design', 'Hardware & DIY', 'History & Culture', 'Internet & Social Media ', 'Mobile Phones, Tablets & E-Readers', 'Networking & Cloud Computing', 'Operating Systems' , 'Programming', 'Programming Languages', 'Security & Encryption', 'Software', 'Web Development & Design']
	return ancestor in list

# function to create a dictionary of the book details
def get_details(dataOfAllBooks, book):
	content = {}
	book_url = book.detail_page_url 
	book_url = book_url.split('?',1)[0]
	auth = ', '.join(book.authors)
	name = unicodedata.normalize('NFKD', unicode(auth)).encode('ascii', 'ignore')
	image = book.large_image_url
	book_price = book.price_and_currency[0]
	price = book_price
	if len(book.title) < 80:
		title = book.title
	else:
		title = book.title[:78] + ".."
	content['title'] = title
	content['url'] = book_url
	content['authors'] = name
	content['image_url'] = image
	content['publisher'] = book.publisher 
	content['year'] = book.publication_date.year
	content['isbn'] = book.isbn
	content['price'] = str(price)
	content['pages'] = book.pages
	content['reviews_url'] = book.reviews[1]
	content['sales_rank'] = book.sales_rank
	
	dataOfAllBooks.append(content)
	return dataOfAllBooks

# function to get the book details from Amazon.com
def getTop5Books(queryTerm):
	AWSAccessKeyId = 'AKIAJCMZHQR6KKOAH4SQ'
	AWSSecretKey = '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'
	associateTag = '200b3-21'
	dataOfAllBooks = []
	api = AmazonAPI(AWSAccessKeyId , AWSSecretKey , associateTag)
	try:
		books = api.search(Keywords = queryTerm, SearchIndex = 'Books', salesrank = 'Bestselling')
		incrementor = 0
		num_of_books = 1
		for _, book in enumerate(books):
			if num_of_books <= 5:
				book_price = book.price_and_currency[0]
				# skip the book if it is free (they could be promotional stuff)
				if book_price and book.pages and int(book.pages) >= 50:
					node = book.browse_nodes[0]
					category = node.ancestor.name
					if (category == 'Books'):
						continue
					else:
						if not (is_valid_category(category)):
							category = node.ancestor.ancestor.name
							if (is_valid_category(category)):
								dataOfAllBooks = get_details(dataOfAllBooks, book)
								incrementor += 1
								num_of_books += 1
						else:
							dataOfAllBooks = get_details(dataOfAllBooks, book)
							incrementor += 1
							num_of_books += 1
			else:
				break 

		return dataOfAllBooks
	except:
		message = {'contentType': 'PlainText', 'content': """Sorry, no such technical book on Amazon. Please try something else. Ex: suggest me a java book"""}
		return message


	
def isvalid_name(name):
	if name is None:
		return False
	return True
	
def validate(name):
	#try:
	if not isvalid_name(name) :
	
		return build_validation_result(False, 'title', 'Please enter a name ')
	#except SearchException:
	#	return build_validation_result(False, 'title', 'Amazon does not have {}, would you like a different book?  '.format(name))
	
	return build_validation_result(True, None, None)
	
def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': message
        }
    }
	
	
def delegate(session_attributes, slots):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }
def confirm_intent(session_attributes, intent_name, slots, message, book_title, book_image_url, book_url):
	dict = json.dumps(session_attributes)
	encoded_data = base64.b64encode(dict)
	return {
	    'sessionAttributes': {
			'data' : "{}".format(encoded_data)
			},
		'dialogAction': {
			'type': 'ElicitIntent',
			'message': message,
			'responseCard' : {
				'version' : 1,
				'contentType' : 'application/vnd.amazonaws.card.generic',
				'genericAttachments': [
				{	
					'title' : book_title,
					'imageUrl' : book_image_url,
					'attachmentLinkUrl' : book_url,
					'buttons' : [
						{
							'text' : 'More about the author(s)',
							'value' : 'author?'
						},
						{
							'text' : 'Cost',
							'value' : 'what is the cost'
						},
						{
							'text' : 'More options',
							'value' : 'view more'
						},
						{
							'text' : 'Check the reviews',
							'value' : 'reviews'
						}
						
					]
				}
			]
		}
		}
	}

def elicit_intent(message):
	return {
		'dialogAction' : {
		'type' : 'ElicitIntent',
		'message' : message,
		}
	
	}
		
def order_book(intent_request):
	
	source = intent_request['invocationSource']
	output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}
	slots = get_slots(intent_request)
	name = slots['title']
	
	validation_result = validate(name)
	
	if source == 'DialogCodeHook':
		data = getTop5Books(name)
		try:
			count = 0
			book_title = data[0]['title']
			book_authors = data[0]['authors']
			book_pages = data[0]['pages']
			book_price = data[0]['price']
			book_url = data[0]['url']
			book_image_url = data[0]['image_url']
			if not validation_result['isValid']:
				slots[validation_result['violatedSlot']] = None
				return elicit_slot(data, intent_request['currentIntent']['name'], slots, validation_result['violatedSlot'],validation_result['message'])
			message = {'contentType': 'PlainText', 'content': 'Sure! According to Amazon, the top rated book for \"{}\" is: {} by {} and has {} pages. It costs ${}. You can find more information at: \'{}\''.format(name, book_title, book_authors, book_pages, book_price, book_url)}
			return elicit_intent(message)
		except KeyError:
			return elicit_intent(data)
		
	else:
		if not validation_result['isValid']:
			slots[validation_result['violatedSlot']] = None
			return elicit_slot(output_session_attributes, intent_request['currentIntent']['name'], slots, validation_result['violatedSlot'],validation_result['message'])
		try:
			data = getTop5Books(name)
			count = 0
			book_title = data[0]['title']
			book_authors = data[0]['authors']
			book_pages = data[0]['pages']
			book_price = data[0]['price']
			book_url = data[0]['url']
			book_image_url = data[0]['image_url']
			if intent_request['currentIntent']['confirmationStatus'] == 'None':
				return confirm_intent(data, intent_request['currentIntent']['name'], slots, {'contentType': 'PlainText', 'content': 'Sure! According to Amazon, the top rated book for \"{}\" is: {} by {}'.format(name, book_title, book_authors)}, book_title, book_image_url, book_url)
				
			else:
				return close(output_session_attributes, 'Fulfilled', {'contentType': 'PlainText', 'content': 'Thanks! Your order for {} has been placed'.format(book_title)})
		except KeyError:
			return elicit_intent(data)
			
			
def check_intent(intent_request):
    
    logger.debug('check_intent userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))

    intent_name = intent_request['currentIntent']['name']

    if intent_name == 'LexIntent':
        return order_book(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')


def lambda_handler(event, context):

	print("Log stream name:", context.log_stream_name)
	print("Log group name:",  context.log_group_name)
	output = check_intent(event)
	logger.debug('event.bot.name={}, input_from_lex = {}, output_to_lex = {}'.format(event['bot']['name'],event, output))
	
	return output