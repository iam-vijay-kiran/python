# Reduces no.of. lines in code for looping logics
# write a program to generate list of 10 numbers
result=[]
for i in range(1,11):
    result.append(i)
    
print(result)

# how to do it using list comprehension?
result = [ x for x in range(1,11) ]
print(result)


# Get list of all even numbers from 1 to 50
result = [ x for x in range(1,51) if x % 2 == 0 ]
print(result)


# Get list of all even numbers from given list
list_a = [1,2,4,3,6,7,9]
result = [ x for x in list_a if x % 2 == 0 ]
print(result)


# convert elements of given list into uppercase
list_b = ['hi','hello','bye','nice']

result = [x.upper() for x in list_b ]
print(result)


# put all -ve numbers before +ve numbers from given list
list_c = [1,-1,2,-5,9,10,-6]
# result = [1,2,9,10,-1,-5,-6]

result = [x for x in list_c if x>0] + [x for x in list_c if x<0]
print(result)
