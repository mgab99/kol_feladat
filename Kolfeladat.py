import sys

input_data = sys.stdin.read().splitlines()
value = int(input_data[0])

def is_prime(n):

  if n == 0 or n == 1:
      return False
  if n == 2:
      return True
  if n % 2 == 0:
      return False
  else:
      current = 3
      while current * current <= n:
          if n % current == 0:
              return False
          else:
            current += 1

      return True

def get_prime_n(n):
    counter = 0
    current = 1

    while counter < n:
        current += 1
        if is_prime(current):
            counter += 1
        else:
            continue

    return current

print(get_prime_n(value))