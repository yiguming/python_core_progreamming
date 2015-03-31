#!/usr/bin/python
d = {'data1':3, 'data2':1, 'data3':2, 'data4':4}  
newd = sorted(d.iteritems(), reverse=True)  
print newd


student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10)]
new_stu = sorted(student_tuples, key=lambda student: student[2])
print new_stu

