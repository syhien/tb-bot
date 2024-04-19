from topsdk.client import TopApiClient, BaseRequest

class Ability1826:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        淘宝客-推广者-淘礼金创建测试营销ID
    """
    def taobao_tbk_dg_vegas_tlj_temporary_create(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        淘宝客-推广者-淘礼金暂停发放
    """
    def taobao_tbk_dg_vegas_tlj_stop(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        淘宝客-推广者-淘礼金创建
    """
    def taobao_tbk_dg_vegas_tlj_create(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        淘宝客-推广者-淘礼金效果数据
    """
    def taobao_tbk_dg_vegas_tlj_report(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
