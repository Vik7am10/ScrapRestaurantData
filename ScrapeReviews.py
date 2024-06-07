import requests
from bs4 import BeautifulSoup
from langchain_openai import ChatOpenAI

# Replace with your actual OpenAI API key
#openai.api_key = 'sk-proj-V5JpVoeUec0q92bd4ZxxT3BlbkFJ5QZJ3eJKAldvTmSTbkVN'

def web_qa(reviews, query):
    openai = ChatOpenAI(
        model_name="gpt-4",
        max_tokens=2048
    )    
    reviews_text = "\n".join(reviews)
    full_prompt = f"Here are some reviews:\n\n{reviews_text}\n\n{query}"
    
    # Use the __call__ method to send the prompt to the model
    response = openai(full_prompt)
    
    
    #print(response)

def scrape_yelp_reviews(url):
    # Send a GET request to the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all the reviews on the page
    businesses = soup.find_all(class_='raw__09f24__T4Ezm')
    #reviewers = businesses.find(class_='y-css-1iy1dwt')
    #print(businesses)
    review_tags = ''
    for b in businesses[4:10] :
        review_tags = b.find_all('span', class_='raw__09f24__T4Ezm')
        #print(review_tags.text())
    
    # List to hold the text of each review
    reviews = [tag.text for tag in review_tags if tag.text]
    
    return reviews

# URL of the Yelp restaurant page
url = "https://www.yelp.ca/biz/gyubee-japanese-grill-waterloo-waterloo?hrid=Ctuw8s1CEchYMR22akiuQA&osq=Restaurants"

# Scrape the reviews from the Yelp page
reviews = scrape_yelp_reviews(url)
prompt = '''
    Given the context, please provide the folowing:
    1. Information on whether this restaurant is safe to order from
'''

web_qa(reviews,prompt)

