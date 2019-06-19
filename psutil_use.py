import psutil

mm = list()
# 目标执行进程启动文件名
aim_file_name = []

for proc in psutil.process_iter():
    if "python" in proc.name():
        print("pid:{},name{}".format(proc.pid, proc.name()))
        pp = psutil.Process(proc.pid)
        p_status = pp.status()
        mm = pp.cmdline()
        print(mm)
        use_comd = mm[-1].split("/")[-1]
        print("启动文件：{},进程状态：{}".format(use_comd, p_status))
# print(mm)
#
#
# for m in mm:




# pp = psutil.get