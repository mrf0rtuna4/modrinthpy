import logging
from typing import Dict, List, Tuple, Any, Optional

import requests

from .exceptions import ModrinthAPIError
from .utils import create_project_payload, create_version_payload

logging.basicConfig(level=logging.DEBUG)


class ModrinthClient:
    BASE_URL = "https://api.modrinth.com/v2"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({"Authorization": api_key})

    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        url = f"{self.BASE_URL}/{endpoint}"
        logging.debug(f"Request URL: {url}")
        logging.debug(f"Request Method: {method}")
        logging.debug(f"Request Headers: {kwargs.get('headers', {})}")
        logging.debug(f"Request Data: {kwargs.get('data', {})}")
        response = self.session.request(method, url, **kwargs)
        if response.status_code != 200:
            raise ModrinthAPIError(response.status_code, response.text)
        return response.json()

    def search_projects(self, query: str, **kwargs) -> Dict[str, Any]:
        return self._request("GET", "search", params={"query": query, **kwargs})

    def get_project(self, project_id: str) -> Dict[str, Any]:
        return self._request("GET", f"project/{project_id}")

    def get_project_versions(self, project_id: str) -> List[Dict[str, Any]]:
        return self._request("GET", f"project/{project_id}/version")

    def create_project(self, data: Dict[str, Any]) -> Dict[str, Any]:
        payload = create_project_payload(data)
        headers = {"Content-Type": payload.content_type}
        return self._request("POST", "project", data=payload, headers=headers)

    def update_project(self, project_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        return self._request("PATCH", f"project/{project_id}", json=data)

    def delete_project(self, project_id: str) -> Dict[str, Any]:
        return self._request("DELETE", f"project/{project_id}")

    def get_version(self, version_id: str) -> Dict[str, Any]:
        return self._request("GET", f"version/{version_id}")

    def create_version(
            self, version_data: Dict[str, Any], files: List[Tuple[str, Tuple[str, bytes, str]]]) -> Dict[str, Any]:
        payload = create_version_payload(version_data, files)
        headers = {"Content-Type": payload.content_type}
        return self._request("POST", "version", data=payload, headers=headers)

    def update_version(self, version_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        return self._request("PATCH", f"version/{version_id}", json=data)

    def delete_version(self, version_id: str) -> Dict[str, Any]:
        return self._request("DELETE", f"version/{version_id}")

    def get_user(self, user_id: str) -> Dict[str, Any]:
        return self._request("GET", f"user/{user_id}")

    def get_user_projects(self, user_id: str) -> List[Dict[str, Any]]:
        return self._request("GET", f"user/{user_id}/projects")

    def get_user_versions(self, user_id: str) -> List[Dict[str, Any]]:
        return self._request("GET", f"user/{user_id}/versions")

    def get_notifications(self) -> List[Dict[str, Any]]:
        return self._request("GET", "notifications")

    def mark_notification_read(self, notification_id: str) -> Dict[str, Any]:
        return self._request("POST", f"notification/{notification_id}/read")

    def get_email(self) -> Dict[str, Any]:
        return self._request("GET", "user/email")

    def get_payouts(self) -> List[Dict[str, Any]]:
        return self._request("GET", "user/payouts")

    def request_payout(self) -> Dict[str, Any]:
        return self._request("POST", "user/payouts/request")
