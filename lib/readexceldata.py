# -*- coding: utf-8 -*-
import xlrd
'''
我们的⽬的是获取某条⽤例的数据，需要3个参数，excel数据⽂件名（data_file），⼯作簿名（sheet），⽤例名（case_name） 如果我们只封装⼀个函
数，每次调⽤（每条⽤例）都要打开⼀次excel并遍历⼀次，这样效率⽐较低。 我们可以拆分成两个函数，⼀个函数 excel_to_list(data_file, sheet)
⼀次获取⼀个⼯作表的所有数据，另⼀个函数 get_test_data(data_list, case_name) 从所有数据中去查找到该条⽤例的数据。
'''

'''读取excel文件，将excel文件里面对应的sheet的数据转换为python对象（列表），其中列表中每一个元素为一个字典'''
def  excel_to_list(file, sheet):
    """将excel表中数据转换成python对象"""
    data_list = []
    """打开excel文件"""
    wb = xlrd.open_workbook(file)
    """选择读取sheet工作表"""
    sheet = wb.sheet_by_name(sheet)
    """获取行数"""
    row_num = sheet.nrows
    header = sheet.row_values(0)
    for i in range(1, row_num):
        """读取行"""
        row_data = sheet.row_values(i)
        """将表头与每一行的数据拼装成字典，构造传参"""
        d = dict(zip(header, row_data))
        '''将多个字典组成的参数，放到一个大列表中'''
        data_list.append(d)
    return data_list


"""获取测试数据,判断传入的test_name 是否存在，存在则返回一个列表中对应的字典数据"""
def get_test_data(test_name, test_list):
    for test_dict in test_list:
        if test_name == test_dict['test_name']:
            return test_dict

