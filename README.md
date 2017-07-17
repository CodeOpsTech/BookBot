# BookBot
This BookBot is for finding technical books from Amazon

# Why BookBot?
'When in doubt, go to the library' says Hermione Granger, the famous bookworm character from the Harry Potter series. 

The best way to learn something is to read! Searching for books online has always been a difficult task with numerous options available from numerous websites. BookBot is here to solve it for you! It can suggest you the top rated book from Amazon(the best destination for book lovers) given a technical topic. it can also help you with reviews, cost details, author details etc.

# How can BookBot help you?
BookBot primarily uses Amazon's API to get top rated books given a technical topic. One can converse with the bot and check out the price details(in USD), author details, reviews of the book, publisher details, cover picuture of the book, number of pages and also view other options for the given topic. 

# How to use BookBot?
Messaging to the facebook page 'BookBot' will trigger your conversation. It has been customised to respond like Hermione Granger

# BookBot Architecture
BookBot is built using AWS Lex and AWS Lambda. Below is the architectural diagram for the same:

![image](https://user-images.githubusercontent.com/19647546/28265367-f98f4576-6b0c-11e7-8f6e-54d0a3832eb0.PNG)

# What's the future?
BookBot is currently limited to books and reviews from Amazon. Addition of books and reviews from goodreads and other websites. 

1. Addition of 'Compare' feature so that users can compare books, reviews and cost details across other websites
2. check for discounts and offers
3. Preview/first few pages of the book

# Prerequisites for the code:
1. Python 2.7 with python-amazon-simple-product-api module 
2. Amazon API credentials for the amazon simple product API


