from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

EMPTY = -1

POSITIVE = 1
NEUTRAL = 0
NEGATIVE = -1

key = "2260af3f04d142f58f4597d6db740ac7"
endpoint = "https://chosun-capstone-cognitive.cognitiveservices.azure.com/"

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

def detect_abuse(sentence: str) -> int:
    filter = ["시발", "개새끼", "병신", "썅", "좆같네", "좃같네", "좋같네", "아 씨", "아씨", "야발", "염병"]
    for filter_item in filter:
        if sentence.find(filter_item) is not EMPTY:
            return sentence.find(filter_item)
    return EMPTY

def sentiment_analysis_example(client):
    positive_sum = 0.0
    neutral_sum = 0.0
    negative_sum = 0.0
    count = 0
    # 1. documents 내용물에 텍스트를 입력해서 결과를 확인한다.
    # 2. 결과를 스크린샷으로 찍는다. (10개 정도)
    # 3. 스크린샷을 sample_screenshots 폴더에 올린다.
    # 4. 스크린샷을 보고 어떻게 정확도를 올릴까 분석해본다.
    documents = ["야 이 병신아"]
    
    # 미리 걸러낼 것들이 있으면 if문으로 걸러내기
    if documents[0].find("ㅋㅋㅋㅋㅋ") is not EMPTY:
        print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(1.0, 0.0, 0.0))
        positive_sum = 1.0
    elif documents[0].find("ㅠㅠ") is not EMPTY:
        pass            # pass로 나중에 코드 입력하도록 남겨둠
    elif detect_abuse(documents[0]) is not EMPTY:
        print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(0.0, 0.0, 1.0))
        negative_sum = 1.0
    else:
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
            positive_sum += sentence.confidence_scores.positive
            neutral_sum += sentence.confidence_scores.neutral
            negative_sum += sentence.confidence_scores.negative
            count += 1
        
    if max(positive_sum, neutral_sum, negative_sum) is positive_sum:
        return POSITIVE
    elif max(positive_sum, neutral_sum, negative_sum) is neutral_sum:
        return NEUTRAL
    else:
        return NEGATIVE
          
result = sentiment_analysis_example(client)
print("Result =", result)