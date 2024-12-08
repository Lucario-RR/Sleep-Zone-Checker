from datetime import datetime,timezone
import random

# Configs
sleep_time = 22
probability = 0.2 # Lucky draw

time_zones = {
    -12: ["美国贝克岛", "美国豪兰岛","新西兰奥克兰", "新西兰惠灵顿", "斐济"],
    -11.25: ["新西兰查塔姆群岛"],
    -11: ["美属萨摩亚", "美国中途岛","汤加", "萨摩亚", "托克劳"],
    -10: ["美国夏威夷", "库克群岛", "莱恩群岛", "基里巴斯", "法属波利尼西亚"],
    -9: ["美国阿拉斯加", "美国甘贝尔"],
    -8: ["美国洛杉矶", "加拿大温哥华"],
    -7: ["美国丹佛", "美国菲尼克斯", "加拿大"],
    -6: ["美国芝加哥", "墨西哥", "危地马拉", "洪都拉斯", "萨尔瓦多"],
    -5: ["美国东", "加拿大多伦多", "古巴", "哥伦比亚", "秘鲁", "墨西哥", "牙买加"],
    -4: ["委内瑞拉", "玻利维亚", "多米尼加", "波多黎各", "智利"],
    -3: ["阿根廷", "乌拉圭", "巴西"],
    -2: ["南乔治亚岛和南桑威奇群岛"],
    -1: ["葡萄牙亚速尔群岛", "佛得角群岛"],
    0: ["英国", "爱尔兰", "冰岛", "加纳", "塞内加尔", "葡萄牙"],
    1: ["德国", "西班牙", "意大利", "法国", "尼日利亚", "阿尔及利亚"],
    2: ["埃及", "希腊", "以色列", "南非", "土耳其"],
    3: ["俄罗斯莫斯科", "沙特阿拉伯", "伊拉克", "肯尼亚"],
    3.5: ["伊朗"],
    4: ["阿联酋", "阿塞拜疆", "亚美尼亚","格鲁吉亚"],
    4.5: ["阿富汗"],
    5: ["巴基斯坦", "乌兹别克斯坦", "塔吉克斯坦"],
    5.5: ["印度", "斯里兰卡"],
    5.75: ["加德满都，尼泊尔"],
    6: ["孟加拉国", "哈萨克斯坦", "布丹"],
    6.5: ["缅甸", "科科斯群岛"],
    7: ["泰国", "越南", "印度尼西亚"],
    8: ["中国", "新加坡", "澳大利亚珀斯", "马来西亚"],
    9: ["日本", "韩国", "朝鲜"],
    9.5: ["澳大利亚达尔文", "澳大利亚阿德莱德"],
    10: ["澳大利亚悉尼", "澳大利亚布里斯班", "巴布亚新几内亚"],
    10.5: ["澳大利亚洛德豪岛"],
    11: ["所罗门群岛", "新喀里多尼亚", "瓦努阿图"],
    12: ["美国贝克岛", "美国豪兰岛","新西兰奥克兰", "新西兰惠灵顿", "斐济"],
}

time_zones_special = {
    -12: ["美✌️"],
    -11: ["美✌️"],
    -10: ["美✌️"],
    -9: ["美✌️"],
    -8: ["美加✌️"],
    -7: ["美加✌️"],
    -6: ["美加✌️"],
    -5: ["美加✌️", "南美外派"],
    -4: ["南美外派"],
    -3: ["南美外派"],
    -1: ["非酋"],
    0: ["英✌️", "欧皇", "非酋"],
    1: ["欧皇", "非酋"],
    2: ["欧皇", "非酋"],
    3: ["欧皇", "非酋", "石油佬"],
    4: ["石油佬"],
    6.5: ["kk园区人"],
    8: ["正常人作息", "沪✌️", "京✌️", "港✌️", "澳✌️"],
    9.5: ["澳✌️"],
    10: ["澳✌️"],
    10.5: ["澳✌️"],
    12: ["美✌️"],
}

def getCurrentHours():
    # Get current UTC time
    current_utc_time = datetime.now(timezone.utc)
    # Round to the nearest hours with decimal
    current_utc_hours = current_utc_time.hour + (current_utc_time.minute / 60)
    return current_utc_hours


def getTimeZone():
    zone = (sleep_time - getCurrentHours()) # Get target time zone
    if zone > 12:
        zone -= 24
    # Find the closest value by calculating the minimum difference if zone not in dict
    if zone not in time_zones.keys():
        zone = min(time_zones.keys(), key=lambda x: abs(x - zone))
    return zone # Return zones int


def luckyDraw():
    zone = getTimeZone()
    # debug # print(f"[Debug]当前英国时间：{getCurrentHours()}，作息：{time_zones[zone]}")

    # Perform lucky draw with prob set
    if (random.random() < probability) and (zone in time_zones_special):
        return(f"这人一定是{random.choice(time_zones_special[zone])}！")
    else:
        return(f"这人一定是{random.choice(time_zones[zone])}人！")


print(luckyDraw())