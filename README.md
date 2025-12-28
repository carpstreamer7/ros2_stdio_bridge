# ros2_stdio_bridge


## 概要

`ros2_stdio_bridge` は、標準入力（stdin）と標準出力（stdout）を ROS 2 トピックで接続する入出力ブリッジである。  
ターミナルから入力した文字列をROS2のトピックとしてパブリッシュし、別ノードでサブスクライブして表示する。

---
## ノードとトピックの構成

本パッケージには、以下の 2 つの ROS 2 ノードが含まれている。

### ノード一覧

| ノード名 | 機能 |
|---|---|
| `stdin_bridge` | 標準入力（stdin）から文字列を読み取り、ROS 2 トピック `/stdin` に `std_msgs/String` 型で publish する |
| `stdout_sink` | トピック `/stdin` を subscribe し、受信した文字列を標準出力（stdout）に表示する |

### 使用トピック

| トピック名 | 型 | 説明 |
|---|---|---|
| `/stdin` | `std_msgs/String` | 標準入力から受け取った文字列を送信するためのトピック |

---
## ダウンロード

任意の作業ディレクトリで、以下のコマンドを実行する。

```bash
cd ~/ros2_ws/src
git clone https://github.com/carpstreamer7/ros2_stdio_bridge.git
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
を実行し確認する。

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
---

## テスト環境
- WSL
  - Ubuntu 22.04 LTS
---

## ライセンス
© 2025  Junko Morofuji

本パッケージは BSD 3-Clause License のもとで公開されている。
