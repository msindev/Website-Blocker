# Website Blocker
This Python script blocks the websites written in the website_list.txt files during the given working hours.
Make sure the python script and website_list.txt are in same folder.

To execute this program on a daily basis, you can use Task Scheduler in Windows, or cron in LINUX to start the script automatically at startup and execute the program.

It is a pyw file and not py file, so make sure you use pythonw.exe to run the script in background, which wouldn't show any command prompt or terminal output.
Use python.exe to see the output on command prompt and terminal.

To edit the websites which have to be blocked, add or delete the website name in the fie website_list.txt