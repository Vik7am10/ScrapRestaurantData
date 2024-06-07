import requests
from bs4 import BeautifulSoup
import os
from openai import OpenAI

def web_qa(url, query):
    response = requests.get(url)
    
    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the text content from the HTML
    html_content = soup.get_text()
    client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": html_content + prompt,
            }
        ],
        model="gpt-4",
    )
    print("")
    print(chat_completion)

url = "https://www.yelp.ca/biz/gyubee-japanese-grill-waterloo-waterloo?hrid=Ctuw8s1CEchYMR22akiuQA&osq=Restaurants"

prompt = '''
    Given the context, please provide the folowing:
    1. Inferences you can make from the reviews
'''

web_qa(url, prompt)

OPENAI_API_KEY='sk-proj-VDO47fkDwMiT1f8KpgnjT3BlbkFJ2UzLnLfcR3abDRMQQKpF'