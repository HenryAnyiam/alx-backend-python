#!/usr/bin/env python3
"""create various tests for
the utils module"""


from utils import access_nested_map as access
from parameterized import parameterized
import unittest
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """write test for the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """basic tests for the access_nested_map"""
        self.assertEqual(access(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """error tests for the access_nested_map"""
        with self.assertRaises(KeyError) as error:
            access(nested_map, path)
        msg = str(error.exception)
        expected = path[-1]
        self.assertTrue(expected in msg)
