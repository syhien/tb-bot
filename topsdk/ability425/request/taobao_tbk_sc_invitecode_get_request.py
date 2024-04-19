from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkScInvitecodeGetRequest(BaseRequest):

    def __init__(
        self,
        relation_id: int = None,
        relation_app: str = None,
        code_type: int = None
    ):
        """
            渠道关系ID
        """
        self._relation_id = relation_id
        """
            渠道推广的物料类型
        """
        self._relation_app = relation_app
        """
            邀请码类型，1 - 渠道邀请，2 - 渠道裂变，3 -会员邀请
        """
        self._code_type = code_type

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
    def relation_app(self):
        return self._relation_app

    @relation_app.setter
    def relation_app(self, relation_app):
        if isinstance(relation_app, str):
            self._relation_app = relation_app
        else:
            raise TypeError("relation_app must be str")

    @property
    def code_type(self):
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        if isinstance(code_type, int):
            self._code_type = code_type
        else:
            raise TypeError("code_type must be int")


    def get_api_name(self):
        return "taobao.tbk.sc.invitecode.get"

    def to_dict(self):
        request_dict = {}
        if self._relation_id is not None:
            request_dict["relation_id"] = convert_basic(self._relation_id)

        if self._relation_app is not None:
            request_dict["relation_app"] = convert_basic(self._relation_app)

        if self._code_type is not None:
            request_dict["code_type"] = convert_basic(self._code_type)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

