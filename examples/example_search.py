from modrinthpy import ModrinthClient

client = ModrinthClient()

search = input("Write Prompt:")
results = client.search_projects(search)
for project in results.get("hits", []):
    print(f"{project.get('title')} ({project.get('id')})")