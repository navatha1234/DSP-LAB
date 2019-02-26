x=[]
y=[]
i=input("enter the sample range")
for n in range(0,i):
	a=int(input("enter the amplitude"))
	x.append(a)
for k in range(0,i):
	b=x[-k]
	y.append(b)
	
print y
