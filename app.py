from flask import Flask, render_template, request
app = Flask(__name__)

def taobao(message):
    import top
    import top.api
    import top.api.base
    import zhon.hanzi
    import re
    find_req = top.api.TbkDgMaterialOptionalRequest(
        domain="http://gw.api.taobao.com/router/rest"
    )
    find_req.set_app_info(top.appinfo("33082016", "df6564cdf0c69b64581f915c4b770324"))
    find_req.adzone_id = "111713900272"
    find_req.material_id = "6707"

    ring_req = top.api.TbkTpwdCreateRequest(domain="http://gw.api.taobao.com/router/rest")
    ring_req.set_app_info(top.appinfo("33082016", "df6564cdf0c69b64581f915c4b770324"))

    possible_keywords = re.split("[{}]".format(zhon.hanzi.non_stops), message)
    keywords = []
    for i in possible_keywords:
        if len(re.findall("[%s]" % zhon.hanzi.characters, i)) > 0:
            keywords.append(i)
    if len(keywords) == 0:
        return "请输入搜索关键词"
    keyword = sorted(keywords, key=lambda x: len(x), reverse=True)[0]
    if keyword == "":
        return "请输入搜索关键词"

    print(keyword)
    find_req.q = keyword
    try:
        find_resqonse = find_req.getResponse()["tbk_dg_material_optional_response"][
            "result_list"
        ]["map_data"][0]
    except top.api.base.TopException:
        return "没有找到相关商品"

    msg = str(float(find_resqonse["commission_rate"]) / 100) + "%\n"

    if find_resqonse["url"] == "":
        keyword = keyword + "淘宝"
        find_req.q = keyword
        try:
            find_resqonse = find_req.getResponse()["tbk_dg_material_optional_response"][
                "result_list"
            ]["map_data"][0]
        except top.api.base.TopException:
            return "没有找到相关商品"

    if "coupon_share_url" in find_resqonse:
        ring_req.url = "https:" + find_resqonse["coupon_share_url"]
    else:
        ring_req.url = "https:" + find_resqonse["url"]

    msg += ring_req.getResponse()["tbk_tpwd_create_response"]["data"]["model"]
    link = re.search("(?P<url>https?://[^\s]+)", msg) # extracting link with regex
    if link is not None:
        link = link.group("url")
    return msg, link

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        keyword = request.form.get('keyword')
        result, link = taobao(keyword)
        return render_template('result.html', result=result, link=link)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False, host='::', port=80)