#!/usr/bin/env bash
# 注意不同的任务需要修改 # runs/exp train.py

# 工作服(反光衣) 2类 单独训练
python train.py --img 640 --batch 32 --epochs 300 --data ./data/Reflective_vests.yaml --cfg ./models/yolov5s_fs.yaml --weights './yolov5s.pt' --device 1