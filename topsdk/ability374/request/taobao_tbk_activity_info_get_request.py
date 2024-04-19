from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkActivityInfoGetRequest(BaseRequest):

    def __init__(
        self,
        activity_material_id: str = None,
        adzone_id: int = None,
        sub_pid: str = None,
        relation_id: int = None,
        union_id: str = None
    ):
        """
            官方活动会场ID，从淘宝客后台“我要推广-活动推广”中获取
        """
        self._activity_material_id = activity_material_id
        """
            mm_xxx_xxx_xxx的第三位
        """
        self._adzone_id = adzone_id
        """
            mm_xxx_xxx_xxx 仅三方分成场景使用
        """
        self._sub_pid = sub_pid
        """
            渠道关系id
        """
        self._relation_id = relation_id
        """
            自定义输入串，英文和数字组成，长度不能大于12个字符，区分不同的推广渠道
        """
        self._union_id = union_id

    @property
    def activity_material_id(self):
        return self._activity_material_id

    @activity_material_id.setter
    def activity_material_id(self, activity_material_id):
        if isinstance(activity_material_id, str):
            self._activity_material_id = activity_material_id
        else:
            raise TypeError("activity_material_id must be str")

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
    def sub_pid(self):
        return self._sub_pid

    @sub_pid.setter
    def sub_pid(self, sub_pid):
        if isinstance(sub_pid, str):
            self._sub_pid = sub_pid
        else:
            raise TypeError("sub_pid must be str")

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
    def union_id(self):
        return self._union_id

    @union_id.setter
    def union_id(self, union_id):
        if isinstance(union_id, str):
            self._union_id = union_id
        else:
            raise TypeError("union_id must be str")


    def get_api_name(self):
        return "taobao.tbk.activity.info.get"

    def to_dict(self):
        request_dict = {}
        if self._activity_material_id is not None:
            request_dict["activity_material_id"] = convert_basic(self._activity_material_id)

        if self._adzone_id is not None:
            request_dict["adzone_id"] = convert_basic(self._adzone_id)

        if self._sub_pid is not None:
            request_dict["sub_pid"] = convert_basic(self._sub_pid)

        if self._relation_id is not None:
            request_dict["relation_id"] = convert_basic(self._relation_id)

        if self._union_id is not None:
            request_dict["union_id"] = convert_basic(self._union_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

