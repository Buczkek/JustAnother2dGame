class Object:  # TODO Object class
    def __init__(self, x=0, y=0, z=0, *, bound: 'Object' = None):
        self._Pos = [x, y, z]
        self._Interactable = True
        self._Texture = None  # TODO Set default texture (image)
        self._Bound = bound

    def draw(self, surface):  # TODO ...
        pass

    def get_pos(self):
        return tuple(self._Pos)

    def _get_bound_pos(self):
        return self._Bound.get_pos()

