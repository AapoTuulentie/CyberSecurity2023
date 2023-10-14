from __future__ import unicode_literals
import hashlib
import importlib
from collections import OrderedDict
from django.utils.encoding import force_bytes
from django.utils.crypto import constant_time_compare, get_random_string


class BasePasswordHasher(object):
    algorithm = None
    library = None

    def _load_library(self):
        if self.library is not None:
            if isinstance(self.library, (tuple, list)):
                name, mod_path = self.library
            else:
                name = mod_path = self.library
            try:
                module = importlib.import_module(mod_path)
            except ImportError as e:
                raise ValueError("Couldn't load %r algorithm library: %s" %
                                 (self.__class__.__name__, e))
            return module
        raise ValueError("Hasher %r doesn't specify a library attribute" %
                         self.__class__.__name__)

    def salt(self):
        return get_random_string()

    def verify(self, password, encoded):
        raise NotImplementedError()

    def encode(self, password, salt):
        raise NotImplementedError()

    def safe_summary(self, encoded):
        raise NotImplementedError()

    def must_update(self, encoded):
        return False

def mask_hash(hash, show=6, char="*"):
    masked = hash[:show]
    masked += char * len(hash[show:])
    return masked

class UnsaltedMD5PasswordHasher(BasePasswordHasher):

    algorithm = "unsalted_md5"

    def salt(self):
        return ''

    def encode(self, password, salt):
        assert salt == ''
        return hashlib.md5(force_bytes(password)).hexdigest()

    def verify(self, password, encoded):
        if len(encoded) == 37 and encoded.startswith('md5$$'):
            encoded = encoded[5:]
        encoded_2 = self.encode(password, '')
        return constant_time_compare(encoded, encoded_2)

    def safe_summary(self, encoded):
        return OrderedDict([
            (_('algorithm'), self.algorithm),
            (_('hash'), mask_hash(encoded, show=3)),
        ])