from pathlib import Path

default_manifest = """{
    "aidoc": "AI_DOCUMENT_LOADER"
}
"""


def write_default_manifest(filepath):
    filepath = Path(filepath)

    if not filepath.parent.is_dir():
        print(f"Parent directory doesn't exists for {filepath}")
        return
    
    if filepath.is_file():
        print(f"File already exists at {filepath}")
        return
    
    try:
        with open(filepath, 'w') as file:
            file.write(default_manifest)
    
    except IOError as e:
        print(f"Error writing default inventory manifest: {e}")