x=3
y=1
while y<11:
    print(x,'*',y,'=',x*y)
    y=y+1


print('helloworld')


# mytext= 'hello iam sabrina'
myfile= open('sabrina.txt', 'w')
myfile.write('hello i am sabrina')
myfile.close()


# mytext= 'hello iam sabrina'
myfile= open('sabrina.txt', 'a')
myfile.write('\nhello i am towshif')
myfile.close()



class calc:
    def add(x,y):
        answer = x + y
        print (answer)
        
    def sub(x,y):
        answer = x - y
        print (answer)
        
    def mult(x,y):
        answer = x * y
        print (answer)
        
    def div(x,y):
        answer = x / y
        print (answer)
        
