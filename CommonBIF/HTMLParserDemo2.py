#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 学习使用 HTMLParser 解析 HTML
# 解析 http://www.python.org/events/python-events
# 提取Python 官网的活动时间.地点.主题


from html.parser import HTMLParser
from urllib import request


class PythonEventHtmlParser(HTMLParser):
    events = []
    bool_title = False
    bool_time = False
    bool_place = False

    def handle_starttag(self, tag, attrs):
        if len(attrs) > 0:
            if tag == 'h3' and attrs[0][1] == 'event-title':
                self.bool_title = True
            if tag == 'time' and attrs[0][0] == 'datetime':
                self.bool_time = True
            if tag == 'span' and attrs[0][1] == 'event-location':
                self.bool_place = True

    def handle_data(self, data):
        if self.bool_title:
            event = {}
            event['event-title'] = data
            self.events.append(event)
            self.bool_title = False
        if self.bool_time:
            event = self.events.pop()
            event['datetime'] = data
            self.bool_time = False
            self.events.append(event)
        if self.bool_place:
            event = self.events.pop()
            event['event-location'] = data
            self.bool_place = False
            self.events.append(event)


def parse_python_events():
    parser = PythonEventHtmlParser()
    html = ''
    with request.urlopen('http://www.python.org/events/python-events') as f:
        html = f.read().decode('utf-8')
    parser.feed(html)
    events = parser.events
    for event in events:
        print('-' * 50)
        print('会议名:\t\t%s' % event.get('event-title'))
        print('会议时间:\t%s' % event.get('datetime'))
        print('会议地点:\t%s' % event.get('event-location'))


parse_python_events()
