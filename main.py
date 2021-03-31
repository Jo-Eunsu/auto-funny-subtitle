# JSON 파일을 불러오기 위해 모듈 임포트
import json

# Azure Text Analytics API 모듈
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# XML 파일을 불러오기 위해 모듈 임포트
from xml.etree.ElementTree import parse

import sys

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

# Azure AI Text Analytics 서비스(client)를 이용해 텍스트(documents)의 감정(긍정, 중립, 부정) 분석
def sentiment_analysis(client, documents):
    # API를 사용하여 입력받은 텍스트의 감정을 분석하고, 분석 결과를 response에 저장
    response = client.analyze_sentiment(documents=documents, language="ko")[0]
    # 텍스트 분석 결과를 긍정값, 중립값, 부정값 순서로 딕셔너리로 리턴
    result_score = {
        "positive": response.confidence_scores.positive,        # 긍정 값
        "neutral": response.confidence_scores.neutral,         # 중립 값
        "negative": response.confidence_scores.negative        # 부정 값
    }
    return result_score

# 파이널 컷 XML 파일을 읽어와서 파이널컷 예능자막 템플릿 정보 추출
xml_file = sys.argv[1]
video_info = parse(xml_file)
root = video_info.getroot()

# 예능자막 템플릿에 관한 정보를 태그 형태로 만들기 위해서
# 딕셔너리 형태의 정보 기록
with open('title-template/neutral-1.json') as positive_sub_file:
    positive_sub = json.load(positive_sub_file)


# XML에서 자막에 해당되는 클립 정보를 읽기
for title in root.iter("title"):

    # 자막 텍스트 추출
    subtitle = [title.find("text").findtext("text-style"),]
    print(subtitle[0], "- 스타일: ", title.attrib["ref"])
    # 읽어들인 자막 텍스트를 바탕으로 문장 감정 분석
    result_analysis = sentiment_analysis(client, subtitle)
    print("positive: ", result_analysis["positive"])
    print("neutral: ", result_analysis["neutral"])
    print("negative: ", result_analysis["negative"])



# output_xml_file = xml_file.replace(".fcpxml", "_edit.fcpxml")
# video_info.write(output_xml_file, encoding="utf-8", xml_declaration=True) 