import json
from typing import List, Dict, Union, Optional, Tuple, Any
from requests_toolbelt import MultipartEncoder


def create_project_payload(project_data: Dict[str, Any]) -> MultipartEncoder:
    """
    Создает payload для создания проекта.

    :param project_data: Данные проекта в формате JSON.
    :return: MultipartEncoder для отправки в запросе.
    """
    fields = {
        'data': (None, json.dumps(project_data), 'application/json'),
    }
    return MultipartEncoder(fields=fields)


def create_version_payload(version_data: Dict[str, Any], files: List[Tuple[str, Tuple[str, bytes, str]]]) -> MultipartEncoder:
    """
    Создает payload для создания версии проекта.

    :param version_data: Данные версии в формате JSON.
    :param files: Список файлов для загрузки.
    :return: MultipartEncoder для отправки в запросе.
    """
    fields = {
        'data': (None, json.dumps(version_data), 'application/json'),
    }

    for i, file in enumerate(files):
        fields[f'file_{i}'] = file

    return MultipartEncoder(fields=fields)


def create_project_data(slug: str, title: str, description: str, categories: List[str], client_side: str, server_side: str, body: str,
                        license_id: str, project_type: str, status: Optional[str] = None, requested_status: Optional[str] = None,
                        additional_categories: Optional[List[str]] = None, issues_url: Optional[str] = None, source_url: Optional[str] = None,
                        wiki_url: Optional[str] = None, discord_url: Optional[str] = None, donation_urls: Optional[List[Dict[str, str]]] = None,
                        license_url: Optional[str] = None) -> Dict[str, Any]:
    """
    Создает данные для создания нового проекта.

    :param slug: Slug проекта.
    :param title: Название проекта.
    :param description: Описание проекта.
    :param categories: Список категорий проекта.
    :param client_side: Поддержка клиентской стороны.
    :param server_side: Поддержка серверной стороны.
    :param body: Длинное описание проекта.
    :param license_id: ID лицензии проекта.
    :param project_type: Тип проекта.
    :param status: Статус проекта.
    :param requested_status: Запрошенный статус проекта.
    :param additional_categories: Дополнительные категории.
    :param issues_url: Ссылка на отслеживание ошибок.
    :param source_url: Ссылка на исходный код.
    :param wiki_url: Ссылка на вики.
    :param discord_url: Ссылка на Discord.
    :param donation_urls: Список ссылок для пожертвований.
    :param license_url: Ссылка на лицензию.
    :return: Данные проекта в формате JSON.
    """
    data = {
        "slug": slug,
        "title": title,
        "description": description,
        "categories": categories,
        "client_side": client_side,
        "server_side": server_side,
        "body": body,
        "license_id": license_id,
        "project_type": project_type,
    }
    if status:
        data["status"] = status
    if requested_status:
        data["requested_status"] = requested_status
    if additional_categories:
        data["additional_categories"] = additional_categories
    if issues_url:
        data["issues_url"] = issues_url
    if source_url:
        data["source_url"] = source_url
    if wiki_url:
        data["wiki_url"] = wiki_url
    if discord_url:
        data["discord_url"] = discord_url
    if donation_urls:
        data["donation_urls"] = donation_urls
    if license_url:
        data["license_url"] = license_url
    return data


def create_version_data(name: str, version_number: str, project_id: str, dependencies: List[Dict[str, str]], game_versions: List[str],
                        version_type: str, loaders: List[str], featured: bool, status: str, requested_status: str,
                        changelog: Optional[str] = None, file_parts: Optional[List[str]] = None, primary_file: Optional[str] = None) -> Dict[str, Any]:
    """
    Создает данные для создания новой версии проекта.

    :param name: Название версии.
    :param version_number: Номер версии.
    :param project_id: ID проекта.
    :param dependencies: Список зависимостей версии.
    :param game_versions: Список поддерживаемых версий игры.
    :param version_type: Тип версии (release, beta, alpha).
    :param loaders: Список поддерживаемых загрузчиков.
    :param featured: Определяет, является ли версия рекомендованной.
    :param status: Статус версии.
    :param requested_status: Запрошенный статус версии.
    :param changelog: Изменения в версии.
    :param file_parts: Список частей файлов.
    :param primary_file: Основной файл.
    :return: Данные версии в формате JSON.
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
    Создает данные для зависимости версии.

    :param version_id: ID версии зависимости.
    :param project_id: ID проекта зависимости.
    :param file_name: Имя файла зависимости.
    :param dependency_type: Тип зависимости.
    :return: Данные зависимости в формате JSON.
    """
    return {
        "version_id": version_id,
        "project_id": project_id,
        "file_name": file_name,
        "dependency_type": dependency_type
    }
