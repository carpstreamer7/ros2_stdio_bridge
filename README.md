# ros2_stdio_bridge

## 概要

`ros2_stdio_bridge` は、標準入力（stdin）と標準出力（stdout）を ROS 2 トピックで接続する入出力ブリッジである。  
ターミナルから入力した文字列を ROS 2 の topic として publish し、別ノードで subscribe して表示する。

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
