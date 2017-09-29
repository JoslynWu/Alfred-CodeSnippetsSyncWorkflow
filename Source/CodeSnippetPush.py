# -*- coding:utf-8 -*-
# Author: Joslyn Wu

import sys
import os
import time
from workflow import Workflow


def main(w_f):
    title = ''

    target = "~/Library/Mobile Documents/com~apple~CloudDocs/CSSync/CodeSnippets"
    source = "~/Library/Developer/Xcode/UserData/CodeSnippets"

    # Get query from Alfred
    # if len(w_f.args):
    #     query = w_f.args[0]
    # else:
    #     query = '--'

    target_dir = os.path.expanduser(target)
    zip_name = time.strftime("%Y%m%d")
    target = target_dir + os.sep + zip_name + ".zip"

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    source_dir = os.path.expanduser(source).replace(" ", r"\ ")
    # -r 递归； -j 不存放目录名； -x 不包含的文件
    zip_command = "zip -jqr {0} {1} -x \"*.DS_Store\"".format(target.replace(' ', r'\ '), source_dir)
    if os.system(zip_command) == 0:
        title = 'Push Successful! '
        print(target)
    else:
        title = 'Push FAILED! '
        target = ''
        print(title)

    # w_f.add_item(title=title, subtitle=subtitle, arg=target, icon='', valid=True, uid='1234', autocomplete='')
    # w_f.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
