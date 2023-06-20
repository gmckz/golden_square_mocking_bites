from lib.task_formatter import TaskFormatter
from unittest.mock import Mock
"""
task formatter constructs task
"""
def test_constructs_task():
    task = Mock()
    task_formatter = TaskFormatter(task)
    assert task_formatter.task == task

"""
When task is incomplete ...
#format returns "- [ ] Task title"
"""
def test_incomplete_task_returns_correctly():
    task = Mock()
    task.title = "my task"
    task.is_complete.return_value = False
    task_formatter = TaskFormatter(task)
    assert task_formatter.format() == "- [ ] my task"

"""
When task is complete ...
#format returns "- [x] Task title"
"""
def test_complete_task_returns_correctly():
    task = Mock()
    task.title = "my task"
    task.is_complete.return_value = True
    task_formatter = TaskFormatter(task)
    assert task_formatter.format() == "- [x] my task"