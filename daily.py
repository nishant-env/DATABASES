import os
from datetime import date

dir_path = "C:\\Users\\Nishant\\Desktop\\Reports\\" 
append_path = date.today().strftime("%Y-%m-%d")

if (os.path.isdir(dir_path+append_path)):
    pass

else:
    os.mkdir(dir_path+append_path)