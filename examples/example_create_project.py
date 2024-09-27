from modrinthpy import ModrinthClient
from modrinthpy.utils import create_project_data

client = ModrinthClient(api_key="APIKEY")

project_data = create_project_data(
    slug="super_new_project",
    title="My New Project",
    description="This is a new project",
    categories=["technology", "game"],
    client_side="required",
    server_side="required",
    body="A long form description of the project",
    license_id="MIT",
    project_type="mod",
    status="draft",
    requested_status="draft",
    additional_categories=["other"],
    issues_url="https://example.com/issues",
    source_url="https://example.com/source",
    wiki_url="https://example.com/wiki",
    discord_url="https://discord.gg/example",
    donation_urls=[{"platform": "patreon", "url": "https://patreon.com/example"}],
    license_url="https://opensource.org/licenses/MIT"
)

new_project = client.create_project(project_data)
print(new_project)