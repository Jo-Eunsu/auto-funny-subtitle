
# FCPX XML 수정을 위해서는 Template_JSON 클래스와 AzureAnalytics 및 ElementTree(XML 처리 모듈) 클래스가 필요
from typing import List, NoReturn, Tuple, TypeVar
from xml.etree.ElementTree import Element, ElementTree, SubElement, parse
from Template_JSON import Template_JSON
from AzureAnalytics import AzureAnalytics
EMPTY = -1


# FCPX XML 처리에 관한 클래스
class FCPX_XML:
    # 입력받은 XML 파일을 파싱한 결과를 저장할 ElementTree 객체
    __xml_tree = None
    # 위 객체의 루트
    __xml_root = None
    # 템플릿 JSON 파일 자체를 담는 객체
    __funny_title_text_templates = None

    # 기본 생성자: XML을 불러와 ElementTree 자료형으로 저장, Azure AI API의 클라이언트 정보 불러오기
    def __init__(self, input_xml_dest: str) -> None:
        # input_xml_dest 경로에 있는 xml 파일을 파싱한 데이터를 __xml_tree에 저장
        self.__xml_tree = parse(input_xml_dest)
        # __xml_tree 객체의 루트 노드 찾기
        self.__xml_root = self.__xml_tree.getroot()
        # Azure Text Analytics 서비스의 클라이언트 객체 얻기
        self.__api_client = AzureAnalytics().get_client()
        # 수정된 XML 파일의 이름을 따로 지정
        self.__input_xml_dest = input_xml_dest
        # 템플릿 정보 파일(JSON)을 처리하는 객체 생성
        self.__funny_title_text_templates = Template_JSON()
        
        # xml이 감정분석으로 바뀌었는지 확인하는 플래그 변수
        self.xml_modified = False

        print("XML 처리 객체", self.__input_xml_dest, "생성됨\n")

        # 등록한 모든 템플릿에 대해 effect 태그 재작성
        self.__effect_xml_modifiction()
    
    def __del__(self):
        print("XML 처리 객체", self.__input_xml_dest, "삭제됨\n")

    # XML의 모든 자막 태그 엘리먼트(Element)를 불러오는 함수
    def loadAllElements(self) -> list:
        # 모든 자막 태그 엘리먼트를 담는 리스트
        title_elements = []

        # asset-clip 태그를 찾기
        # asset-clip 태그는 파이널컷에서 메인 스토리라인에 들어가는 각 동영상 클립의 정보
        for asset_clip in self.__xml_root.iter("asset-clip"):
            for title in asset_clip.iter("title"):
                # 일반자막 엘리먼트 (부모 엘리먼트 포함) 추출
                nodeDict = {"node": title, "parent": asset_clip}
                title_elements.append(nodeDict)
        return title_elements

    # XML에서 새로 예능자막 템플릿을 적용한 태그를 찾는 함수
    def loadAllVideoElements(self) -> list:
        # 모든 예능자막 태그 엘리먼트를 담는 리스트
        video_elements = []

        # 모든 자막 템플릿의 ID 정보 저장
        templateIDs = []
        for template in self.__funny_title_text_templates.get_all_template():
            templateIDs.append(template["effect"]["id"])

        for asset_clip in self.__xml_root.iter("asset-clip"):
            for video in asset_clip.iter("video"):
                # Generator 템플릿이 적용된 클립 중 예능자막 템플릿이 적용된 엘리먼트를 찾아 예능자막 엘리먼트 (부모 엘리먼트 포함) 추출
                if video.attrib["ref"] in templateIDs:
                    nodeDict = {"node": video, "parent": asset_clip}
                    video_elements.append(nodeDict)

        return video_elements


    # 각 자막 텍스트에 대해 감정분석
    def xml_text_analysis(self, title: Element, parent: Element) -> None:
        # 자막에서 텍스트 추출
        title_text = title.find("text").findtext("text-style")
        # 자막 분석 결과(감정 텍스트)와 각 감정별 템플릿의 번호를 추출
        result, template_number = self.__sentiment_analysis(title_text)

        # 기존 자막 템플릿을 삭제하고 분석 결과를 XML에 반영 (video 태그 추가)
        parent.remove(title)
        self.title_xml_modification(parent, title, result, template_number)

    # Azure AI Text Analytics 서비스(client)를 이용해 텍스트(documents)의 감정(긍정, 중립, 부정) 분석
    def __sentiment_analysis(self, document: str):
        # API를 사용하여 입력받은 텍스트의 감정을 분석하고, 분석 결과를 response에 저장
        response = (self.__api_client.analyze_sentiment([document], language="ko")[0])

        # 텍스트별 최종 감정을 저장하는 리스트, 감정별 자막 번호를 지정하는 변수
        result_emotion: str
        result_emotion_num: int

        positive_score = neutral_score = negative_score = 0.0
        # 감정을 분석해서 결과값에 감정 문자열과 자막 번호 지정하는 코드
        # 1. 특수 함수 - 필터링을 통해 감정 설정
        if self.__detect_funny(document) is not EMPTY:
            result_emotion = 'funny'
            result_emotion_num = 0
        elif self.__detect_abuse(document) is not EMPTY:
            result_emotion = 'negative'
            result_emotion_num = 0
        elif self.__detect_interjection(document) is not EMPTY:
            result_emotion = 'positive'
            result_emotion_num = 0
        # 2. 일반 함수 - positive, neutral, negative 함수 중 가장 높은 값을 지정
        else:
            positive_score = response.confidence_scores.positive
            neutral_score = response.confidence_scores.neutral
            negative_score = response.confidence_scores.negative
            
            if max(positive_score, neutral_score, negative_score) is positive_score:
                result_emotion = 'positive'
                result_emotion_num = 0
            elif max(positive_score, neutral_score, negative_score) is neutral_score:
                result_emotion = 'neutral'
                result_emotion_num = 0
            else:
                result_emotion = 'negative'
                result_emotion_num = 0
            
        # 테스트용: 각 텍스트에 대해 결과 감정을 출력
        print("Input Text:", document)
        print("Result Emotion:", result_emotion)
        print("positive score:", positive_score)
        print("neutral score:", neutral_score)
        print("negative score:", negative_score)
        print("")
        
        return result_emotion, result_emotion_num

    # 문장 안에서 욕설을 찾아내는 함수 - 욕설이 없을 경우 -1 리턴, 있을 경우 위치값 리턴
    def __detect_abuse(self, sentence: str) -> int: 
        filter = ["시발", "개새끼", "병신", "썅", "좆같네", "좃같네", "좋같네", "아 씨", "아씨", "야발"]
        for filter_item in filter: 
            if sentence.find(filter_item) is not EMPTY:
                return sentence.find(filter_item)
        return EMPTY 

    # 문장 안에서 즐거움을 찾아내는 함수 - 'ㅋㅋㅋ'와 '하하하'
    def __detect_funny(self, sentence: str) -> int: 
        filter = ["ㅋㅋ", "하하하", "웃겨"]
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
    def title_xml_modification(self, asset_clip_element: Element, title_element: Element, emotion: str, template_number: int) -> NoReturn:
        text = title_element.find("text").findtext("text-style")

        # 각 title 태그에 들어 있는 텍스트의 감정에 알맞는 템플릿(json) 불러오기
        template_json = self.__funny_title_text_templates.get_template_at_number(emotion, template_number)["video"]
        # 템플릿 json의 id를 ref로 변수 생성해서 자막 텍스트에 연결하도록 지정
        ref: str = self.__funny_title_text_templates.get_template_at_number(emotion, template_number)["effect"]["id"]
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
                param_attrib["value"] = text
            # param 태그를 만들어서 video 태그 안에 달아주기
            SubElement(video_element, "param", param_attrib)            

    # 이미 적용된 video 엘리먼트를 다시 한 번 바꾸는 함수
    def video_xml_modification(self, video_element: Element, offset_attrib: str, duration_attrib: str, template_name: str, title_text: str) -> NoReturn:

        # 새로 바뀐 감정에 알맞는 템플릿(json) 불러오기
        template_json = self.__funny_title_text_templates.get_template_at_name(template_name)["video"]
        # 템플릿 json의 id를 ref로 변수 생성해서 자막 텍스트에 연결하도록 지정
        ref: str = self.__funny_title_text_templates.get_template_at_name(template_name)["effect"]["id"]
        # 해당 템플릿 json의 video 태그 속성 불러오기
        video_tag_attrib = video_element.attrib
        # video 태그의 속성 수정
        video_tag_attrib["name"] = template_json["name"]
        video_tag_attrib["ref"] = ref
        video_tag_attrib["offset"] = offset_attrib
        video_tag_attrib["duration"] = duration_attrib

        # 기존의 모든 param 속성 삭제
        for param in video_element.iter("param"):
            video_element.remove(param)

        # json 파일에 담겨 있는 여러 param 태그 탐색 후 param 태그 추가
        for param_attrib in template_json["param"]:
            # param 태그를 만들어서 video 태그 안에 달아주기
            SubElement(video_element, "param", param_attrib)    

        # 자막 텍스트 삽입
        for param in video_element.iter("param"):
            if param.attrib["name"] == "Text":
                param.attrib["value"] = title_text 


    # Templ
    def get_all_template(self) -> List:
        return self.__funny_title_text_templates.get_all_template()    
        

    # 새로운 XML 파일을 작성하는 메소드 (리턴값은 xml 구조를 가지는 ElementTree)
    def write_xml(self) -> ElementTree:
        if self.xml_modified == False: 
            return None
        else:
            return self.__xml_tree
        # self.__xml__tree.write(self.__output_xml_dest, encoding="utf8", xml_declaration=True)