# 定义物品类，包含信息物品名称，物品主人姓名，物品个数，物品主人电话，备注
class Item:
    def __init__(self, name, master, number, phone, detail):
        self.name = name
        self.master = master
        self.number = number
        self.phone = phone
        self.detail = detail
    