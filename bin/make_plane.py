"""
计划类

当前的计划

{'round': 1, 'current': 1, 'salary': 0.99}
{'round': 2, 'current': 2, 'salary': 0.98}
{'round': 3, 'current': 5, 'salary': 1.9499999999999993}
{'round': 4, 'current': 10, 'salary': 1.8999999999999986}
{'round': 5, 'current': 21, 'salary': 2.789999999999999}
{'round': 6, 'current': 42, 'salary': 2.5799999999999983}
{'round': 7, 'current': 85, 'salary': 3.1500000000000057}
{'round': 8, 'current': 172, 'salary': 4.279999999999973}
{'round': 9, 'current': 346, 'salary': 4.539999999999964}
{'round': 10, 'current': 696, 'salary': 5.039999999999964}
{'round': 11, 'current': 1399, 'salary': 5.0099999999997635}
{'round': 12, 'current': 2813, 'salary': 5.869999999999891}
{'round': 13, 'current': 5655, 'salary': 6.450000000000728}
{'round': 14, 'current': 11368, 'salary': 7.319999999999709}
{'round': 15, 'current': 22851, 'salary': 7.489999999997963}
"""

class Plane:
    def __init__(self):
        self.start_money = 1  # 起始1元人民币
        self.coast = 0  # 全局，统计总共的花销的
        self.earn = 0  # 赚钱的金额
        self.peilv = 1.99  # 赔率

    def get_plane(self, round=15):
        """计算期数所需要的金额"""
        data_info_list = list()
        spand_money_list = list()  # 花费列表
        current_spand = self.start_money  # 当前的投入
        for i in range(1,round+1):
            info_dict = {"round": i}  # 数据情报表
            # 购买一波
            spand_money_list.append(current_spand)
            info_dict["current"] = current_spand
            # 计算收益
            total_coast = sum(spand_money_list)
            salary = current_spand*self.peilv - total_coast
            print(f'第{i}轮:收益{salary}，投入金额{total_coast}')
            info_dict["salary"] = salary
            # 计算下一轮要投入多少钱
            # guss_next_salary = self.start_money
            current_spand = self.get_current_spand(current_spand,spand_money_list,i)

            data_info_list.append(info_dict)
        return data_info_list

    def get_current_spand(self, current_spand, spand_money_list,n):
        """
        计算下一期要给多少钱
        :param current_spand:
        :param spand_money_list:
        :return:
        """
        container_list = list()
        for i in range(current_spand,100000):
            li = spand_money_list.copy()  # 存款列表
            li.append(i)  # 添加新投入
            sum_li = sum(li)  # 总投入
            salary = i*self.peilv - sum_li
            # print(f'{sum_li}')
            # print(i)
            if salary > n*0.5:
                # print(f'n的值{n}')
                container_list.append(i)
                break

        print(container_list)
        return container_list[0]



if __name__ == '__main__':


    plan = Plane()
    res = plan.get_plane()
    print(res)
    print()

    s = 0
    for r in res:
        print(r)
        s += r['current']

    print(s)


