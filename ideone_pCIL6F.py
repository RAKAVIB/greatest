a=int(raw_input())
b=int(raw_input())
c=int(raw_input())
if (a>b) and (a>c):
	print "a is the greatest"
elif (b>c) and (b>a):
	print "b is the greatest"
else:
	print "c is the greatest"