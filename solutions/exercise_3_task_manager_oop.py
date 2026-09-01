"""
Exercise 3: Task Manager with OOP (Hard)

Problem Statement:
Create a Task Manager system using Object-Oriented Programming.
Implement a Task class and a TaskManager class with the following features:

Task Class:
- Attributes: id, title, description, status (pending/completed), priority (1-5)
- Methods: mark_complete(), __str__()

TaskManager Class:
- Methods: add_task(), remove_task(), get_pending(), get_by_priority(), summary()

Requirements:
- Auto-increment task IDs
- Filter tasks by status and priority
- Generate a summary report
"""

class Task:
    """Represents a single task with title, description, status, and priority."""
    
    def __init__(self, task_id: int, title: str, description: str = "", priority: int = 3):
        self.id = task_id
        self.title = title
        self.description = description
        self.status = "pending"
        self.priority = max(1, min(5, priority))  # Clamp between 1-5
    
    def mark_complete(self):
        """Mark the task as completed."""
        self.status = "completed"
    
    def __str__(self):
        return f"[{self.status.upper()}] #{self.id} {self.title} (Priority: {self.priority})"


class TaskManager:
    """Manages a collection of tasks with filtering and reporting capabilities."""
    
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    
    def add_task(self, title: str, description: str = "", priority: int = 3) -> Task:
        """Add a new task and return it."""
        task = Task(self.next_id, title, description, priority)
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def remove_task(self, task_id: int) -> bool:
        """Remove a task by ID. Returns True if found and removed."""
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                return True
        return False
    
    def get_pending(self) -> list:
        """Return all pending tasks."""
        return [t for t in self.tasks if t.status == "pending"]
    
    def get_by_priority(self, priority: int) -> list:
        """Return all tasks with the given priority."""
        return [t for t in self.tasks if t.priority == priority]
    
    def summary(self) -> dict:
        """Return a summary of tasks."""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t.status == "completed")
        pending = total - completed
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "completion_rate": (completed / total * 100) if total > 0 else 0
        }


# Test Cases
def test_task_manager():
    """Test cases for Task and TaskManager classes"""
    
    manager = TaskManager()
    
    # Test 1: Add tasks
    t1 = manager.add_task("Learn Python", "Study basics", priority=5)
    t2 = manager.add_task("Build Project", "Create app", priority=3)
    assert t1.id == 1 and t2.id == 2, "Test 1 failed: IDs not auto-incremented"
    print("✓ Test 1 passed: Tasks added with auto-increment IDs")
    
    # Test 2: Mark complete and filter
    t1.mark_complete()
    pending = manager.get_pending()
    assert len(pending) == 1 and pending[0].id == 2, "Test 2 failed"
    print("✓ Test 2 passed: Mark complete and filter pending")
    
    # Test 3: Priority filtering
    high_priority = manager.get_by_priority(5)
    assert len(high_priority) == 1 and high_priority[0].title == "Learn Python", "Test 3 failed"
    print("✓ Test 3 passed: Filter by priority")
    
    # Test 4: Summary report
    summary = manager.summary()
    assert summary == {"total": 2, "completed": 1, "pending": 1, "completion_rate": 50.0}, f"Test 4 failed: {summary}"
    print("✓ Test 4 passed: Summary report generated")
    
    # Test 5: Remove task
    assert manager.remove_task(1) == True, "Test 5a failed"
    assert manager.remove_task(999) == False, "Test 5b failed"
    print("✓ Test 5 passed: Remove task by ID")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    print("Running Task Manager OOP Tests...\n")
    test_task_manager()