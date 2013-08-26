#!usr/bin/python


import Queue
q=Queue.Queue()

class node:
	def __init__(self,data):
		self.val=data
		self.l=None
		self.r=None

class list:
	def __init__(self):
		self.root=node(None)

	def insert(self,temp,data):
		if temp == None or temp.val==None:
			temp=node(data)
			return temp
		elif temp.val > data:
			if temp.l == None and temp.r==None:
				temp.l=node(data)
			else:
				temp.l=self.insert(temp.l,data)
		else:
			if temp.r==None and temp.l==None:
				temp.r=node(data)
			else:
				temp.r=self.insert(temp.r,data)
		return temp
	
	def start(self,d):
		if self.root.val == None:
			return
		level=1
		q.put(self.root)
		while q.empty() == False:
			self.pre(q.get(),d,level)

	def pre(self,temp,d,level):
		if temp==None:
			return
		print temp.val,
		if level%d ==0:
			q.put(temp.l)
			q.put(temp.r)
		else:
			self.pre(temp.l,d,level+1)
			self.pre(temp.r,d,level+1)

n=input()
while n:
	l=list()
	x=raw_input()
	x=x.split()
	for y in x:
		y=int(y)
		l.root=l.insert(l.root,y)
	d=input()
	l.start(d)
	print
	n=n-1
