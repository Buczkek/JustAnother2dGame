from Object import Object


class Inventory(Object):  # TODO Inventory class
    def __init__(self, size=5):
        self._Items = []
        self._Size = size
        self._Empty = True
        self._Occupied = 0
        self._Pos = self._Bound.get_pos()

    def get_items(self):
        return self._Items

    def insert_item(self, index, item):
        if self._Items[index]:
            self.drop_item()
            return self.insert_item(index, item)

    def drop_item(self):
        raise NotImplementedError
