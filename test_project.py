import pytest
from project import guess_check, validate_level, generate_randomnumber

def test_generate_randomnumber():
    num, upper = generate_randomnumber(1)
    assert 1 <= num <= 10
    assert upper == 10

    rn, upper = generate_randomnumber(2)
    assert 1 <= rn <= 50
    assert upper == 50

    rn, upper =generate_randomnumber(3)
    assert 1 <= rn <= 100
    assert upper == 100

def test_validate_level(monkeypatch):
    # Simulate user typing "2"
    monkeypatch.setattr("builtins.input", lambda _: "2")
    assert validate_level() == 2

def test_guess_check(monkeypatch):
    # Force random number to be 5
    monkeypatch.setattr("project.generate_randomnumber", lambda _: (5, 10))

    # Simulate user guesses: 1, 5 (correct on second try)
    inputs = iter(["1", "5"])
    monkeypatch.setattr("builtins.input", lambda : next(inputs))

    score = guess_check(1)
    assert score <= 100
    assert isinstance(score, int)
