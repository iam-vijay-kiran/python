## Y to create lambda functions?
# lambda Functions:
#     Inline/annynomous Functions
#     we don't need def keyword like normal function
#     only logical expression 


# How to create lambda function?
# normal functon for adding 5 to given number

def add_five(x):
    result = x + 5
    return x

x = 7 
print(add_five(x))


## same funciton using lamda function
lambda_add_five = lambda x : x + 5
y = 10 

print(lambda_add_five(y))


## lambda funciton to add 2 input functions

lambda_add_2_num = lambda x , y : x + y 
a = 30 
b = 20 

print(lambda_add_2_num(a,b))


## lambda function to concatinate 2 input strings

lambda_concatinate_2strings = lambda x , y : x + y
c = 'abcd'
d = 'efgh'

print(lambda_concatinate_2strings(c,d))


#### lambda function to calculate max of 2 numbers

lambda_max = lambda x, y : max(x,y)     # lambda_max = lambda x, y : x if x>y else y 

print(lambda_max(20,30))





## How 2 work with MAP(), FILTER(), REDUCE()

## Implimenting MAP funtion == list mapping 1 element to other without looping

list1 = [1,2,3,4,5,6,7,8,9]   # o/p needed = square of list

square_num = lambda x : x * x

# syntax : map(func, iter1)
square_list = list(map(square_num, list1))   # directly gives map object so we typecase o/p to list            
print(square_list)

# Add sequential respective elements in two given lists
l_a = [1,2,3,4,5]
l_b = [5,4,3,2,1]

#result = [6,6,6,6,6]
sum_2_elements = lambda x , y : x + y 
result = list(map(sum_2_elements, l_a, l_b))
print(result)
