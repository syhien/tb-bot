from topsdk.client import TopApiClient, BaseRequest

class Ability376:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        淘宝客-公用-长链转短链
    """
    def taobao_tbk_spread_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
