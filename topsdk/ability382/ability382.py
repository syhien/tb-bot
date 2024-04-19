from topsdk.client import TopApiClient, BaseRequest

class Ability382:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        淘宝客-推广者-红包领取状态查询
    """
    def taobao_tbk_dg_vegas_send_status(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
