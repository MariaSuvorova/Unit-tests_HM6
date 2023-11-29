"""Module providing tests of Class 'list_comparator'"""
import pytest
from list_comparator import AverageCounter, ListComparator


@pytest.fixture
def setup_empty_list():
    """Creat empty list"""
    return []

@pytest.fixture
def setup_list_lower_average():
    """Creat list with lower average meaning"""
    return [1, 2, 3, 4, 5]

@pytest.fixture
def setup_list_bigger_average():
    """Creat list with bigger average meaning"""
    return [6, 7, 8, 9, 10]

@pytest.fixture(name="setup")
def setup_list_negative_numbers():
    """Creat list with negative numbers"""
    return [-6, -7, -8, -9, -10]

# Test AverageCounter class function

def test_average_counter_empty_list(setup_empty_list):
    """Test Class AverageCounter with empty list"""
    result = AverageCounter(setup_empty_list)
    with pytest.raises(ZeroDivisionError):
        result.average_of_list()

def test_average_counter(setup_list_lower_average):
    """Test Class AverageCounter with non empty list"""
    result = 3
    assert result == AverageCounter(setup_list_lower_average).average_of_list()

def test_average_counter_failed(setup_list_lower_average):
    """Failed test Class AverageCounter with non empty list"""
    result = 5
    assert result != AverageCounter(setup_list_lower_average).average_of_list()

def test_average_counter_negative_numbers(setup_list_negative_numbers):
    """Test Class AverageCounter with negative_numbers list"""
    result = -8
    assert result == AverageCounter(setup_list_negative_numbers).average_of_list()

# Test List_comparator class function

def test_list_comparator_lower_bigger_average(setup_list_lower_average, setup_list_bigger_average):
    """Тест, когда среднее значение второго списка больше."""
    result = ListComparator(setup_list_lower_average, setup_list_bigger_average)
    assert result.compare_of_lists() == "Второй список имеет большее среднее значение"

def test_list_comparator_bigger_lower_average(setup_list_bigger_average, setup_list_lower_average):
    """Тест, когда среднее значение первого списка больше."""
    result = ListComparator(setup_list_bigger_average, setup_list_lower_average)
    assert result.compare_of_lists() == "Первый список имеет большее среднее значение"

def test_list_comparator_equal_averages(setup_list_bigger_average):
    """Тест, когда средние значения равны."""
    result = ListComparator(setup_list_bigger_average, setup_list_bigger_average)
    assert result.compare_of_lists() == "Средние значения равны"
