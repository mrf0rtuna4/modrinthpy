import aiohttp
from modrinthpy import ModrinthClient
import hashlib

client = ModrinthClient(api_key="KEY")


def calculate_hash(file_content):
    return hashlib.sha256(file_content).hexdigest()


version_data = {
        "name": "Version 1.0.0",
        "version_number": "1.0.0",
        "changelog": "List of changes in this version: ...",
        "dependencies": [],
        "game_versions": ["1.16.5", "1.17.1"],
        "version_type": "release",
        "loaders": ["fabric", "forge"],
        "featured": True,
        "status": "listed",
        "requested_status": "listed",
        "project_id": "2WdB3LG4", # YOUR PROJECT ID
        "file_parts": ["file_0"]
    }


with open("test.jar", "rb") as f:
        file_content = f.read()
        files = [
            ('test.jar', file_content, 'application/java-archive')
        ]

new_version = client.run(client.create_version(version_data, files))
print(new_version)

