from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkDgMaterialOptionalUpgradeRequest(BaseRequest):

    def __init__(
        self,
        start_dsr: int = None,
        page_size: int = None,
        page_no: int = None,
        end_tk_rate: int = None,
        start_tk_rate: int = None,
        end_price: int = None,
        start_price: int = None,
        is_overseas: bool = None,
        is_tmall: bool = None,
        sort: str = None,
        itemloc: str = None,
        cat: str = None,
        q: str = None,
        material_id: int = None,
        has_coupon: bool = None,
        ip: str = None,
        adzone_id: int = None,
        need_free_shipment: bool = None,
        need_prepay: bool = None,
        include_pay_rate_30: bool = None,
        include_good_rate: bool = None,
        include_rfd_rate: bool = None,
        npx_level: int = None,
        device_encrypt: str = None,
        device_value: str = None,
        device_type: str = None,
        special_id: str = None,
        relation_id: str = None,
        get_topn_rate: int = None,
        biz_scene_id: str = None,
        promotion_type: str = None,
        mgc_start_time: str = None,
        mgc_end_time: str = None,
        mgc_status: str = None,
        ucrowd_id: int = None,
        ucrowd_rank_items: list = None
    ):
        """
            商品筛选-店铺dsr评分。筛选大于等于当前设置的店铺dsr评分的商品0-50000之间
        """
        self._start_dsr = start_dsr
        """
            页大小，默认20，1~100
        """
        self._page_size = page_size
        """
            第几页，默认：１
        """
        self._page_no = page_no
        """
            商品筛选-淘客收入比率上限(商品佣金比率+补贴比率)。如：1234表示12.34%
        """
        self._end_tk_rate = end_tk_rate
        """
            商品筛选-淘客收入比率下限(商品佣金比率+补贴比率)。如：1234表示12.34%
        """
        self._start_tk_rate = start_tk_rate
        """
            商品筛选-预估到手价范围上限。单位：元
        """
        self._end_price = end_price
        """
            商品筛选-预估到手价范围下限。单位：元
        """
        self._start_price = start_price
        """
            商品筛选-是否海外商品。true表示属于海外商品，false或不设置表示不限
        """
        self._is_overseas = is_overseas
        """
            商品筛选-是否天猫商品。true表示属于天猫商品，false或不设置表示不限
        """
        self._is_tmall = is_tmall
        """
            排序_des（降序），排序_asc（升序），销量（total_sales），淘客收入比率（tk_rate）， 累计推广量（tk_total_sales），总支出佣金（tk_total_commi），预估到价格（final_promotion_price），匹配分（match）
        """
        self._sort = sort
        """
            商品筛选-所在地
        """
        self._itemloc = itemloc
        """
            商品筛选-后台类目ID。用,分割，最大10个
        """
        self._cat = cat
        """
            商品筛选-查询词；注意：使用标题精准搜索时，若无消费者比价场景ID2权限，当搜索结果只有一个商品时则出参不再提供商品推广链接和商品id字段，若搜索结果仍有多个商品，则正常出参。同时无消费者比价场景ID2权限，q参数也不再支持入参淘宝复制的商品链接进行搜索查询，仅支持入参含新商品id的淘宝客推广链接如uland链接进行搜索查询(场景id使用说明参考《淘宝客新商品ID升级》白皮书：https://www.yuque.com/taobaolianmengguanfangxiaoer/zmig94/tfyt0pahmlpzu2ud)
        """
        self._q = q
        """
            物料id，不传时默认物料material_id=80309；如果直接对消费者投放，可使用官方个性化算法优化的搜索物料material_id=17004（注意：若物料id=17004没查询到结果则出系统默认物料id=80309的查询结果）
        """
        self._material_id = material_id
        """
            优惠券筛选-是否有优惠券。true表示该商品有优惠券，false或不设置表示不限
        """
        self._has_coupon = has_coupon
        """
            ip参数影响邮费获取，如果不传或者传入不准确，邮费无法精准提供
        """
        self._ip = ip
        """
            推广位id，mm_xxx_xxx_12345678三段式的最后一段数字（登录pub.alimama.com推广管理-推广位管理中查询）
        """
        self._adzone_id = adzone_id
        """
            商品筛选-是否包邮。true表示包邮，false或不设置表示不限
        """
        self._need_free_shipment = need_free_shipment
        """
            商品筛选-是否加入消费者保障。true表示加入，false或不设置表示不限
        """
        self._need_prepay = need_prepay
        """
            商品筛选-成交转化是否高于行业均值。True表示大于等于，false或不设置表示不限
        """
        self._include_pay_rate_30 = include_pay_rate_30
        """
            商品筛选-好评率是否高于行业均值。True表示大于等于，false或不设置表示不限
        """
        self._include_good_rate = include_good_rate
        """
            商品筛选-退款率是否低于行业均值。True表示大于等于，false或不设置表示不限
        """
        self._include_rfd_rate = include_rfd_rate
        """
            商品筛选-牛皮癣程度。取值：1不限，2无，3轻微
        """
        self._npx_level = npx_level
        """
            智能匹配-设备号加密类型：MD5；使用智能推荐请先签署协议https://pub.alimama.com/fourth/protocol/common.htm?key=hangye_laxin
        """
        self._device_encrypt = device_encrypt
        """
            智能匹配-设备号加密后的值（MD5加密需32位小写）；使用智能推荐请先签署协议https://pub.alimama.com/fourth/protocol/common.htm?key=hangye_laxin
        """
        self._device_value = device_value
        """
            智能匹配-设备号类型：IMEI，或者IDFA，或者UTDID（UTDID不支持MD5加密），或者OAID；使用智能推荐请先签署协议https://pub.alimama.com/fourth/protocol/common.htm?key=hangye_laxin
        """
        self._device_type = device_type
        """
            会员运营ID
        """
        self._special_id = special_id
        """
            渠道关系ID，仅适用于渠道推广场景
        """
        self._relation_id = relation_id
        """
            是否获取前N件佣金信息	0否，1是，其他值否
        """
        self._get_topn_rate = get_topn_rate
        """
            1-动态ID转链场景，2-消费者比价场景（不填默认为1）；场景id使用说明参考《淘宝客新商品ID升级》白皮书：https://www.yuque.com/taobaolianmengguanfangxiaoer/zmig94/tfyt0pahmlpzu2ud
        """
        self._biz_scene_id = biz_scene_id
        """
            1-自购省，2-推广赚（代理模式专属ID，代理模式必填，非代理模式不用填写该字段）
        """
        self._promotion_type = promotion_type
        """
            线报内容筛选—内容生产开始时间，13毫秒时间戳
        """
        self._mgc_start_time = mgc_start_time
        """
            线报内容筛选—内容生产截止时间，13毫秒时间戳
        """
        self._mgc_end_time = mgc_end_time
        """
            线报状态筛选，0-全部 1-过期 2-实时生效 3-未来生效 不传默认过滤有效
        """
        self._mgc_status = mgc_status
        """
            人群ID，仅适用于物料评估场景material_id=41377
        """
        self._ucrowd_id = ucrowd_id
        """
            物料评估-商品列表
        """
        self._ucrowd_rank_items = ucrowd_rank_items

    @property
    def start_dsr(self):
        return self._start_dsr

    @start_dsr.setter
    def start_dsr(self, start_dsr):
        if isinstance(start_dsr, int):
            self._start_dsr = start_dsr
        else:
            raise TypeError("start_dsr must be int")

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
    def end_tk_rate(self):
        return self._end_tk_rate

    @end_tk_rate.setter
    def end_tk_rate(self, end_tk_rate):
        if isinstance(end_tk_rate, int):
            self._end_tk_rate = end_tk_rate
        else:
            raise TypeError("end_tk_rate must be int")

    @property
    def start_tk_rate(self):
        return self._start_tk_rate

    @start_tk_rate.setter
    def start_tk_rate(self, start_tk_rate):
        if isinstance(start_tk_rate, int):
            self._start_tk_rate = start_tk_rate
        else:
            raise TypeError("start_tk_rate must be int")

    @property
    def end_price(self):
        return self._end_price

    @end_price.setter
    def end_price(self, end_price):
        if isinstance(end_price, int):
            self._end_price = end_price
        else:
            raise TypeError("end_price must be int")

    @property
    def start_price(self):
        return self._start_price

    @start_price.setter
    def start_price(self, start_price):
        if isinstance(start_price, int):
            self._start_price = start_price
        else:
            raise TypeError("start_price must be int")

    @property
    def is_overseas(self):
        return self._is_overseas

    @is_overseas.setter
    def is_overseas(self, is_overseas):
        if isinstance(is_overseas, bool):
            self._is_overseas = is_overseas
        else:
            raise TypeError("is_overseas must be bool")

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
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, sort):
        if isinstance(sort, str):
            self._sort = sort
        else:
            raise TypeError("sort must be str")

    @property
    def itemloc(self):
        return self._itemloc

    @itemloc.setter
    def itemloc(self, itemloc):
        if isinstance(itemloc, str):
            self._itemloc = itemloc
        else:
            raise TypeError("itemloc must be str")

    @property
    def cat(self):
        return self._cat

    @cat.setter
    def cat(self, cat):
        if isinstance(cat, str):
            self._cat = cat
        else:
            raise TypeError("cat must be str")

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
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, material_id):
        if isinstance(material_id, int):
            self._material_id = material_id
        else:
            raise TypeError("material_id must be int")

    @property
    def has_coupon(self):
        return self._has_coupon

    @has_coupon.setter
    def has_coupon(self, has_coupon):
        if isinstance(has_coupon, bool):
            self._has_coupon = has_coupon
        else:
            raise TypeError("has_coupon must be bool")

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
    def adzone_id(self):
        return self._adzone_id

    @adzone_id.setter
    def adzone_id(self, adzone_id):
        if isinstance(adzone_id, int):
            self._adzone_id = adzone_id
        else:
            raise TypeError("adzone_id must be int")

    @property
    def need_free_shipment(self):
        return self._need_free_shipment

    @need_free_shipment.setter
    def need_free_shipment(self, need_free_shipment):
        if isinstance(need_free_shipment, bool):
            self._need_free_shipment = need_free_shipment
        else:
            raise TypeError("need_free_shipment must be bool")

    @property
    def need_prepay(self):
        return self._need_prepay

    @need_prepay.setter
    def need_prepay(self, need_prepay):
        if isinstance(need_prepay, bool):
            self._need_prepay = need_prepay
        else:
            raise TypeError("need_prepay must be bool")

    @property
    def include_pay_rate_30(self):
        return self._include_pay_rate_30

    @include_pay_rate_30.setter
    def include_pay_rate_30(self, include_pay_rate_30):
        if isinstance(include_pay_rate_30, bool):
            self._include_pay_rate_30 = include_pay_rate_30
        else:
            raise TypeError("include_pay_rate_30 must be bool")

    @property
    def include_good_rate(self):
        return self._include_good_rate

    @include_good_rate.setter
    def include_good_rate(self, include_good_rate):
        if isinstance(include_good_rate, bool):
            self._include_good_rate = include_good_rate
        else:
            raise TypeError("include_good_rate must be bool")

    @property
    def include_rfd_rate(self):
        return self._include_rfd_rate

    @include_rfd_rate.setter
    def include_rfd_rate(self, include_rfd_rate):
        if isinstance(include_rfd_rate, bool):
            self._include_rfd_rate = include_rfd_rate
        else:
            raise TypeError("include_rfd_rate must be bool")

    @property
    def npx_level(self):
        return self._npx_level

    @npx_level.setter
    def npx_level(self, npx_level):
        if isinstance(npx_level, int):
            self._npx_level = npx_level
        else:
            raise TypeError("npx_level must be int")

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
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        if isinstance(device_type, str):
            self._device_type = device_type
        else:
            raise TypeError("device_type must be str")

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
    def relation_id(self):
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        if isinstance(relation_id, str):
            self._relation_id = relation_id
        else:
            raise TypeError("relation_id must be str")

    @property
    def get_topn_rate(self):
        return self._get_topn_rate

    @get_topn_rate.setter
    def get_topn_rate(self, get_topn_rate):
        if isinstance(get_topn_rate, int):
            self._get_topn_rate = get_topn_rate
        else:
            raise TypeError("get_topn_rate must be int")

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
    def mgc_start_time(self):
        return self._mgc_start_time

    @mgc_start_time.setter
    def mgc_start_time(self, mgc_start_time):
        if isinstance(mgc_start_time, str):
            self._mgc_start_time = mgc_start_time
        else:
            raise TypeError("mgc_start_time must be str")

    @property
    def mgc_end_time(self):
        return self._mgc_end_time

    @mgc_end_time.setter
    def mgc_end_time(self, mgc_end_time):
        if isinstance(mgc_end_time, str):
            self._mgc_end_time = mgc_end_time
        else:
            raise TypeError("mgc_end_time must be str")

    @property
    def mgc_status(self):
        return self._mgc_status

    @mgc_status.setter
    def mgc_status(self, mgc_status):
        if isinstance(mgc_status, str):
            self._mgc_status = mgc_status
        else:
            raise TypeError("mgc_status must be str")

    @property
    def ucrowd_id(self):
        return self._ucrowd_id

    @ucrowd_id.setter
    def ucrowd_id(self, ucrowd_id):
        if isinstance(ucrowd_id, int):
            self._ucrowd_id = ucrowd_id
        else:
            raise TypeError("ucrowd_id must be int")

    @property
    def ucrowd_rank_items(self):
        return self._ucrowd_rank_items

    @ucrowd_rank_items.setter
    def ucrowd_rank_items(self, ucrowd_rank_items):
        if isinstance(ucrowd_rank_items, list):
            self._ucrowd_rank_items = ucrowd_rank_items
        else:
            raise TypeError("ucrowd_rank_items must be list")


    def get_api_name(self):
        return "taobao.tbk.dg.material.optional.upgrade"

    def to_dict(self):
        request_dict = {}
        if self._start_dsr is not None:
            request_dict["start_dsr"] = convert_basic(self._start_dsr)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._end_tk_rate is not None:
            request_dict["end_tk_rate"] = convert_basic(self._end_tk_rate)

        if self._start_tk_rate is not None:
            request_dict["start_tk_rate"] = convert_basic(self._start_tk_rate)

        if self._end_price is not None:
            request_dict["end_price"] = convert_basic(self._end_price)

        if self._start_price is not None:
            request_dict["start_price"] = convert_basic(self._start_price)

        if self._is_overseas is not None:
            request_dict["is_overseas"] = convert_basic(self._is_overseas)

        if self._is_tmall is not None:
            request_dict["is_tmall"] = convert_basic(self._is_tmall)

        if self._sort is not None:
            request_dict["sort"] = convert_basic(self._sort)

        if self._itemloc is not None:
            request_dict["itemloc"] = convert_basic(self._itemloc)

        if self._cat is not None:
            request_dict["cat"] = convert_basic(self._cat)

        if self._q is not None:
            request_dict["q"] = convert_basic(self._q)

        if self._material_id is not None:
            request_dict["material_id"] = convert_basic(self._material_id)

        if self._has_coupon is not None:
            request_dict["has_coupon"] = convert_basic(self._has_coupon)

        if self._ip is not None:
            request_dict["ip"] = convert_basic(self._ip)

        if self._adzone_id is not None:
            request_dict["adzone_id"] = convert_basic(self._adzone_id)

        if self._need_free_shipment is not None:
            request_dict["need_free_shipment"] = convert_basic(self._need_free_shipment)

        if self._need_prepay is not None:
            request_dict["need_prepay"] = convert_basic(self._need_prepay)

        if self._include_pay_rate_30 is not None:
            request_dict["include_pay_rate_30"] = convert_basic(self._include_pay_rate_30)

        if self._include_good_rate is not None:
            request_dict["include_good_rate"] = convert_basic(self._include_good_rate)

        if self._include_rfd_rate is not None:
            request_dict["include_rfd_rate"] = convert_basic(self._include_rfd_rate)

        if self._npx_level is not None:
            request_dict["npx_level"] = convert_basic(self._npx_level)

        if self._device_encrypt is not None:
            request_dict["device_encrypt"] = convert_basic(self._device_encrypt)

        if self._device_value is not None:
            request_dict["device_value"] = convert_basic(self._device_value)

        if self._device_type is not None:
            request_dict["device_type"] = convert_basic(self._device_type)

        if self._special_id is not None:
            request_dict["special_id"] = convert_basic(self._special_id)

        if self._relation_id is not None:
            request_dict["relation_id"] = convert_basic(self._relation_id)

        if self._get_topn_rate is not None:
            request_dict["get_topn_rate"] = convert_basic(self._get_topn_rate)

        if self._biz_scene_id is not None:
            request_dict["biz_scene_id"] = convert_basic(self._biz_scene_id)

        if self._promotion_type is not None:
            request_dict["promotion_type"] = convert_basic(self._promotion_type)

        if self._mgc_start_time is not None:
            request_dict["mgc_start_time"] = convert_basic(self._mgc_start_time)

        if self._mgc_end_time is not None:
            request_dict["mgc_end_time"] = convert_basic(self._mgc_end_time)

        if self._mgc_status is not None:
            request_dict["mgc_status"] = convert_basic(self._mgc_status)

        if self._ucrowd_id is not None:
            request_dict["ucrowd_id"] = convert_basic(self._ucrowd_id)

        if self._ucrowd_rank_items is not None:
            request_dict["ucrowd_rank_items"] = convert_struct_list(self._ucrowd_rank_items)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoTbkDgMaterialOptionalUpgradeUcrowdrankitems:
    def __init__(
        self,
        commirate: int = None,
        price: str = None,
        item_id: str = None
    ):
        """
            物料评估-商品佣金率，如：1234表示12.34%，material_id=41377时选填
        """
        self.commirate = commirate
        """
            物料评估-商品价格，单位：元，material_id=41377时选填
        """
        self.price = price
        """
            物料评估-商品ID，material_id=41377时必填
        """
        self.item_id = item_id

