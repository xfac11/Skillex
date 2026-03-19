import json

def load_config() -> tuple:
    """Returns a tuple (name, id) or None if no config file was found"""
    with open("config.json", "r") as f:
        data = json.load(f)
        name = data["current_user"]
        id = data["current_user_id"]
        return (name, id)
    return None

def save_config(name, id) -> bool:
    """Writes name and id to a file called config.json"""
    data = {
        "current_user" : name,
        "current_user_id" : id,
    }
    json_str = json.dumps(data, indent=4)
    with open("config.json", "w") as f:
        f.write(json_str)
        return True
    return False