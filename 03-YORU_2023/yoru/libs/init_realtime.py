import datetime
import re
import sys
import time

import numpy as np
import torch

sys.path.append("../yoru")
from yoru.libs.util import loadingParam

# try:
#     from yoru.libs.util import loadingParam
# except ModuleNotFoundError:
#     from libs.util import loadingParam


class init_asovi:
    def __init__(self, config_file="asovi_default.yaml", m_dict={}):
        self.conf = loadingParam(config_file).yml
        self.m_dict = m_dict

        # Essential & Control
        self.m_dict["now"] = datetime.datetime.now()
        self.m_dict["t0"] = time.perf_counter()
        self.m_dict["quit"] = False
        self.m_dict["back_to_home"] = False
        self.m_dict["init_finished"] = False
        self.m_dict["stream"] = False
        self.m_dict["stg_obst"] = False
        self.m_dict["export"] = self.conf["export"]
        self.m_dict["curLog"] = "hoge.txt"
        self.m_dict["total_time"] = 0

        # camera or screencapture
        self.m_dict["stream_MSS"] = self.conf["capture_style"]["stream_MSS"]

        # - Camera:
        self.m_dict["camera_id"] = self.conf["hardware"]["camera_id"]
        self.m_dict["camera_width"] = self.conf["hardware"]["camera_width"]
        self.m_dict["camera_height"] = self.conf["hardware"]["camera_height"]
        self.m_dict["camera_scale"] = self.conf["hardware"]["camera_scale"]
        self.m_dict["camera_fps"] = self.conf["hardware"]["camera_fps"]
        self.m_dict["current_camera_frame"] = np.zeros(
            (
                int(
                    self.conf["hardware"]["camera_height"]
                    * self.conf["hardware"]["camera_scale"]
                ),
                int(
                    self.conf["hardware"]["camera_width"]
                    * self.conf["hardware"]["camera_scale"]
                ),
                3,
            ),
            dtype="uint8",
        )
        self.m_dict["yolo_detection_frame"] = np.zeros(
            (
                int(
                    self.conf["hardware"]["camera_height"]
                    * self.conf["hardware"]["camera_scale"]
                ),
                int(
                    self.conf["hardware"]["camera_width"]
                    * self.conf["hardware"]["camera_scale"]
                ),
                3,
            ),
            dtype="uint8",
        )
        self.m_dict["camera_imshow"] = self.conf["hardware"]["camera_imshow"]

        # Camera
        # self.m_dict["camera_fps"] = 0.0

        # capture
        self.m_dict["capture_area_select"] = True
        self.m_dict["capture_area"] = {"top": 0, "left": 0, "width": 640, "height": 480}

        # YOLO model
        self.m_dict["yolo_model"] = self.conf["model"]["yolo_model_path"]
        self.m_dict["yolo_detection"] = self.conf["model"]["yolo_detection"]
        self.m_dict["yolo_results"] = []
        self.m_dict["yolo_process_state"] = True
        self.m_dict["YOLO_quit"] = False

        # trigger conditions
        self.m_dict["Trigger"] = False
        self.m_dict["COM_list"] = []
        self.m_dict["pin"] = 13
        self.m_dict["trigger_th_conf"] = self.conf["trigger"][
            "trigger_threshold_configuration"
        ]
        self.m_dict["trigger_class"] = self.conf["trigger"]["trigger_class"]
        self.m_dict["class_list"] = {}
        self.m_dict["class_name_list"] = []
        self.m_dict["arduino_com"] = self.conf["trigger"]["Arduino_COM"]
        self.m_dict["trigger_style"] = self.conf["trigger"]["trigger_style"]
        self.m_dict["serial_ser"] = "None"

        # trigger plugins
        self.m_dict["plugins"] = []
        self.m_dict["in_plugin_name"] = self.conf["trigger"]["trigger_style"]
        self.m_dict["plugin_name"] = "trigger_plugins.straight"
        self.m_dict["trigger_signal"] = 0

        # VR environment
        self.m_dict["now"] = datetime.datetime.now()
        self.m_dict["FileNameHead"] = self.conf["export_name"]
        self.m_dict["initialized"] = True

    def listCh(self, linestr="line0:3", default=False):
        daqreg = r"(\d{1,}):(\d{1,})"
        if not (re.search(daqreg, linestr)):
            daqChlist = [default]
        else:
            daqCh = np.double(
                [re.search(daqreg, linestr).group(x) for x in range(1, 3)]
            )
            daqCh = list(range(int(daqCh[0]), int(daqCh[1] + 1)))
            daqChList = [default for v in daqCh]
        return daqChList

    def __del__(self):
        print("== Initialization finished ==.")


if __name__ == "__main__":
    mdict0 = init_asovi(config_file="asovi_T490.yaml")
    print(mdict0.m_dict)
