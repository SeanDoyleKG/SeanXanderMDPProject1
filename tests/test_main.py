import pytest
from src.main import makelist

EXPECTED_TASK_HEADER = """1. Add Task
2. View Tasks
3. Mark Task as Done
4. Exit
""" + "=" * 50 + "\n"

DASHES_50 = "-" * 50 + "\n"

def make_list_generic_test(
        capsys,
        monkeypatch,
        inputs:list[str],
        lst:list[str],
        expected_lst:list[str],
        expected_out:str,
        expected_input_args:list[str],
        make_list_ret:int
    ):
    next_input = iter(inputs).__next__
    input_args = []
    def input_patch(input_arg):
        input_args.append(input_arg)
        return next_input()
    monkeypatch.setattr("builtins.input", input_patch)
    res = makelist(lst)
    assert res == make_list_ret
    assert lst == expected_lst
    captured = capsys.readouterr()
    assert captured.out == expected_out
    assert input_args == expected_input_args


def test_add_task(capsys, monkeypatch):

    def add_task_helper(initial_task_list, expected_task_list):
        make_list_generic_test(
            capsys,
            monkeypatch,
            ["1", "new task"],
            initial_task_list,
            expected_task_list,
            EXPECTED_TASK_HEADER + DASHES_50,
            ["Enter your choice: ", "Enter task: "],
            1
        )
    add_task_helper([],["new task"],)
    add_task_helper(["first", "second", "third"], ["first", "second", "third", "new task"],)


def test_get_tasks(capsys, monkeypatch):
    def assemble_get_tasks_str(tasks:str=""):
        return "Tasks:\n{}{}".format(tasks, DASHES_50)

    make_list_generic_test(
        capsys,
        monkeypatch,
        ["2"],
        ["first", "second", "third"],
        ["first", "second", "third"],
        EXPECTED_TASK_HEADER + assemble_get_tasks_str("""1. first
2. second
3. third
"""),
        ["Enter your choice: "],
        2
    )

def test_mark_done(capsys, monkeypatch):

    def mark_done_helper(task_to_mark_done, expected_lst, expected_print_out):
        make_list_generic_test(
            capsys,
            monkeypatch,
            ["3", task_to_mark_done],
            ["first", "second", "third"],
            expected_lst,
            EXPECTED_TASK_HEADER + expected_print_out,
            ["Enter your choice: ", "Enter task number to mark as done: "],
            3
        )

    mark_done_helper("2", ["first", "third"], "Task marked as done.\n")
    mark_done_helper("4", ["first", "second", "third"], "Invalid task number.\n")


def test_exit(capsys, monkeypatch):
    make_list_generic_test(
        capsys,
        monkeypatch,
        ["4"],
        ["first", "second", "third"],
        ["first", "second", "third"],
        EXPECTED_TASK_HEADER + "Exiting.\n" + DASHES_50,
        ["Enter your choice: "],
        4
    )

def test_invalid_num(capsys, monkeypatch):
    make_list_generic_test(
        capsys,
        monkeypatch,
        ["5"],
        ["first", "second", "third"],
        ["first", "second", "third"],
        EXPECTED_TASK_HEADER + "Invalid choice.\n" + DASHES_50,
        ["Enter your choice: "],
        5
    )

def test_unexpected_inputs(capsys, monkeypatch):
    make_list_generic_test(
        capsys,
        monkeypatch,
        ["HELLO WORLD"],
        ["first", "second", "third"],
        ["first", "second", "third"],
        EXPECTED_TASK_HEADER + "Invalid choice.\n" + DASHES_50,
        ["Enter your choice: "],
        5
    )