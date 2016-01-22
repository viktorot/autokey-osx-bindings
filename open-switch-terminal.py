import subprocess
#command = 'wmctrl -l'
command = 'xlsclients'
output = system.exec_command(command, getOutput=True)

if 'mate-terminal' in output:
    window.activate('term')
else:
    #dialog.info_dialog("Window information", "asd")
    #keyboard.send_keys("<ctrl>+<alt>+t")
    subprocess.Popen(["mate-terminal"])
    
    





