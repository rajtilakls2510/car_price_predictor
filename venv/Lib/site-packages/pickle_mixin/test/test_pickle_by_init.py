import pickle
from pickle import PicklingError

import pytest

from pickle_mixin import PickleByInit


class Foo(PickleByInit):
    def __init__(self, obj):
        super(Foo, self).__init__()
        self.obj = obj


class Bar(object):
    def __init__(self, filename):
        self.filename = filename

    def __getstate__(self):
        raise PicklingError

    def init_dict(self):
        return dict(filename=self.filename)


def test_pickle_by_name_error():
    f = Foo(Bar('file.txt'))
    with pytest.raises(PicklingError):
        pickle.dumps(f)


def test_pickle_by_name_set_signature():
    f = Foo(Bar('file.txt'))
    f.set_signature_only_attr('obj')
    o = pickle.dumps(f)
    f = pickle.loads(o)
    assert f.obj.filename == 'file.txt'
