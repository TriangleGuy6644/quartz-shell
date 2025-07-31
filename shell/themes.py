import json
import os
from prompt_toolkit.styles import Style

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')

THEMES = {
    "quartz": {
        'prefix': 'bold #40e0d0',
        'arrow': 'bold #a0f0f0',
        'input': '#66ccee',
        'completion-menu.completion': 'bg:#e0f7f7 #2a2a2a',
        'completion-menu.completion.current': 'bg:#40c0c0 #ffffff',
        'completion-menu.meta': 'bg:#b0e0e6 #2a2a2a',
        'completion-menu.meta.completion.current': 'bg:#40c0c0 #ffffff',
        'banner': '#40e0d0',      # Turquoise
        'greeting': '#40e0d0',    # Turquoise
    },
    "rosequartz": {
        'prefix': 'bold #ff7f7f',
        'arrow': 'bold #ffb6b6',
        'input': '#ff9999',
        'completion-menu.completion': 'bg:#ffe5e5 #2a2a2a',
        'completion-menu.completion.current': 'bg:#ff7f7f #ffffff',
        'completion-menu.meta': 'bg:#ffc2c2 #2a2a2a',
        'completion-menu.meta.completion.current': 'bg:#ff7f7f #ffffff',
        'banner': '#ff7f7f',      # Pinkish
        'greeting': '#ff7f7f',
    },
    "smokyquartz": {
        'prefix': 'bold #a0522d',
        'arrow': 'bold #c08060',
        'input': '#b07a6f',
        'completion-menu.completion': 'bg:#f0e6e0 #2a2a2a',
        'completion-menu.completion.current': 'bg:#a0522d #ffffff',
        'completion-menu.meta': 'bg:#c0a080 #2a2a2a',
        'completion-menu.meta.completion.current': 'bg:#a0522d #ffffff',
        'banner': '#a0522d',      # Brownish
        'greeting': '#a0522d',
    },
}


def load_config():
    try:
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except Exception:
        return {}

def save_config(cfg):
    try:
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(cfg, f, indent=4)
    except Exception as e:
        print(f"Failed to save config: {e}")
