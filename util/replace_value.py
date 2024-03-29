import json


class ReplaceValue:

    def __init__(self, obj):
        self.obj = obj

    def replace_value(self, data):
        if data:
            # 保存数据类型
            data_type = type(data)
            # 判断数据类型转换成str
            if isinstance(data, dict) or isinstance(data, list):
                str_data = json.dumps(data)
            else:
                str_data = str(data)
            for cs in range(1, str_data.count('${') + 1):
                # 替换
                if "${" in str_data and "}" in str_data:
                    start_index = str_data.index("${")
                    end_index = str_data.index("}", start_index)
                    old_value = str_data[start_index:end_index + 1]
                    # 反射：通过类的对象和方法字符串调用方法
                    func_name = old_value[2:old_value.index('(')]
                    print(func_name)
                    args_value1 = old_value[old_value.index('(') + 1:old_value.index(')')]
                    new_value = ""
                    if args_value1 != "":
                        args_value2 = args_value1.split(',')
                        new_value = getattr(self.obj, func_name)(*args_value2)
                    else:
                        new_value = getattr(self.obj, func_name)()
                    str_data = str_data.replace(old_value, str(new_value))
            # 还原数据类型
            if isinstance(data, dict) or isinstance(data, list):
                data = json.loads(str_data)
            else:
                data = data_type(str_data)
        return data
