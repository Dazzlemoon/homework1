from item import Item
import pandas as pd
#将物品信息转化为python中DataFrame形式进行输出
def get_dataframe(items):
    all = []
    for i in range(len(items)):
        temp = [items[i].name, items[i].master, items[i].number\
                    , items[i].phone, items[i].detail]
        all.append(temp)
        all_df = pd.DataFrame(all, columns=["物品名称", "物品主人姓名", \
                            "物品个数", "物品主人电话号码", "备注"])
    return all_df
#定义操作类，包含所有的操作
class Operation:
    def __init__(self):
        self.items = []
    #添加物品    
    def Add(self):
        name = input("请输入物品的名称：")
        master = input("请输入物品主人的姓名：")
        number = input("请输入物品的个数：")
        phone = input("请输入物品主人电话号码：")
        detail = input("该栏为备注：")
        item = Item(name, master, number, phone, detail)
        self.items.append(item)
    #显示所有物品列表
    def Show_all(self):
        if len(self.items) == 0:    
            print("这里暂时没有物品。")
        else:
            print("所有物品如下：")
            all_items = get_dataframe(self.items)
            print(all_items)
    # 查找物品信息
    def Search(self):
        search_name = input("请输入要寻找的物品名称：")
        all_items = get_dataframe(self.items)
        all_items_search = all_items[all_items["物品名称"]== search_name]
        if all_items_search.empty:
            print("该表单中没有您所找的物品。")
        else:
            print("所寻找符合条件的所有物品如下：")
            print(all_items_search)
    # 删除物品信息
    def Delete(self):
        delete_name = input("请输入您所需删除物品的名称：")
        delete_master = input("请输入您所需删除物品主人的姓名：")
        begin_lens = len(self.items)
        for item in self.items:
            if delete_name == item.name and delete_master == item.master:
                self.items.remove(item)
        end_lens = len(self.items)
        if begin_lens == end_lens:
            print("这里没有您所需要删除的物品。")
        else:
            print("您所需要删除的物品已删除")
    # 展示菜单
    def Show_menus(self):
        print("这里是物品交换系统，您可以对该系统进行一下操作：")
        print("-"*6+"1.添加物品"+"-"*14)
        print("-"*6+"2.删除物品"+"-"*14)
        print("-"*6+"3.显示所有物品信息"+"-"*6)
        print("-"*6+"4.查找物品信息"+"-"*10)
        print("-"*6+"0.退出系统"+"-"*14)
        
                
        
            