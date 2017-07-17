import ast
import json
import unicodedata
import base64
from amazon.api import AmazonAPI
import logging
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
					'text' : 'python',
					'value' : 'show python book'
				}
			]
		}
		]
	}
		}
	}
	
def create_response_cards(books_list, books_url, books_image):
	length = books_list.__len__()
	list = []
	for incrementor in range(length):
		template = {}
		template['title'] = books_list[incrementor]
		template['attachmentLinkUrl'] = books_url[incrementor]
		template['imageUrl'] = books_image[incrementor]
		list.append(template)
	return list	

def lambda_handler(event, context):	
	logger.debug('input to lambda: {}'.format(event) )
	try:
		session_attributes = event['sessionAttributes']['data']
		decoded = base64.b64decode(session_attributes)
		data = json.loads(decoded)
		title = data[0]['title']
		
		AWSAccessKeyId = 'AKIAJCMZHQR6KKOAH4SQ'
		AWSSecretKey = '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'
		associateTag = '200b3-21'
		api = AmazonAPI(AWSAccessKeyId , AWSSecretKey , associateTag)
		decoded = base64.b64decode(session_attributes)
		
		data = json.loads(decoded)
		print data[0]
		book_authors = []
		book_authors = str(data[0]['authors']).split(",")
		print 'authors after split:', book_authors
		length = book_authors.__len__()
		books_list = range(length)
		
		books_url = []
		books_image = []
		for incrementor in range(length):
			book_titles = ""
			book_url = ""
			book_image_url = ""
			number = 0
			print 'Author: ', book_authors[incrementor]
			
			books = api.search(Author = book_authors[incrementor], SearchIndex = 'Books', salesrank = 'Bestselling')
			for _, book in enumerate(books):
				if number == 0:
					book_titles =  book.title[:78] + '..'
					if book_titles == title:
						continue
					else:
						#book_titles =  book.title 
						book_url = book.detail_page_url.split('?',1)[0]
						book_image_url = book.large_image_url
						number += 1
				else:
					break
				print 'other books by {} are {}'.format(book_authors[incrementor], book_titles)
				books_list[incrementor] = book_titles
				books_url.append(book_url)
				books_image.append(book_image_url)
		print 'titles: ', books_list
		print 'urls: ', books_url
		print 'images: ', books_image
		content = ""
		for len in range(books_list.__len__()):
			content = content + " " + str(books_list[len])
		message = {'contentType': 'PlainText', 'content': """The author(s) for {} is {}. Other books by the same author(s): {}""".format(data[0]['title'], data[0]['authors'], content)}

		print books_list
		output = elicit_intent(message, create_response_cards(books_list, books_url, books_image))
		logger.debug('output to lex: {}'.format(output))
		return output
	
	except:
		message = {'contentType': 'PlainText', 'content': """Please choose a book first. How about these:"""}
		return elicit(message)