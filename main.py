from todo import load_tasks, save_tasks 

def main():
    tasks = load_tasks()
    print("Loaded tasks:", tasks)
    new_task = {"description": "Buy groceries", "priority": "low", "completed": False}
    tasks.append(new_task)
    save_tasks(tasks)
    print("Updated tasks:", tasks)

if __name__ == "__main__":
    main()
