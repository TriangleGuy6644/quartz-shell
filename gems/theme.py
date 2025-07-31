import os
import json
import sys

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')

# Ensure shell folder is in sys.path to import themes properly
shell_dir = os.path.join(os.path.dirname(__file__), '..', 'shell')
if shell_dir not in sys.path:
    sys.path.insert(0, shell_dir)

from shell.themes import THEMES, load_config, save_config

def main(args):
    cfg = load_config()
    current_theme = cfg.get('theme', 'quartz')
    # Debug print, remove if not needed
    # print(f"Current theme from config: {current_theme}")

    if not args or args[0] == 'list':
        print("Available themes:")
        for theme_name in THEMES.keys():
            marker = " *" if theme_name == current_theme else "  "
            current = " (current)" if theme_name == current_theme else ""
            print(f"{marker} {theme_name}{current}")
        return

    if args[0] == 'set':
        if len(args) < 2:
            print("Usage: theme set [themename]")
            return
        new_theme = args[1]
        if new_theme not in THEMES:
            print(f"Theme '{new_theme}' not found. Use 'theme list' to see available themes.")
            return
        cfg['theme'] = new_theme
        save_config(cfg)
        print(f"Theme changed to '{new_theme}'. Restart the shell to see the effect.")
    else:
        print("Unknown subcommand. Use 'list' or 'set'.")
