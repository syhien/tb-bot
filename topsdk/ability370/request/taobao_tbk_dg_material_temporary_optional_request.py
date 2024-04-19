from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkDgMaterialTemporaryOptionalRequest(BaseRequest):

    def __init__(
        self,
        start_dsr: int = None,
        page_size: int = None,
        page_no: int = None,
        platform: int = None,
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
        end_ka_tk_rate: int = None,
        start_ka_tk_rate: int = None,
        lock_rate_end_time: int = None,
        lock_rate_start_time: int = None,
        longitude: str = None,
        latitude: str = None,
        city_code: str = None,
        seller_ids: str = None,
        special_id: str = None,
        relation_id: str = None,
        page_result_key: str = None,
        ucrowd_id: int = None,
        ucrowd_rank_items: list = None,
        get_topn_rate: int = None
    ):
        """
            商品筛选(特定媒体支持)-店铺dsr评分。筛选大于等于当前设置的店铺dsr评分的商品0-50000之间
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
            链接形式：1：PC，2：无线，默认：１
        """
        self._platform = platform
        """
            商品筛选-淘客佣金比率上限。如：1234表示12.34%
        """
        self._end_tk_rate = end_tk_rate
        """
            商品筛选-淘客佣金比率下限。如：1234表示12.34%
        """
        self._start_tk_rate = start_tk_rate
        """
            商品筛选-折扣价范围上限。单位：元
        """
        self._end_price = end_price
        """
            商品筛选-折扣价范围下限。单位：元
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
            排序_des（降序），排序_asc（升序），销量（total_sales），淘客佣金比率（tk_rate）， 累计推广量（tk_total_sales），总支出佣金（tk_total_commi），价格（price），匹配分（match）
        """
        self._sort = sort
        """
            商品筛选-所在地
        """
        self._itemloc = itemloc
        """
            商品筛选-后台类目ID。用,分割，最大10个，该ID可以通过taobao.itemcats.get接口获取到
        """
        self._cat = cat
        """
            商品筛选-查询词
        """
        self._q = q
        """
            不传时默认物料id=2836；如果直接对消费者投放，可使用官方个性化算法优化的搜索物料id=17004
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
            mm_xxx_xxx_12345678三段式的最后一段数字
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
            商品筛选(特定媒体支持)-成交转化是否高于行业均值。True表示大于等于，false或不设置表示不限
        """
        self._include_pay_rate_30 = include_pay_rate_30
        """
            商品筛选-好评率是否高于行业均值。True表示大于等于，false或不设置表示不限
        """
        self._include_good_rate = include_good_rate
        """
            商品筛选(特定媒体支持)-退款率是否低于行业均值。True表示大于等于，false或不设置表示不限
        """
        self._include_rfd_rate = include_rfd_rate
        """
            商品筛选-牛皮癣程度。取值：1不限，2无，3轻微
        """
        self._npx_level = npx_level
        """
            智能匹配-设备号加密类型：MD5
        """
        self._device_encrypt = device_encrypt
        """
            智能匹配-设备号加密后的值（MD5加密需32位小写）
        """
        self._device_value = device_value
        """
            智能匹配-设备类型：IMEI/IDFA/UTDID/OAID，（IOS推荐使用IDFA，android等推荐使用OAID）
        """
        self._device_type = device_type
        """
            商品筛选-KA媒体淘客佣金比率上限。如：1234表示12.34%
        """
        self._end_ka_tk_rate = end_ka_tk_rate
        """
            商品筛选-KA媒体淘客佣金比率下限。如：1234表示12.34%
        """
        self._start_ka_tk_rate = start_ka_tk_rate
        """
            锁佣结束时间
        """
        self._lock_rate_end_time = lock_rate_end_time
        """
            锁佣开始时间
        """
        self._lock_rate_start_time = lock_rate_start_time
        """
            本地化业务入参-LBS信息-经度
        """
        self._longitude = longitude
        """
            本地化业务入参-LBS信息-纬度
        """
        self._latitude = latitude
        """
            本地化业务入参-LBS信息-国标城市码，仅支持单个请求，请求饿了么卡券物料时，该字段必填。 （详细城市ID见：https://mo.m.taobao.com/page_2020010315120200508）
        """
        self._city_code = city_code
        """
            商家id，仅支持饿了么卡券商家ID，支持批量请求1-100以内，多个商家ID使用英文逗号分隔
        """
        self._seller_ids = seller_ids
        """
            会员运营ID
        """
        self._special_id = special_id
        """
            渠道关系ID，仅适用于渠道推广场景
        """
        self._relation_id = relation_id
        """
            本地化业务入参-分页唯一标识，非首页的请求必传，值为上一页返回结果中的page_result_key字段值
        """
        self._page_result_key = page_result_key
        """
            人群ID，仅适用于物料评估场景material_id=41377
        """
        self._ucrowd_id = ucrowd_id
        """
            物料评估-商品列表
        """
        self._ucrowd_rank_items = ucrowd_rank_items
        """
            是否获取前N件佣金信息	0否，1是，其他值否
        """
        self._get_topn_rate = get_topn_rate

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
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, platform):
        if isinstance(platform, int):
            self._platform = platform
        else:
            raise TypeError("platform must be int")

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
    def end_ka_tk_rate(self):
        return self._end_ka_tk_rate

    @end_ka_tk_rate.setter
    def end_ka_tk_rate(self, end_ka_tk_rate):
        if isinstance(end_ka_tk_rate, int):
            self._end_ka_tk_rate = end_ka_tk_rate
        else:
            raise TypeError("end_ka_tk_rate must be int")

    @property
    def start_ka_tk_rate(self):
        return self._start_ka_tk_rate

    @start_ka_tk_rate.setter
    def start_ka_tk_rate(self, start_ka_tk_rate):
        if isinstance(start_ka_tk_rate, int):
            self._start_ka_tk_rate = start_ka_tk_rate
        else:
            raise TypeError("start_ka_tk_rate must be int")

    @property
    def lock_rate_end_time(self):
        return self._lock_rate_end_time

    @lock_rate_end_time.setter
    def lock_rate_end_time(self, lock_rate_end_time):
        if isinstance(lock_rate_end_time, int):
            self._lock_rate_end_time = lock_rate_end_time
        else:
            raise TypeError("lock_rate_end_time must be int")

    @property
    def lock_rate_start_time(self):
        return self._lock_rate_start_time

    @lock_rate_start_time.setter
    def lock_rate_start_time(self, lock_rate_start_time):
        if isinstance(lock_rate_start_time, int):
            self._lock_rate_start_time = lock_rate_start_time
        else:
            raise TypeError("lock_rate_start_time must be int")

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        if isinstance(longitude, str):
            self._longitude = longitude
        else:
            raise TypeError("longitude must be str")

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        if isinstance(latitude, str):
            self._latitude = latitude
        else:
            raise TypeError("latitude must be str")

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, city_code):
        if isinstance(city_code, str):
            self._city_code = city_code
        else:
            raise TypeError("city_code must be str")

    @property
    def seller_ids(self):
        return self._seller_ids

    @seller_ids.setter
    def seller_ids(self, seller_ids):
        if isinstance(seller_ids, str):
            self._seller_ids = seller_ids
        else:
            raise TypeError("seller_ids must be str")

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
    def page_result_key(self):
        return self._page_result_key

    @page_result_key.setter
    def page_result_key(self, page_result_key):
        if isinstance(page_result_key, str):
            self._page_result_key = page_result_key
        else:
            raise TypeError("page_result_key must be str")

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

    @property
    def get_topn_rate(self):
        return self._get_topn_rate

    @get_topn_rate.setter
    def get_topn_rate(self, get_topn_rate):
        if isinstance(get_topn_rate, int):
            self._get_topn_rate = get_topn_rate
        else:
            raise TypeError("get_topn_rate must be int")


    def get_api_name(self):
        return "taobao.tbk.dg.material.temporary.optional"

    def to_dict(self):
        request_dict = {}
        if self._start_dsr is not None:
            request_dict["start_dsr"] = convert_basic(self._start_dsr)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._platform is not None:
            request_dict["platform"] = convert_basic(self._platform)

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

        if self._end_ka_tk_rate is not None:
            request_dict["end_ka_tk_rate"] = convert_basic(self._end_ka_tk_rate)

        if self._start_ka_tk_rate is not None:
            request_dict["start_ka_tk_rate"] = convert_basic(self._start_ka_tk_rate)

        if self._lock_rate_end_time is not None:
            request_dict["lock_rate_end_time"] = convert_basic(self._lock_rate_end_time)

        if self._lock_rate_start_time is not None:
            request_dict["lock_rate_start_time"] = convert_basic(self._lock_rate_start_time)

        if self._longitude is not None:
            request_dict["longitude"] = convert_basic(self._longitude)

        if self._latitude is not None:
            request_dict["latitude"] = convert_basic(self._latitude)

        if self._city_code is not None:
            request_dict["city_code"] = convert_basic(self._city_code)

        if self._seller_ids is not None:
            request_dict["seller_ids"] = convert_basic(self._seller_ids)

        if self._special_id is not None:
            request_dict["special_id"] = convert_basic(self._special_id)

        if self._relation_id is not None:
            request_dict["relation_id"] = convert_basic(self._relation_id)

        if self._page_result_key is not None:
            request_dict["page_result_key"] = convert_basic(self._page_result_key)

        if self._ucrowd_id is not None:
            request_dict["ucrowd_id"] = convert_basic(self._ucrowd_id)

        if self._ucrowd_rank_items is not None:
            request_dict["ucrowd_rank_items"] = convert_struct_list(self._ucrowd_rank_items)

        if self._get_topn_rate is not None:
            request_dict["get_topn_rate"] = convert_basic(self._get_topn_rate)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoTbkDgMaterialTemporaryOptionalUcrowdrankitems:
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

