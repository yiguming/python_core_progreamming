#!/usr/bin/env python
class SortedKeyDict(dict):
    def keys(self):
        return sorted(self.keys())

if __name__ == "__main__":
    d = SortedKeyDict((('zheng-cai', 67), ('hui-jun', 68),('xin-yi', 2)))
    print d
