import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'ros2_stdio_bridge'


setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Junko Morofuji',
    maintainer_email='mimosa4kai@gmail.com',
    description='標準入出力（stdin / stdout）をROS 2ノードとして扱うためのブリッジ'
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'stdin_bridge = ros2_stdio_bridge.stdin_bridge:main',
            'stdout_sink = ros2_stdio_bridge.stdout_sink:main',
        ],
    },
)

