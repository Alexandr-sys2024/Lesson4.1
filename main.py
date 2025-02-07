class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"{self.description} (срок: {self.due_date.strftime('%d-%m-%Y')}) - {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
        else:
            print(f"Ошибка: задача с индексом {task_index} не существует.")

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def show_tasks(self):
        if not self.tasks:
            print("Задач нет.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")


if __name__ == "__main__":
    from datetime import datetime
    
    manager = TaskManager()
    manager.add_task("Купить продукты", datetime(2024, 9, 20))
    manager.add_task("Написать отчет", datetime(2024, 9, 18))

    manager.mark_task_completed(1)  # Отметка второй задачи как выполненной
    manager.mark_task_completed(5)  # Попытка отметить несуществующую задачу

    print("\nВсе задачи:")
    manager.show_tasks()

    print("\nНевыполненные задачи:")
    pending_tasks = manager.get_pending_tasks()
    for task in pending_tasks:
        print(task)