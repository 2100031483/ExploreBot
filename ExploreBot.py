import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import random
import requests
from bs4 import BeautifulSoup


convo_starters = [
    "Tell me about a place you'd like to visit.",
    "What's your dream travel destination?",
    "If you could travel anywhere, where would you go?",
    "Do you have a favorite travel destination?"
]

convo_responses = [
    "I've always wanted to visit {destination}! It's such a fascinating place.",
    "That sounds like an amazing destination. I'd love to learn more about it.",
    "I've heard so many great things about {destination}. It's definitely on my travel bucket list."
]
def process_query(query):
    tokens = word_tokenize(query.lower())
    tokens = [token for token in tokens if token not in stopwords.words('english') and token not in string.punctuation]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens

def scrape_tourist_info(destination):
    url = f'https://en.wikipedia.org/wiki/{destination.replace(" ", "_")}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.find('div', id='mw-content-text')
        paragraphs = content.find_all('p')
        tourist_info = ''
        for p in paragraphs:
            tourist_info += p.get_text() + '\n'
        return tourist_info
    else:
        return "Sorry, I couldn't find information about that destination."
def travel_chatbot():
    print("Welcome to the ExploreBot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        processed_query = process_query(user_input)
        destination = ' '.join(processed_query)
        tourist_info = scrape_tourist_info(destination)
        if tourist_info:
            print("Chatbot:", tourist_info)
        else:
            print("Chatbot:", random.choice(convo_responses).format(destination=destination))
            print("Chatbot:", random.choice(convo_starters))

# Run the chatbot
travel_chatbot()
