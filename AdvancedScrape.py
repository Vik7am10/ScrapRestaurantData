from langchain_community.document_loaders import WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_openai import ChatOpenAI

def web_qa(url_list, query):
    openai = ChatOpenAI(
        model_name="gpt-4",
        max_tokens=2048
    )
    loader_list = []
    for i in url_list:
        print('loading url: %s' % i)
        loader_list.append(WebBaseLoader(i))
    
    index = VectorstoreIndexCreator().from_loaders(loader_list)
    ans = index.query(query)
    print("")
    print(ans)

#can add urls here
url_list = []


prompt = '''
    Given the context, please provide the folowing:
    1. summary
    2. details
'''

web_qa(url_list, prompt)

OPENAI_API_KEY='sk-proj-VDO47fkDwMiT1f8KpgnjT3BlbkFJ2UzLnLfcR3abDRMQQKpF'