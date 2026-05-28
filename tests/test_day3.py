from day3 import calculate_bill


def test_child_no_photo():
    assert calculate_bill(130, 8, False) == 5


def test_child_with_photo():
    assert calculate_bill(130, 8, True) == 8


def test_teen_no_photo():
    assert calculate_bill(130, 16, False) == 7


def test_teen_with_photo():
    assert calculate_bill(130, 16, True) == 10


def test_adult_no_photo():
    assert calculate_bill(130, 25, False) == 12


def test_adult_with_photo():
    assert calculate_bill(130, 25, True) == 15


def test_too_short_returns_none():
    assert calculate_bill(100, 25, False) is None


def test_exactly_120cm_can_ride():
    assert calculate_bill(120, 25, False) == 12


def test_age_boundary_under_12():
    assert calculate_bill(130, 11, False) == 5


def test_age_boundary_exactly_18():
    assert calculate_bill(130, 18, False) == 7


def test_age_boundary_just_over_18():
    assert calculate_bill(130, 19, False) == 12
