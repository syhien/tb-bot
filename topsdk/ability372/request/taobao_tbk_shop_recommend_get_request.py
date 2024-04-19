from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkShopRecommendGetRequest(BaseRequest):

    def __init__(
        self,
        count: int = None,
        fields: str = None,
        platform: int = None,
        user_id: int = None
    ):
        """
            返回数量，默认20，最大值40
        """
        self._count = count
        """
            需返回的字段列表
        """
        self._fields = fields
        """
            链接形式：1：PC，2：无线，默认：１
        """
        self._platform = platform
        """
            卖家Id
        """
        self._user_id = user_id

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        if isinstance(count, int):
            self._count = count
        else:
            raise TypeError("count must be int")

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        if isinstance(fields, str):
            self._fields = fields
        else:
            raise TypeError("fields must be str")

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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if isinstance(user_id, int):
            self._user_id = user_id
        else:
            raise TypeError("user_id must be int")


    def get_api_name(self):
        return "taobao.tbk.shop.recommend.get"

    def to_dict(self):
        request_dict = {}
        if self._count is not None:
            request_dict["count"] = convert_basic(self._count)

        if self._fields is not None:
            request_dict["fields"] = convert_basic(self._fields)

        if self._platform is not None:
            request_dict["platform"] = convert_basic(self._platform)

        if self._user_id is not None:
            request_dict["user_id"] = convert_basic(self._user_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

