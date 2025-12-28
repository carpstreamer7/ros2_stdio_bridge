#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Junko Morofuji
# SPDX-License-Identifier: BSD-3-Clause

import sys
import threading

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class StdinBridge(Node):
    def __init__(self):
        super().__init__('stdin_bridge')
        self.publisher = self.create_publisher(String, 'stdin', 10)

    def stdin_loop(self):
        for line in sys.stdin:
            msg = String()
            msg.data = line.rstrip('\n')
            self.publisher.publish(msg)


def main():
    rclpy.init()
    node = StdinBridge()

    # stdin は別スレッドで読む
    thread = threading.Thread(target=node.stdin_loop, daemon=True)
    thread.start()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

