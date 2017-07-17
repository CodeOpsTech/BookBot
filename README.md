# BookBot
Bookbot is a chatbot built using cognitive services and serverless architecture. It is a very conversational interface for finding technical books from Amazon

# Why BookBot?
'When in doubt, go to the library' says Hermione Granger, the famous bookworm character from the Harry Potter series. 

The best way to learn something is to read! Searching for books online has always been a difficult task with numerous options available from numerous websites. BookBot is here to solve it for you! It can suggest you the top rated book from Amazon(the best destination for book lovers) given a technical topic. it can also help you with reviews, cost details, author details etc.

BookBot primarily uses Amazon's API to get top rated books given a technical topic. One can converse with the bot and check out the price details(in USD), author details, reviews of the book, publisher details, cover picuture of the book, number of pages and also view other options for the given topic. 

# How to use BookBot?
Bookbot has been customised to respond like Hermione Granger and messaging to the facebook page '<a href= "https://www.facebook.com/BookBot-1293871334043466/">BookBot</a>' will trigger your conversation. The bot can be initiated with a gretting like a 'hi' or 'hello'. BookBot suggests the top rated book on Amazon for a given technical topic. 

The basic utterance is: 'suggest a <title> book'. Example: 'suggest a python book', this returns the top rated python book and also displays a few options in the form of buttons. 

Please check out <a href= "BookBot/Testing instructions">Testing instructions</a> for more details on how to use BookBot.

# BookBot Architecture
BookBot is built using:
1. AWS Lex - for Natural Language Processing 
2. AWS Lambda - serverless platform for the business logic
3. CloudWatch - to monitor and log data of various Lambda functions.

Below is the architectural diagram for the same:

![image](https://user-images.githubusercontent.com/19647546/28272569-84d35a0c-6b29-11e7-820d-f0d4db1144e5.PNG)

# What to expect in the future?
BookBot is currently limited to books and reviews from Amazon. Addition of books and reviews from goodreads and other websites. 

1. BookBot is currently limited only to technical books, the bot will be available for all the genres in the future
2. Addition of 'Compare' feature so that users can compare books, reviews and cost details across other websites
3. Details of discounts and offers
4. Preview/first few pages of the book 

# Prerequisites for using the code:
1. Python 2.7 with python-amazon-simple-product-api module 
2. Amazon API credentials for the amazon simple product API and embedding the same while creating the Lambda function


