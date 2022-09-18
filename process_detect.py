# import time
import ctypes

def lock_sys():
    ctypes.windll.user32.LockWorkStation()

def get_running_processes():
    import subprocess

    cmd = 'powershell "gps | where {$_.MainWindowTitle} | select ProcessName'
    proc = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE)
    to_skip, running = 0, 0

    for i in proc.stdout:
        if (to_skip <= 2):
            to_skip += 1
            continue
        else:
            if (i.strip()):
                running += 1
    return running

def start_detect():
    starting_proc = 0
    while True:
        res = get_running_processes()
        if starting_proc == 0:
            starting_proc = res

        if res > starting_proc:
            starting_proc = res
            yield True
        elif res < starting_proc:
            starting_proc = res

        # time.sleep(2)

if(__name__ == '__main__'):
    lock_sys()