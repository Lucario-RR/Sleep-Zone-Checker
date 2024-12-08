from datetime import datetime,timezone
import random
from config import config,time_zones,time_zones_special


def getCurrentHours():
    # Get current UTC time
    current_utc_time = datetime.now(timezone.utc)
    # Round to the nearest hours with decimal
    current_utc_hours = current_utc_time.hour + (current_utc_time.minute / 60)
    return current_utc_hours


def getTimeZone():
    zone = (config['sleep_time'] - getCurrentHours()) # Get target time zone
    if zone > 12:
        zone -= 24
    # Find the closest value by calculating the minimum difference if zone not in dict
    if zone not in time_zones.keys():
        zone = min(time_zones.keys(), key=lambda x: abs(x - zone))
    return zone # Return zones int


def luckyDraw():
    zone = getTimeZone()
    if config['debug']:
        debug # print(f"[Debug]当前英国时间：{getCurrentHours()}，作息：{time_zones[zone]}")

    # Perform lucky draw with prob set
    if (random.random() < config['probability']) and (zone in time_zones_special):
        return(f"这人一定是{random.choice(time_zones_special[zone])}！")
    else:
        return(f"这人一定是{random.choice(time_zones[zone])}人！")


print(luckyDraw())