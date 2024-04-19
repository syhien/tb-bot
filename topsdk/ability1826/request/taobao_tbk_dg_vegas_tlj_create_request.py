from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkDgVegasTljCreateRequest(BaseRequest):

    def __init__(
        self,
        adzone_id: int = None,
        security_level: int = None,
        use_start_time: str = None,
        use_end_time_mode: int = None,
        use_end_time: str = None,
        send_end_time: datetime = None,
        send_start_time: datetime = None,
        per_face: str = None,
        security_switch: bool = None,
        user_total_win_num_limit: int = None,
        name: str = None,
        total_num: int = None,
        item_id: str = None,
        campaign_type: str = None
    ):
        """
            妈妈广告位Id
        """
        self._adzone_id = adzone_id
        """
            必须传入0
        """
        self._security_level = security_level
        """
            使用开始日期。相对时间，无需填写，以用户领取时间作为使用开始时间。绝对时间，格式 yyyy-MM-dd，例如，2019-01-29，表示从2019-01-29 00:00:00 开始
        """
        self._use_start_time = use_start_time
        """
            结束日期的模式,1:相对时间，2:绝对时间
        """
        self._use_end_time_mode = use_end_time_mode
        """
            使用结束日期。如果是结束时间模式为相对时间，时间格式为1-7直接的整数, 例如，1（相对领取时间1天）； 如果是绝对时间，格式为yyyy-MM-dd，例如，2019-01-29，表示到2019-01-29 23:59:59结束
        """
        self._use_end_time = use_end_time
        """
            发放截止时间
        """
        self._send_end_time = send_end_time
        """
            发放开始时间
        """
        self._send_start_time = send_start_time
        """
            单个淘礼金面额，支持两位小数，单位元
        """
        self._per_face = per_face
        """
            必须设置为true，默认开启安全
        """
        self._security_switch = security_switch
        """
            单用户累计中奖次数上限
        """
        self._user_total_win_num_limit = user_total_win_num_limit
        """
            淘礼金名称，最大10个字符
        """
        self._name = name
        """
            淘礼金总个数
        """
        self._total_num = total_num
        """
            宝贝ID或营销ID
        """
        self._item_id = item_id
        """
            已下线，后续不需要填写
        """
        self._campaign_type = campaign_type

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
    def security_level(self):
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        if isinstance(security_level, int):
            self._security_level = security_level
        else:
            raise TypeError("security_level must be int")

    @property
    def use_start_time(self):
        return self._use_start_time

    @use_start_time.setter
    def use_start_time(self, use_start_time):
        if isinstance(use_start_time, str):
            self._use_start_time = use_start_time
        else:
            raise TypeError("use_start_time must be str")

    @property
    def use_end_time_mode(self):
        return self._use_end_time_mode

    @use_end_time_mode.setter
    def use_end_time_mode(self, use_end_time_mode):
        if isinstance(use_end_time_mode, int):
            self._use_end_time_mode = use_end_time_mode
        else:
            raise TypeError("use_end_time_mode must be int")

    @property
    def use_end_time(self):
        return self._use_end_time

    @use_end_time.setter
    def use_end_time(self, use_end_time):
        if isinstance(use_end_time, str):
            self._use_end_time = use_end_time
        else:
            raise TypeError("use_end_time must be str")

    @property
    def send_end_time(self):
        return self._send_end_time

    @send_end_time.setter
    def send_end_time(self, send_end_time):
        if isinstance(send_end_time, datetime):
            self._send_end_time = send_end_time
        else:
            raise TypeError("send_end_time must be datetime")

    @property
    def send_start_time(self):
        return self._send_start_time

    @send_start_time.setter
    def send_start_time(self, send_start_time):
        if isinstance(send_start_time, datetime):
            self._send_start_time = send_start_time
        else:
            raise TypeError("send_start_time must be datetime")

    @property
    def per_face(self):
        return self._per_face

    @per_face.setter
    def per_face(self, per_face):
        if isinstance(per_face, str):
            self._per_face = per_face
        else:
            raise TypeError("per_face must be str")

    @property
    def security_switch(self):
        return self._security_switch

    @security_switch.setter
    def security_switch(self, security_switch):
        if isinstance(security_switch, bool):
            self._security_switch = security_switch
        else:
            raise TypeError("security_switch must be bool")

    @property
    def user_total_win_num_limit(self):
        return self._user_total_win_num_limit

    @user_total_win_num_limit.setter
    def user_total_win_num_limit(self, user_total_win_num_limit):
        if isinstance(user_total_win_num_limit, int):
            self._user_total_win_num_limit = user_total_win_num_limit
        else:
            raise TypeError("user_total_win_num_limit must be int")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("name must be str")

    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        if isinstance(total_num, int):
            self._total_num = total_num
        else:
            raise TypeError("total_num must be int")

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
    def campaign_type(self):
        return self._campaign_type

    @campaign_type.setter
    def campaign_type(self, campaign_type):
        if isinstance(campaign_type, str):
            self._campaign_type = campaign_type
        else:
            raise TypeError("campaign_type must be str")


    def get_api_name(self):
        return "taobao.tbk.dg.vegas.tlj.create"

    def to_dict(self):
        request_dict = {}
        if self._adzone_id is not None:
            request_dict["adzone_id"] = convert_basic(self._adzone_id)

        if self._security_level is not None:
            request_dict["security_level"] = convert_basic(self._security_level)

        if self._use_start_time is not None:
            request_dict["use_start_time"] = convert_basic(self._use_start_time)

        if self._use_end_time_mode is not None:
            request_dict["use_end_time_mode"] = convert_basic(self._use_end_time_mode)

        if self._use_end_time is not None:
            request_dict["use_end_time"] = convert_basic(self._use_end_time)

        if self._send_end_time is not None:
            request_dict["send_end_time"] = convert_basic(self._send_end_time)

        if self._send_start_time is not None:
            request_dict["send_start_time"] = convert_basic(self._send_start_time)

        if self._per_face is not None:
            request_dict["per_face"] = convert_basic(self._per_face)

        if self._security_switch is not None:
            request_dict["security_switch"] = convert_basic(self._security_switch)

        if self._user_total_win_num_limit is not None:
            request_dict["user_total_win_num_limit"] = convert_basic(self._user_total_win_num_limit)

        if self._name is not None:
            request_dict["name"] = convert_basic(self._name)

        if self._total_num is not None:
            request_dict["total_num"] = convert_basic(self._total_num)

        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._campaign_type is not None:
            request_dict["campaign_type"] = convert_basic(self._campaign_type)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

