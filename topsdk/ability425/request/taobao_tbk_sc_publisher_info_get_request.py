from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkScPublisherInfoGetRequest(BaseRequest):

    def __init__(
        self,
        relation_id: int = None,
        page_no: int = None,
        page_size: int = None,
        info_type: int = None,
        relation_app: str = None,
        special_id: str = None,
        external_id: str = None,
        external_type: int = None
    ):
        """
            渠道独占 - 渠道关系ID
        """
        self._relation_id = relation_id
        """
            第几页，下标从0开始
        """
        self._page_no = page_no
        """
            每页大小
        """
        self._page_size = page_size
        """
            类型，必选 1:渠道信息；2:会员信息
        """
        self._info_type = info_type
        """
            备案的场景：common（通用备案），etao（一淘备案），minietao（一淘小程序备案），offlineShop（线下门店备案），offlinePerson（线下个人备案）。如不填默认common。查询会员信息只需填写common即可
        """
        self._relation_app = relation_app
        """
            会员独占 - 会员运营ID
        """
        self._special_id = special_id
        """
            淘宝客外部用户标记，如自身系统账户ID；微信ID等
        """
        self._external_id = external_id
        """
            1-微信、2-微博、3-抖音、4-快手、5-QQ，0-其他；默认为0
        """
        self._external_type = external_type

    @property
    def relation_id(self):
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        if isinstance(relation_id, int):
            self._relation_id = relation_id
        else:
            raise TypeError("relation_id must be int")

    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        if isinstance(page_no, int):
            self._page_no = page_no
        else:
            raise TypeError("page_no must be int")

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        if isinstance(page_size, int):
            self._page_size = page_size
        else:
            raise TypeError("page_size must be int")

    @property
    def info_type(self):
        return self._info_type

    @info_type.setter
    def info_type(self, info_type):
        if isinstance(info_type, int):
            self._info_type = info_type
        else:
            raise TypeError("info_type must be int")

    @property
    def relation_app(self):
        return self._relation_app

    @relation_app.setter
    def relation_app(self, relation_app):
        if isinstance(relation_app, str):
            self._relation_app = relation_app
        else:
            raise TypeError("relation_app must be str")

    @property
    def special_id(self):
        return self._special_id

    @special_id.setter
    def special_id(self, special_id):
        if isinstance(special_id, str):
            self._special_id = special_id
        else:
            raise TypeError("special_id must be str")

    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        if isinstance(external_id, str):
            self._external_id = external_id
        else:
            raise TypeError("external_id must be str")

    @property
    def external_type(self):
        return self._external_type

    @external_type.setter
    def external_type(self, external_type):
        if isinstance(external_type, int):
            self._external_type = external_type
        else:
            raise TypeError("external_type must be int")


    def get_api_name(self):
        return "taobao.tbk.sc.publisher.info.get"

    def to_dict(self):
        request_dict = {}
        if self._relation_id is not None:
            request_dict["relation_id"] = convert_basic(self._relation_id)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._info_type is not None:
            request_dict["info_type"] = convert_basic(self._info_type)

        if self._relation_app is not None:
            request_dict["relation_app"] = convert_basic(self._relation_app)

        if self._special_id is not None:
            request_dict["special_id"] = convert_basic(self._special_id)

        if self._external_id is not None:
            request_dict["external_id"] = convert_basic(self._external_id)

        if self._external_type is not None:
            request_dict["external_type"] = convert_basic(self._external_type)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

