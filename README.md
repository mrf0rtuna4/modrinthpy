# ModrinthPy

[![PyPI version](https://img.shields.io/pypi/v/modrinthpy)](https://pypi.org/project/modrinthpy/)
[![License](https://img.shields.io/github/license/mrf0rtuna4/modrinthpy)](https://github.com/mrf0rtuna4/modrinthpy/blob/main/LICENSE)
[![Python version](https://img.shields.io/pypi/pyversions/modrinthpy)](https://pypi.org/project/modrinthpy/)

**ModrinthPy** — это неофициальный Python API клиент для взаимодействия с платформой [Modrinth](https://modrinth.com/), которая позволяет пользователям находить и загружать моды для Minecraft.

## Установка

Установить библиотеку можно с помощью pip:

```bash
pip install modrinthpy
```

## Примеры использования

### Поиск модов

Вы можете легко искать моды на Modrinth по названию, идентификатору или фильтрам:

```python
import modrinthpy

# Инициализация клиента
client = modrinthpy.Client()

# Поиск мода по названию
results = client.search_projects("Sodium")
for project in results.get("hits", []):
    print(f"{project.get('title')} ({project.get('id')})")
```

<!--### Получение информации о моде--

Вы также можете получить информацию о конкретном моде, зная его идентификатор:

```python
mod = client.get_mod("AANobbMI")
print(mod.title)
print(mod.description)
print(mod.downloads)
```

### Скачивание файла мода

Вы можете найти доступные файлы для скачивания и скачать их:

```python
mod = client.get_mod("AANobbMI")
for version in mod.versions:
    print(version.filename)
    # Скачивание файла
    client.download_file(version, path="./downloads/")
```-->

<!--## Возможности

- Поиск модов по названию, фильтрам и категориям.
- Получение подробной информации о модах.
- Скачивание модов и версий модов.
- Поддержка различных параметров и фильтров для более точного поиска.-->

## Документация

[Coming soon..]
<!--Полная документация и примеры использования доступны на [GitHub Pages](https://github.com/mrf0rtuna4/modrinthpy/wiki).-->

## Contributing

Приветствуются все формы участия в проекте! Если вы нашли ошибку или хотите предложить улучшения, создайте `Issue` или сделайте `Pull Request`.

1. Форкните репозиторий
2. Создайте новую ветку для своих изменений (`git checkout -b feature/YourFeature`)
3. Внесите изменения
4. Откройте Pull Request

## Лицензия

Этот проект лицензирован под лицензией MIT. Подробнее см. файл [LICENSE](https://github.com/mrf0rtuna4/modrinthpy/blob/main/LICENSE).
