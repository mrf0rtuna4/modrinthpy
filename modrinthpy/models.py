class Project:
    def __init__(self, data):
        self.id = data.get("id")
        self.slug = data.get("slug")
        self.title = data.get("title")
        self.description = data.get("description")
        self.categories = data.get("categories", [])
        self.versions = data.get("versions", [])

    def __repr__(self):
        return f"<Project id={self.id} title={self.title}>"


class Version:
    def __init__(self, data):
        self.id = data.get("id")
        self.project_id = data.get("project_id")
        self.name = data.get("name")
        self.version_number = data.get("version_number")
        self.changelog = data.get("changelog")

    def __repr__(self):
        return f"<Version id={self.id} name={self.name}>"


class User:
    def __init__(self, data):
        self.id = data.get("id")
        self.username = data.get("username")
        self.name = data.get("name")
        self.email = data.get("email")
        self.payouts_enabled = data.get("payouts_enabled")

    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"


class Notification:
    def __init__(self, data):
        self.id = data.get("id")
        self.type = data.get("type")
        self.message = data.get("message")
        self.read = data.get("read")

    def __repr__(self):
        return f"<Notification id={self.id} type={self.type}>"
