import CSP_3_05_Learning_Arguments_and_return as HW


def test_convert_temperature():
    assert HW.convertTemperature("32F") == "0C"
    assert HW.convertTemperature("42F") == "5C"
    assert HW.convertTemperature("42C") == "107F"
    assert HW.convertTemperature("12C") == "53F"


def test_larger():
    assert HW.larger(5,0) ==5
    assert HW.larger(0,5) ==5
    assert HW.larger(5,5) ==5
    assert HW.larger(15,5) ==15


def test_grade():
    assert HW.grade(92)=="A"
    assert HW.grade(90)=="A"
    assert HW.grade(80)=="B"
    assert HW.grade(89)=="B"
    assert HW.grade(79)=="C"
    assert HW.grade(70)=="C"
    assert HW.grade(60)=="D"
    assert HW.grade(63)=="D"
    assert HW.grade(50)=="F"
    assert HW.grade(-50)=="F"


def test_fizz_buzz():
    assert HW.fizzBuzz(15)=="FizzBuzz"
    assert HW.fizzBuzz(5)=="buzz"
    assert HW.fizzBuzz(9)=="fizz"
    assert HW.fizzBuzz(99)=="fizz"
    assert HW.fizzBuzz(17)==17


def test_collatz():
    assert HW.collatz(5) ==16
    assert HW.collatz(6) ==3.0
    assert HW.collatz(4) ==2.0
    assert HW.collatz(1) ==1
