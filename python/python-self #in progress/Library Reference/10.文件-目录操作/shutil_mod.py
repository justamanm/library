
import shutil


# src仅支持文件，不能是目录
# dst可以是文件也可以是文件夹，当是文件时相当于复制且重命名
# 会复制文件数据和权限信息，而不会复制其他metadata，创建时间-修改时间等
shutil.copy("./dir1/a.txt", "./dir2")
shutil.copy("./dir1/a.txt", "./dir2/b.txt")

# 在copy的基础上，额外可以复制源信息
# 相当于cop -p命令，会复制原文件的metadata，如创建时间-修改时间等
shutil.copy2("./dir1/a.txt", "./dir2")
shutil.copy2("./dir1/a.txt", "./dir2/b.txt")


# src和dst都必须是文件，即dst不能是文件夹
# 不会复制其他metadata
shutil.copyfile("./dir1/a.txt", "./dir2/a.txt")

# 剪切，相当于mv命令
# src可以是文件或文件夹
shutil.move("./dir1", "./dir2")
shutil.move("./dir1/a.txt", "./dir2")

# 复制文件夹
shutil.copytree("./dir1", "./dir2")