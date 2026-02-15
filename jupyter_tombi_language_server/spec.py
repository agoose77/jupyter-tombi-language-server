import shutil
import importlib.resources
import json
from . import schema


def tombi(app):
    tombi_lsp_path = shutil.which("tombi")

    if not tombi_lsp_path:
        return {}

    tombi_schema = json.loads(importlib.resources.read_text(schema, "tombi.json"))

    return {
        "tombi-language-server": {
            "version": 2,
            "argv": [tombi_lsp_path, "lsp"],
            "languages": ["toml"],
            "mime_types": ["application/toml"],
            "config_schema": tombi_schema,
            "workspace_configuration": {
                "serverSettings": {
                    "files": None,
                }
            },
        }
    }
