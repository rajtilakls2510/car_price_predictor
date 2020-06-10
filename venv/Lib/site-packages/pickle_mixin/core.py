from __future__ import absolute_import

from importlib import import_module

def _fullname(o):
    """Object's full name."""
    return o.__class__.__module__ + "." + o.__class__.__name__

class PickleByInit(object):
    """Makes un-pickle-able objects pick-able.

    It sets its un-pickle-able attributes as signature-only attributes.

    """
    def __init__(self):
        self._signature_only_attrs = set()

    def set_signature_only_attr(self, attr_name):
        self._signature_only_attrs.add(attr_name)

    def __getstate__(self):
        d = self.__dict__.copy()
        for attr_name in self._signature_only_attrs:
            o = getattr(self, attr_name)

            d[attr_name + '_fullname'] = _fullname(o)
            d[attr_name + '_init_dict'] = o.init_dict()
            del d[attr_name]
        return d

    def __setstate__(self, d):

        for attr_name in d['_signature_only_attrs']:
            fn = d[attr_name + '_fullname']
            k = fn.rfind(".")
            module_name, class_name = fn[:k], fn[k+1:]
            init_dict = d[attr_name + '_init_dict']
            mod = import_module(module_name)
            class_ = getattr(mod, class_name)
            o = class_(**init_dict)
            d[attr_name] = o
            del d[attr_name + '_fullname']
            del d[attr_name + '_init_dict']

        self.__dict__.update(d)

class SlotPickleMixin(object):
    """Top-class that allows mixing of classes with and without slots.

    Takes care that instances can still be pickled with the lowest
    protocol. Moreover, provides a generic `__dir__` method that
    lists all slots.

    """

    # We want to allow weak references to the objects
    __slots__ = ['__weakref__']

    def _get_all_slots(self):
        """Returns all slots as set"""
        all_slots = (getattr(cls, '__slots__', [])
                         for cls in self.__class__.__mro__)
        return set(slot for slots in all_slots for slot in slots)

    def __getstate__(self):
        if hasattr(self, '__dict__'):
            # We don't require that all sub-classes also define slots,
            # so they may provide a dictionary
            statedict = self.__dict__.copy()
        else:
            statedict = {}
        # Get all slots of potential parent classes
        for slot in self._get_all_slots():
            try:
                value = getattr(self, slot)
                statedict[slot] = value
            except AttributeError:
                pass
        # Pop slots that cannot or should not be pickled
        statedict.pop('__dict__', None)
        statedict.pop('__weakref__', None)
        return statedict

    def __setstate__(self, state):
        for key, value in state.items():
            setattr(self, key, value)

    def __dir__(self):
        result = dir(self.__class__)
        result.extend(self._get_all_slots())
        if hasattr(self, '__dict__'):
            result.extend(self.__dict__.keys())
        return result
