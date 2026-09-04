from app.models.task import Task
from app.repositories.task_repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def validate_title(self, title: str) -> str:
        # TODO (Copilot Edit demo):
        # Normalize surrounding whitespace and reject an empty title.
        # Raise ValueError("Task title cannot be empty") for invalid input.
        cleaned_title = title.strip()
        if not cleaned_title:
            raise ValueError("Task title cannot be empty")

        return cleaned_title

    def list_tasks(self) -> list[Task]:
        return self.repository.list_tasks()

    def create_task(self, title: str) -> Task:
        cleaned_title = self.validate_title(title)
        return self.repository.create_task(cleaned_title)

    def get_task(self, task_id: int) -> Task | None:
        return self.repository.get_task(task_id)

    def delete_task(self, task_id: int) -> bool:
        # TODO (Copilot Agent demo):
        # Delegate deletion to the repository.
        return self.repository.delete_task(task_id)
