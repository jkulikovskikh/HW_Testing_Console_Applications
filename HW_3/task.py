import subprocess
import zlib

def check_command(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0 and text in out:
        return True
    else:
        return False

def get_hash(path):
    with open(path, 'rb') as f:
        data = f.read()
    return hex(zlib.crc32(data))