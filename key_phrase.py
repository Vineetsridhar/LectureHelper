from dotenv import load_dotenv
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()

key = os.environ['AZURE_KEY']
endpoint = os.environ['AZURE_ENDPOINT']

# Conecting to Azure using documentation linked here: 
# https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/key-phrase-extraction/quickstart?pivots=programming-language-python 
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
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
    