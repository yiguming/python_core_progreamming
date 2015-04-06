#!/usr/bin/env python
class AddrBookEntry(object):
    'address book entry class'
    def __init__(self,nm,ph):
        self.name = nm
        self.phone = ph
        print "Created instance for:",self.name
    def updatePhone(self,newph):
        self.phone = newph
        print "Updated phone# for",self.name

class EmplAddrBookEntry(AddrBookEntry):
    'Employee Addredd Book Entry class'
    def __init__(self,nm,ph,id,em):
        AddrBookEntry.__init__(self,nm,ph)
        self.empid = id
        self.email = em

    def updateEmail(self,newem):
        self.email = newem
        print "Updated e-email address for:",self.name


if __name__ =="__main__":
    john = AddrBookEntry('John Doe','408-555-1212')
    jane = AddrBookEntry('Jane Doe','650-555-1212')
    print john.name
    print john.phone
    print jane.name
    print jane.phone
    john.updatePhone('415-555-1212')
    print john.phone

    print "=========================="
    john = EmplAddrBookEntry('John Doe','408-555-1212',42,'John@spam.doe')
    print john.name
    print john.phone
    print john.empid
    print john.email
    john.updatePhone('415-555-1212')
    print john.phone
    john.updateEmail('john@doe.spam')
    print john.email
