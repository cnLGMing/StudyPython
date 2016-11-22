# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import athletemodel  # 即使报错也没关系，其实是可以运行
import yate  # 即使报错也没关系，其实是可以运行

athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Kelly 教练的时间数据"))
print(yate.header("姓名:" + athlete_name + ",出生日期:" + athletes[athlete_name].dob + "."))
print(yate.para("比较好的成绩:"))
print(yate.u_list(athletes[athlete_name].top3))
print(yate.include_footer({"首页": "/index.html", "查看其他选手": "generate_list.py"}))
