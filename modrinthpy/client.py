import logging
from typing import Dict, List, Tuple, Any, Optional

import aiohttp

from .exceptions import ModrinthAPIError
from .utils import create_project_payload, create_version_payload
from .models import Project, Version, User, Notification, SearchResult
from .decorators import check_project

logging.basicConfig(level=logging.DEBUG)


class BaseModrinthClient:
    BASE_URL = "https://api.modrinth.com/v2"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    
    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError


    async def search_projects(self, query: str, **kwargs) -> List[SearchResult]:
        response = await self._request("GET", "search", params={"query": query, **kwargs})
        return [SearchResult(item) for item in response.get("hits", [])]


    @check_project
    async def get_project(self, id: str = None, slug: str = None) -> Project:
        response = await self._request("GET", f"project/{id or slug}")
        return Project(response)

    
    @check_project
    async def get_project_versions(self, id: str = None, slug: str = None) -> List[Version]:
        response = await self._request("GET", f"project/{id or slug}/version")
        return [Version(item) for item in response]


    async def create_project(self, data: Dict[str, Any]) -> Project:
        payload = create_project_payload(data)
        headers = {"Content-Type": payload.content_type}
        response = await self._request("POST", "project", data=payload, headers=headers)
        return Project(response)

    async def update_project(self, project_id: str, data: Dict[str, Any]) -> Project:
        response = await self._request("PATCH", f"project/{project_id}", json=data)
        return Project(response)

    async def delete_project(self, project_id: str) -> Dict[str, Any]:
        return await self._request("DELETE", f"project/{project_id}")

    async def get_version(self, version_id: str) -> Version:
        response = await self._request("GET", f"version/{version_id}")
        return Version(response)

    async def create_version(
            self, version_data: Dict[str, Any], files: List[Tuple[str, Tuple[str, bytes, str]]]) -> Version:
        payload = create_version_payload(version_data, files)
        headers = {"Content-Type": payload.content_type}
        response = await self._request("POST", "version", data=payload, headers=headers)
        return Version(response)

    async def update_version(self, version_id: str, data: Dict[str, Any]) -> Version:
        response = await self._request("PATCH", f"version/{version_id}", json=data)
        return Version(response)

    async def delete_version(self, version_id: str) -> Dict[str, Any]:
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
        response = await self._request("GET", "notifications")
        return [Notification(item) for item in response]

    async def mark_notification_read(self, notification_id: str) -> Dict[str, Any]:
        return await self._request("POST", f"notification/{notification_id}/read")

    async def get_email(self) -> Dict[str, Any]:
        return await self._request("GET", "user/email")

    async def get_payouts(self) -> List[Dict[str, Any]]:
        return await self._request("GET", "user/payouts")

    async def request_payout(self) -> Dict[str, Any]:
        return await self._request("POST", "user/payouts/request")


class ModrinthClient(BaseModrinthClient):
    def __init__(self, api_key: Optional[str] = None):
        super().__init__(api_key)
        self.session = None

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
            if response.status != 200:
                raise ModrinthAPIError(response.status, await response.text())
            return await response.json()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()