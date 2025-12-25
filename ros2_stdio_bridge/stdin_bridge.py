#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Junko Morofuji
# SPDX-License-Identifier: Apache-2.0

import sys

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class StdinBridge(Node):
    def __init__(self):
        super().__init__('stdin_bridge')
        self.publisher = self.create_publisher(String, 'stdin', 10)

    def run(self):
        for line in sys.stdin:
            msg = String()
            msg.data = line.rstrip('\n')
            self.publisher.publish(msg)

        # EOF を受けたら正常終了
        rclpy.shutdown()


def main():
    rclpy.init()
    node = StdinBridge()
    node.run()


if __name__ == '__main__':
    main()

