# batch_file_rename.py
# Created: 6th August 2012

"""
This will batch rename a group of files in a given directory,
once you pass the current and new extensions
"""

# just checking
__author__ = 'Craig Richards'
__version__ = '1.0'

import argparse
import os


def batch_rename(work_dir, old_ext, new_ext):
    """
    This will batch rename a group of files in a given directory,
    once you pass the current and new extensions
    """
    # files = os.listdir(work_dir)
    for filename in os.listdir(work_dir):
        # Get the file extension
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        # Start of the logic to check the file extensions, if old_ext = file_ext
        if old_ext == file_ext:
            # Returns changed name of the file with new extention
            newfile = split_file[0] + new_ext

            # Write the files
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
    print("rename is done!")
    print(os.listdir(work_dir))


def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    # 旧代码
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
                        help='the directory where to change extension')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    #  修复   error: the following arguments are required: WORK_DIR, OLD_EXT, NEW_EXT
    # parser.add_argument('--work_dir', metavar='WORK_DIR', type=str, nargs=1, help='the directory where to change extension')
    # parser.add_argument('--old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
    # parser.add_argument('--new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
# 测试
    args = parser.parse_args()
    print(args.work_dir)
    print(args.old_ext)
    print(args.new_ext)

    return parser


def main():
    """
    This will be called if the script is directly invoked.
    """
    # adding command line argument
    parser = get_parser()
    args = vars(parser.parse_args())

    # Set the variable work_dir with the first argument passed
    work_dir = args['work_dir'][0]
    # Set the variable old_ext with the second argument passed
    old_ext = args['old_ext'][0]


    if old_ext[0] != '.':
        old_ext = '.' + old_ext
    # Set the variable new_ext with the third argument passed
    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext

    print(work_dir
          +"         \r\n"+old_ext
          +"         \r\n"+new_ext
          )

    batch_rename(work_dir, old_ext, new_ext)

# argparse 模块  学习地址：
# https://docs.python.org/zh-cn/3.7/library/argparse.html#creating-a-parser
# https://docs.python.org/zh-cn/3.7/howto/argparse.html#id1

# argparse 模块可以让人轻松编写用户友好的命令行接口。
# 只能通过  命令行执行  命令
# 【python 所在dir\batch_file_rename.py  work_dir old_ext new_ext 】
# 案例：把 要替换后缀文件所在dir txt 换成 doc：
# 【python 所在dir\batch_file_rename.py  要替换后缀文件所在dir txt doc 】
if __name__ == '__main__':
    main()
