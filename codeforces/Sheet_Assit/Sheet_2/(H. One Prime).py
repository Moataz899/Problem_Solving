X = int(input())

def is_prime(X):
  if X <= 1:
    return "NO"

  for i in range(2, int(X**0.5) + 1):
    if X % i == 0:
      return "NO"
  return "YES"
  
print(is_prime(X))
