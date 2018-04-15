#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import json
import os


class Randomize:

    def __init__(self):
        with open(os.path.join(os.path.dirname(__file__),
                  'data/tablet.json')) as tablet_file:
            tablet_data = json.load(tablet_file)
            self.tablet_data = tablet_data
        with open(os.path.join(os.path.dirname(__file__),
                  'data/smartphone.json')) as smartphone_file:
            smartphone_data = json.load(smartphone_file)
            self.smartphone_data = smartphone_data
        with open(os.path.join(os.path.dirname(__file__),
                  'data/desktop.json')) as desktop_file:
            desktop_data = json.load(desktop_file)
            self.desktop_data = desktop_data
        with open(os.path.join(os.path.dirname(__file__),
                  'data/resolution.json')) as resolution_file:
            resolution_data = json.load(resolution_file)
            self.resolution_data = resolution_data

    def get_aspect_ratio_list(self):
        self.aspect_ratio_list = aspect_ratio_list = [
            '3:2',
            '4:3',
            '5:3',
            '5:4',
            '16:9',
            '16:10',
            ]
        return self.aspect_ratio_list

    def random_resolution(self, aspect_ratio):
        if aspect_ratio in self.get_aspect_ratio_list():
            resolution_length = len(self.resolution_data[aspect_ratio])
            return self.resolution_data[aspect_ratio][random.randint(0,
                    resolution_length - 1)]
        else:
            return 'Not allowed, please check .get_aspect_ratio_list()'

    def random_agent(self, device_type, os):
        if device_type.lower() == 'tablet':
            if os.lower() == 'android':
                tablet_android_length = len(self.tablet_data['android'])
                return self.tablet_data['android'][random.randint(0,
                        tablet_android_length - 1)]
            elif os.lower() == 'ios':
                tablet_ios_length = len(self.tablet_data['ios'])
                return self.tablet_data['ios'][random.randint(0,
                        tablet_ios_length - 1)]
            else:
                return 'Unknown operating system!'
        elif device_type.lower() == 'smartphone':
            if os.lower() == 'android':
                smartphone_android_length = \
                    len(self.smartphone_data['android'])
                return self.smartphone_data['android'
                        ][random.randint(0, smartphone_android_length
                          - 1)]
            elif os.lower() == 'ios':
                smartphone_ios_length = len(self.smartphone_data['ios'])
                return self.smartphone_data['ios'][random.randint(0,
                        smartphone_ios_length - 1)]
            else:
                return 'Unknown operating system!'
        elif device_type.lower() == 'desktop':
            if os.lower() == 'windows':
                desktop_windows_length = len(self.desktop_data['windows'
                        ])
                return self.desktop_data['windows'][random.randint(0,
                        desktop_windows_length - 1)]
            elif os.lower() == 'mac':
                desktop_mac_length = len(self.desktop_data['mac'])
                return self.desktop_data['mac'][random.randint(0,
                        desktop_mac_length - 1)]
            elif os.lower() == 'linux':
                desktop_linux_length = len(self.desktop_data['linux'])
                return self.desktop_data['linux'][random.randint(0,
                        desktop_linux_length - 1)]
            else:
                return 'Unknown operating system!'
        else:
            return 'Unknown device type!'
