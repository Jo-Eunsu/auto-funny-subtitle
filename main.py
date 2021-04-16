

# JSON 파일을 불러오기 위해 모듈 임포트
import json

# Azure Text Analytics API 모듈
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# XML 파일을 불러오기 위해 모듈 임포트
from xml.etree.ElementTree import Element, ElementTree, parse

# AI API에서 제공하는 감정의 리스트와 상수
POSITIVE = 0
NEUTRAL = 1
NEGATIVE = 2

# 기타 상수값 지정
EMPTY = -1

import sys

# Azure API에 관한 클래스
class AzureAnalytics:
    # Azure AI Text Analytics 서비스에 연결
    __key = "2260af3f04d142f58f4597d6db740ac7"
    __endpoint = "https://chosun-capstone-cognitive.cognitiveservices.azure.com/"
    __client = None

    # API 객체가 중복 생성되면 안 되므로 싱글톤 클래스로 지정
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(AzureAnalytics, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self.__client = self.authenticate_client()
    def authenticate_client(self) -> TextAnalyticsClient:
        ta_credential = AzureKeyCredential(self.__key)
        text_analytics_client = TextAnalyticsClient(
                endpoint=self.__endpoint, 
                credential=ta_credential)
        return text_analytics_client
    def get_client(self) -> TextAnalyticsClient:
        return self.__client



# 자막 템플릿의 JSON 처리에 관한 클래스
class Template_JSON:
    # 자막 템플릿의 정보가 담겨 있는 딕셔너리 - {"감정": [한 감정에 들어 있는 자막 템플릿의 정보 리스트]} 형태
    __template_info = {}
    # 각 자막 템플릿의 유형 중 몇 번째 자막을 선택할 것인지 결정하는 리스트
    __template_select = []
    # 자막 템플릿의 감정 유형을 저장하는 딕셔너리. {"감정": "지정값"}으로 이루어짐
    __emotions = {}
    __emotion_count = 0

    # 생성자
    def __init__(self) -> None:
        # 템플릿 객체에 우리가 사용할 감정 추가
        # 각 위치는 0번째부터 POSITIVE, NEUTRAL, NEGATIVE 순으로 지정
        self.add_emotion("positive")
        self.add_emotion("neutral")
        self.add_emotion("negative")

        # 추가한 감정에 맞는 템플릿 파일 불러오기
        self.append_template("title-template/positive-1.json", "positive")
        self.append_template("title-template/neutral-1.json", "neutral")
        self.append_template("title-template/negative-1.json", "negative")

        # 각 감정마다 몇 번째로 추가한 템플릿을 쓸 건지 결정
        self.set_template_selection([0, 0, 0])

    def __open_json(self, json_file_path: str) -> dict:
        try:
            with open(json_file_path) as json_file:
                template_json_dict = json.load(json_file)
                return template_json_dict
        except FileNotFoundError as fe:
            print(json_file_path + ": json 파일을 찾지 못했습니다.")
            print(fe)
            return None
    # 감정 유형을 더하는 함수
    def add_emotion(self, emotion: str):
        self.__emotions[emotion] = self.__emotion_count
        self.__template_info[emotion] = []
        self.__template_select.append(0)
        self.__emotion_count += 1
    # 자막 템플릿의 정보가 저장된 JSON 파일을 불러와 리스트에 추가
    def append_template(self, input_json_dest: str, type_str: str) -> None:
        json_dict = self.__open_json(input_json_dest)
        # AI API가 제공하는 다양한 감정타입에 따라 자막 템플릿 분류 -> "type": positive, neutral, negative 등
        self.__template_info[type_str].append(json_dict)
    # 자막 템플릿의 정보 표시
    def show_templates(self):
        try:
            print("- 자막 템플릿 정보 -")
            if len(self.__template_info) < 1:
                raise ValueError
            for template_item in self.__template_info:
                print(self.__template_info[template_item])
                print()
        except ValueError as ve:
            print("불러온 자막 템플릿이 없거나 값에 오류가 발생했습니다.")
            print(ve)
        except Exception:
            print("자막 템플릿 정보를 불러오는 데 문제가 발생했습니다.")
    # 몇 번째 자막 템플릿을 지정할 것인지 지정하는 함수
    def set_template_selection(self, selection_numbers: list):
        for i, num in enumerate(selection_numbers):
            self.__template_select[i] = num
    
    # 감정분석 결과에 따라 미리 저장된 템플릿 정보(딕셔너리)를 꺼내오는 함수
    def get_template(self, emotion: str) -> dict:
        return self.__template_info[emotion][self.__template_select[self.__emotions[emotion]]]

    # 각 감정 키에 해당하는 값을 리턴하는 함수
    def get_emotion_value(self, emotion: str) -> int:
        return self.__emotions[emotion]

    

# FCPX XML 처리에 관한 클래스
class FCPX_XML:
    # 입력받은 XML 파일을 파싱한 결과를 저장할 ElementTree 객체
    __xml_tree = None
    # 위 객체의 루트
    __xml_root = None
    # 새로 만들어진 XML 파일이 저장될 경로
    __output_xml_dest = ""

    # 템플릿 정보 파일(JSON)을 처리하는 객체 생성
    __funny_title_text_templates = Template_JSON()

    # 기본 생성자: XML을 불러와 ElementTree 자료형으로 저장, Azure AI API의 클라이언트 정보 불러오기
    def __init__(self, input_xml_dest: str) -> None:
        # input_xml_dest 경로에 있는 xml 파일을 파싱한 데이터를 __xml_tree에 저장
        self.__xml_tree = parse(input_xml_dest)
        # __xml_tree 객체의 루트 노드 찾기
        self.__xml_root = self.__xml_tree.getroot()
        # Azure Text Analytics 서비스의 클라이언트 객체 얻기
        self.__api_client = AzureAnalytics().get_client()
        # 수정된 XML 파일의 이름을 따로 지정
        self.__output_xml_dest = input_xml_dest.replace(".fcpxml", "") + "-edit.fcpxml"

    # Azure AI Text Analytics 서비스(client)를 이용해 텍스트(documents)의 감정(긍정, 중립, 부정) 분석
    def __sentiment_analysis(self, documents: list) -> str:
        # API를 사용하여 입력받은 텍스트의 감정을 분석하고, 분석 결과를 response에 저장
        response = self.__api_client.analyze_sentiment(documents=documents, language="ko")[0]
        # 텍스트 분석 결과를 긍정값, 중립값, 부정값 순서로 딕셔너리로 리턴
        result_score = {
            "positive": response.confidence_scores.positive,        # 긍정 값
            "neutral": response.confidence_scores.neutral,         # 중립 값
            "negative": response.confidence_scores.negative        # 부정 값
        }

        # 정확도 개선 로직 추가가 필요한 부분
        if result_score["positive"] >= 0.5:
            result_emotion = "positive"
        elif result_score["negative"] >= 0.5:
            result_emotion = "negative"
        else:
            result_emotion = "neutral"
        
        return result_emotion

    # 각 자막 텍스트에 대해 감정분석
    def xml_text_analysis(self) -> None:
        # XML에서 자막에 해당되는 클립 정보를 읽기
        try:
            # asset-clip 태그를 찾기
            # asset-clip 태그는 파이널컷에서 메인 스토리라인에 들어가는 각 동영상 클립의 정보
            for asset_clip in self.__xml_root.iter("asset-clip"):
                for title in asset_clip.findall("title"):
                    # 자막 텍스트 추출
                    title_text = [title.find("text").findtext("text-style"),]
                    title_offset = title["offset"]
                    print(title_text[0], "- 스타일: ", title.attrib["ref"])
                    # 읽어들인 자막 텍스트를 바탕으로 문장 감정을 분석해 최종 감정을 문자열로 출력
                    result_analysis = self.__sentiment_analysis(title_text)
                    self.title_xml_modification(title, result_analysis, title_offset)
                
                

        except KeyboardInterrupt:
            print("\n\n사용자에 의한 강제 취소\n")

    # 자막 텍스트 자체의 정보가 저장된 effect 태그를 새로 쓰는 함수
    def effect_xml_modifiction(self, emotion: str):
        effect_tag_info = self.effect_tag(emotion)

    # 자막 텍스트의 감정에 따라 예능자막을 지정해서 XML을 고쳐쓰는 함수
    def title_xml_modification(self, text: str, emotion: str, offset: str) -> None:
        pass 

    # XML에서 특정 감정(emotion)에 자막 템플릿의 정보가 들어 있는 effects 태그의 객체(Element)를 생성해주는 메소드
    def effect_tag(self, emotion: str) -> Element:
        emotion_json = self.__funny_title_text_templates.get_template(emotion)
        effect_element = Element(tag="effect", attrib=emotion_json["effect"])
        return effect_element

    # XML에서 각 자막 클립에 특정 자막 템플릿을 적용시킨 video 태그의 객체(Element)를 생성해주는 메소드
    def title_video_tag(self) -> Element:
        pass

    # 새로운 XML 파일을 작성하는 메소드
    def write_xml(self):
        # 수정된 트리(__xml_tree)를 새로운 파일 경로(__output_xml_dest)에 fcpxml 파일로 작성
        self.__xml_tree.write(self.__output_xml_dest)


# 메인함수 실행
def main() -> int:

    # 파이널 컷 XML 파일을 읽어오고 파이널컷 예능자막 템플릿 정보 추출
    fcpx_xml = FCPX_XML(sys.argv[1])
    # XML의 자막 텍스트를 읽어와서 텍스트 정보 분석 후 수정
    fcpx_xml.xml_text_analysis()
    # 수정된 XML 파일을 따로 저장
    fcpx_xml.write_xml()

    return 0

# output_xml_file = xml_file.replace(".fcpxml", "_edit.fcpxml")
# video_info.write(output_xml_file, encoding="utf-8", xml_declaration=True) 

# 이 코드가 처음으로 실행될 경우 메인함수 실행
if __name__ == '__main__':
    print("program exited with code", main())
    