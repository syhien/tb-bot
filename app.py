from flask import Flask, render_template, request

app = Flask(__name__)

from topsdk.client import TopApiClient
from topsdk.defaultability.defaultability import Defaultability
from topsdk.defaultability.request.taobao_tbk_dg_material_optional_upgrade_request import (
    TaobaoTbkDgMaterialOptionalUpgradeRequest,
)
from topsdk.ability375.ability375 import Ability375
from topsdk.ability375.request.taobao_tbk_tpwd_create_request import (
    TaobaoTbkTpwdCreateRequest,
)
import zhon.hanzi
import re


def taobao(message):
    client = TopApiClient(
        appkey="33082016",
        app_sercet="df6564cdf0c69b64581f915c4b770324",
        top_gateway_url="https://eco.taobao.com/router/rest",
        verify_ssl=False,
    )
    material_ability = Defaultability(client)
    material_request = TaobaoTbkDgMaterialOptionalUpgradeRequest(
        adzone_id="111713900272", material_id="6707"
    )

    possible_keywords = re.split("[{}]".format(zhon.hanzi.non_stops), message)
    keywords = []
    for i in possible_keywords:
        if len(re.findall("[%s]" % zhon.hanzi.characters, i)) > 0:
            keywords.append(i)
    if len(keywords) == 0:
        return "请输入搜索关键词", "请输入搜索关键词"
    keyword = sorted(keywords, key=lambda x: len(x), reverse=True)[0]
    if keyword == "":
        return "请输入搜索关键词", "请输入搜索关键词"

    keyword += "淘宝天猫"
    print(keyword)
    material_request.q = keyword
    try:
        material_response = material_ability.taobao_tbk_dg_material_optional_upgrade(
            material_request
        )
        material_info = material_response["result_list"][0]
    except Exception as e:
        return (
            "没有找到相关商品，识别出的关键词是："
            + keyword
            + "\n如识别无明显错漏则可能是单纯没开推广",
            str(e),
        )

    msg = material_info["publish_info"]["income_rate"] + "%\n"

    link = (
        material_info["publish_info"]["coupon_share_url"]
        if "coupon_share_url" in material_info["publish_info"]
        else material_info["publish_info"]["click_url"]
    )
    link = "https:" + link

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


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        keyword = request.form.get("keyword")
        result, link = taobao(keyword)
        return render_template("result.html", result=result, link=link)
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    keyword = request.form.get("keyword")
    result, link = taobao(keyword)
    return render_template("result.html", result=result, link=link)


if __name__ == "__main__":
    app.run(debug=True, host="::", port=80)
