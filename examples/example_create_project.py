from modrinthpy import ModrinthClient
from modrinthpy.utils import create_project_data, create_donation_url

client = ModrinthClient(api_key="key")

donation_urls = [
    create_donation_url(platform="patreon", url="https://patreon.com/example"),
    create_donation_url(platform="paypal", url="https://paypal.me/example")
]


project_data = create_project_data(
    title="My New Project",
    project_type="mod",
    slug="my-new-project",
    description="This is a new project",
    body="A long form description of the project",
    client_side="required",
    server_side="required",
    categories=["technology", "adventure"],
    issues_url="https://example.com/issues",
    source_url="https://example.com/source",
    wiki_url="https://example.com/wiki",
    discord_url="https://discord.gg/example",
    license_id="MIT",
    license_url="https://opensource.org/licenses/MIT",
    is_draft=True, 
    requested_status="unlisted",
    uploaded_images=[],
    organization_id=None,
)

new_project = client.create_project(project_data)
print(new_project)
