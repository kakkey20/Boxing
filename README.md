# Boxing
Open AI GymのBoxingにおいて、AIに遅延を与えることで難易度調整ができるか検証する

## 使用環境

- python=3.10.*

## Gymnasiumのインストール
```
pip install gymnasium[atari]
pip install gymnasium[accept-lom-ricense]
```

## 学習方法
```
python Boxing-rl.py
```

学習が完了すると、param.h5 ファイルが作成されます。

## 参考文献

- [Gymで強化学習①準備編](https://note.com/kikaben/n/n57584c49d5c2)
- [Ubuntu 18.04 / Windows 10で Open AI Gym API for Fighting ICEを使ってみた](https://kbkn.xyz/ue4/fightingicesetup/)
- [Gym-FightingICE](https://github.com/TeamFightingICE/Gym-FightingICE)
- [OpenAI Gym API for Fighting ICEを動かしてみる](https://www.inoue-kobo.com/ai_ml/gym-fightingice/)
- [Fighting ICEを動かしてみる](https://qiita.com/hideki/items/589a4fad8e135d5adcbd)
- [FightingICE公式サイト](https://www.ice.ci.ritsumei.ac.jp/~ftgaic/index.htm)

