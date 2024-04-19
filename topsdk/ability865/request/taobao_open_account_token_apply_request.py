from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoOpenAccountTokenApplyRequest(BaseRequest):

    def __init__(
        self,
        isv_account_id: str = None,
        login_state_expire_in: int = None,
        open_account_id: int = None,
        token_timestamp: int = None,
        uuid: str = None,
        ext: dict = None
    ):
        """
            isv自己账号的唯一id
        """
        self._isv_account_id = isv_account_id
        """
            ISV APP的登录态时长单位是秒
        """
        self._login_state_expire_in = login_state_expire_in
        """
            open account id
        """
        self._open_account_id = open_account_id
        """
            时间戳单位是毫秒
        """
        self._token_timestamp = token_timestamp
        """
            用于防重放的唯一id
        """
        self._uuid = uuid
        """
            用于透传一些业务附加参数
        """
        self._ext = ext

    @property
    def isv_account_id(self):
        return self._isv_account_id

    @isv_account_id.setter
    def isv_account_id(self, isv_account_id):
        if isinstance(isv_account_id, str):
            self._isv_account_id = isv_account_id
        else:
            raise TypeError("isv_account_id must be str")

    @property
    def login_state_expire_in(self):
        return self._login_state_expire_in

    @login_state_expire_in.setter
    def login_state_expire_in(self, login_state_expire_in):
        if isinstance(login_state_expire_in, int):
            self._login_state_expire_in = login_state_expire_in
        else:
            raise TypeError("login_state_expire_in must be int")

    @property
    def open_account_id(self):
        return self._open_account_id

    @open_account_id.setter
    def open_account_id(self, open_account_id):
        if isinstance(open_account_id, int):
            self._open_account_id = open_account_id
        else:
            raise TypeError("open_account_id must be int")

    @property
    def token_timestamp(self):
        return self._token_timestamp

    @token_timestamp.setter
    def token_timestamp(self, token_timestamp):
        if isinstance(token_timestamp, int):
            self._token_timestamp = token_timestamp
        else:
            raise TypeError("token_timestamp must be int")

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        if isinstance(uuid, str):
            self._uuid = uuid
        else:
            raise TypeError("uuid must be str")

    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, ext):
        if isinstance(ext, dict):
            self._ext = ext
        else:
            raise TypeError("ext must be dict")


    def get_api_name(self):
        return "taobao.open.account.token.apply"

    def to_dict(self):
        request_dict = {}
        if self._isv_account_id is not None:
            request_dict["isv_account_id"] = convert_basic(self._isv_account_id)

        if self._login_state_expire_in is not None:
            request_dict["login_state_expire_in"] = convert_basic(self._login_state_expire_in)

        if self._open_account_id is not None:
            request_dict["open_account_id"] = convert_basic(self._open_account_id)

        if self._token_timestamp is not None:
            request_dict["token_timestamp"] = convert_basic(self._token_timestamp)

        if self._uuid is not None:
            request_dict["uuid"] = convert_basic(self._uuid)

        if self._ext is not None:
            request_dict["ext"] = convert_struct(self._ext)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

