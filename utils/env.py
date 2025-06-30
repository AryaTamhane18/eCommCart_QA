import os
from dotenv import load_dotenv

load_dotenv()


def get_env_variable(key: str, required: bool = True):
    value = os.getenv(key)
    if required and not value:
        raise RuntimeError(f"Environment variable '{key}' not found.")
    return value


def is_truthy(bool_as_string: str):
    return str(bool_as_string).lower() == "true"
