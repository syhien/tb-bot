from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkItemInfoGetRequest(BaseRequest):

    def __init__(
        self,
        num_iids: str = None,
        platform: int = None,
        ip: str = None,
        biz_scene_id: str = None,
        promotion_type: str = None,
        relation_id: str = None,
        manage_item_pub_id: int = None
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
        """
            1-动态ID转链场景，2-消费者比价场景，3-商品库导购场景（不填默认为1）
        """
        self._biz_scene_id = biz_scene_id
        """
            1-自购省，2-推广赚（代理模式专属ID，代理模式必填，非代理模式不用填写该字段）
        """
        self._promotion_type = promotion_type
        """
            渠道关系ID
        """
        self._relation_id = relation_id
        """
            商品库服务账户(场景id3权限对应的memberid）
        """
        self._manage_item_pub_id = manage_item_pub_id

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

    @property
    def biz_scene_id(self):
        return self._biz_scene_id

    @biz_scene_id.setter
    def biz_scene_id(self, biz_scene_id):
        if isinstance(biz_scene_id, str):
            self._biz_scene_id = biz_scene_id
        else:
            raise TypeError("biz_scene_id must be str")

    @property
    def promotion_type(self):
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, promotion_type):
        if isinstance(promotion_type, str):
            self._promotion_type = promotion_type
        else:
            raise TypeError("promotion_type must be str")

    @property
    def relation_id(self):
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        if isinstance(relation_id, str):
            self._relation_id = relation_id
        else:
            raise TypeError("relation_id must be str")

    @property
    def manage_item_pub_id(self):
        return self._manage_item_pub_id

    @manage_item_pub_id.setter
    def manage_item_pub_id(self, manage_item_pub_id):
        if isinstance(manage_item_pub_id, int):
            self._manage_item_pub_id = manage_item_pub_id
        else:
            raise TypeError("manage_item_pub_id must be int")


    def get_api_name(self):
        return "taobao.tbk.item.info.get"

    def to_dict(self):
        request_dict = {}
        if self._num_iids is not None:
            request_dict["num_iids"] = convert_basic(self._num_iids)

        if self._platform is not None:
            request_dict["platform"] = convert_basic(self._platform)

        if self._ip is not None:
            request_dict["ip"] = convert_basic(self._ip)

        if self._biz_scene_id is not None:
            request_dict["biz_scene_id"] = convert_basic(self._biz_scene_id)

        if self._promotion_type is not None:
            request_dict["promotion_type"] = convert_basic(self._promotion_type)

        if self._relation_id is not None:
            request_dict["relation_id"] = convert_basic(self._relation_id)

        if self._manage_item_pub_id is not None:
            request_dict["manage_item_pub_id"] = convert_basic(self._manage_item_pub_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

