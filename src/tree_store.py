from typing import Optional


class TreeStore:
    def __init__(self, items: list[dict]):
        self.items = items
        self.item_by_id = {item['id']: item for item in items}
        self.children_by_parent = {}
        self.parent_by_id = {}

        for item in items:
            parent_id = item['parent']
            self.parent_by_id[item['id']] = parent_id
            if parent_id not in self.children_by_parent:
                self.children_by_parent[parent_id] = []
            self.children_by_parent[parent_id].append(item)

    def getAll(self) -> list[dict]:
        return self.items

    def getItem(self, id: int) -> Optional[dict]:
        return self.item_by_id.get(id, None)

    def getChildren(self, id: int) -> list[dict]:
        return self.children_by_parent.get(id, [])

    def getAllParents(self, id: int) -> list[dict]:
        parents = []
        current_id = id

        while current_id in self.parent_by_id:
            parent_id = self.parent_by_id[current_id]
            if parent_id == 'root':
                break
            parent_item = self.item_by_id.get(parent_id)
            if parent_item:
                parents.append(parent_item)
            current_id = parent_id

        return parents