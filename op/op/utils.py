# -*- coding: utf-8 -*-

from fnmatch import fnmatch


class glob_list(list):
    def __contains__(self, value):
        for pattern in self:
            if fnmatch(value, pattern):
                return True
        return False
