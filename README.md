# reflective-clothes-detect and dataset
# 工作服(反光衣)检测数据集

* author is leilei
* reflective-clothes-detect qq群: 980489677
* 如果此项目对您有所帮助，请给个star，您的star是对我的鼓励！

## Some details
* reflective-clothes-detect-dataset (with xml annotations 1083) download: [BaiDuYunPan](https://pan.baidu.com/s/1_Ei9bYmUpa-8q-hXZk1u8w) 提取码->(dooh) 
* yolov5s's weight is in reflective-clothes-detect-dataset !

## Applicable instructions
0. download BaidDuYunPan's data and weight file
1. put yolov5s's weight file into yolov5 folder
2. cd yolov5, and excuting an order:
    ```
    python detect.py --source ***/aaa.jpg --weights ./best.pt
    ```
3. convert VOC2021 to YOLO format：
    ```
    call yolov5's voc_label_Re.py
    ```

## How to use dataset?
* We annotate the reflective-clothes-detect-dataset as Pascal VOC format:
    ```
    --VOC2021(反光衣)
        --Annotations (xml_num: 1083)
        --ImageSets(Main)
        --JPEGImages (image_num: 1083)

        --images (yolov5 need, the same with JPEGImages)
        --labels (yolov4-5 need)
        --txt_yolov5 (yolov5 need 2021_train.txt)
        --2021_train.txt (yolov4 need)

        --yolov5_weight (yolov5s's weight)

        --label_name: reflective_clothes、other_clothes
    ```

* If you want to crawl some images
    ```
    Please refer to this crawler code on github:
    https://github.com/gengyanlei/fire-detect-yolov4 -> test_baidu.py | test_google.py
    ```

## demo
* ./result: 

|![demo1](https://github.com/gengyanlei/reflective-clothes-detect/blob/master/result/test02.jpg)|
|----|
|![demo2](https://github.com/gengyanlei/reflective-clothes-detect/blob/master/result/test05.jpg)|
|----|

## How to expand reflective clothing data?
0. Based on the trained yolov4 model of 1083 reflective clothing images, expand the reflective clothing category of the [SHWD](https://github.com/njvisionpower/Safety-Helmet-Wearing-Dataset) data set;
1. Based on the data set expanded by 0 steps, train yolov4.

## 如何基于此项目进行反光衣数据扩充，并进行自动标注？
0. 基于1083张反光衣图像训练好的yolov4模型，对[SHWD](https://github.com/njvisionpower/Safety-Helmet-Wearing-Dataset)数据集进行反光衣类别扩充；
1. 基于0步骤扩充得到的数据集，训练yolov4.

## Cite
* [yolov5](https://github.com/ultralytics/yolov5) (supports empty-labeled images)
* [yolov4](https://github.com/AlexeyAB/darknet) (supports empty-labeled images)
* [博客blog](https://blog.csdn.net/LEILEI18A/article/details/108694753)
* **本数据仅学术探索！！！**

## Other
* [building-segmentation-dataset](https://github.com/gengyanlei/build_segmentation_dataset)
* [fire-smoke-detect-datatset](https://github.com/gengyanlei/fire-detect-yolov4)