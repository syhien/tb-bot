from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkItemInfoTemporaryGetRequest(BaseRequest):

    def __init__(
        self,
        num_iids: str = None,
        platform: int = None,
        ip: str = None
    ):
        """
            商品ID串，用,分割，最大40个
        """
        self._num_iids = num_iids
        """
            链接形式：1：PC，2：无线，默认：１
        """
        self._platform = platform
        """
            ip地址，影响邮费获取，如果不传或者传入不准确，邮费无法精准提供
        """
        self._ip = ip

    @property
    def num_iids(self):
        return self._num_iids

    @num_iids.setter
    def num_iids(self, num_iids):
        if isinstance(num_iids, str):
            self._num_iids = num_iids
        else:
            raise TypeError("num_iids must be str")

    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, platform):
        if isinstance(platform, int):
            self._platform = platform
        else:
            raise TypeError("platform must be int")

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, ip):
        if isinstance(ip, str):
            self._ip = ip
        else:
            raise TypeError("ip must be str")


    def get_api_name(self):
        return "taobao.tbk.item.info.temporary.get"

    def to_dict(self):
        request_dict = {}
        if self._num_iids is not None:
            request_dict["num_iids"] = convert_basic(self._num_iids)

        if self._platform is not None:
            request_dict["platform"] = convert_basic(self._platform)

        if self._ip is not None:
            request_dict["ip"] = convert_basic(self._ip)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

