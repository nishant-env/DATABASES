from datetime import date,timedelta
import os
import shutil
from glob import glob

previous_month = (date.today() - timedelta(days=30)).strftime("%Y-%m")



src_path_dir = "C:\\Users\\Nishant\\Desktop\\Reports\\"
src_path_folders = previous_month + "*"

main_archive_dir = "C:\\Users\\Nishant\\Desktop\\Reports\\Archive\\"
sub_archive_dir = previous_month

if (os.path.isdir(main_archive_dir+sub_archive_dir)):
    pass

else:
    os.mkdir(main_archive_dir+sub_archive_dir)
    

previous_month_folders = glob(src_path_dir+previous_month+'*/', recursive = True)
for dir in previous_month_folders:
    shutil.move(dir,main_archive_dir+sub_archive_dir)

