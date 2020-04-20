import cv2
import time
import tensorflow as tf
from tensorflow.python.platform import gfile
import numpy as np
from threading import Thread
from random import randrange
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
import os

from Viz import Visual
from crypt import Cryp_Decry 


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color:#101357;")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(45, 10, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(10, 100, 531, 61))
        font = QtGui.QFont()
        font.setFamily("Prestige Elite Std")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label6.setFont(font)
        self.label6.setObjectName("label6")
        self.label6.setStyleSheet("color:#ffffff")

        self.label7 = QtWidgets.QLabel(self.centralwidget)
        self.label7.setGeometry(QtCore.QRect(10, 160, 531, 61))
        font = QtGui.QFont()
        font.setFamily("Prestige Elite Std")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label7.setFont(font)
        self.label7.setObjectName("label6")
        self.label7.setStyleSheet("color:#ffffff")


        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 228, 180, 38))
        font = QtGui.QFont()
        font.setFamily("Prestige Elite Std")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label8")
        self.label_8.setStyleSheet("color:#ffffff")




        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(355, 60, 210, 41))
        font = QtGui.QFont()
        font.setFamily("Prestige Elite Std")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label.setStyleSheet("color:#ffffff")
        self.label_2.setStyleSheet("color:#ffffff")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 62, 80, 38))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        # For the graphic view setup 
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 273, 502, 233))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_3.setStyleSheet("color:#fbaf08")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 117, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Prestige Elite Std")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("color:#32CD32")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(220, 117, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Prestige Elite Std")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.pushButton2.setFont(font)
        self.pushButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.setStyleSheet("color:#32CD32")

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(290, 117, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Prestige Elite Std")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.pushButton3.setFont(font)
        self.pushButton3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton3.setStyleSheet("color:#32CD32")

        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(
            QtCore.QRect(360, 117, 70, 31))  # right,verti
        font = QtGui.QFont()
        font.setFamily("Prestige Elite Std")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.pushButton4.setFont(font)
        self.pushButton4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton4.setStyleSheet("color:#32CD32")

        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(
            QtCore.QRect(230, 175, 110, 31))  # right,verti
        font = QtGui.QFont()
        font.setFamily("Prestige Elite Std")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.pushButton5.setFont(font)
        self.pushButton5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton5.setStyleSheet("color:#32CD32")

        #start encryption boutton 
        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton6.setGeometry(
            QtCore.QRect(140,232, 125, 31))  # right,verti
        font = QtGui.QFont()
        font.setFamily("Prestige Elite Std")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(50)
        self.pushButton6.setFont(font)
        self.pushButton6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton6.setObjectName("pushButton6")
        self.pushButton6.setStyleSheet("color:#32CD32")


        self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)
        Window_View = QtWidgets.QGraphicsScene()
        pixmap = QtGui.QPixmap(
            "/root/Documents/MaskProject/Assests/1.png")
        Window_View.addPixmap(pixmap.scaled(
            500, 500, QtCore.Qt.KeepAspectRatio))
        self.graphicsView.setScene(Window_View)

        
        #self.graphicsView1 = QtWidgets.QGraphicsView(self.centralwidget)
        #self.graphicsView1.setGeometry(QtCore.QRect(350, 230, 183,115))
        #self.graphicsView1.setObjectName("graphicsView")

        #Window_View1 = QtWidgets.QGraphicsScene()
        #pixmap = QtGui.QPixmap(
        #    "/root/Documents/MaskProject/Assests/nateg_enetcom.png")
        #Window_View1.addPixmap(pixmap.scaled(
        #    180,180, QtCore.Qt.KeepAspectRatio))
        #self.graphicsView1.setScene(Window_View1)

        self.pushButton5.clicked.connect(self.decryp_Boutton)
        self.pushButton6.clicked.connect(self.encrypt_Boutton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate(
            "MainWindow", "MASK DETECTION APPLICATION "))
        self.label_2.setText(_translate("MainWindow", "NATEG ENET\'Com Team"))
        self.label_3.setText(_translate("MainWindow", "Developed by : "))
        self.pushButton.setText(_translate("MainWindow", "Camera 1"))
        self.pushButton.clicked.connect(self.mask_detection)
        self.pushButton2.setText(_translate("MainWindow", "Camera 2"))
        self.pushButton3.setText(_translate("MainWindow", "Camera 3"))
        self.pushButton4.setText(_translate("MainWindow", "Camera 4"))
        self.pushButton5.setText(_translate("MainWindow", "Decrypt Images"))
        self.pushButton6.setText(_translate("MainWindow", "Start Encryption !"))
        self.label6.setText(_translate("MainWindow", "Available Camera :"))
        self.label7.setText(_translate(
            "MainWindow", "Visualizing Crypted Images : "))
        self.label_8.setText(_translate("MainWidow", "Encrypt Images : "))

    def model_restore_from_pb(self, pb_path, node_dict):
        config = tf.ConfigProto(log_device_placement=True,
                                allow_soft_placement=True,
                                )
        config.gpu_options.allow_growth = True
        # config.gpu_options.per_process_gpu_memory_fraction = 0.6
        sess = tf.Session(config=config)
        with gfile.FastGFile(pb_path, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            sess.graph.as_default()
            tf.import_graph_def(graph_def, name='')  # 匯入計算圖
        sess.run(tf.global_variables_initializer())
        for key, value in node_dict.items():
            node = sess.graph.get_tensor_by_name(value)
            node_dict[key] = node
        return sess, node_dict

    def video_init(self):
        cap = cv2.VideoCapture(0)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # default 640x480
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        return cap, height, width

    def generate_anchors(self, feature_map_sizes, anchor_sizes, anchor_ratios, offset=0.5):
        '''
        generate anchors.
        :param feature_map_sizes: list of list, for example: [[40,40], [20,20]]
        :param anchor_sizes: list of list, for example: [[0.05, 0.075], [0.1, 0.15]]
        :param anchor_ratios: list of list, for example: [[1, 0.5], [1, 0.5]]
        :param offset: default to 0.5
        :return:'''
        anchor_bboxes = []
        for idx, feature_size in enumerate(feature_map_sizes):
            cx = (np.linspace(0, feature_size[0] - 1,
                              feature_size[0]) + 0.5) / feature_size[0]
            cy = (np.linspace(0, feature_size[1] - 1,
                              feature_size[1]) + 0.5) / feature_size[1]
            cx_grid, cy_grid = np.meshgrid(cx, cy)
            cx_grid_expend = np.expand_dims(cx_grid, axis=-1)
            cy_grid_expend = np.expand_dims(cy_grid, axis=-1)
            center = np.concatenate((cx_grid_expend, cy_grid_expend), axis=-1)

            num_anchors = len(anchor_sizes[idx]) + len(anchor_ratios[idx]) - 1
            center_tiled = np.tile(center, (1, 1, 2 * num_anchors))
            anchor_width_heights = []

            # different scales with the first aspect ratio
            for scale in anchor_sizes[idx]:
                ratio = anchor_ratios[idx][0]  # select the first ratio
                width = scale * np.sqrt(ratio)
                height = scale / np.sqrt(ratio)
                anchor_width_heights.extend(
                    [-width / 2.0, -height / 2.0, width / 2.0, height / 2.0])

            # the first scale, with different aspect ratios (except the first one)
            for ratio in anchor_ratios[idx][1:]:
                s1 = anchor_sizes[idx][0]  # select the first scale
                width = s1 * np.sqrt(ratio)
                height = s1 / np.sqrt(ratio)
                anchor_width_heights.extend(
                    [-width / 2.0, -height / 2.0, width / 2.0, height / 2.0])

            bbox_coords = center_tiled + np.array(anchor_width_heights)
            bbox_coords_reshape = bbox_coords.reshape((-1, 4))
            anchor_bboxes.append(bbox_coords_reshape)
        anchor_bboxes = np.concatenate(anchor_bboxes, axis=0)
        return anchor_bboxes

    def decode_bbox(self, anchors, raw_outputs, variances=[0.1, 0.1, 0.2, 0.2]):
        '''
        Decode the actual bbox according to the anchors.
        the anchor value order is:[xmin,ymin, xmax, ymax]
        :param anchors: numpy array with shape [batch, num_anchors, 4]
        :param raw_outputs: numpy array with the same shape with anchors
        :param variances: list of float, default=[0.1, 0.1, 0.2, 0.2]
        :return:
        '''
        anchor_centers_x = (anchors[:, :, 0:1] + anchors[:, :, 2:3]) / 2
        anchor_centers_y = (anchors[:, :, 1:2] + anchors[:, :, 3:]) / 2
        anchors_w = anchors[:, :, 2:3] - anchors[:, :, 0:1]
        anchors_h = anchors[:, :, 3:] - anchors[:, :, 1:2]
        raw_outputs_rescale = raw_outputs * np.array(variances)
        predict_center_x = raw_outputs_rescale[:,
                                               :, 0:1] * anchors_w + anchor_centers_x
        predict_center_y = raw_outputs_rescale[:,
                                               :, 1:2] * anchors_h + anchor_centers_y
        predict_w = np.exp(raw_outputs_rescale[:, :, 2:3]) * anchors_w
        predict_h = np.exp(raw_outputs_rescale[:, :, 3:]) * anchors_h
        predict_xmin = predict_center_x - predict_w / 2
        predict_ymin = predict_center_y - predict_h / 2
        predict_xmax = predict_center_x + predict_w / 2
        predict_ymax = predict_center_y + predict_h / 2
        predict_bbox = np.concatenate(
            [predict_xmin, predict_ymin, predict_xmax, predict_ymax], axis=-1)
        return predict_bbox

    def single_class_non_max_suppression(self, bboxes, confidences, conf_thresh=0.2, iou_thresh=0.5, keep_top_k=-1):
        '''
        do nms on single class.
        Hint: for the specific class, given the bbox and its confidence,
        1) sort the bbox according to the confidence from top to down, we call this a set
        2) select the bbox with the highest confidence, remove it from set, and do IOU calculate with the rest bbox
        3) remove the bbox whose IOU is higher than the iou_thresh from the set,
        4) loop step 2 and 3, util the set is empty.
        :param bboxes: numpy array of 2D, [num_bboxes, 4]
        :param confidences: numpy array of 1D. [num_bboxes]
        :param conf_thresh:
        :param iou_thresh:
        :param keep_top_k:
        :return:
        '''
        if len(bboxes) == 0:
            return []

        conf_keep_idx = np.where(confidences > conf_thresh)[0]

        bboxes = bboxes[conf_keep_idx]
        confidences = confidences[conf_keep_idx]

        pick = []
        xmin = bboxes[:, 0]
        ymin = bboxes[:, 1]
        xmax = bboxes[:, 2]
        ymax = bboxes[:, 3]

        area = (xmax - xmin + 1e-3) * (ymax - ymin + 1e-3)
        idxs = np.argsort(confidences)

        while len(idxs) > 0:
            last = len(idxs) - 1
            i = idxs[last]
            pick.append(i)

            # keep top k
            if keep_top_k != -1:
                if len(pick) >= keep_top_k:
                    break

            overlap_xmin = np.maximum(xmin[i], xmin[idxs[:last]])
            overlap_ymin = np.maximum(ymin[i], ymin[idxs[:last]])
            overlap_xmax = np.minimum(xmax[i], xmax[idxs[:last]])
            overlap_ymax = np.minimum(ymax[i], ymax[idxs[:last]])
            overlap_w = np.maximum(0, overlap_xmax - overlap_xmin)
            overlap_h = np.maximum(0, overlap_ymax - overlap_ymin)
            overlap_area = overlap_w * overlap_h
            overlap_ratio = overlap_area / \
                (area[idxs[:last]] + area[i] - overlap_area)

            need_to_be_deleted_idx = np.concatenate(
                ([last], np.where(overlap_ratio > iou_thresh)[0]))
            idxs = np.delete(idxs, need_to_be_deleted_idx)

        # if the number of final bboxes is less than keep_top_k, we need to pad it.
        # TODO
        return conf_keep_idx[pick]

    def mask_detection(self):
        pb_path = "/root/Documents/MaskProject/face_mask_detection.pb"
        node_dict = {'input': 'data_1:0',
                     'detection_bboxes': 'loc_branch_concat_1/concat:0',
                     'detection_scores': 'cls_branch_concat_1/concat:0'}
        conf_thresh = 0.5
        iou_thresh = 0.4
        frame_count = 0
        FPS = "0"
        # ====anchors config
        feature_map_sizes = [[33, 33], [17, 17], [9, 9], [5, 5], [3, 3]]
        anchor_sizes = [[0.04, 0.056], [0.08, 0.11],
                        [0.16, 0.22], [0.32, 0.45], [0.64, 0.72]]
        anchor_ratios = [[1, 0.62, 0.42]] * 5
        id2class = {0: 'Safe', 1: 'NoMask'}

        # ----video streaming init
        cap, height, width,  = self.video_init()

        # ----model init

        # ====generate anchors
        anchors = self.generate_anchors(
            feature_map_sizes, anchor_sizes, anchor_ratios)
        # for inference , the batch size is 1, the model output shape is [1, N, 4],
        # so we expand dim for anchors to [1, anchor_num, 4]
        anchors_exp = np.expand_dims(anchors, axis=0)

        # ====model restore from pb file
        sess, node_dict = self.model_restore_from_pb(pb_path, node_dict)
        tf_input = node_dict['input']
        model_shape = tf_input.shape  # [N,H,W,C]
        print("model_shape = ", model_shape)
        detection_bboxes = node_dict['detection_bboxes']
        detection_scores = node_dict['detection_scores']

        while (cap.isOpened()):

            # ----get image
            ret, img = cap.read()

            if ret:
                # ----image processing
                img_resized = cv2.resize(img, (model_shape[2], model_shape[1]))
                img_resized = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
                img_resized = img_resized.astype('float32')
                img_resized /= 255

                # ----mask detection
                y_bboxes_output, y_cls_output = sess.run([detection_bboxes, detection_scores],
                                                         feed_dict={tf_input: np.expand_dims(img_resized, axis=0)})

                # remove the batch dimension, for batch is always 1 for inference.
                y_bboxes = self.decode_bbox(anchors_exp, y_bboxes_output)[0]
                y_cls = y_cls_output[0]
                # To speed up, do single class NMS, not multiple classes NMS.
                bbox_max_scores = np.max(y_cls, axis=1)
                bbox_max_score_classes = np.argmax(y_cls, axis=1)

                # keep_idx is the alive bounding box after nms.
                keep_idxs = self.single_class_non_max_suppression(y_bboxes,
                                                                  bbox_max_scores,
                                                                  conf_thresh=conf_thresh,
                                                                  iou_thresh=iou_thresh,
                                                                  )
                # ====draw bounding box

                for idx in keep_idxs:

                    conf = float(bbox_max_scores[idx])
                    class_id = bbox_max_score_classes[idx]
                    bbox = y_bboxes[idx]
                    # clip the coordinate, avoid the value exceed the image boundary.
                    xmin = max(0, int(bbox[0] * width))
                    ymin = max(0, int(bbox[1] * height))
                    xmax = min(int(bbox[2] * width), width)
                    ymax = min(int(bbox[3] * height), height)

                    if class_id == 0:
                        color = (0, 255, 0)  # (B,G,R)
                    else:
                        color = (0, 0, 255)  # (B,G,R)
                        date_string = time.strftime("%Y-%m-%d-%H:%M")
                        time.sleep(0.05)
                        cv2.imwrite('/root/Documents/MaskProject/Streaming record/screen' + date_string +
                                    str(randrange(100))+'.png', img)

                    # Variable conf : probabilty of wearing Mask
                    #cv2.rectangle(img, (xmin, ymin), (xmax, ymax), color, 2)
                    # cv2.putText(img, "%s: %.2f" % (id2class[class_id], conf), (xmin + 2, ymin - 2),
                        # cv2.FONT_HERSHEY_SIMPLEX, 0.8, color)
                    cv2.putText(img, "%s" % (id2class[class_id]), (xmin + 2, ymin - 2),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, color)

                # ----FPS count
                if frame_count == 0:
                    t_start = time.time()
                frame_count += 1
                if frame_count >= 10:
                    FPS = "FPS=%1f" % (10 / (time.time() - t_start))
                    frame_count = 0
                # cv2.putText
                cv2.putText(img, FPS, (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

                # ----image display
                cv2.imshow("NATEG ENETCOM ", img)

                # ----'q' key pressed?
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                print("get image failed")
                break

        # ----release
        cap.release()

        cv2.destroyAllWindows()

    def decryp_Boutton(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Visual()
        self.ui.setupUi(self.window)
        self.window.show()

    def encrypt_Boutton(self):
        try:
            encrypt=Cryp_Decry()
            encrypt.folder_crypting("/root/Documents/MaskProject/Streaming record/")
        except :
            print("Please Start MySQL Service on your computer !! ")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
