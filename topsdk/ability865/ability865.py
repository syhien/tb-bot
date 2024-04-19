from topsdk.client import TopApiClient, BaseRequest

class Ability865:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        open account token验证
    """
    def taobao_open_account_token_validate(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        申请免登Open Account Token
    """
    def taobao_open_account_token_apply(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
