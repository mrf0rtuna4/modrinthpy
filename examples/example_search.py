from modrinthpy import ModrinthClient

client = ModrinthClient()


def display_search_results(results):
    if not results:
        print("No projects found.")
    else:
        print(f"Found {len(results)} projects:")
        for project in results:
            print(f"Slug: {project.slug} | Title: {project.title}")


async def run_search(search_query):
    results = await client.search_projects(search_query)
    display_search_results(results)


search = input("Write Prompt: ")

client.run(run_search(search))
