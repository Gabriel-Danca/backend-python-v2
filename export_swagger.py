import json
import yaml
import sys
import os  
from app.main import app

def export_openapi():
    openapi_data = app.openapi()

    output_dir = "docs"

    os.makedirs(output_dir, exist_ok=True)

    json_path = os.path.join(output_dir, "openapi.json")
    yaml_path = os.path.join(output_dir, "openapi.yaml")

    with open(json_path, "w") as f:
        json.dump(openapi_data, f, indent=2)

    with open(yaml_path, "w") as f:
        yaml.dump(openapi_data, f, sort_keys=False)

if __name__ == "__main__":
    export_openapi()