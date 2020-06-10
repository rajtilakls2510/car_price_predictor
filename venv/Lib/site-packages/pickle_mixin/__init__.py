from __future__ import absolute_import as _
from __future__ import unicode_literals as _

from pkg_resources import DistributionNotFound as _DistributionNotFound
from pkg_resources import get_distribution as _get_distribution

from .core import PickleByInit, SlotPickleMixin

try:
    __version__ = _get_distribution('pickle_mixin').version
except _DistributionNotFound:
    __version__ = 'unknown'


def test():
    r"""Tests this package.

    You will need `pytest` installed in order to use this function.
    """
    import os
    p = __import__('pickle_mixin').__path__[0]
    src_path = os.path.abspath(p)
    old_path = os.getcwd()
    os.chdir(src_path)

    try:
        return_code = __import__('pytest').main(['-q', '--doctest-modules'])
    finally:
        os.chdir(old_path)

    if return_code == 0:
        print("Congratulations. All tests have passed!")

    return return_code


__all__ = ['__version__', 'test', 'PickleByInit', 'SlotPickleMixin']
