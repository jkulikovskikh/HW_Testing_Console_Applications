import subprocess
import string

'''
Задание 1
'''

def check_command(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0 and text in out:
        print('True')
    else:
        print('False')

'''
Задание 2
'''

def check_output(text, is_delete_punctuation=False):
    result = subprocess.run('cat /etc/os-release', shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout

    if is_delete_punctuation:
        for smbl in out:
            if smbl in string.punctuation:
                out = out.replace(smbl, '')

    if result.returncode == 0:
        if text in out:
            print('SUCCESS')
        else:
            print('FAIL')
