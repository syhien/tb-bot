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

        # Process multiple results (up to 10 items)
        results = []
        for material_info in material_response["result_list"][:10]:
            # Extract the link
            link = (
                material_info["publish_info"]["coupon_share_url"]
                if "coupon_share_url" in material_info["publish_info"]
                else material_info["publish_info"]["click_url"]
            )

            # Extract item information
            item = {
                "title": material_info["item_basic_info"]["title"],
                "price": material_info["price_promotion_info"]["zk_final_price"],
                "shop_name": material_info["item_basic_info"]["shop_title"],
                "income_rate": material_info["publish_info"]["income_rate"],
                "link": "https:" + link if link else ""
            }
            results.append(item)

        if results:
            return results
    raise Exception("No item found")


def taobao(message):
    client = TopApiClient(
        appkey="33082016",
        app_sercet="df6564cdf0c69b64581f915c4b770324",
        top_gateway_url="https://eco.taobao.com/router/rest",
    )
    items = None
    for _ in range(3):
        try:
            items = search_item(client, message)
        except Exception as e:
            pass
        if items is not None:
            break
    if items is None:
        return "未找到商品，疑似真的没加推广", []

    tpwd_ability = Ability375(client)

    # Build structured results with tpwd for each item
    results = []
    msg = f"找到 {len(items)} 个商品：\n\n"
    links = []

    for i, item in enumerate(items, 1):
        # Generate tpwd for each item
        tpwd = ""
        try:
            tpwd_request = TaobaoTbkTpwdCreateRequest(
                url=item['link'],
            )
            tpwd_response = tpwd_ability.taobao_tbk_tpwd_create(tpwd_request)
            tpwd = tpwd_response["data"]["model"]
        except Exception as e:
            tpwd = ""

        # Build formatted message
        msg += f"{i}. {item['title']}\n"
        msg += f"   价格: {item['price']}\n"
        msg += f"   店铺: {item['shop_name']}\n"
        msg += f"   收入: {item['income_rate']}%\n"
        if tpwd:
            msg += f"   淘口令: {tpwd}\n\n"
        else:
            msg += f"   链接: {item['link']}\n\n"

        # Extract clean link for storage
        link_match = re.search(r"(?P<url>https?://[^\s]+)", tpwd) if tpwd else None
        if link_match:
            clean_link = link_match.group("url").replace("https://", "")
            links.append(clean_link)
        else:
            links.append(item['link'].replace("https://", ""))

        # Add tpwd to structured data
        result_item = item.copy()
        result_item['tpwd'] = tpwd
        results.append(result_item)

    return results, msg, links
