class Vector:
    def __init__(self, lst):
        self._values = lst

    # Method used by system ->>> u
    def __repr__(self):
        return "Vector({})".format(self._values)

    # Method used by client ->>> print(v)
    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
