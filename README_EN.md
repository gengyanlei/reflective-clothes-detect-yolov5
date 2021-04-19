# Construction workers wear detection yolov5
## helmet-clothes-detect-yolov5

* author is leilei
* reflective-clothes-detect qq-group: 980489677, qq-group2: 710514100
* If this project is helpful to you, please give a star, your star is an encouragement to me!

### dataset download details
* reflective-clothes-detect-dataset (with xml annotations 1083) download: [BaiDuYunPan](https://pan.baidu.com/s/1_Ei9bYmUpa-8q-hXZk1u8w) 提取码->(dooh) 
* ~~yolov5s's weight is in reflective-clothes-detect-dataset !~~

### demo
|![new_demo](./result/re_pred.jpg)|
|----|

### Applicable instructions
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

### How to use dataset?
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
    + [crawl.py](https://github.com/gengyanlei/fire-detect-yolov4/tree/master/crawl)

### Practical application ############### Key ###################
* Based on the SHWD data set, perform the five-category labeling training yolov4-yolov5 for helmet-reflective clothing-holistic people to achieve detection of construction areas or dangerous areas:
    1. Based on the trained yolov4 or yolov5 model of 1083 reflective clothing images, expand the reflective clothing category of the SHWD data set;
    2. Based on the data set obtained by the 1-step expansion, train yolov4.

### Cite
* [SHWD-helmet-dataset](https://github.com/njvisionpower/Safety-Helmet-Wearing-Dataset)
* [yolov5](https://github.com/ultralytics/yolov5) (supports empty-labeled images)
* [yolov4](https://github.com/AlexeyAB/darknet) (supports empty-labeled images)
* [leilei's blog](https://blog.csdn.net/LEILEI18A/article/details/108694753)

### Reputation:
* **This data is for academic exploration only！！！**

### Other
* [building-segmentation-dataset](https://github.com/gengyanlei/build_segmentation_dataset)
* [fire-smoke-detect-datatset](https://github.com/gengyanlei/fire-detect-yolov4)