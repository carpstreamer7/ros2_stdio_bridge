#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Junko Morofuji
# SPDX-License-Identifier: Apache-2.0

import sys

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class StdoutSink(Node):
    def __init__(self):
        super().__init__('stdout_sink')
        self.subscription = self.create_subscription(
            String,
            'stdin',
            self.callback,
            10
        )

    def callback(self, msg: String):
        # 標準出力にはデータのみ
        print(msg.data, flush=True)


def main():
    rclpy.init()
    node = StdoutSink()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

