# -*- coding: utf-8 -*-
import pytest

from primes import is_prime


@pytest.fixture()
def prime_numbers():
    return [3, 5, 7]


@pytest.fixture()
def non_prime_numbers():
    return [8, 0, 1]


@pytest.fixture()
def negative_numbers():
    return [-1, -3, -6]


def test_is_prime_true(prime_numbers):
    for number in prime_numbers:
        assert is_prime(number)


def test_is_prime_false(non_prime_numbers, negative_numbers):
    for number in non_prime_numbers:
        assert not is_prime(number)

    for number in non_prime_numbers:
        assert not is_prime(number)
