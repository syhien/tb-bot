from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkTpwdCreateRequest(BaseRequest):

    def __init__(
        self,
        text: str = None,
        logo: str = None,
        ext: str = None,
        user_id: str = None,
        url: str = None
    ):
        """
            兼容旧版本api参数，无实际作用
        """
        self._text = text
        """
            兼容旧版本api参数，无实际作用
        """
        self._logo = logo
        """
            兼容旧版本api参数，无实际作用
        """
        self._ext = ext
        """
            兼容旧版本api参数，无实际作用
        """
        self._user_id = user_id
        """
            联盟官方渠道获取的淘客推广链接，请注意，不要随意篡改官方生成的链接，否则可能无法生成淘口令
        """
        self._url = url

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if isinstance(text, str):
            self._text = text
        else:
            raise TypeError("text must be str")

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, logo):
        if isinstance(logo, str):
            self._logo = logo
        else:
            raise TypeError("logo must be str")

    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, ext):
        if isinstance(ext, str):
            self._ext = ext
        else:
            raise TypeError("ext must be str")

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if isinstance(user_id, str):
            self._user_id = user_id
        else:
            raise TypeError("user_id must be str")

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        if isinstance(url, str):
            self._url = url
        else:
            raise TypeError("url must be str")


    def get_api_name(self):
        return "taobao.tbk.tpwd.create"

    def to_dict(self):
        request_dict = {}
        if self._text is not None:
            request_dict["text"] = convert_basic(self._text)

        if self._logo is not None:
            request_dict["logo"] = convert_basic(self._logo)

        if self._ext is not None:
            request_dict["ext"] = convert_basic(self._ext)

        if self._user_id is not None:
            request_dict["user_id"] = convert_basic(self._user_id)

        if self._url is not None:
            request_dict["url"] = convert_basic(self._url)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

