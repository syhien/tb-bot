from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkDgMaterialRecommendRequest(BaseRequest):

    def __init__(
        self,
        page_size: int = None,
        page_no: int = None,
        material_id: int = None,
        adzone_id: int = None,
        relation_id: int = None,
        device_type: str = None,
        device_encrypt: str = None,
        device_value: str = None,
        promotion_type: str = None,
        special_id: str = None,
        item_id: str = None,
        favorites_id: str = None
    ):
        """
            页大小，默认20，1~100
        """
        self._page_size = page_size
        """
            第几页，默认：1
        """
        self._page_no = page_no
        """
            官方提供的物料Id；可以通过taobao.tbk.optimus.tou.material.ids.get接口获取公开的物料id列表或查看物料id汇总贴：https://market.m.taobao.com/app/qn/toutiao-new/index-pc.html#/detail/10628875?_k=gpov9a
        """
        self._material_id = material_id
        """
            推广位id，mm_xxx_xxx_12345678三段式的最后一段数字（登录pub.alimama.com推广管理-推广位管理中查询）
        """
        self._adzone_id = adzone_id
        """
            渠道关系ID，仅适用于渠道推广场景
        """
        self._relation_id = relation_id
        """
            智能匹配-设备号类型：IMEI，或者IDFA，或者UTDID（UTDID不支持MD5加密），或者OAID；使用智能推荐请先签署协议https://pub.alimama.com/fourth/protocol/common.htm?key=hangye_laxin
        """
        self._device_type = device_type
        """
            智能匹配-设备号加密类型：MD5；使用智能推荐请先签署协议https://pub.alimama.com/fourth/protocol/common.htm?key=hangye_laxin
        """
        self._device_encrypt = device_encrypt
        """
            智能匹配-设备号加密后的值（MD5加密需32位小写）；使用智能推荐请先签署协议https://pub.alimama.com/fourth/protocol/common.htm?key=hangye_laxin
        """
        self._device_value = device_value
        """
            1-自购省，2-推广赚（代理模式专属ID，代理模式必填，非代理模式不用填写该字段）
        """
        self._promotion_type = promotion_type
        """
            会员运营ID
        """
        self._special_id = special_id
        """
            淘宝客新商品ID；用于相似商品推荐（注意：使用相似商品推荐material_id=13256必传，并请先签署协议https://pub.alimama.com/fourth/protocol/common.htm?key=hangye_laxin)；另关于《淘宝客新商品ID升级》参考白皮书：https://www.yuque.com/taobaolianmengguanfangxiaoer/zmig94/tfyt0pahmlpzu2ud
        """
        self._item_id = item_id
        """
            选品库收藏夹id，获取收藏夹id参考文档：https://mos.m.taobao.com/union/page_20230109_175050_176?spm=a219t._portal_v2_pages_promo_goods_index_htm.0.0.7c2a75a5H2ER3N
        """
        self._favorites_id = favorites_id

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
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, material_id):
        if isinstance(material_id, int):
            self._material_id = material_id
        else:
            raise TypeError("material_id must be int")

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
    def relation_id(self):
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        if isinstance(relation_id, int):
            self._relation_id = relation_id
        else:
            raise TypeError("relation_id must be int")

    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        if isinstance(device_type, str):
            self._device_type = device_type
        else:
            raise TypeError("device_type must be str")

    @property
    def device_encrypt(self):
        return self._device_encrypt

    @device_encrypt.setter
    def device_encrypt(self, device_encrypt):
        if isinstance(device_encrypt, str):
            self._device_encrypt = device_encrypt
        else:
            raise TypeError("device_encrypt must be str")

    @property
    def device_value(self):
        return self._device_value

    @device_value.setter
    def device_value(self, device_value):
        if isinstance(device_value, str):
            self._device_value = device_value
        else:
            raise TypeError("device_value must be str")

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
    def special_id(self):
        return self._special_id

    @special_id.setter
    def special_id(self, special_id):
        if isinstance(special_id, str):
            self._special_id = special_id
        else:
            raise TypeError("special_id must be str")

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
    def favorites_id(self):
        return self._favorites_id

    @favorites_id.setter
    def favorites_id(self, favorites_id):
        if isinstance(favorites_id, str):
            self._favorites_id = favorites_id
        else:
            raise TypeError("favorites_id must be str")


    def get_api_name(self):
        return "taobao.tbk.dg.material.recommend"

    def to_dict(self):
        request_dict = {}
        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._material_id is not None:
            request_dict["material_id"] = convert_basic(self._material_id)

        if self._adzone_id is not None:
            request_dict["adzone_id"] = convert_basic(self._adzone_id)

        if self._relation_id is not None:
            request_dict["relation_id"] = convert_basic(self._relation_id)

        if self._device_type is not None:
            request_dict["device_type"] = convert_basic(self._device_type)

        if self._device_encrypt is not None:
            request_dict["device_encrypt"] = convert_basic(self._device_encrypt)

        if self._device_value is not None:
            request_dict["device_value"] = convert_basic(self._device_value)

        if self._promotion_type is not None:
            request_dict["promotion_type"] = convert_basic(self._promotion_type)

        if self._special_id is not None:
            request_dict["special_id"] = convert_basic(self._special_id)

        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._favorites_id is not None:
            request_dict["favorites_id"] = convert_basic(self._favorites_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

