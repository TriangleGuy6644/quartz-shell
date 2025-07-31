import os
import getpass
import datetime
import importlib
import glob
import json
from prompt_toolkit import PromptSession, print_formatted_text, HTML
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.styles import Style
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.formatted_text import HTML
from html import escape as escape_html

from shell.themes import THEMES, load_config, save_config

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')

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

# Special subcommands for image gem:
IMAGE_SUBCOMMANDS = ['invert', 'grayscale', 'blur', 'rotate', 'resize']

def get_all_commands():
    builtin_cmds = ['help', '?', 'exit', 'quit', 'clear', 'config', 'theme', 'image']
    return builtin_cmds + list(aliases.keys()) + list_available_gems()

class QuartzCompleter(Completer):
    def get_completions(self, document, complete_event):
        text_before_cursor = document.text_before_cursor.lstrip()
        parts = text_before_cursor.split()

        # If starting the command (first word)
        if len(parts) == 0 or (len(parts) == 1 and not text_before_cursor.endswith(' ')):
            # Complete main commands + aliases + gems
            for cmd in get_all_commands():
                if cmd.startswith(parts[0] if parts else ''):
                    yield Completion(cmd, start_position=-len(parts[0]) if parts else 0)
        elif parts[0].lower() == 'image':
            # If inside image command, complete image subcommands or file paths
            if len(parts) == 1:
                # Complete image subcommands
                for sub in IMAGE_SUBCOMMANDS:
                    if sub.startswith(''):
                        yield Completion(sub, start_position=0)
            elif len(parts) == 2:
                # Complete image subcommands filtered by user input
                for sub in IMAGE_SUBCOMMANDS:
                    if sub.startswith(parts[1]):
                        yield Completion(sub, start_position=-len(parts[1]))
            elif len(parts) == 3:
                # Complete file path for third arg (image path)
                # We'll do simple filename completion from current directory
                prefix = parts[2]
                dirname = os.path.dirname(prefix) or '.'
                base = os.path.basename(prefix)
                try:
                    for fname in os.listdir(dirname):
                        if fname.startswith(base):
                            full_path = os.path.join(dirname, fname)
                            display = fname + ('/' if os.path.isdir(full_path) else '')
                            yield Completion(display, start_position=-len(base))
                except Exception:
                    pass
        else:
            # For other commands, no special completion for now
            pass

config = load_config()
prefix = config.get("prefix", ">>")
current_theme_name = config.get("theme", "quartz")
current_theme = THEMES.get(current_theme_name, THEMES["quartz"])

style = Style.from_dict({
    'prefix': current_theme['prefix'],
    'input': current_theme['input'],
    'completion-menu.completion': current_theme['completion-menu.completion'],
    'completion-menu.completion.current': current_theme['completion-menu.completion.current'],
    'completion-menu.meta': current_theme['completion-menu.meta'],
    'completion-menu.meta.completion.current': current_theme['completion-menu.meta.completion.current'],
})

session = PromptSession(completer=QuartzCompleter(), style=style)

class InputLexer(Lexer):
    def lex_document(self, document):
        text = document.text
        def get_line(lineno):
            return [('class:input', text)]
        return get_line

def get_colored_prompt():
    # Just prefix text colored by theme
    return HTML(f'<prefix>{prefix} </prefix>')

def printbanner():
    banner_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'banner.txt')
    try:
        with open(banner_path, 'r', encoding='utf-8') as f:
            banner_text = f.read()
        color = current_theme.get('banner', '#40e0d0')
        safe_text = escape_html(banner_text)
        print_formatted_text(HTML(f'<ansifg="{color}">{safe_text}</ansifg>'))
    except FileNotFoundError:
        print_formatted_text(HTML(f'<ansired>Banner not found. Please ensure the file exists at: {banner_path}</ansired>'))

def get_greeting():
    hour = datetime.datetime.now().hour
    user = getpass.getuser()

    greeting_color = current_theme.get('greeting', '#40e0d0')

    if 5 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 17:
        greeting = "Good Afternoon"
    elif 17 <= hour < 21:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"

    return HTML(f'<ansifg="{greeting_color}">{greeting}</ansifg>, <b>{escape_html(user)}</b>!\nWelcome back to <ansifg="{greeting_color}">Quartz Shell</ansifg>!\nType <b><ansicyan>?</ansicyan></b> for commands.')

def parse_command(line):
    parts = line.strip().split()
    if not parts:
        return None, []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args

def dispatch_command(cmd, args):
    global prefix, current_theme_name, current_theme, style, session

    cmd = aliases.get(cmd, cmd)  # support aliases

    if cmd in ('exit', 'quit', 'bye', 'nomoreshellpls'):
        print_formatted_text(HTML('<ansigreen>Goodbye!</ansigreen>'))
        return False
    elif cmd in ('help', 'h', 'cmds', 'commands', '?'):
        print_formatted_text(HTML('<b><ansicyan>Commands:</ansicyan></b> help, exit, clear, config, theme, plus all gems...'))
    elif cmd == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cmd == '':
        pass
    else:
        try:
            gem_module = importlib.import_module(f'gems.{cmd}')
            gem_module.main(args)

            # reload config if config or theme changed
            if cmd in ('config', 'theme'):
                new_cfg = load_config()
                # Update prefix
                prefix = new_cfg.get("prefix", prefix)
                # Update theme and style
                new_theme_name = new_cfg.get("theme", current_theme_name)
                if new_theme_name != current_theme_name:
                    current_theme_name = new_theme_name
                    current_theme = THEMES.get(current_theme_name, THEMES["quartz"])
                    style = Style.from_dict({
                        'prefix': current_theme['prefix'],
                        'input': current_theme['input'],
                        'completion-menu.completion': current_theme['completion-menu.completion'],
                        'completion-menu.completion.current': current_theme['completion-menu.completion.current'],
                        'completion-menu.meta': current_theme['completion-menu.meta'],
                        'completion-menu.meta.completion.current': current_theme['completion-menu.meta.completion.current'],
                    })
                    session.style = style

        except ModuleNotFoundError:
            print_formatted_text(HTML(f'<ansired>Command \'{cmd}\' not found. Type \'?\' for help.</ansired>'))
        except AttributeError:
            print_formatted_text(HTML(f'<ansired>Gem \'{cmd}\' does not have a main() function. Check gem implementation.</ansired>'))
        except Exception as e:
            print_formatted_text(HTML(f'<ansired>Error while executing \'{cmd}\': {escape_html(str(e))}</ansired>'))
    return True


def shell_loop():
    printbanner()
    print_formatted_text(get_greeting())

    running = True
    while running:
        try:
            line = session.prompt(get_colored_prompt(), lexer=InputLexer())
            cmd, args = parse_command(line)
            if cmd is None:
                continue
            running = dispatch_command(cmd, args)
        except KeyboardInterrupt:
            print_formatted_text(HTML('\n<ansiyellow>Interrupted. Type \'exit\' to quit.</ansiyellow>'))
        except EOFError:
            print_formatted_text(HTML('\n<ansiyellow>EOF received. Exiting.</ansiyellow>'))
            break

if __name__ == "__main__":
    shell_loop()
