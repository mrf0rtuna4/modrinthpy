import json
from typing import List, Tuple

from requests_toolbelt import MultipartEncoder
from .models import Project, Version


def create_project_payload(project: Project) -> MultipartEncoder:
    """
    Creates a payload to create a project. 
    
    :param project: An instance of the Project model.
    :return: MultipartEncoder to send in the request.
    """
    fields = {
        'data': (None, json.dumps(project.to_dict()), 'application/json'),
    }
    return MultipartEncoder(fields=fields)


def create_version_payload(version: Version, files: List[Tuple[str, Tuple[str, bytes, str]]]) -> MultipartEncoder:
    """
    Creates a payload to create a version of the project. 
    
    :param version: An instance of the Version model.
    :param files: List of files to load. 
    :return: MultipartEncoder to send in the request.
    """
    fields = {
        'data': (None, json.dumps(version), 'application/json'),
    }

    for i, file in enumerate(files):
        fields[f'file_{i}'] = file

    return MultipartEncoder(fields=fields)
