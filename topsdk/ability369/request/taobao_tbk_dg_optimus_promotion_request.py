from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkDgOptimusPromotionRequest(BaseRequest):

    def __init__(
        self,
        page_size: int = None,
        page_num: int = None,
        adzone_id: int = None,
        promotion_id: int = None
    ):
        """
            页大小，一次请求请限制在10以内
        """
        self._page_size = page_size
        """
            第几页，默认：1
        """
        self._page_num = page_num
        """
            mm_xxx_xxx_xxx的第3段数字
        """
        self._adzone_id = adzone_id
        """
            官方提供的权益物料Id。有价券-37104、大额店铺券-37116、天猫店铺券-62191、券券补-61809 更多权益物料id敬请期待！
        """
        self._promotion_id = promotion_id

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
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        if isinstance(page_num, int):
            self._page_num = page_num
        else:
            raise TypeError("page_num must be int")

    @property
    def adzone_id(self):
        return self._adzone_id

    @adzone_id.setter
    def adzone_id(self, adzone_id):
        if isinstance(adzone_id, int):
            self._adzone_id = adzone_id
        else:
            raise TypeError("adzone_id must be int")

    @property
    def promotion_id(self):
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, promotion_id):
        if isinstance(promotion_id, int):
            self._promotion_id = promotion_id
        else:
            raise TypeError("promotion_id must be int")


    def get_api_name(self):
        return "taobao.tbk.dg.optimus.promotion"

    def to_dict(self):
        request_dict = {}
        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._page_num is not None:
            request_dict["page_num"] = convert_basic(self._page_num)

        if self._adzone_id is not None:
            request_dict["adzone_id"] = convert_basic(self._adzone_id)

        if self._promotion_id is not None:
            request_dict["promotion_id"] = convert_basic(self._promotion_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

