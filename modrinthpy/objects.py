from typing import List, Optional, Dict
from .models import BaseModelWithAutoMapping, DonationUrl, Dependency

class CreatableProject(BaseModelWithAutoMapping):
    slug: str
    title: str
    description: str
    categories: List[str]
    client_side: str
    server_side: str
    body: str
    status: Optional[str]
    requested_status: Optional[str]
    additional_categories: List[str] = []
    issues_url: Optional[str]
    source_url: Optional[str]
    wiki_url: Optional[str]
    discord_url: Optional[str]
    donation_urls: Optional[List[DonationUrl]] = []
    license_id: str
    license_url: Optional[str]
    project_type: str
    is_draft: Optional[bool] = True
    gallery_items: Optional[List[str]] = []
    icon: Optional[str] = None
    initial_versions: Optional[Dict] = []

    def __init__(self, data: Optional[dict] = None, **kwargs):
        super().__init__(data, **kwargs)


class CreatableVersion(BaseModelWithAutoMapping):
    name: str
    version_number: str
    changelog: Optional[str]
    dependencies: List['Dependency']
    game_versions: List[str]
    version_type: str  # Enum: 'release', 'beta', 'alpha'
    loaders: List[str]
    featured: bool
    status: Optional[str]  # Enum: 'listed', 'archived', 'draft', 'unlisted', 'scheduled', 'unknown'
    requested_status: Optional[str]
    project_id: str
    file_parts: List[str]
    primary_file: Optional[str]
