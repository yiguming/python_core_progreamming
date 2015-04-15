class PersonDataBase(object):
    def __init__(self):
        self.__personDataBase = [("user1",1),("user2",2)]
    def login(self, userName, userPasswd):
        if (userName, userPasswd) not in self.__personDataBase:
            print "sorry, error"
            return None
        else:
            print "ok"
    
 
oneObj = PersonDataBase()
oneObj.login("test",1)
oneObj.login("user1",1)
