import os
import copy
from math import ceil
from random import randint
import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

original_input=[]
input_=[]
sessions=[]
totalTime=0
totalEvents=0
totalDays=0

def getMngSession():
	global original_input,input_
	sum=0
	while sum!=180:
		sum=0
		input_bk=copy.deepcopy(input_)
		mng=[]
		for i in xrange(0,totalEvents):
			j=randint(0,totalEvents-1)
			if input_bk[j][2]!=1:
				if sum+input_bk[j][0]>180:
					continue
				elif sum>=180:
					break
				else:
					sum+=input_bk[j][0]
					input_bk[j][2]=1
					mng.append(input_bk[j])
	for x in mng:
		for y in input_:
			if x[1]==y[1]:
				#print "here"
				y[2]=1
	#print "finish mng",input_	
	return mng

def getEvngSession():
	global original_input,input_
	sum=0
	while sum<180:
		sum=0
		input_bk=copy.deepcopy(input_)
		evng=[]
		for i in xrange(0,totalEvents):
			j=randint(0,totalEvents-1)
			if input_bk[j][2]!=1:
				if sum+input_bk[j][0]>240:
					continue
				elif sum>=180:
					break
				else:
					sum+=input_bk[j][0]
					input_bk[j][2]=1
					evng.append(input_bk[j])
	for x in evng:
		for y in input_:
			if x[1]==y[1]:
				#print "here"
				y[2]=1
		
	return evng

def arrangeEvents():
	global original_input,input_
	sessions=[]
	for session in xrange(0,2*totalDays):
		if session%2==0:#morning
			sessions.append(getMngSession())
		else:#evening
			sessions.append(getEvngSession())
	#print "finishorder",input_
	return sessions


def readInput():
	global original_input,input_
	global original_input,totalTime,totalEvents,totalDays
	file=open("input.txt","r").readlines()
	for line in file:
		name=str(line).replace("\n","")
		time=int(name.split(" ")[-1].replace("min","").replace("lightning","5"))
		totalTime+=time
		totalEvents+=1
		e=([time,name,0])
		original_input.append(e)
	totalDays=int(ceil(totalTime/420.0))
		
def countOfNotIncluded(arr):
	count=0
	for x in arr:
		if x[2]==0:
			count+=1
	return count
	
def main():
	global original_input,input_
	readInput()
	print "Input"
	for e in original_input:
		print e
	print "\nOutput\n"
	original_input=sorted(original_input)
	input_=copy.deepcopy(original_input)
	while countOfNotIncluded(input_)!=0:
		input_=copy.deepcopy(original_input)
		orderdEventList=arrangeEvents()
	
	
	
	for i in xrange(0,len(orderdEventList)):

		if i%2==0:#mng
			print "\n\nTrack {0}:".format(i/2+1)
			start = datetime.datetime.strptime('09:00:AM', '%H:%M:%p')
			#start=datetime.timedelta(hours=int(9))
		else:
			#start=datetime.timedelta(hours=int(13))
			start = datetime.datetime.strptime('01:00:PM', '%I:%M:%p')
		
		for x in orderdEventList[i]:
			human_time =start
			print human_time.strftime("%I:%M%p"),x[1]
			start=(start+datetime.timedelta(minutes=int(x[0])))

		if i%2==0:
			human_time =start
			print human_time.strftime("%I:%M%p"),"Lunch"
		else:
			human_time =start
			print human_time.strftime("%I:%M%p"),"Networking Event"
			
	
	
if __name__ == '__main__':
	main()