import unittest

from src.tree_store import TreeStore


class TestTreeStore(unittest.TestCase):
    def setUp(self):
        self.items = [
            {"id": 1, "parent": "root"},
            {"id": 2, "parent": 1, "type": "test"},
            {"id": 3, "parent": 1, "type": "test"},
            {"id": 4, "parent": 2, "type": "test"},
            {"id": 5, "parent": 2, "type": "test"},
            {"id": 6, "parent": 2, "type": "test"},
            {"id": 7, "parent": 4, "type": None},
            {"id": 8, "parent": 4, "type": None}
        ]
        self.ts = TreeStore(self.items)

    def test_getAll(self):
        self.assertEqual(self.ts.getAll(), self.items)

    def test_getItem(self):
        self.assertEqual(self.ts.getItem(7), {"id": 7, "parent": 4, "type": None})
        self.assertIsNone(self.ts.getItem(999))

    def test_getChildren(self):
        self.assertEqual(self.ts.getChildren(4), [
            {"id": 7, "parent": 4, "type": None},
            {"id": 8, "parent": 4, "type": None}
        ])
        self.assertEqual(self.ts.getChildren(5), [])

    def test_getAllParents(self):
        self.assertEqual(self.ts.getAllParents(7), [
            {"id": 4, "parent": 2, "type": "test"},
            {"id": 2, "parent": 1, "type": "test"},
            {"id": 1, "parent": "root"}
        ])
        self.assertEqual(self.ts.getAllParents(1), [])
