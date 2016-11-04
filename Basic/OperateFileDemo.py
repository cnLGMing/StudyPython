#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 对一个文件中的进行分类，保存

# 将文件 Test01.txt中的对话。通过"---------------------"进行分割保存
# 每个对话，男和女分别保存，最后的保存效果是：
# boy_file_1.txt、boy_file_2.txt、boy_file_3.txt
# girl_file_1.txt、girl_file_2.txt、girl_file_3.txt

def save_spoken(boy, girl, count):
    boy_file_name = 'boy_file_' + str(count) + '.txt'
    girl_file_name = 'girl_file_' + str(count) + '.txt'

    boy_file = open(boy_file_name, 'w')
    girl_file = open(girl_file_name, 'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()


def spit_file(file_name):
    file = open(file_name)

    boy = []
    girl = []
    count = 1

    for aline in file:
        if aline[:4] != '----':  # 每行的前4个是否为"----"
            (role, line_spoken) = aline.split(':', 1)
            if role == '男':
                boy.append(line_spoken)
            elif role == '女':
                girl.append(line_spoken)
        else:
            save_spoken(boy, girl, count)
            count += 1
            boy = []
            girl = []

    save_spoken(boy, girl, count)
    file.close()



spit_file("Test01.txt")
