from gym_core import tgym


class myTGym(tgym.TradingGymEnv):
    def _rewards(self, observation, action, done, info):
        if action == 1:
            if info['stop_loss']:
                return -1
            if info['reached_profit']:
                return 1
        return 0
