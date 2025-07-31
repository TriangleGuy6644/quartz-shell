import os
from PIL import Image, ImageOps
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter, PathCompleter, NestedCompleter

TOOLS = {
    'invert': 'Invert colors',
    'grayscale': 'Convert to grayscale',
    'thumbnail': 'Create a 128x128 thumbnail',
    'rotate': 'Rotate 90 degrees clockwise',
}

def process_image(tool, image_path):
    if not os.path.isfile(image_path):
        print(f"File not found: {image_path}")
        return

    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    if tool == 'invert':
        if img.mode == 'RGBA':
            r, g, b, a = img.split()
            rgb_image = Image.merge("RGB", (r, g, b))
            inverted = ImageOps.invert(rgb_image)
            img = Image.merge("RGBA", (*inverted.split(), a))
        elif img.mode == 'RGB':
            img = ImageOps.invert(img)
        else:
            print("Invert only supports RGB or RGBA images.")
            return

        out_path = _get_output_path(image_path, 'invert')

    elif tool == 'grayscale':
        img = img.convert('L')
        out_path = _get_output_path(image_path, 'grayscale')

    elif tool == 'thumbnail':
        img.thumbnail((128, 128))
        out_path = _get_output_path(image_path, 'thumbnail')

    elif tool == 'rotate':
        img = img.rotate(-90, expand=True)
        out_path = _get_output_path(image_path, 'rotate')

    else:
        print(f"Unknown tool: {tool}")
        return

    img.save(out_path)
    print(f"Processed image saved to: {out_path}")

def _get_output_path(original_path, tool_name):
    base, ext = os.path.splitext(original_path)
    return f"{base}_{tool_name}{ext}"

def main(args):
    session = PromptSession()

    # If args given, use them; else prompt interactively
    if len(args) >= 2:
        tool = args[0].lower()
        image_path = args[1]
    else:
        tool_completer = WordCompleter(list(TOOLS.keys()), ignore_case=True)
        tool = session.prompt("Tool: ", completer=tool_completer).lower()

        path_completer = PathCompleter(file_filter=lambda f: f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')))
        image_path = session.prompt("Image path: ", completer=path_completer)

    if tool not in TOOLS:
        print(f"Invalid tool. Available tools: {', '.join(TOOLS.keys())}")
        return

    process_image(tool, image_path)
