from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkShopGetRequest(BaseRequest):

    def __init__(
        self,
        end_auction_count: int = None,
        end_commission_rate: int = None,
        end_credit: int = None,
        end_total_action: int = None,
        fields: str = None,
        is_tmall: bool = None,
        page_no: int = None,
        page_size: int = None,
        platform: int = None,
        q: str = None,
        sort: str = None,
        start_auction_count: int = None,
        start_commission_rate: int = None,
        start_credit: int = None,
        start_total_action: int = None
    ):
        """
            累计推广商品上限
        """
        self._end_auction_count = end_auction_count
        """
            淘客佣金比率上限，1~10000
        """
        self._end_commission_rate = end_commission_rate
        """
            信用等级上限，1~20
        """
        self._end_credit = end_credit
        """
            店铺商品总数上限
        """
        self._end_total_action = end_total_action
        """
            需返回的字段列表
        """
        self._fields = fields
        """
            是否商城的店铺，设置为true表示该是属于淘宝商城的店铺，设置为false或不设置表示不判断这个属性
        """
        self._is_tmall = is_tmall
        """
            第几页，默认1，1~100
        """
        self._page_no = page_no
        """
            页大小，默认20，1~100
        """
        self._page_size = page_size
        """
            链接形式：1：PC，2：无线，默认：１
        """
        self._platform = platform
        """
            查询词
        """
        self._q = q
        """
            排序_des（降序），排序_asc（升序），佣金比率（commission_rate）， 商品数量（auction_count），销售总数量（total_auction）
        """
        self._sort = sort
        """
            累计推广商品下限
        """
        self._start_auction_count = start_auction_count
        """
            淘客佣金比率下限，1~10000
        """
        self._start_commission_rate = start_commission_rate
        """
            信用等级下限，1~20
        """
        self._start_credit = start_credit
        """
            店铺商品总数下限
        """
        self._start_total_action = start_total_action

    @property
    def end_auction_count(self):
        return self._end_auction_count

    @end_auction_count.setter
    def end_auction_count(self, end_auction_count):
        if isinstance(end_auction_count, int):
            self._end_auction_count = end_auction_count
        else:
            raise TypeError("end_auction_count must be int")

    @property
    def end_commission_rate(self):
        return self._end_commission_rate

    @end_commission_rate.setter
    def end_commission_rate(self, end_commission_rate):
        if isinstance(end_commission_rate, int):
            self._end_commission_rate = end_commission_rate
        else:
            raise TypeError("end_commission_rate must be int")

    @property
    def end_credit(self):
        return self._end_credit

    @end_credit.setter
    def end_credit(self, end_credit):
        if isinstance(end_credit, int):
            self._end_credit = end_credit
        else:
            raise TypeError("end_credit must be int")

    @property
    def end_total_action(self):
        return self._end_total_action

    @end_total_action.setter
    def end_total_action(self, end_total_action):
        if isinstance(end_total_action, int):
            self._end_total_action = end_total_action
        else:
            raise TypeError("end_total_action must be int")

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
    def is_tmall(self):
        return self._is_tmall

    @is_tmall.setter
    def is_tmall(self, is_tmall):
        if isinstance(is_tmall, bool):
            self._is_tmall = is_tmall
        else:
            raise TypeError("is_tmall must be bool")

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
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, platform):
        if isinstance(platform, int):
            self._platform = platform
        else:
            raise TypeError("platform must be int")

    @property
    def q(self):
        return self._q

    @q.setter
    def q(self, q):
        if isinstance(q, str):
            self._q = q
        else:
            raise TypeError("q must be str")

    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, sort):
        if isinstance(sort, str):
            self._sort = sort
        else:
            raise TypeError("sort must be str")

    @property
    def start_auction_count(self):
        return self._start_auction_count

    @start_auction_count.setter
    def start_auction_count(self, start_auction_count):
        if isinstance(start_auction_count, int):
            self._start_auction_count = start_auction_count
        else:
            raise TypeError("start_auction_count must be int")

    @property
    def start_commission_rate(self):
        return self._start_commission_rate

    @start_commission_rate.setter
    def start_commission_rate(self, start_commission_rate):
        if isinstance(start_commission_rate, int):
            self._start_commission_rate = start_commission_rate
        else:
            raise TypeError("start_commission_rate must be int")

    @property
    def start_credit(self):
        return self._start_credit

    @start_credit.setter
    def start_credit(self, start_credit):
        if isinstance(start_credit, int):
            self._start_credit = start_credit
        else:
            raise TypeError("start_credit must be int")

    @property
    def start_total_action(self):
        return self._start_total_action

    @start_total_action.setter
    def start_total_action(self, start_total_action):
        if isinstance(start_total_action, int):
            self._start_total_action = start_total_action
        else:
            raise TypeError("start_total_action must be int")


    def get_api_name(self):
        return "taobao.tbk.shop.get"

    def to_dict(self):
        request_dict = {}
        if self._end_auction_count is not None:
            request_dict["end_auction_count"] = convert_basic(self._end_auction_count)

        if self._end_commission_rate is not None:
            request_dict["end_commission_rate"] = convert_basic(self._end_commission_rate)

        if self._end_credit is not None:
            request_dict["end_credit"] = convert_basic(self._end_credit)

        if self._end_total_action is not None:
            request_dict["end_total_action"] = convert_basic(self._end_total_action)

        if self._fields is not None:
            request_dict["fields"] = convert_basic(self._fields)

        if self._is_tmall is not None:
            request_dict["is_tmall"] = convert_basic(self._is_tmall)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._platform is not None:
            request_dict["platform"] = convert_basic(self._platform)

        if self._q is not None:
            request_dict["q"] = convert_basic(self._q)

        if self._sort is not None:
            request_dict["sort"] = convert_basic(self._sort)

        if self._start_auction_count is not None:
            request_dict["start_auction_count"] = convert_basic(self._start_auction_count)

        if self._start_commission_rate is not None:
            request_dict["start_commission_rate"] = convert_basic(self._start_commission_rate)

        if self._start_credit is not None:
            request_dict["start_credit"] = convert_basic(self._start_credit)

        if self._start_total_action is not None:
            request_dict["start_total_action"] = convert_basic(self._start_total_action)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

