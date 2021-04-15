from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

EMPTY = -1

POSITIVE = 1
NEUTRAL = 0
NEGATIVE = -1 # 프로그램 작성 하기 쉽게 매크로 변수지정

key = "2260af3f04d142f58f4597d6db740ac7"   #애저의 텍스트 애널리틱스 라는 놈의 api에 접속하기 위한 키
endpoint = "https://chosun-capstone-cognitive.cognitiveservices.azure.com/"   #접속하기 위한 엔드포인트(있어야 api에 접속할수있다)

def authenticate_client():   #api에 연결시키는 함수로서 이미 정의 된 함수를 가져와 사용 이름을 바꿀수 없음
    ta_credential = AzureKeyCredential(key)  
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()  #client는 api연결이 성공하면 client변수에다가 api에 접속하기 위한 값을 대입 (api에 접속하는 클라이언트 변수 선언)

def detect_abuse(sentence: str) -> int: #욕설 걸러주는 함수인데 sentence(인자값)를 사용해서 문자열로 받아낸다. return값이 int임을 나타냄 
    filter = ["시발", "개새끼", "병신", "썅", "좆같네", "좃같네", "좋같네", "아 씨", "아씨", "야발"]
    for filter_item in filter: #item은 하나씩 골라서 index로 저장시키는 함수이다.
        if sentence.find(filter_item) is not EMPTY: #filter_item의 숫자를 돌려 받아낸후 비어있는지 확인한다
            return sentence.find(filter_item)  #비어있는게 아니니까 -1대신 원래 기존 값을 리턴한다
    return EMPTY  # 포함되는게 없는 상태이므로 -1을 반환한다.

def detect_interjection(sentence: str) -> int:
    filter = ["무야호", "오진다", "오매", "좋은그" ]
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
    documents = ["신나는 토요일 밤 유후~"]
    
    # 미리 걸러낼 것들이 있으면 if문으로 걸러내기
    with open("analysis-results/" + documents[0] + ".txt", "w") as result_file:
      if documents[0].find("ㅋㅋㅋㅋㅋ") is not EMPTY:
          result_file.write("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n\n".format(1.0, 0.0, 0.0))
          positive_sum = 1.0
      elif documents[0].find("ㅠㅠ") is not EMPTY:
          pass            # pass로 나중에 코드 입력하도록 남겨둠
      elif detect_abuse(documents[0]) is not EMPTY:
          result_file.write("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n\n".format(0.0, 0.0, 1.0))
          negative_sum = 1.0
      elif detect_interjection(documents[0]) is not EMPTY:
          result_file.write("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n\n".format(1.0, 0.0, 0.0))
          positive_sum = 1.0
      else:
          response = client.analyze_sentiment(documents=documents, language="ko")[0]
          result_file.write("Document Sentiment: {}\n".format(response.sentiment))
          result_file.write("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n\n".format(
              response.confidence_scores.positive,
              response.confidence_scores.neutral,
              response.confidence_scores.negative,
          ))
          for idx, sentence in enumerate(response.sentences):
              result_file.write("Sentence: {}".format(sentence.text) + "\n")
              result_file.write("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment) + "\n")
              result_file.write("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
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