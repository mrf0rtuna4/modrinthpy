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
import asyncio
from modrinthpy import AsyncModrinthClient
from modrinthpy.models import Project

async def main():
    project: 'Project'
    async with AsyncModrinthClient() as client:
        projects = await client.search_projects("sodium")
        for project in projects:
            print(project)

asyncio.run(main())
```

<!--### Getting information about fashion--

You can also get information about a particular mod by knowing its ID:

```python
mod = client.get_mod("AANobbMI")
print(mod.title)
print(mod.description)
print(mod.downloads)
```

### Downloading a mod file 

You can find available downloads and download them:

```python
mod = client.get_mod("AANobbMI")
for version in mod.versions:
    print(version.filename)
    
    client.download_file(version, path="./downloads/")
```-->

<!--### Features - Search for mods by name, filters and categories. - Get detailed information about mods. - Download mods and mod versions. - Support for various parameters and filters for more accurate search.

## Документация

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
