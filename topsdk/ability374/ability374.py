from topsdk.client import TopApiClient, BaseRequest

class Ability374:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        淘宝客-推广者-官方活动转链
    """
    def taobao_tbk_activity_info_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
