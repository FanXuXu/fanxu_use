import psutil

mm = list()

for proc in psutil.process_iter():
    if "python" in proc.name():
        print("pid:{},name{}".format(proc.pid, proc.name()))
        mm.append(proc.pid)
print(mm)


for m in mm:
    pp = psutil.Process(m)
    mm = pp.cmdline()
    use_comd = mm[-1].split("/")[-1]
    print(use_comd)



# pp = psutil.get