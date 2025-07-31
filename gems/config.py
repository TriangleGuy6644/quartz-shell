import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')

def load_config():
    try:
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def save_config(cfg):
    try:
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(cfg, f, indent=4)
    except Exception as e:
        print(f"Failed to save config: {e}")
 
def main(args):
    if not args:
        print("Usage: config [set|get] [key] [value]")
        return

    action = args[0].lower()
    cfg = load_config()

    if action == "set":
        if len(args) < 3:
            print("Usage: config set [key] [value]")
            return
        key, value = args[1], args[2]
        cfg[key] = value
        save_config(cfg)
        print(f"Config '{key}' set to '{value}'")
    elif action == "get":
        if len(args) < 2:
            print("Usage: config get [key]")
            return
        key = args[1]
        print(f"{key} = {cfg.get(key, '(not set)')}")
    else:
        print("Unknown action. Use 'set' or 'get'.")
