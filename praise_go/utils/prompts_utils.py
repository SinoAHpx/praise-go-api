import os
import yaml

def read_prompt_source() -> str:
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        yaml_path = os.path.join(current_dir, "..", "prompts", "prompts.yaml")
        
        with open(yaml_path, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        raise FileNotFoundError(f"prompts.yaml file not found at: {yaml_path}")

def load_prompt(name: str):
    content = read_prompt_source()
    yaml_data = yaml.load(content, Loader=yaml.SafeLoader)
    
    matching_prompts = [p for p in yaml_data["prompts"] if p["name"] == name]
    
    if not matching_prompts:
        raise ValueError(f"No prompt found with name: {name}")    
    return matching_prompts[0]["value"]

# print(load_prompt('Praisia'))