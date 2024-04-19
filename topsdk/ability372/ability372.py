from topsdk.client import TopApiClient, BaseRequest

class Ability372:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        淘宝客-公用-店铺关联推荐
    """
    def taobao_tbk_shop_recommend_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
