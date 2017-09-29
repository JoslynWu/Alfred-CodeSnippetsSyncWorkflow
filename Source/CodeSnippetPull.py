# -*- coding:utf-8 -*-
# Author: Joslyn Wu

import sys
import os
from workflow import Workflow


def main(w_f):
    title = ''

    source = "~/Library/Mobile Documents/com~apple~CloudDocs/CSSync/CodeSnippets"
    target = "~/Library/Developer/Xcode/UserData/CodeSnippets"

    source_dir = os.path.expanduser(source)
    newest_zip_name = 0
    file_list = os.listdir(source_dir)
    for i in range(0, len(file_list)):
        if file_list[i].endswith('.zip'):
            temp_zip_name = int(file_list[i].split('.')[0])
            if temp_zip_name > newest_zip_name:
                newest_zip_name = temp_zip_name

    source_zip = source_dir + os.sep + str(newest_zip_name) + ".zip"
    source_zip = source_zip.replace(" ", r"\ ")
    target_dir = os.path.expanduser(target).replace(" ", r"\ ")

    unzip_command = "unzip -qo {0} -d {1} -x \"*.DS_Store\"".format(source_zip, target_dir)
    if os.system(unzip_command) == 0:
        title = 'Pull Successful! '
        print(target_dir)
    else:
        title = 'FAILED! '
        target = ''
        print(title)


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
