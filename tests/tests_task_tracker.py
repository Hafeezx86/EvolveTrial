from src.task_tracker import Task, TaskManager


def test_task_starts_incomplete():
    task = Task("Study Git")
    assert task.completed is False


def test_task_can_be_completed():
    task = Task("Study Git")
    task.complete()
    assert task.completed is True


def test_manager_can_add_task():
    manager = TaskManager()
    manager.add_task("Complete assignment")

    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Complete assignment"