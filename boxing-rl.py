import gymnasium as gym
import numpy as np

def get_status(_observation, count):
    env_low = env.observation_space.low
    env_high = env.observation_space.high
    env_dx = (env_high - env_low) / 40

    print(_observation[0])
    if count == 0:
        position = int((_observation[0][0] - env_low[0])/env_dx[0])
        print(position)
        velocity = int((_observation[0][1] - env_low[1])/env_dx[1])
        print(velocity)
    else:
        position = int((_observation[0] - env_low[0])/env_dx[0])
        print(position)
        velocity = int((_observation[1] - env_low[1])/env_dx[1])
        print(velocity)
    return position, velocity

def update_q_table(_q_table, _action, _observation, _next_observation, _reward, _episode, count):

    alpha = 0.2
    gamma = 0.99

    next_position, next_velocity = get_status(_next_observation, count)
    next_max_q_value = max(_q_table[next_position][next_velocity])

    position, velocity = get_status(_observation, count)
    q_value = _q_table[position][velocity][_action]

    _q_table[position][velocity][_action] = q_value + alpha * (_reward + gamma * next_max_q_value - q_value)

    return _q_table

def get_action(_env, _q_table, _observation, _episode, count):
    epsilon = 0.02
    if np.random.uniform(0, 1) > epsilon:
        position, velocity = get_status(_observation, count)
        _action = np.argmax(_q_table[position][velocity])
    else:
        _action = np.random.choice([0, 1, 2])
    return _action

def main():

    env = gym.make("ALE/Boxing-v5", render_mode='human')

    action_space

    # ゲーム環境を初期化
    observation, info = env.reset()

    # ゲームのステップを1000回プレイ
    for _ in range(1000):
        # env.render()    # 環境からランダムな行動を取得
        # これがエージェントの行動になるので、本来はAIが行動を決定するべきところ
        action = env.action_space.sample()

        # 行動を実行すると、環境の状態が更新される
        observation, reward, terminated, truncated, info = env.step(action)

        # ゲームが終了したら、環境を初期化して再開
        if terminated or truncated:
            observation, info = env.reset()

    env.close()

if __name__ == '__main__':


