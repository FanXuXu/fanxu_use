
my_list = list()
def test(value, **AAA):
    use_list = list()
    root_key = AAA.get("key")
    for key_, value_ in value.items():
        if isinstance(value_, dict):
            if root_key:
                AAA = {"key": "{}->{}".format(root_key, key_)}
            else:
                AAA = {"key": key_}
            # use_list.append(key_)
            test(value_, **AAA)
        else:
            mes_ = "{}->{}->{}".format(root_key, key_, value_)
            use_list.append(mes_)
            root_key =None
            # use_list.append(value_)
            # my_list.append(use_list)
    return use_list



if __name__ == '__main__':
    my_dict = {"樊旭_1": {"fanxu_1": "测试数据1", "fanxu_2": "测试数据2"},
               "mmmmm":{"樊旭_2": {"test": {"test_1": "content_1", "test_2": "content_2"},
                         "my_test": {"my_test_1": "my_my", "my_test_2": "my_1_my"}}},
              "kkkk":{"樊旭_3": "tt"}
    }
    print(test(my_dict))