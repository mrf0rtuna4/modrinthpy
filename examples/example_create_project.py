from modrinthpy import ModrinthClient, CreatableProject

client = ModrinthClient(api_key="KEY")

project = CreatableProject(
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
    requested_status="draft"
)


client.run(client.create_project(project))
