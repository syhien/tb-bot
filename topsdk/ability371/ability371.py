from topsdk.client import TopApiClient, BaseRequest

class Ability371:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        淘宝客-公用-阿里妈妈推广券详情查询
    """
    def taobao_tbk_coupon_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        淘宝客-公用-淘宝客商品详情查询(简版)
    """
    def taobao_tbk_item_info_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        淘宝客商品详情查询（简版）（临时接口）
    """
    def taobao_tbk_item_info_temporary_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        淘宝客-公用-淘宝客商品详情查询升级版（简易版）
    """
    def taobao_tbk_item_info_upgrade_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
