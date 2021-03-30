
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

from xml.etree.ElementTree import parse


# Azure AI Text Analytics 서비스에 연결
key = "2260af3f04d142f58f4597d6db740ac7"
endpoint = "https://chosun-capstone-cognitive.cognitiveservices.azure.com/"
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client
client = authenticate_client()

# Azure AI Text Analytics 서비스(client)를 이용해 
# 텍스트(documents)의 감정(긍정, 중립, 부정) 분석
def sentiment_analysis(client, documents):
    
    response = client.analyze_sentiment(documents=documents, language="ko")
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
          
sentiment_analysis(client, "모든 게 여유로워 보이는 이른 시간")

# Import & Parse XML File
video_info = parse('video-sample/히밥님...재료가 다 떨어졌어요...-TTfzRbSFtLY.fcpxml')
root = video_info.getroot()

for title in root.iter("title"):
    print(title.attrib["name"], "- 스타일: ", title.attrib["ref"])