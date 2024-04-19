from topsdk.client import TopApiClient, BaseRequest

class Ability2138:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        淘宝客-推广者-新用户订单明细查询
    """
    def taobao_tbk_dg_newuser_order_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
