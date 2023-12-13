import gymnasium as gym
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten
from tensorflow.keras.optimizers import Adam
# from keras.models import Sequential
# from keras.layers import Dense, Activation, Flatten
# from keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory

import keras
import tensorflow as tf

# print("Keras version:", keras.__version__) 
# print("TensorFlow version:", tf.__version__) 

env = gym.make('MountainCar-v0')
nb_actions = env.action_space.n
# print("np_actions=", nb_actions) # 3
# print("env.observation_space.shape=", env.observation_space.shape) # (2, )
# print("env.step(action)")
# 環境の作成
env.reset()

# 環境を一度ステップ実行してみる
action = env.action_space.sample()  # ランダムなアクション
observation, reward, done, info, _ = env.step(action)
# print(env.step(action)) # (array([-0.44767037, -0.00056871], dtype=float32), -1.0, False, False, {})


# 結果の表示
# print("Observation:", observation)
# print("Reward:", reward)
# print("Done:", done)
# print("Info:", info)

model = Sequential()
model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))
# print("model.summary=", model.summary())

memory = SequentialMemory(limit=50000, window_length=1)

policy = EpsGreedyQPolicy(eps=0.001)
dqn = DQNAgent(model=model, nb_actions=nb_actions,gamma=0.99, memory=memory, nb_steps_warmup=10,
               target_model_update=1e-2, policy=policy)
dqn.compile(Adam(learning_rate=1e-3), metrics=['mae'])

history = dqn.fit(env, nb_steps=50000, visualize=False, verbose=2)

dqn.test(env, nb_episodes=1, visualize=True)
