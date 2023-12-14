# Boxing
Open AI GymのBoxingにおいて、AIに遅延を与えることで難易度調整ができるか検証する

## 使用環境（暫定であり、この環境が正しいかどうかの確証はない）

- python=3.10.*
- tensorflow=2.10.0

## Gymnasiumのインストール
```
pip install gymnasium
pip install gymnasium[atari] → atariのインストール、ゲームによっては[box2D]等
pip install gymnasium[accept-rom-license] → romのインストール
```

## その他のインストール
```
pip install keras-rl2 → keras-rlだとエラーが起きた
pip install tensorflow==2.10.0 → 場合によって変更
pip install protobuf==3.20.0 → tensorflowが低いバージョンの際にインストール必要
pip install numpy==1.21.0 → tenosorflowが低いバージョンの際にインストール必要
```

## pythonのインストール（主がpoetryを使い、自分の環境を作成するためのコード）
```
pyenv install -l
pyenv install 3.9.16
source ~/.bash_profile
pyenv local 3.9.16
poetry env use 3.9.16
```

## 学習方法（コードを
```
python Boxing-rl.py
```
  
## 現状の課題（全体図）
- 実験用のAIをどうするか　→　強化学習搭載のAIをまずはね
- AIをどう学習させるか　→　まずはこれを頑張る
- AI同士の対戦方法　→　絶対に必要（AIの保存がわからん）
- AIと人間の対戦方法　→　対戦出来ればいいけど、最悪必要ない
- 修士論文の構成 → なんとなくはわかるけど厳密じゃない
- 修士論文参考文献 → どの論文読もうかしら

## 現状
- BoxingのDQNがうまくいかないので、他のコードのDQNを実装する
- GymnasiumとGymの違いに苦しんでいる
- Gymnasiumの参考コードがなさすぎてうざすぎる
- mountaincardqn.pyが実行できないが、PythonとTensorflowによる問題ではないので、コードによる問題と思われる。一番うざい
- Pendulum.py → srlというgymを使わずにAtariを使用、いったん放置
- cartpoledqn.py → コード量が多いので、いったん放置

## 次やること
- コードと素直に格闘する　←　無理！
- 修士論文やる（金土日）

## エラーの種類（Chatgptに詳しく記述あり）
### cartpole1
- oneDNN → 大丈夫
- libcudart.so.11.0 → CUDAについて、多分大丈夫
- cuBLASファクトリー登録エラー → CUDAのセットアップ
- libvinfer.so.7 → NVIDIDIA TensorRTをインストールが必要、詳しく調べる必要あり
- CartPole-v0の非推奨警告 → バージョンが古いかも、多分大丈夫
- libcuda.so.1がみつからない → GPU関連なので無視
- lr非推奨 → learning_rateに変更
- ValueError → 値がおかしいかも

### Mountain_car
- TensorFlowのCPU最適化に関する情報 → 問題なし
- CUDAライブラリが見つからない → GPU使う場合
- cuBLASプラグインの登録エラー → cuBLAS、バージョン不一致やライブラリの不足
- TensorRTライブラリが見つからない → 上記と一緒
- calnitの失敗 → GPUが認識されてない、問題なし
- Pythonスカラー変換のエラー → Pythonスカラー変換のエラー、これが問題
- 配列要素の設定エラー → 配列要素の設定エラー、これが問題

### Boxing
- おそらくinputがおかしい、けどわからない
- Error when checking input: expected flatten_input to have 5 dimensions, but got array with shape (1, 1, 2)


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
- [Mountain Car(Gym)](https://www.gymlibrary.dev/environments/classic_control/mountain_car/)
- [Mountain Car(Gymnasium)](https://gymnasium.farama.org/environments/classic_control/mountain_car/)
  
## Tensorflow(version)　→ mountaincarを各バージョンで実行したが、うまくいかず
- 2.11.1 ダメだけど、エラー変化あり
- 2.12.1 ダメ
- 2.13.1 ダメだけど、エラー変化あり
- 2.10.0 ダメ
- 2.10.1 ダメ
- 2.9.1 ダメ
- 2.9.2 ダメ
- 2.9.3 ダメ
- 2.8.4 ダメ
- 2.7.4 ダメ
- 2.6.3 ダメ
- 2.5.3 3.8 ダメ
- 2.4.4 (numpy →← keras)両立できない

