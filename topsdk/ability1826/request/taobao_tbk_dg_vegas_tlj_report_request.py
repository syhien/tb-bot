from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkDgVegasTljReportRequest(BaseRequest):

    def __init__(
        self,
        adzone_id: int = None,
        rights_id: str = None
    ):
        """
            adzoneId
        """
        self._adzone_id = adzone_id
        """
            创建淘礼金时返回的rightsId
        """
        self._rights_id = rights_id

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
    def rights_id(self):
        return self._rights_id

    @rights_id.setter
    def rights_id(self, rights_id):
        if isinstance(rights_id, str):
            self._rights_id = rights_id
        else:
            raise TypeError("rights_id must be str")


    def get_api_name(self):
        return "taobao.tbk.dg.vegas.tlj.report"

    def to_dict(self):
        request_dict = {}
        if self._adzone_id is not None:
            request_dict["adzone_id"] = convert_basic(self._adzone_id)

        if self._rights_id is not None:
            request_dict["rights_id"] = convert_basic(self._rights_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

