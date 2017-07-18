# BookBot
BookBot is a chatbot built using cognitive services and serverless architecture. It is a conversational interface that suggests top rated technical books from Amazon

# Why BookBot?
'When in doubt, go to the library' says Hermione Granger, the famous bookworm character from the Harry Potter series. 

The best way to learn something is to read! Searching for books online has always been a difficult task with numerous options available from numerous websites. BookBot is here to solve it for you! It can suggest you the top rated book from Amazon(the best destination for book lovers) given a technical topic. 

BookBot primarily uses Amazon's API to get top rated books given a technical topic. One can converse with the bot and upon its suggestion, one can check out the price details(in USD), author details, reviews of the book, publisher details, cover picture of the book, number of pages and also view other options for the given topic. 

# How to use BookBot?
BookBot has been customised to respond like Hermione Granger and messaging to the facebook page '<a href= "https://www.facebook.com/BookBot-1293871334043466/">BookBot</a>' will trigger your conversation. The bot can be initiated with a greeting like a 'hi' or 'hello'. The basic utterance is: 'suggest a <title> book'. Example: 'suggest a python book', this returns the top rated python book and also displays a few options() in the form of buttons. 

For more details on how to use BookBot, check out <a href= "https://github.com/CodeOpsTechnologies/BookBot/blob/master/Testing%20instructions">Testing instructions</a>.

# BookBot Architecture
BookBot is built using:
1. AWS Lex - for Natural Language Processing 
2. AWS Lambda - serverless platform for the business logic
3. CloudWatch - to monitor and log data of various Lambda functions

Below is the architectural diagram for the same:

![image](https://user-images.githubusercontent.com/19647546/28272569-84d35a0c-6b29-11e7-820d-f0d4db1144e5.PNG)

# What to expect in the future?
BookBot is currently limited to technical books and reviews from Amazon. Future additions:

1. Books and reviews from goodreads and other websites 
2. Expanding the scope of suggestions for other genres as well
3. Addition of 'Compare' feature so that users can compare books, reviews and cost details across other websites
4. Details of discounts and offers
5. Preview/first few pages of the book 

# Prerequisites for using the code:
1. Python 2.7 with python-amazon-simple-product-api module 
2. Amazon API credentials for the amazon simple product API and embedding the same while creating the Lambda function


