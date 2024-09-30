from typing import List, Optional, Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BaseModelWithAutoMapping:
    def __init__(self, data: Optional[Dict[str, Any]] = None, **kwargs):
        """
        Initialize the model. Supports both dictionary data and keyword arguments.

        :param data: A dictionary with field names and values.
        :param kwargs: Field names and values as keyword arguments.
        """
        cls = self.__class__
        hints = getattr(cls, '__annotations__', {})

        if data:
            for key, value in data.items():
                if key in hints:
                    setattr(self, key, value)
                else:
                    logger.warning(
                        f"Unknown field '{key}' for class '{cls.__name__}'")

        for key, value in kwargs.items():
            if key in hints:
                setattr(self, key, value)
            else:
                logger.warning(
                    f"Unknown field '{key}' for class '{cls.__name__}'")

        for key in hints:
            if not hasattr(self, key):
                setattr(self, key, None)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(data)

    def to_dict(self):
        """
        Converts the model instance into a dictionary, including only the annotated attributes.
        """
        cls = self.__class__
        hints = getattr(cls, '__annotations__', {})
        return {key: getattr(self, key, None) for key in hints}

    def __repr__(self) -> str:
        annotations = list(self.__annotations__.keys())[:3]
        repr_str = ", ".join([f"{key}={getattr(self, key, None)}" for key in annotations])
        return f"<{self.__class__.__name__} {repr_str}>"


class DonationUrl(BaseModelWithAutoMapping):
    id: Optional[str]
    platform: Optional[str]
    url: Optional[str]


class License(BaseModelWithAutoMapping):
    id: Optional[str]
    name: Optional[str]
    url: Optional[str]


class GalleryItem(BaseModelWithAutoMapping):
    url: Optional[str]
    featured: Optional[bool]
    title: Optional[str]
    description: Optional[str]
    created: Optional[str]
    ordering: Optional[int]


class Project(BaseModelWithAutoMapping):
    id: str
    slug: str
    title: Optional[str]
    description: Optional[str]
    categories: List[str]
    versions: List[str]
    client_side: Optional[bool]
    server_side: Optional[bool]
    body: Optional[str]
    status: Optional[str]
    requested_status: Optional[str]
    additional_categories: List[str]
    issues_url: Optional[str]
    source_url: Optional[str]
    wiki_url: Optional[str]
    discord_url: Optional[str]
    donation_urls: List[DonationUrl]
    project_type: Optional[str]
    downloads: Optional[int]
    icon_url: Optional[str]
    color: Optional[str]
    thread_id: Optional[str]
    monetization_status: Optional[str]
    team: Optional[str]
    body_url: Optional[str]
    moderator_message: Optional[str]
    published: Optional[str]
    updated: Optional[str]
    approved: Optional[bool]
    queued: Optional[bool]
    followers: Optional[int]
    license: License
    game_versions: List[str]
    loaders: List[str]
    gallery: List[GalleryItem]


class Version(BaseModelWithAutoMapping):
    name: str
    version_number: str
    changelog: Optional[str]
    dependencies: List['Dependency']
    game_versions: List[str]
    version_type: Optional[str]
    loaders: List[str]
    featured: Optional[bool]
    status: Optional[str]
    requested_status: Optional[str]
    id: str
    project_id: str
    author_id: str
    date_published: Optional[str]
    downloads: Optional[int]
    changelog_url: Optional[str]
    files: List['File']


class User(BaseModelWithAutoMapping):
    id: str
    username: str
    name: str
    bio: Optional[str]
    email: Optional[str]
    payout_data: Optional['PayoutData']
    avatar_url: Optional[str]
    created: Optional[str]
    role: Optional[str]
    badges: Optional[int]
    auth_providers: Optional[List[str]]
    email_verified: Optional[bool]
    has_password: Optional[bool]
    has_totp: Optional[bool]


class Notification(BaseModelWithAutoMapping):
    id: str
    type: str
    message: str
    read: bool


class Dependency(BaseModelWithAutoMapping):
    version_id: str
    project_id: str
    file_name: Optional[str]
    dependency_type: str


class File(BaseModelWithAutoMapping):
    hashes: Dict[str, str]
    url: str
    filename: str
    primary: bool
    size: int
    file_type: str


class PayoutData(BaseModelWithAutoMapping):
    balance: Optional[int]
    payout_wallet: Optional[str]
    payout_wallet_type: Optional[str]
    payout_address: Optional[str]


class SearchResult(BaseModelWithAutoMapping):
    slug: str
    title: str
    description: Optional[str]
    categories: List[str]
    client_side: Optional[str]
    server_side: Optional[str]
    project_type: Optional[str]
    downloads: Optional[int]
    icon_url: Optional[str]
    color: Optional[int]
    thread_id: Optional[str]
    monetization_status: Optional[str]
    project_id: Optional[str]
    author: Optional[str]
    display_categories: List[str]
    versions: List[str]
    follows: Optional[int]
    date_created: Optional[str]
    date_modified: Optional[str]
    latest_version: Optional[str]
    license: Optional[str]
    gallery: List[str]
    featured_gallery: Optional[str]
