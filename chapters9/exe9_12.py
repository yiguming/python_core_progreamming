#!/usr/bin/env python
__author__ = 'nhchen'
import time,string,os,shelve
dbfile=shelve.open('db.sheve')
#dbfile['superadmin']={'name':'suppername','pwd':323859219,'lasttime':0}
dbfile.close()
nowtime=time.time()  # get time vlaue
 
def gettime(nowtime):
    #change time 'example 1357635049.372' to be '%Y/%m/%d %H:%M:%S'
    return time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(nowtime))
#db = {'superadmin':[323859219,0]}  ##{name:[pwd,time]}  superadmin:861116
 
 
def newuser():
    #create user
    dbfile=shelve.open('db.sheve')
    keys=[key for key in dbfile]
    dbfile.close()
    prompt = 'login desired: '
    while True:
        name1 = raw_input(prompt)
        name=name1.lower()  ##set lower
        if name in keys:
            prompt = 'name taken, try another: '
            continue
        elif len(set(name) - set(string.letters+string.digits))>0:
            prompt = 'has wrong letter: '
            continue
        else:
            break
    pwd = raw_input('passwd: ')
    dbfile=shelve.open('db.sheve')
    dbfile[name] = {'name':name,'pwd':abs(hash(pwd)),'lasttime':0}
    dbfile.close()
 
def olduser():
    #user login
    dbfile=shelve.open('db.sheve')
    keys=[key for key in dbfile]
    dbfile.close()
    nowtime=time.time()
    name1 = raw_input('login: ')
    name=name1.lower()
    if name not in keys:   #when name not in db
        choose=raw_input("will you create a new user(Y/N):")
        if choose.lower()=='y':      # create new user
            if len(set(name) - set(string.letters+string.digits))>0:
                print 'has wrong letter,goto create to newuser'
                newuser()
            pwd = raw_input('passwd: ')
            dbfile=shelve.open('db.sheve')
            dbfile[name] = {'name':name,'pwd':abs(hash(pwd)),'lasttime':0}
            dbfile.close()
        else:
            pass
        showmenu()
    else:
        pass
    dbfile=shelve.open('db.sheve')
    pwd = raw_input('passwd: ')
    name2=dbfile[name]
    passwd = name2['pwd']
    if passwd == abs(hash(pwd)):
        if name2['lasttime']==0:
            print 'welcome back', name,'your first time loggin'
        else:
            print 'welcome back', name
            if nowtime-name2['pwd']<=14400:    ##14400s=4hours,the time from lastlogin to now
                print 'you already logged at time',gettime(name2['lasttime'])
        name2['lasttime']=nowtime  # set the time of this login
        dbfile[name]=name2
        dbfile.close()
        if name=='superadmin':
            choose=raw_input('you can output the name:')
            if choose.strip()[0].lower()=='y':
                file=open('name_information.txt','w')
                for i in keys():
                    file.write('%s\t%i\t%f\n'%(i,dbfile[i]['pwd'],dbfile[i]['lasttime']))
                file.close()
    else:
        print 'login incorrect'
 
 
def showuser():
    #show all users
    dbfile=shelve.open('db.sheve')
    for key in dbfile:
        print key,dbfile[key]
    dbfile.close()
 
def deluser():
    # delete a user
    dbfile=shelve.open('db.sheve')
    name1=raw_input('delete user:')
    name=name1.lower()
    del dbfile[name]
    dbfile.close()
 
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

