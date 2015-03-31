#!/usr/bin/env python

import time,string
nowtime=time.time()  # get time vlaue
def gettime(nowtime):
    #change time 'example 1357635049.372' to be '%Y/%m/%d %H:%M:%S'
    return time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(nowtime))
db = {}  ##{name:[pwd,time]}
 
 
def checkname(name):
        if len(set(name) - set(string.letters+string.digits))>0:
            prompt = 'has wrong letter: '
        else:  pass
 
def newuser():
    #create user
    prompt = 'login desired: '
    while True:
        name1 = raw_input(prompt)
        name=name1.lower()  ##set lower
        if db.has_key(name):
            prompt = 'name taken, try another: '
            continue
        elif len(set(name) - set(string.letters+string.digits))>0:
            prompt = 'has wrong letter: '
            continue
        else:
            break
    pwd = raw_input('passwd: ')
    db[name] = [abs(hash(pwd))]
    db[name].append(0)
    print db
def olduser():
    #user login
    nowtime=time.time()
    name1 = raw_input('login: ')
    name=name1.lower()
    if name not in db.keys():   #when name not in db
        choose=raw_input("will you create a new user(Y/N):")
        if choose.lower()=='y':      # create new user
            if len(set(name) - set(string.letters+string.digits))>0:
                print 'has wrong letter,goto create to newuser'
                newuser()
            pwd = raw_input('passwd: ')
            db[name] = [abs(hash(pwd))]
            db[name].append(0)
        else:
            pass
        showmenu()
    else:
        pass
    pwd = raw_input('passwd: ')
    passwd = db.get(name)[0]
    if passwd == abs(hash(pwd)):
        if db[name][1]==0:
            print 'welcome back', name,'your first time loggin'
        else:
            print 'welcome back', name
            if nowtime-db[name][1]<=14400:    ##14400s=4hours,the time from lastlogin to now
                print 'you already logged at time',gettime(db[name][1])
        db[name][1]=nowtime  # set the time of this login
    else:
        print 'login incorrect'
        return
 
def showuser():
    #show all users
    print 'all users:'
    for i in db.keys():
        print i
 
def deluser():
    # delete a user
    name1=raw_input('delete user:')
    name=name1.lower()
    del db[name]
 
def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit
(S)how all users
(D)elete user
 
Enter choice: """
 
    done = 0
    while not done:
        chosen = 0
        while not chosen:
            try:
                choice = raw_input(prompt)[0]
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
 
            if choice not in 'neqsd':
                print 'invalid menu option, try again'
            else:
                chosen = 1
 
        if choice == 'q': done = 1
        if choice == 'n': newuser()
        if choice == 'e': olduser()
        if choice == 's': showuser()
        if choice == 'd': deluser()
 
if __name__ == '__main__':
    showmenu()
