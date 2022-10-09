from operation import Operation
sheet = Operation()
while True:
    try:
        sheet.Show_menus() #显示菜单
        choose_operation= int(input("请输入您的选择：")) #让用户选择菜单
        if choose_operation == 1:
            sheet.Add()
        elif choose_operation == 2:
            sheet.Delete()
        elif choose_operation == 3:
            sheet.Show_all()
        elif choose_operation == 4:
            sheet.Search()
        elif choose_operation == 0:
            print("谢谢使用该物品交换系统")
            break
        else:
            print("输入错误，请重新输入。")
        print("操作结束，请选择接下来的操作。")
    except NameError:
        print("输入错误，请重新输入。")
        
        
