from topsdk.client import TopApiClient, BaseRequest

class Ability425:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        淘宝客-公用-私域用户邀请码生成
    """
    def taobao_tbk_sc_invitecode_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        淘宝客-公用-私域用户备案
    """
    def taobao_tbk_sc_publisher_info_save(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        淘宝客-公用-私域用户备案信息查询
    """
    def taobao_tbk_sc_publisher_info_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
