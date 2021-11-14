from dotenv import load_dotenv
import os
import requests
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()

phrase_key = os.environ['AZURE_KEY']
phrase_endpoint = os.environ['AZURE_ENDPOINT']

# Conecting to Azure using documentation linked here: 
# https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/key-phrase-extraction/quickstart?pivots=programming-language-python 
def authenticate_client():
    ta_credential = AzureKeyCredential(phrase_key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=phrase_endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

def get_important_words(sentence):
    documents = [sentence]

    response = client.extract_key_phrases(documents = documents)[0]
    key_words = []
    if not response.is_error:
        key_words = response.key_phrases
    else:
        raise Exception('')
    
    return key_words

search_key = os.environ['SEARCH_KEY']
search_url = "https://api.bing.microsoft.com/v7.0/images/search"

def get_related_image(search_term):
    headers = {"Ocp-Apim-Subscription-Key" : search_key}
    params  = {"q": search_term}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    return search_results["value"][0]["contentUrl"]

