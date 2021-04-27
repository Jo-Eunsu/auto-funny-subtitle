
# JSON 파일을 불러오기 위해 모듈 임포트
import json


# 자막 템플릿의 JSON 처리에 관한 클래스
class Template_JSON:
    # 자막 템플릿의 정보가 담겨 있는 딕셔너리 - {"감정": [한 감정에 들어 있는 자막 템플릿의 정보 리스트]} 형태
    __template_info = {}
    # 각 자막 템플릿의 유형 중 몇 번째 자막을 선택할 것인지 결정하는 딕셔너리 - {"감정": 자막 번호}
    __template_select = {}
    # 자막 템플릿의 감정 유형을 저장하는 딕셔너리. {"감정": "지정값"}으로 이루어짐
    __emotions = {}

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
    
    # 감정분석 결과에 따라 미리 저장된 템플릿 정보(딕셔너리)를 꺼내오는 함수 (특정 감정의 지정 템플릿, 특정 감정의 특정 템플릿, 모든 템플릿)
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

    