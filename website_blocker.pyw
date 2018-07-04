import time
from datetime import datetime as dt
import platform
import ctypes, sys
import os

redirect_url = "127.0.0.1"

web_list_file = open("website_list.txt","r")
website_list = web_list_file.readlines()
web_list_file.close()

starting_hour = 9
end_hour = 17

def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False

def hosts_path():
	if platform.system() == "Windows":
		hosts = r"C:\Windows\System32\drivers\etc\hosts"
	elif platform.system() == "Darwin" or platform.system() == "Linux":
		hosts = r"/etc/hosts"
	else:
		print("Unsupported OS detected. Exiting the program.")
		exit(0)

	return hosts

def web_blocker():
	while True:
		if dt(dt.now().year, dt.now().month, dt.now().day, starting_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_hour):
			print("Working Hours!! Your given websites have been blocked!")
			file = open(hosts_path(), "r+")
			content = file.read()
			for website in website_list:
				if not website in content:
					file.write(redirect_url+" "+website+"\n")
				else:
					pass
			file.close()
		else:
			print("Non Working Hours!! No website has been blocked!")
			with open(hosts_path(),"r+") as file:
				content = file.readlines()
				file.seek(0)
				for line in content:
					if not any(website in line for website in website_list):
						file.write(line)
					file.truncate()
		time.sleep(5)

def main():
	if platform.system() == "Windows":
		if is_admin():
			web_blocker()
		else:
				ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
	elif platform.system() == "Linux":
		if os.geteuid() != 0:
			os.execvp("sudo", ["sudo"] + sys.argv)
	else:
		print("Incompatible OS. Exiting Program.")
		exit(0)

if __name__ == "__main__":
	main()