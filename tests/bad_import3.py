import warnings

def bad_function():
    warnings.warn("This is a deprecated function", DeprecationWarning)


class BadClass():
    def bad_method(self):
        warnings.warn("This is a deprecated method", DeprecationWarning)
