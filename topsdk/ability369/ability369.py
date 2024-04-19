from topsdk.client import TopApiClient, BaseRequest

class Ability369:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        淘宝客-推广者-权益物料精选
    """
    def taobao_tbk_dg_optimus_promotion(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
