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
    "gold": {
    'prefix': 'bold #ffd700',  # Gold
    'arrow': 'bold #ffec8b',   # Light gold
    'input': '#ffe066',
    'completion-menu.completion': 'bg:#fff8dc #2a2a2a',  # Cornsilk
    'completion-menu.completion.current': 'bg:#ffd700 #000000',
    'completion-menu.meta': 'bg:#fffacd #2a2a2a',  # LemonChiffon
    'completion-menu.meta.completion.current': 'bg:#ffd700 #000000',
    'banner': '#ffd700',
    'greeting': '#ffd700',
    },
    "spamton": {
    'prefix': 'bold #ff69b4',  # HotPink
    'arrow': 'bold #ffff00',  # Yellow
    'input': '#ffb6c1',  # LightPink
    'completion-menu.completion': 'bg:#fffacd #2a2a2a',
    'completion-menu.completion.current': 'bg:#ff69b4 #ffffff',
    'completion-menu.meta': 'bg:#ffecb3 #2a2a2a',
    'completion-menu.meta.completion.current': 'bg:#ffff00 #000000',
    'banner': '#ff69b4',
    'greeting': '#ffff00',
    },
    "blackquartz": {
    'prefix': 'bold #dcdcdc',  # Gainsboro
    'arrow': 'bold #c0c0c0',   # Silver
    'input': '#a9a9a9',        # DarkGray
    'completion-menu.completion': 'bg:#2a2a2a #c0c0c0',
    'completion-menu.completion.current': 'bg:#808080 #ffffff',
    'completion-menu.meta': 'bg:#3a3a3a #c0c0c0',
    'completion-menu.meta.completion.current': 'bg:#808080 #ffffff',
    'banner': '#c0c0c0',
    'greeting': '#a9a9a9',
    },
    "obsidian": {
    'prefix': 'bold #444444',
    'arrow': 'bold #666666',
    'input': '#888888',
    'completion-menu.completion': 'bg:#1a1a1a #aaaaaa',
    'completion-menu.completion.current': 'bg:#333333 #ffffff',
    'completion-menu.meta': 'bg:#222222 #aaaaaa',
    'completion-menu.meta.completion.current': 'bg:#333333 #ffffff',
    'banner': '#666666',
    'greeting': '#444444',
    },
    "darkcrystal": {
    'prefix': 'bold #9370db',  # MediumPurple
    'arrow': 'bold #8a2be2',   # BlueViolet
    'input': '#ba55d3',        # MediumOrchid
    'completion-menu.completion': 'bg:#2e003e #dda0dd',  # dark purple bg
    'completion-menu.completion.current': 'bg:#8a2be2 #ffffff',
    'completion-menu.meta': 'bg:#4b0082 #dda0dd',        # Indigo
    'completion-menu.meta.completion.current': 'bg:#8a2be2 #ffffff',
    'banner': '#9370db',
    'greeting': '#dda0dd',     # Plum
    },
    "matrix": {
    'prefix': 'bold #00ff00',  # Bright Green
    'arrow': 'bold #00cc00',   # Slightly dimmer green
    'input': '#00aa00',
    'completion-menu.completion': 'bg:#000000 #00ff00',
    'completion-menu.completion.current': 'bg:#003300 #00ff00',
    'completion-menu.meta': 'bg:#001a00 #00ff00',
    'completion-menu.meta.completion.current': 'bg:#004400 #00ff00',
    'banner': '#00ff00',
    'greeting': '#00ff00',
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
