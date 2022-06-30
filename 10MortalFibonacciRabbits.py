# my approach
def f(n,m):
    if n == 1:
        return 1
    elif n ==2:
        return 1
    elif n-m-1 <= 0:
        return f(n-1,m)+f(n-2,m)
    else: 
        l = [f(n-2-i,m) for i in range(m-1)]
    return sum(l)

'''workaround 1'''
# stored = {}         
# def population(n, m):    
#     """    
#     n is the number of months; m is the lifespan of a rabbit    
#     """    
#     if n in stored:    
#         return(stored[n])             
#     if n == 2 or n == 1 or n == 0:    
#         return 1    
#     elif n > 2:     
#         stored[n] =  population(n-1, m) + population(n-2, m) - population(n-m-1, m)    
#         return stored[n]    
#     else:    
#         return 0

'''workaround 2'''
# n=6
# k=3
# f=[1]*100
# for i in range(2,n):
#   f[i]=f[i-1]+f[i-2]
#   if i>=k:
#     f[i]-=f[(i-k)-1]  
# print (f[i])

# n = 7
# m = 4
# print(population(n,m))

'''solution 2'''
# def fib(month, age):
# 	generation = [0]*age
# 	generation[0], generation[1] = 0,1
# 	for x in range(2,month): 
# 		temp = list(generation)
# 		generation[0] = sum(generation[1:]) #number of new born
# 		for i in range(1,age): 
# 			generation[i] = temp[i-1]
# 	return sum(generation)

# print(fib(4,3))


