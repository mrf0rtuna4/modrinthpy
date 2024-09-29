from typing import List, Dict, Optional, Any


class Project:
    def __init__(self, data):
        self.id = data.get("id")
        self.slug = data.get("slug")
        self.title = data.get("title")
        self.description = data.get("description")
        self.categories = data.get("categories", [])
        self.versions = data.get("versions", [])
        self.client_side = data.get("client_side")
        self.server_side = data.get("server_side")
        self.body = data.get("body")
        self.status = data.get("status")
        self.requested_status = data.get("requested_status")
        self.additional_categories = data.get("additional_categories", [])
        self.issues_url = data.get("issues_url")
        self.source_url = data.get("source_url")
        self.wiki_url = data.get("wiki_url")
        self.discord_url = data.get("discord_url")
        self.donation_urls = [DonationUrl(d) for d in data.get("donation_urls", [])]
        self.project_type = data.get("project_type")
        self.downloads = data.get("downloads")
        self.icon_url = data.get("icon_url")
        self.color = data.get("color")
        self.thread_id = data.get("thread_id")
        self.monetization_status = data.get("monetization_status")
        self.team = data.get("team")
        self.body_url = data.get("body_url")
        self.moderator_message = data.get("moderator_message")
        self.published = data.get("published")
        self.updated = data.get("updated")
        self.approved = data.get("approved")
        self.queued = data.get("queued")
        self.followers = data.get("followers")
        self.license = License(data.get("license", {}))
        self.game_versions = data.get("game_versions", [])
        self.loaders = data.get("loaders", [])
        self.gallery = [GalleryItem(g) for g in data.get("gallery", [])]

    def __repr__(self):
        return f"<Project id={self.id} title={self.title}>"


class Version:
    def __init__(self, data: Dict[str, Any]):
        self.name: str = data.get("name")
        self.version_number: str = data.get("version_number")
        self.changelog: str = data.get("changelog")
        self.dependencies: List[Dependency] = [Dependency(d) for d in data.get("dependencies", [])]
        self.game_versions: List[str] = data.get("game_versions", [])
        self.version_type: str = data.get("version_type")
        self.loaders: List[str] = data.get("loaders", [])
        self.featured: bool = data.get("featured")
        self.status: str = data.get("status")
        self.requested_status: str = data.get("requested_status")
        self.id: str = data.get("id")
        self.project_id: str = data.get("project_id")
        self.author_id: str = data.get("author_id")
        self.date_published: str = data.get("date_published")
        self.downloads: int = data.get("downloads")
        self.changelog_url: Optional[str] = data.get("changelog_url")
        self.files: List[File] = [File(f) for f in data.get("files", [])]

    def __repr__(self):
        return f"<Version id={self.id} name={self.name}>"


class User:
    def __init__(self, data: Dict[str, Any]):
        self.id: str = data.get("id")
        self.username: str = data.get("username")
        self.name: str = data.get("name")
        self.email: str = data.get("email")
        self.payouts_enabled: bool = data.get("payouts_enabled")

    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"


class Notification:
    def __init__(self, data: Dict[str, Any]):
        self.id: str = data.get("id")
        self.type: str = data.get("type")
        self.message: str = data.get("message")
        self.read: bool = data.get("read")

    def __repr__(self):
        return f"<Notification id={self.id} type={self.type}>"


class DonationUrl:
    def __init__(self, data: Dict[str, Any]):
        self.id: str = data.get("id")
        self.platform: str = data.get("platform")
        self.url: str = data.get("url")

    def __repr__(self):
        return f"<DonationUrl id={self.id} platform={self.platform}>"


class License:
    def __init__(self, data: Dict[str, Any]):
        self.id: data.get("id")
        self.name: data.get("name")
        self.url: data.get("url")

    def __repr__(self):
        return f"<License id={self.id} name={self.name}>"


class GalleryItem:
    def __init__(self, data: Dict[str, Any]):
        self.url: data.get("url")
        self.featured: data.get("featured")
        self.title: data.get("title")
        self.description: data.get("description")
        self.created: data.get("created")
        self.ordering: data.get("ordering")

    def __repr__(self):
        return f"<GalleryItem title={self.title} featured={self.featured}>"


class Dependency:
    def __init__(self, data: Dict[str, Any]):
        self.version_id: str = data.get("version_id")
        self.project_id: str = data.get("project_id")
        self.file_name: str = data.get("file_name")
        self.dependency_type: str = data.get("dependency_type")

    def __repr__(self):
        return f"<Dependency version_id={self.version_id} project_id={self.project_id}>"


class File:
    def __init__(self, data: Dict[str, Any]):
        self.hashes: Dict[str, str] = data.get("hashes", {})
        self.url: str = data.get("url")
        self.filename: str = data.get("filename")
        self.primary: bool = data.get("primary")
        self.size: int = data.get("size")
        self.file_type: str = data.get("file_type")

    def __repr__(self):
        return f"<File filename={self.filename} primary={self.primary}>"
