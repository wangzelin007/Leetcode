import time

class Funnel(object):

    def __init__(self, capacity, leaking_rate):
        self.capacity = capacity
        self.leaking_rate = leaking_rate
        self.left_capacity = capacity
        self.leaking_time = time.time()

    def make_space(self):
        now_ts = time.time()
        delta_ts = now_ts - self.leaking_time
        delta_quota = delta_ts * self.leaking_rate
        if delta_quota < 1: return
        self.left_capacity += delta_quota
        self.leaking_time = now_ts
        if self.left_capacity > self.capacity:
            self.left_capacity = self.capacity

    def watering(self, quota):
        self.make_space()
        if self.left_capacity >= quota:
            self.left_capacity -= quota
            return True
        return False

funnels = {}
def is_action_allowed(user_id, user_action, capacity, leaking_rate):
    key = '%s:%s' % (user_id, user_action)
    funnel = funnels.get(key)
    if not funnel:
        funnel = Funnel(capacity, leaking_rate)
        funnels[key] = funnel
    return funnel.watering(1)

for i in range(100):
    time.sleep(0.1)
    print(is_action_allowed('wzl', 'reply', 15, 1))