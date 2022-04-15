class Hours:

    def __init__(self, homework, chores, sports):
        self.hour_list = [homework, chores, sports]

    def get_reward_total(self):
        count = 0
        total = []
        playtime_reward_list = [2, 3, 4]
        for reward in playtime_reward_list:
            total.append(self.hour_list[count] // reward)
            count += 1
        return sum(total)
