from modrinthpy import ModrinthClient
from modrinthpy.utils import create_version_data, create_dependency

client = ModrinthClient(api_key="your_api_key_here")

version_data = create_version_data(
    name="Version 1.0.0",
    version_number="1.0.0",
    project_id="AABBCCDD",
    dependencies=[
        create_dependency(
            version_id="IIJJKKLL",
            project_id="QQRRSSTT",
            file_name="sodium-fabric-mc1.19-0.4.2+build.16.jar",
            dependency_type="required"
        )
    ],
    game_versions=["1.16.5", "1.17.1"],
    version_type="release",
    loaders=["fabric", "forge"],
    featured=True,
    status="listed",
    requested_status="listed",
    changelog="List of changes in this version: ...",
    file_parts=["file_0"],
    primary_file="file_0"
)

files = [
    ('file_0', ('my_file.jar', open('path/to/my_file.jar', 'rb'), 'application/java-archive'))
]

new_version = client.create_version(version_data, files)
print(new_version)