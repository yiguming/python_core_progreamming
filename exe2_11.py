#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
class TextMenu(object):
    """My first class :TextMenu"""
    selection1 = "(1)取五个数的和"
    selection2 = "(2)取五个数的平均数"
    selection3 = "(X)退出"
    def __init__(self,fnl=[1,2,3,4,5]):
    	"""init the five_number_list"""
	self.alist = fnl 
    def total(self):
	total =0
	for i in self.alist:
	    total += i
	return total
    def average(self):
	total =0
	average = 0
	for i in self.alist:
	    total +=i
	average = float(total) / len(self.alist)
	return average
    def exitmenu(self):
	sys.exit() 
    def showmenu(self):
	print "你好，请选择一个菜单执行："
	#print "(1)取五个数的和"
	print self.selection1
	#print "(2)取五个数的平均数"
	print self.selection2
	#print "(X)退出"
	print self.selection3
    def choice(self):
	user_choice = raw_input("您选择：")
	if user_choice == "1":
	    print self.total()
	elif user_choice == "2":
	    print self.average()
    	elif (user_choice == "X") or (user_choice == "x"):
	    print "退出完成"
	    self.exitmenu()
	else:
	    print "输入错误请重新输入"
	    self.choice()

if __name__ == '__main__':
    test = TextMenu([11,22,33,44,55])
    print  "你好，你的列表是：", test.alist
    while (1):
    	test.showmenu()
	test.choice()
	
	
