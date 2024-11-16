ExploreBot: A Simple Travel Chatbot
ExploreBot is an interactive chatbot designed to engage users in travel-related conversations, process their input to identify destinations, and provide insightful information about those destinations by scraping Wikipedia. This project is built using Python and leverages NLP techniques for query processing.

Features:
Conversational Engagement: Initiates and responds to user inputs with travel-related questions and comments.
Destination Processing: Processes user queries to identify travel destinations using tokenization, stopword removal, and lemmatization.
Web Scraping: Scrapes Wikipedia to fetch relevant information about the queried destination.
Randomized Conversations: Includes predefined responses and conversation starters for a dynamic chat experience.
Exit Option: Users can exit the chat at any time by typing exit.


Technologies Used:
Python Libraries:
nltk for natural language processing tasks (tokenization, stopword removal, lemmatization).
requests and BeautifulSoup for web scraping.
Wikipedia Integration: Fetches tourist information dynamically for user-specified destinations.


How to Use:
Clone the repository:
git clone https://github.com/<your-username>/ExploreBot.git
Install the required dependencies:
pip install nltk beautifulsoup4 requests
Run the chatbot:
python explorebot.py


Start chatting! Type in your favorite travel destinations or use exit to end the chat.
Future Enhancements:
Add error handling for invalid or ambiguous destinations.
Integrate APIs (e.g., Google Places API) for more comprehensive and accurate information.
Enhance the conversational flow with a larger variety of prompts and responses.
Implement a GUI version for better user interaction.


Contributions and feedback are welcome! 🚀
