from topsdk.client import TopApiClient, BaseRequest

class Ability370:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        淘宝客-推广者-店铺搜索
    """
    def taobao_tbk_shop_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        淘宝客-推广者-物料搜索（临时接口）
    """
    def taobao_tbk_dg_material_temporary_optional(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
