from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkCouponGetRequest(BaseRequest):

    def __init__(
        self,
        me: str = None,
        item_id: str = None,
        activity_id: str = None
    ):
        """
            带券ID与商品ID的加密串
        """
        self._me = me
        """
            商品ID
        """
        self._item_id = item_id
        """
            券ID
        """
        self._activity_id = activity_id

    @property
    def me(self):
        return self._me

    @me.setter
    def me(self, me):
        if isinstance(me, str):
            self._me = me
        else:
            raise TypeError("me must be str")

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        if isinstance(item_id, str):
            self._item_id = item_id
        else:
            raise TypeError("item_id must be str")

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        if isinstance(activity_id, str):
            self._activity_id = activity_id
        else:
            raise TypeError("activity_id must be str")


    def get_api_name(self):
        return "taobao.tbk.coupon.get"

    def to_dict(self):
        request_dict = {}
        if self._me is not None:
            request_dict["me"] = convert_basic(self._me)

        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._activity_id is not None:
            request_dict["activity_id"] = convert_basic(self._activity_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

