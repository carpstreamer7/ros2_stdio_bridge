# ros2_stdio_bridge


## 概要

`ros2_stdio_bridge` は、標準入力（stdin）と標準出力（stdout）を ROS 2 トピックで接続する入出力ブリッジである。  
ターミナルから入力した文字列をROS2のトピックとしてパブリッシュし、別ノードでサブスクライブして表示する。

---

## ダウンロード

任意の作業ディレクトリで、以下のコマンドを実行する。

```bash
cd ~/ros2_ws/src
git clone https://github.com/carpstreamer7/ros2_stdio_bridge.git
```

## インストール（ビルド）

ROS 2 ワークスペースのルートに移動し、ビルドを行う。

```bash
cd ~/ros2_ws
colcon build --packages-select ros2_stdio_bridge
source install/setup.bash
```

---
## 起動方法

本パッケージは、標準入力を扱う特性上、
ros2 run による個別起動を行う。

ターミナル 1（標準入力 → publish）
```bash
ros2 run ros2_stdio_bridge stdin_bridge
```

ターミナル 2（subscribe → 標準出力）
```bash
ros2 run ros2_stdio_bridge stdout_sink
```

ターミナル 1 で文字列を入力し、Enter を押す。
例:
```text
hello
```

ターミナル 2 に、以下のように同じ文字列が表示される。
例:
```text
hello
```

## 動作確認

データの受け渡しが正しく行われているかは、ターミナル3にて
```bash
ros2 topic echo /stdin
```
を実行する。

ターミナル1で
```bash
aaa
```
を入力した場合、
```text
data: aaa
```
と表示される。

---

## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.7〜3.10


## テスト環境
- WSL
  - Ubuntu 22.04 LTS

## ライセンス
© 2025  Junko Morofuji
本パッケージは BSD 3-Clause License のもとで公開されている。
