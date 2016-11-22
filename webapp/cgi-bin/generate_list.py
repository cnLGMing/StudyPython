#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import athletemodel  # 即使报错也没关系，其实是可以运行
import yate  # 即使报错也没关系，其实是可以运行
import glob

data_files = glob.glob('data/*.txt')
athletes = athletemodel.put_to_store(data_files)

print(yate.start_response())
print(yate.include_header("Kelly 教练所带的选手"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("您需要查询哪个用户?"))

for each_athlete in athletes:
    print(yate.radio_button("which_athlete", athletes[each_athlete].name))

print(yate.end_form('选择'))
print(yate.include_footer({"首页": "/index.html"}))
