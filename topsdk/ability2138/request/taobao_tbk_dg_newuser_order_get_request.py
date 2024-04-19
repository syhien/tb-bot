from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkDgNewuserOrderGetRequest(BaseRequest):

    def __init__(
        self,
        page_size: int = None,
        page_no: int = None,
        adzone_id: int = None,
        start_time: datetime = None,
        end_time: datetime = None,
        activity_id: str = None
    ):
        """
            页大小，默认20，1~100
        """
        self._page_size = page_size
        """
            页码，默认1
        """
        self._page_no = page_no
        """
            mm_xxx_xxx_xxx的第三位
        """
        self._adzone_id = adzone_id
        """
            开始时间，当活动为淘宝活动，表示最早注册时间；当活动为支付宝活动，表示最早绑定时间；当活动为天猫活动，表示最早领取红包时间
        """
        self._start_time = start_time
        """
            结束时间，当活动为淘宝活动，表示最晚结束时间；当活动为支付宝活动，表示最晚绑定时间；当活动为天猫活动，表示最晚领取红包的时间
        """
        self._end_time = end_time
        """
            活动id， 活动名称与活动ID列表（该字段已废弃）
        """
        self._activity_id = activity_id

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
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        if isinstance(page_no, int):
            self._page_no = page_no
        else:
            raise TypeError("page_no must be int")

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
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        if isinstance(start_time, datetime):
            self._start_time = start_time
        else:
            raise TypeError("start_time must be datetime")

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        if isinstance(end_time, datetime):
            self._end_time = end_time
        else:
            raise TypeError("end_time must be datetime")

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
        return "taobao.tbk.dg.newuser.order.get"

    def to_dict(self):
        request_dict = {}
        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._adzone_id is not None:
            request_dict["adzone_id"] = convert_basic(self._adzone_id)

        if self._start_time is not None:
            request_dict["start_time"] = convert_basic(self._start_time)

        if self._end_time is not None:
            request_dict["end_time"] = convert_basic(self._end_time)

        if self._activity_id is not None:
            request_dict["activity_id"] = convert_basic(self._activity_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

