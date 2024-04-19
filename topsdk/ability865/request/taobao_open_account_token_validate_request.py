from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoOpenAccountTokenValidateRequest(BaseRequest):

    def __init__(
        self,
        param_token: str = None
    ):
        """
            token
        """
        self._param_token = param_token

    @property
    def param_token(self):
        return self._param_token

    @param_token.setter
    def param_token(self, param_token):
        if isinstance(param_token, str):
            self._param_token = param_token
        else:
            raise TypeError("param_token must be str")


    def get_api_name(self):
        return "taobao.open.account.token.validate"

    def to_dict(self):
        request_dict = {}
        if self._param_token is not None:
            request_dict["param_token"] = convert_basic(self._param_token)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

