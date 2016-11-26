#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timezone
from datetime import timedelta  # 用于时间的加减
import re  # 下面的练习，进行正则

now = datetime.now()  # 获取当前时间
print('当前的时间是：%s' % now)
print(now.strftime('%a, %b %d %H:%M'))

nowTimeStamp = now.timestamp()
print('对应的时间戳是：%s' % nowTimeStamp)  # 将 datetime 转化为时间戳 timestamp

# 将timestamp 转换为 本地 datetime
print('timestamp: %s, 对应的 datetime 是：%s' % (nowTimeStamp, datetime.fromtimestamp(nowTimeStamp)))
# 将timestamp 转换为 格林威治标准时间 datetime
print('timestamp: %s, 对应的 datetime 是：%s' % (nowTimeStamp, datetime.utcfromtimestamp(nowTimeStamp)))

myTime = datetime(2016, 11, 26, 13, 27, 40)  # 使用构造函数，创建一个datetime
print('构造的时间是：%s' % myTime)

# 将字符串转换为 datetime
str2DateTime = datetime.strptime('2016-11-26 13:27:40', '%Y-%m-%d %H:%M:%S')
print('str2DateTime = %s' % str2DateTime)
print('此时的 str2DateTime 是数据类型是：%s' % type(str2DateTime))

# 时间的加减，需要导入 timedelta 包
nowTime = datetime.now()
print('现在的时间是：%s' % nowTime)
print('十小时后的时间是：', nowTime + timedelta(hours=10))
print('十小时前的时间是：', nowTime - timedelta(hours=10))
print('一天后的时间是：', nowTime + timedelta(days=1))
print('两天后+10小时的时间是：', nowTime + timedelta(days=2, hours=10))

# 时区的转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('现在的0时区的时间是：', utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('现在的8时区的时间是：', bj_dt)
jp_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print('现在的9时区的时间是：', jp_dt)
# 也可以不同时区的时间进行转换，比如北京时间转换为东京时间
tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))  # 9表示目标所在的时区
print('现在的北京时间是：', bj_dt)
print('现在的京东时间是：', tokyo_dt)


# 练习：
# 假设你获取了用户输入的日期和时间
# 如2016-1-21 8:01:30，以及一个时区信息如UTC+5:00，均是str，
# 请编写一个函数将其转换为timestamp：

def str2timestamp(dt_str, tz_str):
    tz = int(re.match(r'UTC([+-]\d{1,2}):00$', tz_str).group(1))
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    return dt.replace(tzinfo=timezone(timedelta(hours=tz))).timestamp()


t1 = str2timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = str2timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('pass')
