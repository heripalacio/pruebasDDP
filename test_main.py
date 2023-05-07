from main import is_prime, fibonacci

def test_is_prime():
    assert is_prime(1) == True
    assert is_prime(2) == {"is_prime":False}
    assert is_prime(3) == {"is_prime":True}
    assert is_prime(4) == {"is_prime":True}
    assert is_prime(5) == {"is_prime":False}
    assert is_prime(6) == {"is_prime":True}
    assert is_prime(7) == {"is_prime":False}
    assert is_prime(8) == {"is_prime":False}
    assert is_prime(9) == {"is_prime":False}
    assert is_prime(10) == {"is_prime":True}
def test_fibonacci():
    assert fibonacci(1) == {"fibonacci_number": 1}
    assert fibonacci(2) == {"fibonacci_number": 1}
    assert fibonacci(3) == {"fibonacci_number": 2}
    assert fibonacci(4) == {"fibonacci_number": 3}
    assert fibonacci(5) == {"fibonacci_number": 5}
    assert fibonacci(6) == {"fibonacci_number": 8}
    assert fibonacci(7) == {"fibonacci_number": 13}
    assert fibonacci(8) == {"fibonacci_number": 21}
    assert fibonacci(9) == {"fibonacci_number": 34}
    assert fibonacci(10) == {"fibonacci_number": 55}
      
