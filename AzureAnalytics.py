
# Azure Text Analytics API 모듈
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Azure API에 관한 클래스
class AzureAnalytics:
    # Azure AI Text Analytics 서비스에 연결
    __key = "adb408a2b6d74ad99e17fef3f4e42a55"
    __endpoint = "https://auto-funny-subtitle.cognitiveservices.azure.com/"

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

