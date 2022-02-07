from data_structures.list import ArrayList
import pytest

def test_add_front():
    array_list = ArrayList()
    array_list.add_front(1)
    array_list.add_front(2)
    array_list.add_front(3)
    assert array_list.items == [3, 2, 1]

def test_add_back():
    array_list = ArrayList()
    array_list.add_back(1)
    array_list.add_back(2)
    array_list.add_back(3)
    assert array_list.items == [1, 2, 3]

def test_insert():
    array_list = ArrayList()
    array_list.insert(1, 0)
    array_list.insert(2, 0)
    array_list.insert(3, 2)
    assert array_list.items == [2, 1, 3]
    array_list.insert(4, 2)
    assert array_list.items == [2, 1, 4, 3]
    array_list.insert(5, 3)
    assert array_list.items == [2, 1, 4, 5, 3]
    with pytest.raises(IndexError):
        array_list.insert(5, 10)

def test_head_tail():
    array_list = ArrayList()
    array_list.add_back(1)
    array_list.add_back(2)
    array_list.add_back(3)
    assert array_list.head() == 1
    assert array_list.tail() == 3