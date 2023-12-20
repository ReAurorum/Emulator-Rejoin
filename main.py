import subprocess
import time
import ctypes, sys
import time
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_emulators():
    command = "E:\\LDPlayer\\LDPlayer9\\ldconsole.exe list2"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    output = output.decode('utf-8')
    error = error.decode('utf-8')

    if process.returncode == 0:
        #print("Output:\n", output)
        return output
    else:
        print("Error:\n", error)
def openLD(id):
    ld = "E:\LDPlayer\LDPlayer9\ldconsole.exe" + (" launch --index {0}").format(id)
    subprocess.run(ld,shell=True)
def convert(data):
    get_lines = data.strip().split('\n')
    headers = ["Index", "Title", "Top Window Handle", "Bind Window Handle", "Android Started", "PID", "PID of Vbox", "Resolution Width", "Resolution Height", "Unknown"]
    __list = []

    for i in get_lines:
        v = i.split(',')
        v2 = dict(zip(headers, v))
        __list.append(v2)

    return __list


def install_autorejoin(id): 
    ld = "E:\LDPlayer\LDPlayer9\ldconsole.exe" + (" installapp --index {0} --filename " +os.path.abspath(__file__) + "hi.apk").format(id)
    subprocess.run(ld,shell=True)
def tranduythieunang(id):
    ld = "E:\LDPlayer\LDPlayer9\ldconsole.exe" + (" runapp --index {0} --packagename com.example.tranduysv12312").format(id)
    subprocess.run(ld,shell=True)

def wait_emulator(id):
    Started = False
    while Started == False:
        mydata =convert(get_emulators())
        if mydata[int(id)]["Android Started"] == "1":
            Started = True
        time.sleep(1)

    print("Emulator " + id + " Started, Running Auto Join Roblox")
    time.sleep(1)
if __name__ == "__main__" :

    需要打开 = [1,2,3,4,5,6] #[List Of Emulator you want to open][Index Starts From 0]
    if is_admin():
        data_list =convert(get_emulators())
        for data in data_list:
            print(data)
            if int(data['Index']) in 需要打开 and data["Android Started"] == "0":
                openLD(data['Index'])
                wait_emulator(data['Index']) # [Wait Till Emulator Starts]
                tranduythieunang(data['Index'])
                time.sleep(1)

    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
