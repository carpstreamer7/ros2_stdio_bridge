# ros2_stdio_bridge

## 概要

`ros2_stdio_bridge` は、標準入力（stdin）と標準出力（stdout）を ROS 2 トピックで接続する入出力ブリッジである。  
ターミナルから入力した文字列を ROS 2 の topic として publish し、別ノードで subscribe して表示する。

---
## 設計意図

### 1. OS 標準入出力と ROS 2 の橋渡し

本パッケージでは

- 標準入力（stdin）
- 標準出力（stdout）

という OS レベルの入出力を ROS 2 の通信に接続することで、
ROS 2 が「外部システムとどのように連携できるか」を明確に示している。


### 2. ノードの役割分離

機能を以下の 2 ノードに分離して実装した。

| ノード名 | 役割 |
|---|---|
| `stdin_bridge` | 標準入力を読み取り、`std_msgs/String` として publish |
| `stdout_sink` | トピックを subscribe し、内容を標準出力に表示 |

これにより、publish と subscribe の役割が明確になっている。


### 3. launch による一括起動

2 つのノードを同時に起動するため、launch ファイルを用意した。

- 複数の `ros2 run` を手動で実行する必要がない
- ROS 2 の標準的な運用方法に沿った実行が可能

---

## システム構成

```text
stdin (CLI)
↓
stdin_bridge
↓ (ROS 2 topic: /stdin)
stdout_sink
↓
stdout (CLI)
```

---
## ディレクトリ構成

```text
ros2_stdio_bridge
├── ros2_stdio_bridge
│ ├── stdin_bridge.py
│ └── stdout_sink.py
├── launch
│ └── stdio_bridge.launch.py
├── package.xml
├── setup.py
└── README.md
```

---
## 使用方法
### 1. ビルド
```bash
cd ~/ros2_ws
colcon build --packages-select ros2_stdio_bridge
source install/setup.bash
```

### 2. 実行（launch）
```bash
ros2 launch ros2_stdio_bridge stdio_bridge.launch.py
```
以下の 2 ノードが同時に起動する。

```text
• stdin_bridge
• stdout_sink
```

### 3. 動作確認
起動したターミナルで文字列を入力し、Enter を押す。

```text
hello
```

ROS 2 トピックを経由して、同じ文字列が標準出力に表示される。

```text
hello
```

