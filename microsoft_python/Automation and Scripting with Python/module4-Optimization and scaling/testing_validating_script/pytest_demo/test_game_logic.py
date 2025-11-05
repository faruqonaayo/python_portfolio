import pytest
from calculate_xp import calculate_xp

# Marking this test as important
@pytest.mark.important
def test_calculate_xp_basic():
    score = 100
    difficulty_multiplier = 1.5
    time_bonus = 20
    expected_xp = 180.0  # 100 * 1.5 + (20% of 150)
    assert calculate_xp(score, difficulty_multiplier, time_bonus) == expected_xp


@pytest.mark.important
def test_calculate_xp_zero_score():
    score = 0
    difficulty_multiplier = 2.0
    time_bonus = 50
    expected_xp = 0.0
    assert calculate_xp(score, difficulty_multiplier, time_bonus) == expected_xp

def test_calculate_xp_high_difficulty():
    score = 200
    difficulty_multiplier = 3.0
    time_bonus = 10
    expected_xp = 660.0  # 200 * 3.0 + (10% of 600)
    assert calculate_xp(score, difficulty_multiplier, time_bonus) == expected_xp

def test_calculate_xp_negative_time_bonus():
    score = 150
    difficulty_multiplier = 2.0
    time_bonus = -10
    expected_xp = 270.0  # 150 * 2.0 - (10% of 300)
    assert calculate_xp(score, difficulty_multiplier, time_bonus) == expected_xp

def test_calculate_xp_invalid_input():
    score = "150"
    difficulty_multiplier = 2.0
    time_bonus = -10
    expected_xp = 270.0  # 150 * 2.0 - (10% of 300)
    with pytest.raises(TypeError):
        calculate_xp(score, difficulty_multiplier, time_bonus)