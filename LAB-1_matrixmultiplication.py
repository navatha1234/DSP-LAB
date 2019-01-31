a1=input("enter no. of rows of matrix1:")
b1=input("enter no. of columns of matrix1:")
a2=input("enter no. of rows of matrix2:")
b2=input("enter no. of columns of matrix2:")
if(b2==a2):
	i=0
	a={}
	while(i<a1):
		j=0
		while(j<b2):
			
			m1=input("enter matrix1 elements")
			a[i,j]=m1
			j=j+1
		
		i=i+1
	b={}
	i=0
	while(i<a2):
			j=0
			while(j<b2):
				m2=input("enter matrix2 elements")
				b[i,j]=m2
				j=j+1
			i=i+1
	c={}
	i=0
	while(i<a1):
			j=0
			while(j<b2):
				c[i,j]=0
				k=0
				while(k<a2):
					c[i,j]=c[i,j]+a[i,k]*b[k,j]
					k=k+1
				j=j+1
			i=i+1
	i=0
	while(i<a1):
			j=0
			while(j<b2):
				print c[i,j],
				j=j+1
			i=i+1
			print
	
	


