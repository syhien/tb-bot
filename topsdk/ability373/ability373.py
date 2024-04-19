from topsdk.client import TopApiClient, BaseRequest

class Ability373:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        聚划算商品搜索接口
    """
    def taobao_ju_items_search(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
