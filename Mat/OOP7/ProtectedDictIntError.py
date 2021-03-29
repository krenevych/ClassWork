class ProtectedDictIntError(KeyError):
    ERROR_KEY_NOT_INT = 0
    ERROR_KEY_EXIST   = 1

    def __init__(self, error_code, key):
        self.error_code = error_code
        self.key = key

    def __str__(self):
        if self.error_code == ProtectedDictIntError.ERROR_KEY_NOT_INT:
            return "Key {} of ProtectedDictInt must be integer".format(self.key)
        elif self.error_code == ProtectedDictIntError.ERROR_KEY_EXIST:
            return "Instance of ProtectedDictInt has already contained key {}".format(self.key)