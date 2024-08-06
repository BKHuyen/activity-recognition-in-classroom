import yaml
import numpy as np
import math
import csv
from metrics2 import *

file_path = 'raising_hand/result_asdf/stt_iou.txt'


def IoU(bbox_gt, bbox_pred, eps=1e-6):
    bbox_gt = bbox_gt.astype(np.float32)
    bbox_pred = bbox_pred.astype(np.float32)

    n_true = bbox_gt.shape[0]
    n_pred = bbox_pred.shape[0]
    ious = np.zeros((n_true, n_pred), dtype = np.float32)

    area1 = (bbox_gt[2] - bbox_gt[0]) * (bbox_gt[3] - bbox_gt[1])
    area2 = (bbox_pred[2] - bbox_pred[0]) * (bbox_pred[3] - bbox_pred[1])

    x_start = np.maximum(bbox_pred[0], bbox_gt[0])
    y_start = np.maximum(bbox_pred[1], bbox_gt[1])
    x_end = np.minimum(bbox_pred[2], bbox_gt[2])
    y_end = np.minimum(bbox_pred[3], bbox_gt[3])
    overlap = np.maximum(x_end - x_start, 0) * np.maximum(y_end - y_start, 0)
    union = area2 + area1 - overlap
    union = np.maximum(union, eps)
    iou = overlap / union

    return iou


def main():
    annotation_file = 'sleeping/data/grt.yaml'
    prediction_file = 'sleeping/data/pre.yaml'

    with open(annotation_file) as r:
        ground_truths = yaml.safe_load(r)
    print('Loaded ground-truths')

    with open(prediction_file) as f:
        predictions = yaml.safe_load(f)
    print('Loaded predictions')

    merged_text = ""
    accuracy = 0
    temporal_score = 0
    temporal_score_sum = 0
    ed_score = 0
    f1_score = 0
    kqs = []
    # csv_file = 'D:/code/sort_old/data/oac.csv'
    for q in predictions:
        if q in predictions.keys():
            pred = predictions[q]
            bbox_pred = np.asarray(pred['bbox'])
            # print(q)
            # print(2346788)

            for k in ground_truths:
                if k in ground_truths.keys():
                    gt = ground_truths[k]
                    bbox_gt = np.asarray(gt['bbox'])
                    temporal_score = temporal_IoU(pred, gt)
                    stt = stt_iou(pred, gt)
            
                    #iou = IoU(bbox_pred,bbox_gt)

                    # if iou > 0:
                    #     merged_text += str(q) + " " + str(k) + " " + str(stt) + "\n"

                    # print(k)    
                    #if iou >= 0.1 and temporal_score > 0:

                    if stt >  0.4:           
                        accuracy = tube_accuracy(pred, gt)
                        temporal_score_sum = temporal_score
                        f1_score = f1_overlap(pred, gt)
                        ed_score = edit_score(pred, gt, norm=True)
                        STT_IoU = stt
                        kq = [q, k, accuracy, temporal_score_sum, f1_score, ed_score, STT_IoU]
                        kq = np.asarray(kq)
                        kqs.append(kq)
                    
                
            #print(5127489)

    # with open(file_path, 'w') as file:
    #     file.write(merged_text)

    out_final = []
    sequen_match_too_gt= []

    seen = []
    for i in range(len(kqs)):
        if kqs[i][1] in seen:
            continue
            
        sequen_match_too_gt.append(kqs[i])
        for j in range(i+1, len(kqs)):
            if not kqs[j][1] == kqs[i][1]:
                continue
            sequen_match_too_gt.append(kqs[j])
            
        stt_max = max(sequen_match_too_gt[_][6] for _ in range(len(sequen_match_too_gt)))
        for v in range(len(sequen_match_too_gt)):
            if sequen_match_too_gt[v][6] == stt_max:
                sequen = sequen_match_too_gt[v]
                out_final.append(sequen)
        sequen_match_too_gt.clear()
        seen.append(kqs[i][1])

    
    for u in range(len(out_final)):
        #print(out_final[u])
        accuracy += out_final[u][2]
        temporal_score_sum += out_final[u][3]
        f1_score += out_final[u][4]
        ed_score += out_final[u][5]
        STT_IoU += out_final[u][6]

    accuracy = accuracy*100
    temporal_score_sum = temporal_score_sum*100
    f1_score = f1_score*100

    print('FW accuracy:', accuracy / len(ground_truths))
    print('F1-score0.3k: ', f1_score / len(ground_truths))
    print('L accuracy: ', ed_score/ len(ground_truths))
    print('Temporal_IoU: ', temporal_score_sum / len(ground_truths))

if __name__ == '__main__':
    main()
