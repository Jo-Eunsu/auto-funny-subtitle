

# JSON 파일을 불러오기 위해 모듈 임포트
import json

# Azure Text Analytics API 모듈
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# XML 파일을 불러오기 위해 모듈 임포트
from xml.etree.ElementTree import Element, ElementTree, SubElement, parse

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
    # 각 자막 템플릿의 유형 중 몇 번째 자막을 선택할 것인지 결정하는 딕셔너리 - {"감정": 자막 번호}
    __template_select = {}
    # 자막 템플릿의 감정 유형을 저장하는 딕셔너리. {"감정": "지정값"}으로 이루어짐
    __emotions = {}
    __emotion_count = 0

    # 생성자
    def __init__(self) -> None:
        # 템플릿 파일 불러오기
        self.append_template("title-template/positive-1.json", "positive")
        self.append_template("title-template/positive-2.json", "positive")
        self.append_template("title-template/neutral-1.json", "neutral")
        self.append_template("title-template/negative-1.json", "negative")

        # 각 감정마다 몇 번째로 추가한 템플릿을 쓸 건지 결정
        self.__template_select["positive"] = 0
        self.__template_select["neutral"] = 0
        self.__template_select["negative"] = 0

    # json 파일을 열어서 딕셔너리 자료형으로 리턴하는 함수
    def __open_json(self, json_file_path: str) -> dict:
        try:
            with open(json_file_path) as json_file:
                template_json_dict = json.load(json_file)
                return template_json_dict
        except FileNotFoundError as fe:
            print(json_file_path + ": json 파일을 찾지 못했습니다.")
            print(fe)
            return None
    
    # 자막 템플릿의 정보가 저장된 JSON 파일을 불러와 리스트에 추가
    def append_template(self, input_json_dest: str, type_str: str) -> None:
        json_dict = self.__open_json(input_json_dest)
        # AI API가 제공하는 다양한 감정타입에 따라 자막 템플릿 분류 -> "type": positive, neutral, negative 등
        if type_str not in self.__template_info: 
            self.__template_info[type_str] = []
        self.__template_info[type_str].append(json_dict)
        self.__template_select[type_str] = 0
    
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
    
    # 감정분석 결과에 따라 미리 저장된 템플릿 정보(딕셔너리)를 꺼내오는 함수
    def get_template(self, emotion: str) -> dict:
        return self.__template_info[emotion][self.__template_select[self.__emotions[emotion]]]

    def get_template_at_number(self, emotion: str, number: int) -> dict:
        return self.__template_info[emotion][number]

    def get_all_template(self) -> list:
        all_template_list = []
        for template_emotion in self.__template_info.values():
            for template_emotion_num in template_emotion:
                all_template_list.append(template_emotion_num)
        return all_template_list

    # 모든 감정의 종류를 리스트 형태로 리턴하는 함수
    def get_emotion_list(self) -> list:
        return self.__template_info.keys()

    

