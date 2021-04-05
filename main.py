from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "2260af3f04d142f58f4597d6db740ac7"
endpoint = "https://chosun-capstone-cognitive.cognitiveservices.azure.com/"

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

def sentiment_analysis_example(client):
    # 1. documents 내용물에 텍스트를 입력해서 결과를 확인한다.
    # 2. 결과를 스크린샷으로 찍는다. (10개 정도)
    # 3. 스크린샷을 sample_screenshots 폴더에 올린다.
    # 4. 스크린샷을 보고 어떻게 정확도를 올릴까 분석해본다.
    documents = ["여기에 텍스트 입력"]
    response = client.analyze_sentiment(documents=documents, language="ko")[0]
    print("Document Sentiment: {}".format(response.sentiment))
    print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
        response.confidence_scores.positive,
        response.confidence_scores.neutral,
        response.confidence_scores.negative,
    ))
    for idx, sentence in enumerate(response.sentences):
        print("Sentence: {}".format(sentence.text))
        print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
        print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
            sentence.confidence_scores.positive,
            sentence.confidence_scores.neutral,
            sentence.confidence_scores.negative,
        ))
          
sentiment_analysis_example(client)