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

my_dict = {
        {"樊旭_1": {"fanxu_1": "测试数据1", "fanxu_2": "测试数据2"}},
        {"樊旭_2": {"test": {"test_1": "content_1", "test_2": "content_2"},
                  "my_test": {"my_test_1": "my_my", "my_test_2": "my_1_my"}}},
        {"樊旭_3": "tt"},
    }