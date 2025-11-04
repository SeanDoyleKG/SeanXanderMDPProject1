import pytest
from src.main import makelist

EXPECTED_TASK_HEADER = """1. Add Task
2. View Tasks
3. Mark Task as Done
4. Exit
""" + "=" * 50 + "\n"

GET_TASKS_HEADER = """Tasks:
"""

GET_TASKS_TAIL = "-" * 50 + "\n"

def assemble_get_tasks_str(tasks:str=""):
    return "{}{}{}".format(GET_TASKS_HEADER, tasks, GET_TASKS_TAIL)


def test_add_task(capsys, monkeypatch):
    next_input = iter(["1", "new task"]).__next__
    monkeypatch.setattr("builtins.input", lambda _ : next_input())
    lst = []
    res = makelist(lst)
    assert res == 1
    assert lst == ["new task"]
    captured = capsys.readouterr()
    expected = EXPECTED_TASK_HEADER + "-" * 50 + "\n"
    assert captured.out == expected

    next_input = iter(["1", "new task"]).__next__
    monkeypatch.setattr("builtins.input", lambda _ : next_input())
    lst = ["first", "second", "third"]
    res = makelist(lst)
    assert res == 1
    assert lst == ["first", "second", "third", "new task"]
    captured = capsys.readouterr()
    expected = EXPECTED_TASK_HEADER + "-" * 50 + "\n"
    assert captured.out == expected


def test_get_tasks(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _ : "2")
    res = makelist([])
    assert res == 2
    captured = capsys.readouterr()
    expected = EXPECTED_TASK_HEADER + assemble_get_tasks_str()
    assert captured.out == expected

    res = makelist(["first", "second", "third"])
    assert res == 2
    captured = capsys.readouterr()
    expected = EXPECTED_TASK_HEADER + assemble_get_tasks_str("""1. first
2. second
3. third
""")
    assert captured.out == expected

def test_mark_done(capsys, monkeypatch):
    next_input = iter(["3", "2"]).__next__
    monkeypatch.setattr("builtins.input", lambda _ : next_input())
    lst = ["first", "second", "third"]
    res = makelist(lst)
    assert res == 3
    assert lst == ["first", "third"]
    captured = capsys.readouterr()
    expected = EXPECTED_TASK_HEADER + "Task marked as done.\n"
    assert captured.out == expected

    next_input = iter(["3", "4"]).__next__
    monkeypatch.setattr("builtins.input", lambda _ : next_input())
    lst = ["first", "second", "third"]
    res = makelist(lst)
    assert res == 3
    assert lst == ["first", "second", "third"]
    captured = capsys.readouterr()
    expected = EXPECTED_TASK_HEADER + "Invalid task number.\n"
    assert captured.out == expected


def test_exit(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _ : "4")
    lst = ["first", "second", "third"]
    res = makelist(lst)
    assert res == 4
    assert lst == ["first", "second", "third"]
    captured = capsys.readouterr()
    expected = EXPECTED_TASK_HEADER + "Exiting.\n" + "-" * 50 + "\n"
    assert captured.out == expected

def test_invalid_num(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _ : "5")
    lst = ["first", "second", "third"]
    res = makelist(lst)
    assert res == 5
    assert lst == ["first", "second", "third"]
    captured = capsys.readouterr()
    expected = EXPECTED_TASK_HEADER + "Invalid choice.\n" + "-" * 50 + "\n"
    assert captured.out == expected

def test_unexpected_inputs(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _ : "HELLO WORLD")
    lst = ["first", "second", "third"]
    res = makelist(lst)
    assert res == 5
    assert lst == ["first", "second", "third"]
    captured = capsys.readouterr()
    expected = EXPECTED_TASK_HEADER + "Invalid choice.\n" + "-" * 50 + "\n"
    assert captured.out == expected