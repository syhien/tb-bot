from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkOptimusTouMaterialIdsGetRequest(BaseRequest):

    def __init__(
        self,
        material_query: object = None
    ):
        """
            请求结构
        """
        self._material_query = material_query

    @property
    def material_query(self):
        return self._material_query

    @material_query.setter
    def material_query(self, material_query):
        if isinstance(material_query, object):
            self._material_query = material_query
        else:
            raise TypeError("material_query must be object")


    def get_api_name(self):
        return "taobao.tbk.optimus.tou.material.ids.get"

    def to_dict(self):
        request_dict = {}
        if self._material_query is not None:
            request_dict["material_query"] = convert_struct(self._material_query)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoTbkOptimusTouMaterialIdsGetMaterialQuery:
    def __init__(
        self,
        page_no: int = None,
        subject: int = None,
        material_type: int = None,
        page_size: int = None
    ):
        """
            页码，默认1，取值范围1~100
        """
        self.page_no = page_no
        """
            物料主题类型, 1促销活动;2热门主题;3精选榜单;4行业频道等;5其他
        """
        self.subject = subject
        """
            物料类型，1: 商品；2:权益
        """
        self.material_type = material_type
        """
            每页物料id数量，默认20，取值范围1~100
        """
        self.page_size = page_size

