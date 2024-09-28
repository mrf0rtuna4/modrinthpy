import json
import warnings
from typing import List, Dict, Union, Optional, Tuple, Any

from requests_toolbelt import MultipartEncoder
from .models import Project


def create_project_payload(project_data: Dict[str, Any]) -> MultipartEncoder:
    """
    Creates a payload to create a project. 
    
    :param project_data: Project data in JSON format. 
    :return: MultipartEncoder to send in the request.
    """
    fields = {
        'data': (None, json.dumps(project_data), 'application/json'),
    }
    return MultipartEncoder(fields=fields)


def create_version_payload(
        version_data: Dict[str, Any], files: List[Tuple[str, Tuple[str, bytes, str]]]) -> MultipartEncoder:
    """
    Creates a payload to create a version of the project. 
    
    :param version_data: Version data in JSON format. 
    :param files: List of files to load. 
    :return: MultipartEncoder to send in the request.
    """
    fields = {
        'data': (None, json.dumps(version_data), 'application/json'),
    }

    for i, file in enumerate(files):
        fields[f'file_{i}'] = file

    return MultipartEncoder(fields=fields)


def create_project_data(
        title: str,
        project_type: str,
        slug: str,
        description: str,
        body: str,
        client_side: str,
        server_side: str,
        categories: List[str],
        additional_categories: Optional[List[str]] = None,
        issues_url: Optional[str] = None,
        source_url: Optional[str] = None,
        wiki_url: Optional[str] = None,
        discord_url: Optional[str] = None,
        donation_urls: Optional[List[Dict[str, str]]] = None,
        license_id: Optional[str] = None,
        license_url: Optional[str] = None,
        is_draft: Optional[bool] = None,
        requested_status: Optional[str] = None,
        uploaded_images: Optional[List[str]] = None,
        organization_id: Optional[str] = None,
        initial_versions: Optional[List[Dict[str, Any]]] = None  # DEPRECATED
) -> Dict[str, Any]:
    """
    ---
    Creates data for creating a new project.
    ---

    :param title: Project Title.
    :param project_type: Type of project.
    :param slug: Project Slug.
    :param description: Project Description.
    :param body: Long project description.
    :param client_side: Client-side support.
    :param server_side: Server-side support.
    :param categories: List of project categories.
    :param additional_categories: Additional categories.
    :param issues_url: Issues Tracking Link.
    :param source_url: Link to source code.
    :param wiki_url: Wiki link.
    :param discord_url: Discord link.
    :param donation_urls: List of donation links.
    :param license_id: Project license ID.
    :param license_url: Link to license.
    :param is_draft: Flag indicating whether the project is a draft or not (DEPRECTED).
    :param requested_status: Requested project status.
    :param uploaded_images: List of uploaded images.
    :param organization_id: Organization ID.
    :param initial_versions: List of initial versions (DEPRECATED).


    :return: Project data in JSON format.
    """
    if initial_versions:
        warnings.warn(
            "The 'initial_versions' parameter is deprecated and will be removed in future versions. "
            "Upload version files after initial upload.",
            DeprecationWarning)

    if is_draft:
        warnings.warn(
            "The 'is_draft' parametr is eprecated - please always mark this as True.",
            DeprecationWarning
        )
    data = {
        "title": title,
        "project_type": project_type,
        "slug": slug,
        "description": description,
        "body": body,
        "client_side": client_side,
        "server_side": server_side,
        "categories": categories,
        "additional_categories": additional_categories or [],
        "issues_url": issues_url,
        "source_url": source_url,
        "wiki_url": wiki_url,
        "discord_url": discord_url,
        "donation_urls": donation_urls or [],
        "license_id": license_id,
        "license_url": license_url,
        "is_draft": is_draft if is_draft is not None else True,
        "requested_status": requested_status,
        "uploaded_images": uploaded_images or [],
        "organization_id": organization_id,
        "initial_versions": initial_versions or []
    }
    return data


def create_donation_url(platform: str, url: str) -> Dict[str, str]:
    """
    Creates the data for the donation link. 
    
    :param platform: The platform of the donation. 
    :param url: URL of the donation link. 
    :return: Donation link data in JSON format.
    """
    return {
        "platform": platform,
        "url": url
    }


def create_initial_version(
        name: str,
        version_number: str,
        changelog: Optional[str] = None,
        dependencies: Optional[List[Dict[str, Union[str, None]]]] = None,
        game_versions: Optional[List[str]] = None,
        version_type: str = "release",
        loaders: Optional[List[str]] = None,
        featured: bool = False,
        status: str = "listed",
        requested_status: Optional[str] = None,
        primary_file: Optional[List[str]] = None,
        file_types: Optional[List[Dict[str, str]]] = None
) -> Dict[str, Any]:
    """
    Creates data for the initial version of the project. 
    
    :param name: The name of the version. 
    :param version_number: Version number. 
    :param changelog: Changes to the version. 
    :param dependencies: List of version dependencies. 
    :param game_versions: List of supported versions of the game.
    :param version_type: Version type. 
    :param loaders: List of supported loaders.
    :param featured: Flag indicating if the version is recommended. 
    :param status: Version status. 
    :param requested_status: Requested version status. 
    :param primary_file: Primary file. 
    :param file_types: List of file types. 
    
    :return: Version data in JSON format.
    """
    data = {
        "name": name,
        "version_number": version_number,
        "changelog": changelog,
        "dependencies": dependencies or [],
        "game_versions": game_versions or [],
        "version_type": version_type,
        "loaders": loaders or [],
        "featured": featured,
        "status": status,
        "requested_status": requested_status,
        "primary_file": primary_file or [],
        "file_types": file_types or []
    }
    return data


def create_version_data(name: str, version_number: str, project_id: str, dependencies: List[Dict[str, str]],
                        game_versions: List[str],
                        version_type: str, loaders: List[str], featured: bool, status: str, requested_status: str,
                        changelog: Optional[str] = None, file_parts: Optional[List[str]] = None,
                        primary_file: Optional[str] = None) -> Dict[str, Any]:
    """
    Creates data for creating a new version of the project.

    :param name: Version Title.
    :param version_number: Version Number.
    :param project_id: Project ID. 
    :param dependencies: List of version dependencies. 
    :param game_versions: List of supported versions of the game. 
    :param version_type: Version type (release, beta, alpha). 
    :param loaders: List of supported loaders. 
    :param featured: Determines if the version is a recommended version. 
    :param status: Version status. 
    :param requested_status: Requested version status. 

    ---
    Optional
    ---
    :param changelog: Changes to the version. 
    :param file_parts: List of file parts. 
    :param primary_file: Primary file. 
    
    :return: Version data in JSON format.
    """
    data = {
        "name": name,
        "version_number": version_number,
        "project_id": project_id,
        "dependencies": dependencies,
        "game_versions": game_versions,
        "version_type": version_type,
        "loaders": loaders,
        "featured": featured,
        "status": status,
        "requested_status": requested_status,
    }
    if changelog:
        data["changelog"] = changelog
    if file_parts:
        data["file_parts"] = file_parts
    if primary_file:
        data["primary_file"] = primary_file
    return data


def create_dependency(version_id: str, project_id: str, file_name: str, dependency_type: str) -> Dict[str, str]:
    """
    Creates data for the version dependency.

    :param version_id: Dependency version ID. 
    :param project_id: Dependency project ID. 
    :param file_name: Dependency file name. 
    :param dependency_type: Type of dependency. 
    
    :return: Dependency data in JSON format.
    """
    return {
        "version_id": version_id,
        "project_id": project_id,
        "file_name": file_name,
        "dependency_type": dependency_type
    }
