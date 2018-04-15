#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import json
import os
from random_useragent import Randomize


class UserAgentsTest(unittest.TestCase):

    def test_load_json(self):
        with open(os.path.join(os.path.dirname(__file__),
                  'data/tablet.json')) as tablet_file:
            tablet_data = json.load(tablet_file)
            self.tablet_data = tablet_data
            self.assertIsNotNone(self.tablet_data['android'])
            self.assertIsNotNone(self.tablet_data['ios'])

        with open(os.path.join(os.path.dirname(__file__),
                  'data/smartphone.json')) as smartphone_file:
            smartphone_data = json.load(smartphone_file)
            self.smartphone_data = smartphone_data
            self.assertIsNotNone(self.smartphone_data['android'])
            self.assertIsNotNone(self.smartphone_data['ios'])

        with open(os.path.join(os.path.dirname(__file__),
                  'data/desktop.json')) as desktop_file:
            desktop_data = json.load(desktop_file)
            self.desktop_data = desktop_data
            self.assertIsNotNone(self.desktop_data['linux'])
            self.assertIsNotNone(self.desktop_data['mac'])
            self.assertIsNotNone(self.desktop_data['windows'])

        with open(os.path.join(os.path.dirname(__file__),
                  'data/resolution.json')) as resolution_file:
            resolution_data = json.load(resolution_file)
            self.resolution_data = resolution_data
            self.assertIsNotNone(self.resolution_data)

    def test_get_aspect_ratio_list(self):
        self.test_aspect_ratio_list = ra.get_aspect_ratio_list
        self.assertIn('3:2', ra.get_aspect_ratio_list())
        self.assertIn('4:3', ra.get_aspect_ratio_list())
        self.assertIn('5:3', ra.get_aspect_ratio_list())
        self.assertIn('5:4', ra.get_aspect_ratio_list())
        self.assertIn('16:9', ra.get_aspect_ratio_list())
        self.assertIn('16:10', ra.get_aspect_ratio_list())

    def test_random_resolution(self):
        self.assertIsNotNone(ra.random_resolution('3:2'))
        self.assertIsNotNone(ra.random_resolution('4:3'))
        self.assertIsNotNone(ra.random_resolution('5:3'))
        self.assertIsNotNone(ra.random_resolution('5:4'))
        self.assertIsNotNone(ra.random_resolution('16:9'))
        self.assertIsNotNone(ra.random_resolution('16:10'))

    def random_agent(self):
        self.assertIsNotNone(ra.random_agent('desktop', 'linux'))
        self.assertIsNotNone(ra.random_agent('desktop', 'mac'))
        self.assertIsNotNone(ra.random_agent('desktop', 'windows'))
        self.assertIsNotNone(ra.random_agent('smartphone',
                             'android'))
        self.assertIsNotNone(ra.random_agent('smartphone', 'ios'))
        self.assertIsNotNone(ra.random_agent('tablet', 'android'))
        self.assertIsNotNone(ra.random_agent('tablet', 'ios'))


if __name__ == '__main__':
    ra = Randomize()
    unittest.main()
