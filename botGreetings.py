import random

def lambda_handler(event, context):
    # TODO implement
    greetings = ["""When in doubt, go to the library or come to me! ;) I am a Hermione Granger, I can help you with details of technical books. Why don't you try me out: 'Suggest me a book on java?'""", """Sup dude? I am here to help you become a technical bookworm!""","""Hey there! I am Hermione Granger. I can help you mirror me, a tech bookworm!"""]
    message = {
        'dialogAction': {
            'type': 'ElicitIntent',
            'message': {
                'contentType': 'PlainText',
                'content' : random.choice(greetings)
            },  
            'responseCard' : {
                'version' : 1,
                'contentType' : 'application/vnd.amazonaws.card.generic',
                'genericAttachments' : [
                    {
                        'title' : 'I can suggest you technical books',
                        'subTitle' : """Ex: 'Suggest me a java book'. How about these to start with?""",
                        'imageUrl' : 'https://s-media-cache-ak0.pinimg.com/236x/a8/04/95/a80495d98e135c54a610e9fcfae149a8--teaching-reading-teaching-ideas.jpg',
                        'buttons' : [
                            {
                                'text' : 'Java',
                                'value' : 'show java book'
                            },
                            {
                                'text' : 'Python',
                                'value' : 'show python book'
                            },
                            {
                                'text' : 'Docker',
                                'value' : 'show docker book'
                            }
                            ]
                        
                    }
                    ]
                
            }    
        
    }
    }
    return message
