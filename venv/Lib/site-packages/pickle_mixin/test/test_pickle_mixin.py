import pickle
import sys
from pickle import PicklingError

import pytest

from pickle_mixin import SlotPickleMixin

PY27 = sys.version_info < (3, )


class Foo(object):
    __slots__ = ['a']

    def __init__(self):
        self.a = 4


class Bar(Foo):
    def __init__(self):
        pass


class FooMixin(object):
    __slots__ = ['a']

    def __init__(self):
        self.a = 4


class BarMixin(FooMixin, SlotPickleMixin):
    def __init__(self):
        FooMixin.__init__(self)
        SlotPickleMixin.__init__(self)


@pytest.mark.skipif(not PY27, reason="requires python2.7")
def test_pickle_mixin_error_27():
    f = Bar()
    with pytest.raises(TypeError):
        pickle.dumps(f)


@pytest.mark.skipif(PY27, reason="requires python3")
def test_pickle_mixin_error():
    f = Bar()
    o = pickle.dumps(f)
    f = pickle.loads(o)
    assert not hasattr(f, 'a')


def test_pickle_mixin_success():
    f = BarMixin()
    o = pickle.dumps(f)
    f = pickle.loads(o)
    assert hasattr(f, 'a')
