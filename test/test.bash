#!/bin/bash
# SPDX-License-Identifier: BSD-3-Clause

set -e

WS=~/ros2_ws
LOG=/tmp/ros2_stdio_bridge_test.log

echo "[TEST] build package"
cd $WS
colcon build --packages-select ros2_stdio_bridge
source install/setup.bash

echo "[TEST] start stdout_sink"
ros2 run ros2_stdio_bridge stdout_sink > $LOG &
SINK_PID=$!

sleep 1

echo "[TEST] send input via stdin_bridge"
echo "hello" | ros2 run ros2_stdio_bridge stdin_bridge

sleep 1
kill $SINK_PID || true

echo "[TEST] check output"
cat $LOG | grep "hello"

echo "[TEST] OK"

