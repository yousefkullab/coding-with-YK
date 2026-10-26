from func import  (
    calculate_avg,
    find_max,
    is_even,
    count_vowels,
    calculate_total
)

def test_calculate_avg():
    assert calculate_avg(1, 2, 3, 4, 5) == 3.0
    assert calculate_avg() == 0

def test_find_max():
    assert find_max(1,2,3,4,5) == 5
    assert find_max() == None

def test_is_even():
    assert is_even(8) == True
    assert is_even(7) == False

def test_count_vowels():
    assert count_vowels("Yousef aaa") == 5 # Failed test case 
    assert count_vowels("Yousef") == 3

def test_calculate_total():
    assert calculate_total(1,2,3,4,5) == 15
    assert calculate_total() == 0


