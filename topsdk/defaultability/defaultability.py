from topsdk.client import TopApiClient, BaseRequest

class Defaultability:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        关键词过滤匹配
    """
    def taobao_kfc_keyword_search(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        淘宝客-推广者-物料id列表查询
    """
    def taobao_tbk_optimus_tou_material_ids_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        淘宝客-推广者-物料搜索升级版
    """
    def taobao_tbk_dg_material_optional_upgrade(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        淘宝客-推广者-物料精选升级版
    """
    def taobao_tbk_dg_material_recommend(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
