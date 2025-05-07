import random
from topsdk.client import TopApiClient
from topsdk.defaultability.defaultability import Defaultability
from topsdk.defaultability.request.taobao_tbk_dg_material_optional_upgrade_request import (
    TaobaoTbkDgMaterialOptionalUpgradeRequest,
)
from topsdk.ability375.ability375 import Ability375
from topsdk.ability375.request.taobao_tbk_tpwd_create_request import (
    TaobaoTbkTpwdCreateRequest,
)
import re


def random_drop_char(s):
    if len(s) > 1:
        i = random.randint(0, len(s) - 1)
        while s[i] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            i = random.randint(0, len(s) - 1)
        return s[:i] + s[i + 1 :]
    return s


def search_item(client, keyword):
    material_ability = Defaultability(client)
    material_request = TaobaoTbkDgMaterialOptionalUpgradeRequest(
        adzone_id="111713900272", material_id="6707"
    )
    link = ""
    for _ in range(5):
        if keyword == "":
            raise Exception("Empty keyword")
        print(keyword)
        material_request.q = keyword
        material_response = material_ability.taobao_tbk_dg_material_optional_upgrade(
            material_request
        )
        if len(material_response["result_list"]) == 0:
            keyword = random_drop_char(keyword)
            continue
        material_info = material_response["result_list"][0]
        link = (
            material_info["publish_info"]["coupon_share_url"]
            if "coupon_share_url" in material_info["publish_info"]
            else material_info["publish_info"]["click_url"]
        )
        if link != "":
            return material_info["publish_info"]["income_rate"] + "%\n", "https:" + link
    raise Exception("No item found")


def taobao(message):
    client = TopApiClient(
        appkey="33082016",
        app_sercet="df6564cdf0c69b64581f915c4b770324",
        top_gateway_url="https://eco.taobao.com/router/rest",
    )
    link = None
    for _ in range(3):
        try:
            msg, link = search_item(client, message)
        except Exception as e:
            pass
        if link is not None:
            break
    if link is None:
        return "未找到商品，疑似真的没加推广", "None"

    tpwd_ability = Ability375(client)
    tpwd_request = TaobaoTbkTpwdCreateRequest(
        url=link,
    )
    try:
        tpwd_response = tpwd_ability.taobao_tbk_tpwd_create(tpwd_request)
        msg += tpwd_response["data"]["model"]
    except Exception as e:
        msg += "获取淘口令失败\n"
        msg += link

    link = re.search("(?P<url>https?://[^\s]+)", msg)  # extracting link with regex
    if link is not None:
        link = link.group("url")
        link = link.replace("https://", "")  # remove https:// from link
    return msg, link
