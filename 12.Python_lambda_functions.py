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
