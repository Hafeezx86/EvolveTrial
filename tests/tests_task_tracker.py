from src.task_tracker import Task


def test_task_starts_incomplete():
    task = Task("Study Git")
    assert task.completed is False