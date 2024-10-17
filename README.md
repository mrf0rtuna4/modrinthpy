<div align="center">
    <image src="https://github.com/user-attachments/assets/c037660a-c363-4794-b805-dfbf7b55f3e3">
    <h1>ModrinthPy</h1>
</div>

<div align="center">
    <a href="https://pypi.org/project/modrinthpy/">
        <img src="https://img.shields.io/pypi/v/modrinthpy">
    </a>
    <a href="https://github.com/mrf0rtuna4/modrinthpy/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/mrf0rtuna4/modrinthpy">
    </a>
    <a href="https://pypi.org/project/modrinthpy/">
        <img src="https://img.shields.io/pypi/pyversions/modrinthpy">
    </a>
</div>

> [!WARNING]
> This library is under development and may contain errors!

**ModrinthPy** is an unofficial Python API client for interacting with the [Modrinth](https://modrinth.com/) platform.

## Installation 

You can install the library using pip:
```bash
pip install modrinthpy
```

## Usage Examples 

### Mod Search 

You can easily search for mods on Modrinth by name, ID or filters:

```python
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
```

### Getting information about project

You can also get information about a particular project by knowing its ID or Slug:

```python
from modrinthpy import ModrinthClient

client = ModrinthClient()

async def get():
    mod = await client.get_project(slug="sodium")
    print(mod.title)
    print(mod.description)
    print(mod.downloads)

client.run(get())
```

<!-- ### Downloading a mod file 

You can find available downloads and download them:

```python
...
```-->

<!--### Features - Search for mods by name, filters and categories. - Get detailed information about mods. - Download mods and mod versions. - Support for various parameters and filters for more accurate search.

## Documentation

[Coming soon..]
<!--Full documentation and examples of use are available at [GitHub Pages](https://github.com/mrf0rtuna4/modrinthpy/wiki).-->

## Contributing

All forms of participation in the project are welcome! If you find a bug or want to suggest improvements, create an `Issue` or make a `Pull Request`.

1. Forks Repository
2. Create a new branch for your changes (`git checkout -b feature/YourFeature`)
3. Make the changes
4. Open Pull Request

## License

This project is licensed under the MIT license. For more details see file [LICENSE](https://github.com/mrf0rtuna4/modrinthpy/blob/main/LICENSE).
