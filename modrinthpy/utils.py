import json
from typing import List, Tuple, Dict, Any

from requests_toolbelt import MultipartEncoder
from .models import Project, Version
from .objects import CreatableProject
from aiohttp import FormData
import json

def create_project_payload(project: CreatableProject) -> FormData:
    """
    Creates a payload to create a project.

    :param project: An instance of the Project model.
    :return: FormData to send in the request.
    """
    fields = FormData()

    fields.add_field('data', json.dumps(project.to_dict()), content_type='application/json')

    # fields.add_field('icon', open('path_to_icon.png', 'rb'), filename='icon.png', content_type='image/png')

    return fields


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
