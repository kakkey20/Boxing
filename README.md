# Boxing
Open AI GymのBoxingにおいて、AIに遅延を与えることで難易度調整ができるか検証する

## 使用環境

- python=3.10.*
- tensorflow=2.10.0

## Gymnasiumのインストール
```
pip install gymnasium
pip install gymnasium[atari]
pip install gymnasium[accept-lom-ricense]
```

## その他のインストール
```
pip install keras-rl2
pip install tensorflow==2.10.0
```

## 学習方法
```
python Boxing-rl.py
```

## 参考文献

- [Gymで強化学習①準備編](https://note.com/kikaben/n/n57584c49d5c2)
- [[強化学習] いつの間にか OpenAI Gym が終焉していた](https://zenn.dev/ymd_h/articles/dd3bce4199e2ba)
- [OpenAI Gym 入門](https://qiita.com/ishizakiiii/items/75bc2176a1e0b65bdd16)
- [Learning_Openai-Gym-Boxing](https://github.com/yunik1004/Learning_Openai-Gym-Boxing)
- [Boxing-RL](https://github.com/rohilG/Boxing-RL)
- [OpenAI Gym で自前の環境をつくる](https://qiita.com/ohtaman/items/edcb3b0a2ff9d48a7def)
- [Pytorchを使って深層強化学習のモデルDQNを構築する 〜Deep Reinforcement Learning〜](https://www.dskomei.com/entry/2021/10/05/140156)
- [【強化学習】DQNを解説・実装](https://qiita.com/pocokhc/items/bb6a47e4d1d15112469f)
- [【強化学習初心者向け】シンプルな実装例で学ぶQ学習、DQN、DDQN【CartPoleで棒立て：1ファイルで完結、Kearas使用】](https://qiita.com/sugulu_Ogawa_ISID/items/bc7c70e6658f204f85f9)
  
## 現状の課題
- 実験用のAIをどうするか　→　強化学習搭載のAIをまずはね
- AIをどう学習させるか　→　まずはこれを頑張る
- AI同士の対戦方法　→　絶対に必要（AIの保存がわからん）
- AIと人間の対戦方法　→　対戦出来ればいいけど、最悪必要ない
- 修士論文の構成 → なんとなくはわかるけど厳密じゃない
- 修士論文参考文献 → どの論文読もうかしら

## 次やること
- DQNの参考コードを実装する（Boxing以外）
- Pendulum.py → srlというgymを使わずにAtariを使用、いったん放置
- cartpoledqn.py
- mountaincardqn.py

## 現状
- BoxingのDQNがうまくいかないので、他のコードのDQNを実装する
