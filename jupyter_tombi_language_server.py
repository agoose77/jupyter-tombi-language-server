import shutil


def tombi(app):
    tombi_lsp_path = shutil.which("tombi")

    if not tombi_lsp_path:
        return {}

    return {
        "tombi-language-server": {
            "version": 2,
            "argv": [tombi_lsp_path, "lsp"],
            "languages": ["toml"],
            "mime_types": ["application/toml"],
        }
    }
