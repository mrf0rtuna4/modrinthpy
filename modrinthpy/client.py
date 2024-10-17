import asyncio
import json
import logging
from typing import Dict, List, Tuple, Any, Optional

import aiohttp

from .decorators import check_project
from .exceptions import ModrinthAPIError, UnauthorizedError
from .models import Project, Version, User, Notification, SearchResult
from .utils import create_project_payload, create_version_payload
from .objects import CreatableProject, CreatableVersion

logging.basicConfig(level=logging.DEBUG)


class BaseModrinthClient:
    BASE_URL = "https://api.modrinth.com/v2"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    def _require_api_token(self):
        """Helper method to check if API token is present"""
        if not self.api_key:
            raise UnauthorizedError("API token is required for this request")

    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError

    async def search_projects(self, query: str, **kwargs) -> List[SearchResult]:
        response = await self._request("GET", "search", params={"query": query, **kwargs})
        return [SearchResult(item) for item in response.get("hits", [])]

    @check_project
    async def get_project(self, id: str = None, slug: str = None) -> Project:
        response = await self._request("GET", f"project/{id or slug}")
        return Project(response)

    async def get_projects(self, ids: List[str]) -> List[Project]:
        response = await self._request("GET", "projects", params={"ids": json.dumps(ids)})
        return [Project(proj_data) for proj_data in response]

    @check_project
    async def get_project_versions(self, id: str = None, slug: str = None) -> List[Version]:
        response = await self._request("GET", f"project/{id or slug}/version")
        return [Version(item) for item in response]

    async def create_project(self, data: Dict[str, Any]) -> Project:
        self._require_api_token()
        payload = create_project_payload(data)
        response = await self._request("POST", "project", data=payload)
        return Project(response)

    @check_project
    async def add_gallery_image(self, ext: str, featured: bool, id: str = None, slug: str = None, **kwargs) -> Dict[
        str, Any]:
        self._require_api_token()
        response = await self._request("POST", f"project/{id or slug}/gallery",
                                       params={"ext": json.dumps(ext), "featured": json.dumps(featured),
                                               "title": kwargs.get("title"), "description": kwargs.get("description"),
                                               "ordering": kwargs.get("ordering")})
        return response

    @check_project
    async def update_project(self, data: Dict[str, Any], id: str = None, slug: str = None) -> Project:
        self._require_api_token()
        response = await self._request("PATCH", f"project/{id or slug}", json=data)
        return Project(response)

    @check_project
    async def update_project_icon(self, icon_file: bytes, id: str = None, slug: str = None) -> Project:
        self._require_api_token()
        response = await self._request("PATCH", f"project/{id or slug}/icon", data={"icon": icon_file})
        return Project(response)

    async def update_gallery_image(self, image_id: str, image_data: Dict[str, Any],
                                   id: str = None, slug: str = None) -> Dict[str, Any]:
        response = await self._request("PATCH", f"project/{id or slug}/gallery", json=image_data)
        return response

    async def bulk_update_projects(self, ids: List[str], data: List[Dict[str, Any]]) -> List[Project]:
        self._require_api_token()
        response = await self._request("PATCH", "projects", params={"ids": [",".join(ids)]}, json=data)
        return [Project(item) for item in response]

    async def get_random_projects(self, count: int) -> List[Project]:
        response = await self._request("GET", "projects_random", params={"count": count})
        return [Project(item) for item in response]

    @check_project
    async def delete_project_icon(self, id: str = None, slug: str = None) -> Dict[str, Any]:
        return await self._request("DELETE", f"project/{id or slug}/icon")

    @check_project
    async def delete_project(self, id: str = None, slug: str = None) -> Dict[str, Any]:
        self._require_api_token()
        return await self._request("DELETE", f"project/{id or slug}")

    @check_project
    async def check_project_slug(self, id: str = None, slug: str = None) -> Dict[str, Any]:
        return await self._request("GET", f"project/{id or slug}/check")

    async def get_version(self, version_id: str) -> Version:
        response = await self._request("GET", f"version/{version_id}")
        return Version(response)

    async def create_version(self, version_data: Dict[str, Any],
                         files: List[Tuple[str, Tuple[str, bytes, str]]]) -> Version:
        self._require_api_token()
        version = CreatableVersion(**version_data)
        payload = create_version_payload(version.to_dict(), files)
        response = await self._request("POST", "version", data=payload)
        return Version(response)


    async def update_version(self, version_id: str, data: Dict[str, Any]) -> Version:
        self._require_api_token()
        response = await self._request("PATCH", f"version/{version_id}", json=data)
        return Version(response)

    async def delete_version(self, version_id: str) -> Dict[str, Any]:
        self._require_api_token()
        return await self._request("DELETE", f"version/{version_id}")

    async def get_user(self, user_id: str) -> User:
        response = await self._request("GET", f"user/{user_id}")
        return User(response)

    async def get_user_projects(self, user_id: str) -> List[Project]:
        response = await self._request("GET", f"user/{user_id}/projects")
        return [Project(item) for item in response]

    async def get_user_versions(self, user_id: str) -> List[Version]:
        response = await self._request("GET", f"user/{user_id}/versions")
        return [Version(item) for item in response]

    async def get_notifications(self) -> List[Notification]:
        self._require_api_token()
        response = await self._request("GET", "notifications")
        return [Notification(item) for item in response]

    async def mark_notification_read(self, notification_id: str) -> Dict[str, Any]:
        self._require_api_token()
        return await self._request("POST", f"notification/{notification_id}/read")

    async def get_email(self) -> Dict[str, Any]:
        self._require_api_token()
        return await self._request("GET", "user/email")

    async def get_payouts(self) -> List[Dict[str, Any]]:
        self._require_api_token()
        return await self._request("GET", "user/payouts")

    async def request_payout(self) -> Dict[str, Any]:
        self._require_api_token()
        return await self._request("POST", "user/payouts/request")


class ModrinthClient(BaseModrinthClient):
    def __init__(self, api_key: Optional[str] = None, default_output: Optional[bool] = None):
        super().__init__(api_key)
        self.session = None
        self.default_output = default_output

    async def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        if not self.session:
            self.session = aiohttp.ClientSession()
            if self.api_key:
                self.session.headers.update({"Authorization": self.api_key})

        url = f"{self.BASE_URL}/{endpoint}"
        logging.debug(f"Request URL: {url}")
        logging.debug(f"Request Method: {method}")
        logging.debug(f"Request Headers: {kwargs.get('headers', {})}")
        logging.debug(f"Request Data: {kwargs.get('data', {})}")
        async with self.session.request(method, url, **kwargs) as response:
            if response.status == 401:
                raise UnauthorizedError((await response.json()).get("description"))
            if response.status not in (200, 204):
                try:
                    error_message = (await response.json()).get("description", "No description")
                except aiohttp.ContentTypeError:
                    error_message = await response.text()
                raise ModrinthAPIError(response.status, error_message)
            try:
                json_data = await response.json()
            except aiohttp.ContentTypeError:
                json_data = {}

            if self.default_output and json_data:
                if isinstance(json_data, list):
                    for item in json_data:
                        print(item)
                else:
                    print(json_data)

            return json_data

    async def start(self):
        if not self.session:
            self.session = aiohttp.ClientSession()
            if self.api_key:
                self.session.headers.update({"Authorization": self.api_key})

    async def close(self):
        if self.session:
            await self.session.close()

    def run(self, coro):
        try:
            asyncio.run(coro)
        finally:
            if self.session and not self.session.closed:
                asyncio.run(self.close())

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
