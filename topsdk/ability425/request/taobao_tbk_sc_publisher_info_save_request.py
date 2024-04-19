from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTbkScPublisherInfoSaveRequest(BaseRequest):

    def __init__(
        self,
        relation_from: str = None,
        offline_scene: str = None,
        online_scene: str = None,
        inviter_code: str = None,
        info_type: int = None,
        note: str = None,
        register_info: str = None
    ):
        """
            渠道备案 - 来源，取链接的来源
        """
        self._relation_from = relation_from
        """
            渠道备案 - 线下场景信息，1 - 门店，2- 学校，3 - 工厂，4 - 其他
        """
        self._offline_scene = offline_scene
        """
            渠道备案 - 线上场景信息，1 - 微信群，2- QQ群，3 - 其他
        """
        self._online_scene = online_scene
        """
            淘宝客邀请渠道或会员的邀请码
        """
        self._inviter_code = inviter_code
        """
            类型，必选 默认为1:
        """
        self._info_type = info_type
        """
            媒体侧渠道备注
        """
        self._note = note
        """
            线下备案注册信息,字段包含: 电话号码(phoneNumber，必填),省(province,必填),市(city,必填),区县街道(location,必填),详细地址(detailAddress,必填),经营类型(career,线下个人必填),店铺类型(shopType,线下店铺必填),店铺名称(shopName,线下店铺必填),店铺证书类型(shopCertifyType,线下店铺选填),店铺证书编号(certifyNumber,线下店铺选填)
        """
        self._register_info = register_info

    @property
    def relation_from(self):
        return self._relation_from

    @relation_from.setter
    def relation_from(self, relation_from):
        if isinstance(relation_from, str):
            self._relation_from = relation_from
        else:
            raise TypeError("relation_from must be str")

    @property
    def offline_scene(self):
        return self._offline_scene

    @offline_scene.setter
    def offline_scene(self, offline_scene):
        if isinstance(offline_scene, str):
            self._offline_scene = offline_scene
        else:
            raise TypeError("offline_scene must be str")

    @property
    def online_scene(self):
        return self._online_scene

    @online_scene.setter
    def online_scene(self, online_scene):
        if isinstance(online_scene, str):
            self._online_scene = online_scene
        else:
            raise TypeError("online_scene must be str")

    @property
    def inviter_code(self):
        return self._inviter_code

    @inviter_code.setter
    def inviter_code(self, inviter_code):
        if isinstance(inviter_code, str):
            self._inviter_code = inviter_code
        else:
            raise TypeError("inviter_code must be str")

    @property
    def info_type(self):
        return self._info_type

    @info_type.setter
    def info_type(self, info_type):
        if isinstance(info_type, int):
            self._info_type = info_type
        else:
            raise TypeError("info_type must be int")

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, note):
        if isinstance(note, str):
            self._note = note
        else:
            raise TypeError("note must be str")

    @property
    def register_info(self):
        return self._register_info

    @register_info.setter
    def register_info(self, register_info):
        if isinstance(register_info, str):
            self._register_info = register_info
        else:
            raise TypeError("register_info must be str")


    def get_api_name(self):
        return "taobao.tbk.sc.publisher.info.save"

    def to_dict(self):
        request_dict = {}
        if self._relation_from is not None:
            request_dict["relation_from"] = convert_basic(self._relation_from)

        if self._offline_scene is not None:
            request_dict["offline_scene"] = convert_basic(self._offline_scene)

        if self._online_scene is not None:
            request_dict["online_scene"] = convert_basic(self._online_scene)

        if self._inviter_code is not None:
            request_dict["inviter_code"] = convert_basic(self._inviter_code)

        if self._info_type is not None:
            request_dict["info_type"] = convert_basic(self._info_type)

        if self._note is not None:
            request_dict["note"] = convert_basic(self._note)

        if self._register_info is not None:
            request_dict["register_info"] = convert_basic(self._register_info)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

