from task import check_command
import pytest
import zlib

folder_in = '/home/user/folder_in'
folder_out = '/home/user/folder_out'
folder_ex = '/home/user/folder_ex'


def test_step_1():
    assert check_command(f'cd {folder_in}; 7z a {folder_out}/archive_1', 'Everything is Ok')

def test_step_2():
    assert check_command(f'cd {folder_out}; 7z rn archive_1 file_1.txt file_100.txt', 'Everything is Ok')

def test_step_3():
    assert check_command(f'cd {folder_out};  7z i archive_1', ' 0  ED  6F00181 AES256CBC')

def test_step_4():
    with open(f'{folder_out}/archive_1.7z', 'rb') as f:
        data = f.read()
    crc32 = zlib.crc32(data)
    assert check_command(f'cd {folder_out}; 7z h archive_1.7z', str(hex(crc32).upper()[2:]))

def test_step_5():
    assert check_command(f'cd {folder_out}; 7z x archive_1.7z', 'Everything is Ok')


if __name__ == '__main__':
    pytest.main(['-vv'])
