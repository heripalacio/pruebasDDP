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
    
