#print ("введите трехзначное число")
#n = int(input())
#sum = 0
#while n > 0:
#    u = n % 10
#    sum = sum + u
#   n = n // 10
#print (sum)     
  
# print ("enter the number")  
# n = int(input())
# print (n//6*4, n//6, n//6)

print ("введи шестизначное число")
n = int(input())
o = n // 1000
sum = 0
while o > 0:
    u = o % 10
    sum = sum + u
    o = o // 10
print (sum)
p = n%1000
sum1 = 0
while p > 0:
    u = p % 10
    sum1 = sum1 + u
    p = p // 10
print (sum1)
if sum1 == sum :
    print('you are very happy men, all girls are yours')
else:
    print ('you are looooooser')    
    