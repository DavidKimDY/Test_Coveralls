import sys
import os


sys.path.insert(0, os.path.abspath(".."))

print(sys.path)

from func import func


def test_add():
    assert func.add(1, 3) == 4
