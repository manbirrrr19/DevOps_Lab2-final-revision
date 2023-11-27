import Lab2


def test_min_max():
    numlist = [3, 1, 7]
    ans = [1, 7]
    result = Lab2.find_min_max(numlist)
    assert (ans == result)


def test_avg():
    numlist = [1, 2, 3, 4, 5]
    ans = 3
    result = Lab2.calc_average(numlist)
    assert (ans == result)


def test_median():
    numlist = [5, 9, 7]
    ans = 7
    result = Lab2.calc_median_temperature(numlist)
    assert (ans == result)
