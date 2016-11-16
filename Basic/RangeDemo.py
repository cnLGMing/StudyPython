#!/usr/bin/env python3
# -*- coding: utf-8 -*-

data = ['地球',
            ['中国',
                ['广东',
                    ['广州','深圳','珠海','梅州']
                ],
                ['江西',
                    ['井冈山','赣州','武昌']
                ],
                ['北京',
                    ['朝阳区']
                ]
            ],
            ['美国']
       ]

def print_item(data_list, leve=0):
    for each_item in data_list:
        if isinstance(each_item, list):
            print_item(each_item, leve + 1)
        else:
            for tab_stop in range(leve):
                print("\t", end = '')
            print(each_item)


print_item(data, 0)