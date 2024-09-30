from functools import wraps
from .exceptions import MissingArguments

def check_project(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        project_id = kwargs.get('id', None)
        slug = kwargs.get('slug', None)
        
        if project_id is None and slug is None:
            raise MissingArguments('id', 'slug')
        
        return func(*args, **kwargs)
    return wrapper
