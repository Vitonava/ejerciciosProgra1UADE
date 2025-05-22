from main import sumar,restar,multiplicar 

def test_sumar():
    assert sumar(1, 2) == 3
    assert sumar(-1, 1) == 0
    assert sumar(1 , 5) == 6

def test_restar():
    assert restar(5, 2) == 3
    assert restar(1, 1) == 0
    assert restar(5 , 5) == 0

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 1) == -1
    assert multiplicar(0, 5) == 0

test_sumar()