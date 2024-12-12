def max_number(*arr):
    return max(arr[0])
 
def min_number(*arr):
    return min(arr[0])
 
def prime(*arr):
    prime_count = 0
    for num in arr[0]:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_count += 1
    return prime_count
 
def palindrome(*arr):
    for num in arr[0]:
        if str(num) == str(num)[::-1]:
            return num
 
def count_palindromes(arr):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]
    
    return sum(is_palindrome(x) for x in arr)
 
def get_max_divisors(arr):
    def count_divisors(n):
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        return count
    
    max_divisors = 0
    number_with_max_divisors = 0
    
    for num in arr:
        divisors = count_divisors(num)
        if divisors > max_divisors or (divisors == max_divisors and num > number_with_max_divisors):
            max_divisors = divisors
            number_with_max_divisors = num
    
    return number_with_max_divisors
 
        
N = int(input())
A = list(map(int, input().split()))
 
print("The maximum number :", max_number(A))
print("The minimum number :", min_number(A))
print("The number of prime numbers :", prime(A))
print("The number of palindrome numbers :", count_palindromes(A))
print("The number that has the maximum number of divisors :", get_max_divisors(A))