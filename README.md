# COSC310-Friend-Chatbot 2.0
![ChatbotImage](https://s3-eu-west-1.amazonaws.com/userlike-cdn-blog/do-i-need-a-chatbot/header-chat-box.png)

## About the project
This repository contains a programming project code for a chatbot that simulates a conversation between friends. 
A specific topic about soccer and some scattered topics are covered.

## Prepare stage
before we start running this code we need to download several libraries
```bash
pip install nltk
pip install -U spacy
python -m spacy download en_core_web_lg
pip install pyspellchecker
pip install -U textblob
```

## How to run the code
run [socket_server.py](https://github.com/COSC310-A2-Team10/COSC310-Friend-ChatBot-A3/blob/main/socket_server.py) first to create a server for project,

then using Command Prompt run [chatbox.py](https://github.com/COSC310-A2-Team10/COSC310-Friend-ChatBot-A3/blob/main/chatbox.py)

## Some features
1. the system can clean all punctuations in the sentence and convert sentence to lower case

2. the system can remove suffixes (e.g.playing and play) and 
convert all the words back to root form (e.g. apples and apple)

3. the system can clean all the words with not much meaning in the sentence (e.g. 'a', 'is')

4. a simple GUI so that the user is typing into a nicer interface and can view a recent history of the conversation

5. new topics about basketball is added to improve the conversation of agent

6. a feature enables agent to give at least 5 different reasonable responses when the user enters something beyond the two topics

7. a feature enables the system to handle spelling mistakes of the words to improve the fluency of conversation
