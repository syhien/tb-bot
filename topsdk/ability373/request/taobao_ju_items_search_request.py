from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoJuItemsSearchRequest(BaseRequest):

    def __init__(
        self,
        param_top_item_query: object = None
    ):
        """
            query
        """
        self._param_top_item_query = param_top_item_query

    @property
    def param_top_item_query(self):
        return self._param_top_item_query

    @param_top_item_query.setter
    def param_top_item_query(self, param_top_item_query):
        if isinstance(param_top_item_query, object):
            self._param_top_item_query = param_top_item_query
        else:
            raise TypeError("param_top_item_query must be object")


    def get_api_name(self):
        return "taobao.ju.items.search"

    def to_dict(self):
        request_dict = {}
        if self._param_top_item_query is not None:
            request_dict["param_top_item_query"] = convert_struct(self._param_top_item_query)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoJuItemsSearchTopItemQuery:
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        pid: str = None,
        postage: bool = None,
        status: int = None,
        taobao_category_id: int = None,
        word: str = None
    ):
        """
            页码,必传
        """
        self.current_page = current_page
        """
            一页大小,必传
        """
        self.page_size = page_size
        """
            媒体pid,必传
        """
        self.pid = pid
        """
            是否包邮,可不传
        """
        self.postage = postage
        """
            状态，预热：1，正在进行中：2,可不传
        """
        self.status = status
        """
            淘宝类目id,可不传
        """
        self.taobao_category_id = taobao_category_id
        """
            搜索关键词,可不传
        """
        self.word = word