# FCPX XML 처리에 관한 클래스
class FCPX_XML:
    # 입력받은 XML 파일을 파싱한 결과를 저장할 ElementTree 객체
    __xml_tree = None
    # 위 객체의 루트
    __xml_root = None
    # 새로 만들어진 XML 파일이 저장될 경로
    __output_xml_dest = ""
    # 템플릿 JSON 파일 자체를 담는 객체
    __funny_title_text_templates = None
    # effect XML 태그를 담고 있는 Element 객체 리스트
    __effect_tag = []

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
        # 템플릿 정보 파일(JSON)을 처리하는 객체 생성
        self.__funny_title_text_templates = Template_JSON()

        # 등록한 모든 템플릿에 대해 effect 태그 재작성
        self.__effect_xml_modifiction()
        

    # Azure AI Text Analytics 서비스(client)를 이용해 텍스트(documents)의 감정(긍정, 중립, 부정) 분석
    def __sentiment_analysis(self, documents: list):
        # API를 사용하여 입력받은 텍스트의 감정을 분석하고, 분석 결과를 response에 저장
        responses = []
        for document in documents:
            if document is None or document is "":
                return None, None
            else:
                responses.append(self.__api_client.analyze_sentiment([document], language="ko")[0])

        # 텍스트별 최종 감정을 저장하는 리스트, 감정별 자막 번호를 지정하는 리스트 작성
        result_emotions = []
        result_emotion_nums = []
        for i, response in enumerate(responses):
            # 감정을 분석해서 결과값에 감정 문자열과 자막 번호 지정하는 코드
            # 1. 특수 함수 - 필터링을 통해 감정 설정
            if documents[i].find("ㅋㅋ") is not EMPTY:
                result_emotions.append("positive")
                result_emotion_nums.append(1)
            elif self.__detect_abuse(documents[i]) is not EMPTY:
                result_emotions.append("negative")
                result_emotion_nums.append(0)
            elif self.__detect_interjection(documents[i]) is not EMPTY:
                result_emotions.append("positive")
                result_emotion_nums.append(0)
            # 2. 일반 함수 - positive, neutral, negative 함수 중 가장 높은 값을 지정
            else:
                positive_score = response.confidence_scores.positive
                neutral_score = response.confidence_scores.neutral
                negative_score = response.confidence_scores.negative
                
                if max(positive_score, neutral_score, negative_score) is positive_score:
                    result_emotions.append("positive")
                    result_emotion_nums.append(0)
                elif max(positive_score, neutral_score, negative_score) is neutral_score:
                    result_emotions.append("neutral")
                    result_emotion_nums.append(0)
                else:
                    result_emotions.append("negative")
                    result_emotion_nums.append(0)
            
            # 테스트용: 각 텍스트에 대해 결과 감정을 출력
            print("Input Text:", documents[i])
            print("Result Emotion:", result_emotions[i])
        
        return result_emotions, result_emotion_nums

    # 문장 안에서 욕설을 찾아내는 함수 - 욕설이 없을 경우 -1 리턴, 있을 경우 위치값 리턴
    def __detect_abuse(self, sentence: str) -> int: 
        filter = ["시발", "개새끼", "병신", "썅", "좆같네", "좃같네", "좋같네", "아 씨", "아씨", "야발"]
        for filter_item in filter: 
            if sentence.find(filter_item) is not EMPTY:
                return sentence.find(filter_item)
        return EMPTY 

    # 문장 안에서 감탄사를 찾아내는 함수 - 감탄사가 없을 경우 -1 리턴, 있을 경우 위치값 리턴
    def __detect_interjection(self, sentence: str) -> int:
        filter = ["무야호", "오진다", "오매", "좋은그" ]
        for filter_item in filter:
            if sentence.find(filter_item) is not EMPTY:
                return sentence.find(filter_item)
        return EMPTY


    # 각 자막 텍스트에 대해 감정분석
    def xml_text_analysis(self) -> None:
        # XML에서 자막에 해당되는 클립 정보를 읽기
        try:
            # asset-clip 태그를 찾기
            # asset-clip 태그는 파이널컷에서 메인 스토리라인에 들어가는 각 동영상 클립의 정보
            for asset_clip in self.__xml_root.iter("asset-clip"):
                # title 태그를 video 태그로 바꾸는 데 필요한 변수 준비물.
                # title_element: title 태그의 Element 객체, title_text: title 태그 안에 있는 text값, results: 감정분석 결과 반환된 감정 텍스트들의 집합
                title_element = []
                title_text = []
                results = []
                template_number = []
                
                for title in asset_clip.iter("title"):
                    # 자막 텍스트 추출
                    title_text.append(title.find("text").findtext("text-style"))

                # 읽어들인 자막 텍스트를 바탕으로 문장 감정을 분석해 예능자막을 지정하고 XML에 적용
                if asset_clip.find("title") is not None:
                    # 자막 분석 결과(감정 텍스트)와 각 감정별 템플릿의 번호를 추출
                    results, template_number = self.__sentiment_analysis(title_text)
                    # 태그 내 자막 텍스트가 있으면 다음을 수행
                    if results is not None:
                        # 기존에 있던 자막 템플릿 불러오기
                        existing_titles = []
                        for title in asset_clip.iter("title"):
                            existing_titles.append(title)
                        # 분석 결과를 XML에 반영
                        self.title_xml_modification(asset_clip, title_text, results, template_number)
                        # 기존 자막 템플릿 삭제
                        for existing_title in existing_titles:
                            asset_clip.remove(existing_title)
        except KeyboardInterrupt:
            print("\n\n사용자에 의한 강제 취소\n")

    # 자막 텍스트 자체의 정보가 저장된 effect 태그를 새로 쓰는 함수
    def __effect_xml_modifiction(self):
        # json 객체에서 모든 템플릿 정보를 불러들임
        all_templates = self.__funny_title_text_templates.get_all_template()
        # resources 태그 불러오기 (effect 태그의 정보는 resources 태그 안에 있음)
        resources = self.__xml_root.find("resources")
        

        # 모든 템플릿의 effect 태그 정보를 XML에 기록
        for template in all_templates:
            # 중복되는 effect 태그가 있으면 지우기 - 중복된 effect 태그가 있으면 오류가 생길 수 있음
            for existing_effect in self.__xml_root.iter("effect"):
                if existing_effect.attrib["name"] == template["effect"]["name"]:
                    resources.remove(existing_effect)

            # 템플릿의 effect 태그를 추출해 resources 태그 불러오기
            SubElement(resources, "effect", template["effect"])

    # 자막 텍스트의 감정에 따라 예능자막을 지정해서 XML의 title 태그를 고쳐쓰는 함수 
    # (title_element: 기존 자막의 태그 정보가 담겨있는 element 객체, text: 입력 문자열, emotion: 감정, type: 같은 감정의 템플릿이 여러 개면 특정 번호 지정, offset: )
    def title_xml_modification(self, asset_clip_element: Element, texts: list, emotions: list, template_numbers: list) -> None:
        # asset-clip 태그 안에 있는 모든 title 태그 찾기 (enumerate 사용)
        for i, title_element in enumerate(asset_clip_element.iter("title")):
            # 각 title 태그에 들어 있는 텍스트의 감정에 알맞는 템플릿(json) 불러오기
            template_json = self.__funny_title_text_templates.get_template_at_number(emotions[i], template_numbers[i])["video"]
            # 템플릿 json의 id를 ref로 변수 생성해서 자막 텍스트에 연결하도록 지정
            ref: int = self.__funny_title_text_templates.get_template_at_number(emotions[i], template_numbers[i])["effect"]["id"]
            # 해당 템플릿 json의 video 태그 속성 불러오기
            video_tag_attrib = title_element.attrib
            # video 태그의 이름 속성을 템플릿의 video 속성에서 붙여넣기
            video_tag_attrib["name"] = template_json["name"]
            # video 태그의 ref 속성을 템플릿의 ref로 수정
            video_tag_attrib["ref"] = ref
            # XML에 태그를 추가하기 위해 video라는 Element 객체 생성해서 asset-clip 태그에 붙여주기
            video_element = SubElement(asset_clip_element, "video", video_tag_attrib)

            # json 파일에 담겨 있는 여러 param 태그 탐색
            for param_attrib in template_json["param"]:
                # 이름 속성이 Text인 param 태그를 찾아 자막 텍스트 삽입
                if param_attrib["name"] == "Text":
                    param_attrib["value"] = texts[i]
                # param 태그를 만들어서 video 태그 안에 달아주기
                SubElement(video_element, "param", param_attrib)                
            

    # XML에서 각 자막 클립에 특정 자막 템플릿을 적용시킨 video 태그의 객체(Element)를 생성해주는 메소드
    def title_video_tag(self) -> Element:
        pass

    # 새로운 XML 파일을 작성하는 메소드
    def write_xml(self):
        # 수정된 트리(__xml_tree)를 새로운 파일 경로(__output_xml_dest)에 fcpxml 파일로 작성
        self.__xml_tree.write(self.__output_xml_dest, encoding="utf8", xml_declaration=True)


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
    
