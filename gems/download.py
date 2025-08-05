ALIASES = {
    'dl' : 'download'
}

import os
import subprocess
import sys

def main(args):
    if not args:
        print("Usage: download [youtube/tiktok/other URL]")
        return

    url = args[0]

    # Path to downloads folder (relative to this gem file)
    downloads_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'downloads'))
    os.makedirs(downloads_dir, exist_ok=True)

    print("Downloading...")

    try:
        # Run yt-dlp with output template to downloads folder
        subprocess.run([
            sys.executable, '-m', 'yt_dlp',  # run yt-dlp module with current Python interpreter
            url,
            '-o', os.path.join(downloads_dir, '%(title)s.%(ext)s'),
            '--no-progress',  # optional: hides progress bar for cleaner output
        ], check=True)

        print(f"Done! Saved to {downloads_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Download failed: {e}")
    except FileNotFoundError:
        print("yt-dlp is not installed. Please install it with 'pip install yt-dlp'")

