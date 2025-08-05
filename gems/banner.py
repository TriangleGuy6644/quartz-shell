import os

ALIASES = {
    "bn": "banner",
    'logo': 'banner'
}

def main(args):
    banner_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'banner.txt')
    
    try:
        with open(banner_path, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print("Banner file not found at /assets/banner.txt.")
    except Exception as e:
        print(f"Error reading banner: {e}")
