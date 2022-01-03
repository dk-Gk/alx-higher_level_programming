#!/usr/bin/python3
import unittest
from models.base import Base
"""Test for base class"""


class TestBase(unittest.TestCase):
    """Tests the base model"""
    
    def test_id(self):
        """Tests id"""
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_to_json_string(self):
        """Tests to json string"""
        Base._Base__nb_objects = 0
        jd = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        sd = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        js = Base.to_json_string([jd, sd])
        self.assertTrue(type(js) is str)
        d = json.loads(js)
        self.assertEqual(d, [jd, sd])

    def test_from_json_string(self):
        """Tests regular from_json_string"""
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
    {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

    def test_nb(self):
        """Tests if nb_objects are private"""
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)
