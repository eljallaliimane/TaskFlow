"""
Programme principal - Démonstration des 4 Design Patterns:
1. Factory: Création des tâches
2. Singleton: NotificationService
3. Observer: Notification des utilisateurs
4. Strategy: Filtrage dynamique des tâches
"""
from observer.user import User
from factory import TaskFactory
from enums import TaskStatus
from strategy import (
    FilterByStatus,
    FilterByPriority,
    FilterByUser,
    TaskFilterContext
)
# Étape 3+5+6: Création des utilisateurs

u1 = User("Ali")
u2 = User("Sara")
# Étape : Création des tâches via Factory + Notification Observer
t1 = TaskFactory.create_task(
    "Login Page",
    "HIGH",
    u1
)

t2 = TaskFactory.create_task(
    "API Backend",
    "LOW",
    u2
)

t3 = TaskFactory.create_task(
    "Dashboard",
    "HIGH",
    u1
)

t1.assign_user(u1)
t2.assign_user(u2)
t3.assign_user(u1)

# Étape 7: Changement de statut

t1.change_status(TaskStatus.IN_PROGRESS)
t2.change_status(TaskStatus.DONE)
t3.change_status(TaskStatus.IN_PROGRESS)

tasks = [t1, t2, t3]

print("\n===== Toutes les tâches =====")

for task in tasks:
    print(task)
# Étape 8: Filtrage avec Strategy Pattern

print("\n===== Filter By Status =====")

status_filter = TaskFilterContext(
    FilterByStatus(TaskStatus.IN_PROGRESS)
)

filtered_tasks = status_filter.execute_filter(tasks)

for task in filtered_tasks:
    print(task)

print("\n===== Filter By Priority =====")

priority_filter = TaskFilterContext(
    FilterByPriority("HIGH")
)

filtered_tasks = priority_filter.execute_filter(tasks)

for task in filtered_tasks:
    print(task)

print("\n===== Filter By User =====")

user_filter = TaskFilterContext(
    FilterByUser(u1)
)

filtered_tasks = user_filter.execute_filter(tasks)

for task in filtered_tasks:
    print(task)
# Étape 9: Modifier une tâche
    print("\n===== Modification =====")
    t1.update_task(new_title="Login Page V2", new_priority="MEDIUM")
    print(t1)

# Étape 10: Supprimer une tâche

    print("\n===== Suppression =====")
    t2.delete_task()
if t2 in tasks:
    tasks.remove(t2)

    print("\n===== Tâches après suppression =====")
for task in tasks:
        print(task)
