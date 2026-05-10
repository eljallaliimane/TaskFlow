from models import Projet

class ProjectService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ProjectService, cls).__new__(cls)
            cls._instance.all_projects = []
        return cls._instance

    def create_project(self, name, admin, description=""):
        if admin.role == "ADMIN":
            new_id = len(self.all_projects) + 1
            new_proj = Projet(new_id, name, description, "2024-05-10")
            self.all_projects.append(new_proj)
            return new_proj
        else:
            print("❌ Error: Only ADMIN can create projects.")
            return None

    def find_project_by_id(self, project_id):
        return next((p for p in self.all_projects if p.id == project_id), None)