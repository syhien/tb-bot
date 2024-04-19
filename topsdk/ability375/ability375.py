from topsdk.client import TopApiClient, BaseRequest

class Ability375:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        淘宝客-公用-淘口令生成
    """
    def taobao_tbk_tpwd_create(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
