from unittest.mock import Mock
from lib.task_list import TaskList


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

def test_adds_mock_tasks_to_list():
    task_list = TaskList()
    task_1 = Mock()
    task_2 = Mock()
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.tasks == [task_1, task_2]


def test_marks__mock_tasks_as_complete():
    task_list = TaskList()
    task_1 = Mock()
    task_2 = Mock()
    task_1.is_complete.return_value = True
    task_2.is_complete.return_value = True
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.all_complete() == True

def test_all_mock_returns_list():
    task_list = TaskList()
    task_1 = Mock()
    task_2 = Mock()
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.all() == [task_1, task_2]