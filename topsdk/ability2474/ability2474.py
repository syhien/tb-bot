from topsdk.client import TopApiClient, BaseRequest

class Ability2474:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        淘宝客-推广者-查询红包发放个数
    """
    def taobao_tbk_dg_vegas_send_report(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
