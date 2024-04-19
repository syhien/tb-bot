from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkItemInfoUpgradeGetRequest(BaseRequest):

    def __init__(
        self,
        item_id: str = None,
        ip: str = None,
        biz_scene_id: str = None,
        promotion_type: str = None,
        relation_id: str = None,
        manage_item_pub_id: int = None
    ):
        """
            商品ID。多个用","分割，一次最多查询20个
        """
        self._item_id = item_id
        """
            ip地址，影响邮费获取，如果不传或者传入不准确，邮费无法精准提供
        """
        self._ip = ip
        """
            1-动态ID转链场景，2-消费者比价场景，3-商品库导购场景（不填默认为1）；场景id使用说明参考《淘宝客新商品ID升级》白皮书：https://www.yuque.com/taobaolianmengguanfangxiaoer/zmig94/tfyt0pahmlpzu2ud
        """
        self._biz_scene_id = biz_scene_id
        """
            1-自购省，2-推广赚（代理模式专属ID，代理模式必填，非代理模式不用填写该字段）
        """
        self._promotion_type = promotion_type
        """
            渠道关系ID，仅适用于渠道推广场景
        """
        self._relation_id = relation_id
        """
            商品库服务账户(场景id3权限对应的memberid）
        """
        self._manage_item_pub_id = manage_item_pub_id

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
        return "taobao.tbk.item.info.upgrade.get"

    def to_dict(self):
        request_dict = {}
        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

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

