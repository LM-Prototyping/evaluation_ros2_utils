import os
import rclpy
from rclpy.node import Node
from ament_index_python.packages import get_package_share_directory

from datetime import datetime

import numpy as np

NOW = datetime.now().strftime("%m_%d__%H_%M_%S")
DIR = os.environ.get("LM_FRAMEWORK_PATH") + "recording/" + NOW

class CameraPlugin():
    def init(self, webots_node, properties={}):
        try: 
            rclpy.init(args=None)
        except:
            pass

        self.node = Node("CameraNode")

        self.robot = webots_node.robot
        self.device = self.robot.getDevice("top_camera")
        self.timestep = int(self.robot.getBasicTimeStep())

        self.device.enable(33)

        self.current_timestep = 0

        # Create directory for recordings
        os.mkdir(DIR)

    def step(self, timestep=0):
        rclpy.spin_once(self.node, timeout_sec=0)
        
        # image = self.device.getImageArray()
        # self.device.saveImage(DIR + "/" + str(self.current_timestep) + ".png", 90)

        print("Running", timestep) # , image[:1])

        self.current_timestep += self.timestep
        pass

