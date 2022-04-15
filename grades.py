class Grades:

    def __init__(self, sys_price, a, b, c):
        self.sys_price = sys_price
        self.grade_list = [a, b, c]

    def can_buy_console(self):
        count = 0
        total = []
        playtime_reward_list = [150, 75, -100]
        for reward in playtime_reward_list:
            total.append(self.grade_list[count] * reward)
            count += 1
        if sum(total) > self.sys_price:
            return True
