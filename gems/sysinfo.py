ALIASES = {
    'neofetch': 'sysinfo',
    'si': 'sysinfo',
    'fastfetch': 'sysinfo'
}


import platform
import socket
import psutil
import time
import subprocess

ASCII_ART = r"""
   ____  __  _____    ____  ___________
  / __ \/ / / /   |  / __ \/_  __/__  /
 / / / / / / / /| | / /_/ / / /    / / 
/ /_/ / /_/ / ___ |/ _, _/ / /    / /__
\___\_\____/_/  |_/_/ |_| /_/    /____/
        
"""

def get_uptime():
    boot_time = psutil.boot_time()
    now = time.time()
    uptime_seconds = int(now - boot_time)
    hours, remainder = divmod(uptime_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}h {minutes}m {seconds}s"

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "Unavailable"

def get_gpu():
    try:
        # Windows: Use WMIC
        if platform.system() == "Windows":
            result = subprocess.check_output("wmic path win32_VideoController get name", shell=True)
            lines = result.decode().split('\n')
            gpus = [line.strip() for line in lines if line.strip() and "Name" not in line]
            return ', '.join(gpus) if gpus else "Unknown"

        # Linux: Try lspci
        elif platform.system() == "Linux":
            result = subprocess.check_output("lspci | grep -i vga", shell=True)
            return result.decode().strip()

        else:
            return "Unsupported OS"
    except:
        return "Unavailable"

def main(args):
    print(ASCII_ART)
    print(f"{'OS:':<12} {platform.system()} {platform.release()}")
    print(f"{'Hostname:':<12} {socket.gethostname()}")
    print(f"{'IP Addr:':<12} {get_ip()}")
    print(f"{'Uptime:':<12} {get_uptime()}")
    print(f"{'Python:':<12} {platform.python_version()}")
    print(f"{'CPU:':<12} {platform.processor() or 'N/A'}")

    try:
        mem = psutil.virtual_memory()
        used = round(mem.used / (1024**3), 2)
        total = round(mem.total / (1024**3), 2)
        print(f"{'Memory:':<12} {used}GB / {total}GB")
    except:
        print(f"{'Memory:':<12} Not available")

    print(f"{'GPU:':<12} {get_gpu()}")

