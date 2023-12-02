import pytest
import yaml
from task import check_command
from datetime import datetime
import random, string
import subprocess

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture(scope='class')
def make_folders():
    return check_command(f'mkdir -p {data.get("folder_in")} {data.get("folder_out")} {data.get("folder_ex")}', '')


@pytest.fixture(scope='class')
def delete_folders():
    yield
    return check_command(f'rm -rf {data.get("folder_in")} {data.get("folder_out")} {data.get("folder_ex")}', '')


@pytest.fixture(scope='class')
def make_files():
    list_off_files = []
    for i in range(data.get("count")):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if check_command(f'cd {data.get("folder_in")}; dd if=/dev/urandom of={filename} bs={data.get("bs")} count=1', ''):
            list_off_files.append(filename)
    return list_off_files


@pytest.fixture(scope='function')
def write_stat():
    with open('stat.txt', 'a', encoding='utf-8') as f:
        f.write('start: ' + str(datetime.now().time()) + ' ')
        result = subprocess.run('cat /proc/loadavg', shell=True, stdout=subprocess.PIPE, encoding='utf-8')
        f.write('/proc/loadavg: ' + result.stdout[:-1] + ' ')
        f.write('count: ' + str(data.get("count")) + ' ')
        f.write('size: ' + str(data.get("bs")) + ' ')
        yield
        f.write('finish: ' + str(datetime.now().time()) + '\n')