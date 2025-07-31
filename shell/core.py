import os
import getpass
import datetime
import importlib
import glob
import json
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style
from prompt_toolkit.lexers import Lexer

# Import themes and config helpers
from themes import THEMES, load_config, save_config

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')

config = load_config()
current_theme_name = config.get("theme", "quartz")
theme = THEMES.get(current_theme_name, THEMES["quartz"])  # fallback theme

prefix = config.get("prefix", ">>")

aliases = {
    'calc': 'calculator'
}

def list_available_gems():
    gems_path = os.path.join(os.path.dirname(__file__), '..', 'gems')
    gem_files = glob.glob(os.path.join(gems_path, '*.py'))
    commands = [
        os.path.splitext(os.path.basename(f))[0]
        for f in gem_files
        if not os.path.basename(f).startswith('_')
    ]
    return commands

def get_all_commands():
    builtin_cmds = ['help', '?', 'exit', 'quit', 'clear', 'config', 'theme']
    return builtin_cmds + list(aliases.keys()) + list_available_gems()

completer = WordCompleter(get_all_commands(), ignore_case=True)

style = Style.from_dict(theme)

session = PromptSession(completer=completer, style=style)

class InputLexer(Lexer):
    def lex_document(self, document):
        text = document.text
        def get_line(lineno):
            return [('class:input', text)]
        return get_line

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return f"{r};{g};{b}"

def printbanner():
    banner_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'banner.txt')
    try:
        with open(banner_path, 'r', encoding='utf-8') as f:
            banner_text = f.read()
            color_code = theme.get('banner', '#40e0d0')
            rgb = hex_to_rgb(color_code)
            print(f"\033[38;2;{rgb}m{banner_text}\033[0m")
    except FileNotFoundError:
        print(f"\033[91mBanner not found. Please ensure the file exists at: {banner_path}\033[0m")

def get_greeting():
    hour = datetime.datetime.now().hour
    user = getpass.getuser()

    if 5 <= hour < 12:
        greet = "Good Morning"
    elif 12 <= hour < 17:
        greet = "Good Afternoon"
    elif 17 <= hour < 21:
        greet = "Good Evening"
    else:
        greet = "Good Night"

    color_code = theme.get('greeting', '#40e0d0')
    rgb = hex_to_rgb(color_code)

    return f"\033[38;2;{rgb}m{greet}\033[0m, \033[1m{user}\033[0m! \nWelcome back to \033[38;2;{rgb}mQuartz Shell\033[0m!\nType \033[1;96m'?' \033[0mfor commands."

def get_colored_prompt():
    return HTML(f'<prefix>{prefix}</prefix> ')

def parse_command(line):
    parts = line.strip().split()
    if not parts:
        return None, []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args

def dispatch_command(cmd, args):
    global prefix, theme, style, session

    cmd = aliases.get(cmd, cmd)

    if cmd in ('exit', 'quit', 'bye', 'nomoreshellpls'):
        print("\033[92mGoodbye!\033[0m")
        return False
    elif cmd in ('help', 'h', 'cmds', 'commands', '?'):
        print("\033[1;96mCommands:\033[0m help, exit, clear, config, theme, plus all gems...")
    elif cmd == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cmd == '':
        pass
    else:
        try:
            gem_module = importlib.import_module(f'gems.{cmd}')
            gem_module.main(args)

            # Reload config after config or theme commands
            if cmd in ('config', 'theme'):
                new_cfg = load_config()
                prefix = new_cfg.get("prefix", prefix)
                current_theme_name = new_cfg.get("theme", current_theme_name)
                theme = THEMES.get(current_theme_name, THEMES["quartz"])
                # update style and session with new theme
                style = Style.from_dict(theme)
                session.style = style

        except ModuleNotFoundError:
            print(f"\033[91mCommand '{cmd}' not found. Type '?' for help.\033[0m")
        except AttributeError:
            print(f"\033[91mGem '{cmd}' does not have a main function. Please check the gem implementation.\033[0m")
        except Exception as e:
            print(f"\033[91mAn error occurred while executing '{cmd}': {e}\033[0m")
    return True

def shell_loop():
    printbanner()
    print(get_greeting())
    running = True
    while running:
        try:
            line = session.prompt(get_colored_prompt(), lexer=InputLexer())
            cmd, args = parse_command(line)
            if cmd is None:
                continue
            running = dispatch_command(cmd, args)
        except KeyboardInterrupt:
            print("\n\033[93mInterrupted. Type 'exit' to quit.\033[0m")
        except EOFError:
            print("\n\033[93mEOF received. Exiting.\033[0m")
            break

if __name__ == "__main__":
    shell_loop()
