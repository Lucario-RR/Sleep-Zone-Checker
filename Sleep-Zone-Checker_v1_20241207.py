from datetime import datetime,timezone
# Configs
sleep_time = 22
time_zones = [
    "UTC+0: 伦敦，英国",
    "UTC+1: 柏林，德国",
    "UTC+2: 开罗，埃及",
    "UTC+3: 莫斯科，俄罗斯",
    "UTC+4: 迪拜，阿联酋",
    "UTC+5: 卡拉奇，巴基斯坦",
    "UTC+6: 达卡，孟加拉国",
    "UTC+7: 曼谷，泰国",
    "UTC+8: 北京，中国",
    "UTC+9: 东京，日本",
    "UTC+10: 悉尼，澳大利亚",
    "UTC+11: 霍尼亚拉，所罗门群岛",
    "UTC+12: 奥克兰，新西兰",
    "UTC-11: 帕果帕果，美属萨摩亚",
    "UTC-10: 火奴鲁鲁，美国",
    "UTC-9: 阿拉斯加，美国",
    "UTC-8: 洛杉矶，美国",
    "UTC-7: 丹佛，美国",
    "UTC-6: 芝加哥，美国",
    "UTC-5: 纽约，美国",
    "UTC-4: 加拉加斯，委内瑞拉",
    "UTC-3: 布宜诺斯艾利斯，阿根廷",
    "UTC-2: 南乔治亚岛和南桑威奇群岛",
    "UTC-1: 亚速尔群岛，葡萄牙"
]


def getCurrentHours():
    # Get current UTC time
    current_utc_time = datetime.now(timezone.utc)

    # Round to the nearest hour
    if current_utc_time.minute >= 30:
        current_utc_time = int(current_utc_time.strftime('%H')) + 1
    else:
        current_utc_time = int(current_utc_time.strftime('%H'))
    return current_utc_time


def getTimeZone(utc_time):
    zone = sleep_time - utc_time
    if zone > 12:
        zone -= 24
    return time_zones[zone]

print(f"这个人一定是{getTimeZone(getCurrentHours())}时区的人！")
print(f"[Debug]当前北京时间：{getCurrentHours() + 8}，作息：{getTimeZone(getCurrentHours())}")