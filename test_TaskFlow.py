from factory import TaskFactory
from observer import User
from enums import TaskStatus

def test_factory_creation():
    u = User("Ali")
    t = TaskFactory.create_task("Login Page", "HIGH", u)
    assert t.title == "Login Page"
    assert t.status == TaskStatus.TODO
