import json
from typing import List, Tuple

from aiohttp import FormData
from requests_toolbelt import MultipartEncoder

from .objects import CreatableProject, CreatableVersion


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


def create_version_payload(version: dict, files: List[Tuple[str, bytes, str]]) -> FormData:
    """
    Creates a payload for the version creation request using aiohttp.FormData.
    
    :param version: An instance of the CreatableVersion model.
    :param files: List of files to upload.
    :return: FormData to send in the request.
    """
    form_data = FormData()

    form_data.add_field('data', json.dumps(version), content_type='application/json')

    # Добавляем файлы
    for i, (filename, file_content, mime_type) in enumerate(files):
        form_data.add_field(
            f'file_{i}',
            file_content,
            filename=filename,
            content_type=mime_type
        )

    return form_data
