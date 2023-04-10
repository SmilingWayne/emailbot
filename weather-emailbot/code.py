import requests


# NJ：101190101
# TZ：101191201

# api地址

if __name__ == "__main__":
    url = 'http://t.weather.sojson.com/api/weather/city/'
    try:
        response_NJ = requests.get(url + "101190101")
        d = response_NJ.json()
        message = ""
        if(d['status'] == 200):
            message += ("城市：" + d["cityInfo"]["parent"] +
                        d["cityInfo"]["city"] + "\n")
            message += ("温度：" + d["data"]["forecast"][0]["high"] +
                        "  " + d["data"]["forecast"][0]["low"] + "\n")
            message += ("天气: " + d["data"]["forecast"][0]["type"] + "\n")
            if "雨" in d["data"]["forecast"][0]["type"]:
                message += ("下雨，别忘记带雨伞～" + "\n")
            message += "记得微笑😊天天开心～"
            # message += ("城市：" + d["cityInfo"]["parent"], d["cityInfo"]["city"] + "\n")
            # print(message)
    except Exception:
        message = "数据载入失败～机器人故障~(BIBI)\n"

    with open("ToSendEmail.txt", 'w', encoding="utf-8") as email:
        email.writelines(message)
