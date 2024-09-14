#Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи - description, срок выполнения - period of execution,
# и статус - status (выполнено - done/не выполнено - not completed).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих
# (не выполненных) задач.
from datetime import datetime


class Task:
    def __init__(self, description, due_date):
        """Инициализация задачи с описанием и сроком выполнения."""
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        """Отметить задачу как выполненную."""
        self.completed = True

    def __str__(self):
        """Вернуть строковое представление задачи."""
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"{self.description} (срок: {self.due_date.strftime('%d-%m-%Y')}) - {status}"


class TaskManager:
    def __init__(self):
        """Инициализация списка задач."""
        self.tasks = []

    def add_task(self, description, due_date):
        """Добавление новой задачи."""
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_completed(self, task_index):
        """Отметить задачу как выполненную по индексу."""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()

    def get_pending_tasks(self):
        """Получить список невыполненных задач."""
        return [task for task in self.tasks if not task.completed]

    def show_tasks(self):
        """Вывести список всех задач."""
        if not self.tasks:
            print("Задач нет.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()

    # Добавление задач
    manager.add_task("Купить продукты", datetime(2024, 9, 20))
    manager.add_task("Написать отчет", datetime(2024, 9, 18))

    # Отметить задачу как выполненную
    manager.mark_task_completed(1)  # Отметка второй задачи как выполненной

    # Вывод всех задач
    print("Все задачи:")
    manager.show_tasks()

    # Вывод невыполненных задач
    print("\nНевыполненные задачи:")
    pending_tasks = manager.get_pending_tasks()
    for task in pending_tasks:
        print(task)

