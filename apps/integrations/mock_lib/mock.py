import random
from enum import Enum


class Status(Enum):
    SUCCESS = 1
    FAIL = 2


# I know it is not necessary to create the library but I want this running!
# Just a dummy for mockLib.updateUser()
# It will randomly choose a status
class MockLib:
    def update_user(user):
        return random.choice(list(Status))
