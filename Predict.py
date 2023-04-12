from ultralytics import YOLO
import cv2
import torch

fname = "yolo_model/classes.txt"

class_names = []
with open(fname, 'r') as f:
    class_names = [name.strip() for name in f.readlines()]

def custom_detect(img_path:str, score:int=0.25):
    model = YOLO('yolo_model/best.pt')
    result = model.predict(source=img_path, conf=score)
    img = cv2.imread(img_path)

    clsIdx = torch.tensor(result[0].boxes.cls, dtype=torch.int32).tolist()
    bboxs = torch.tensor(result[0].boxes.xyxy, dtype=torch.int32).tolist()
    confs = torch.tensor(result[0].boxes.conf, dtype=torch.float16).tolist()

    count = len(clsIdx)

    result_string = 'The image contains {} bird(s).'.format(count)

    if count > 0:
        result_string += 'The bird names are '

    for idx, box, conf in zip(clsIdx, bboxs, confs):
        classname = class_names[idx]
        print('class name : ', idx,  classname)
        result_string += "{0}({1:.2f}) ,  ".format(classname, conf)

        bbox = (box[0], box[1], box[2]-box[0], box[3]-box[1])
        cv2.rectangle(img, bbox, color=(255, 0, 0), thickness=2)
        cv2.putText(img, '{0}_{1:.2f}'.format(classname, conf), (box[0]+5, box[1]+20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    cv2.imwrite('static/uploads/result.png', img)

    print(result_string)
    return result_string, clsIdx, confs

def main():
    custom_detect('images/test.png')

if __name__ == '__main__' : 
    main()