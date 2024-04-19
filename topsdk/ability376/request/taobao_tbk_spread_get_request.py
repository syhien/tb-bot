from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkSpreadGetRequest(BaseRequest):

    def __init__(
        self,
        requests: list = None
    ):
        """
            请求列表，内部包含多个url
        """
        self._requests = requests

    @property
    def requests(self):
        return self._requests

    @requests.setter
    def requests(self, requests):
        if isinstance(requests, list):
            self._requests = requests
        else:
            raise TypeError("requests must be list")


    def get_api_name(self):
        return "taobao.tbk.spread.get"

    def to_dict(self):
        request_dict = {}
        if self._requests is not None:
            request_dict["requests"] = convert_struct_list(self._requests)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoTbkSpreadGetTbkSpreadRequest:
    def __init__(
        self,
        url: str = None
    ):
        """
            原始url, 只支持uland.taobao.com，s.click.taobao.com， ai.taobao.com，temai.taobao.com的域名转换，否则判错
        """
        self.url = url

