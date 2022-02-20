### 16 enero 2022
### clase de skillshare de python
### como usar los loops con listas de números

#using the range function
# range function is to count the numbers between a set of numbers? apparently

for value in range(10,26):
    print(value)

#it doesn't count the last number as it's counting between numbers


##create a list of numbers

#convert numbers into a list

numbers = list(range(1,50))
print(numbers)

odd_numbers = list(range(1,50,2))
print(odd_numbers)


squares = []
for value in range(1,11):
    square = value **2
    squares.append(square)


print(squares)

print(sum(squares))
print(min(squares))
print(max(squares))

#para hacer la formula de numeros primos es:  numero a + numero b
## numero esl el resultado de a+b = ab, de ahi c es el resultado de ab+b 
primes = []
for value in range(1,1000):
    prime = 