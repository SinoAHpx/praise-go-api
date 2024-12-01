import os
import yaml

def load_prompt(name: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_path = os.path.join(current_dir, "..", "prompts", "prompts.yaml")
    
    try:
        with open(yaml_path, "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        
        matching_prompts = [p for p in yaml_data["prompts"] if p["name"] == name]
        if not matching_prompts:
            raise ValueError(f"No prompt found with name: {name}")
            
        return matching_prompts[0]["value"]
    except FileNotFoundError:
        raise FileNotFoundError(f"prompts.yaml file not found at: {yaml_path}")