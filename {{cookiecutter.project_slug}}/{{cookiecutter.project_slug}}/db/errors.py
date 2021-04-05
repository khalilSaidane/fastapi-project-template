class EmailAlreadyExists(Exception):
    """Raised when creating a new user with a used email"""


class ObjectDoesNotExist(Exception):
    """Raised when query by pk returns None"""
