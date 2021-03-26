class ProtectedDictIntError(KeyError):
    KEY_EXIST = 0
    KEY_NOT_INT = 1

    def __init__(self, error_type, key):
        self.error_type = error_type
        self.key = key

    def __str__(self):
        if self.error_type == ProtectedDictIntError.KEY_EXIST:
            return "ProtectedDictIntError: key {} exists in instance of ProtectedDictInt".format(self.key)
        elif self.error_type == ProtectedDictIntError.KEY_NOT_INT:
            return "ProtectedDictIntError: key '{}' is not int".format(self.key)
