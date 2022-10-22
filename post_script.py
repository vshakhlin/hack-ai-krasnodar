import os

import pandas as pd
import numpy as np

def give_sings_new(number):
    signs_new = ['unknown'
        '2_1',
        '1_23',
        '1_17',
        '3_24',
        '8_2_1',
        '5_20',
        '5_19_1',
        '5_16',
        '3_25',
        '6_16',
        '7_15',
        '2_2',
        '2_4',
        '8_13_1',
        '4_2_1',
        '1_20_3',
        '1_25',
        '3_4',
        '8_3_2',
        '3_4_1',
        '4_1_6',
        '4_2_3',
        '4_1_1',
        '1_33',
        '5_15_5',
        '3_27',
        '1_15',
        '4_1_2_1',
        '6_3_1',
        '8_1_1',
        '6_7',
        '5_15_3',
        '7_3',
        '1_19',
        '6_4',
        '8_1_4',
        '8_8',
        '1_16',
        '1_11_1',
        '6_6',
        '5_15_1',
        '7_2',
        '5_15_2',
        '7_12',
        '3_18',
        '5_6',
        '5_5',
        '7_4',
        '4_1_2',
        '8_2_2',
        '7_11',
        '1_22',
        '1_27',
        '2_3_2',
        '5_15_2_2',
        '1_8',
        '3_13',
        '2_3',
        '8_3_3',
        '2_3_3',
        '7_7',
        '1_11',
        '8_13',
        '1_12_2',
        '1_20',
        '1_12',
        '3_32',
        '2_5',
        '3_1',
        '4_8_2',
        '3_20',
        '3_2',
        '2_3_6',
        '5_22',
        '5_18',
        '2_3_5',
        '7_5',
        '8_4_1',
        '3_14',
        '1_2',
        '1_20_2',
        '4_1_4',
        '7_6',
        '8_1_3',
        '8_3_1',
        '4_3',
        '4_1_5',
        '8_2_3',
        '8_2_4',
        '1_31',
        '3_10',
        '4_2_2',
        '7_1',
        '3_28',
        '4_1_3',
        '5_4',
        '5_3',
        '6_8_2',
        '3_31',
        '6_2',
        '1_21',
        '3_21',
        '1_13',
        '1_14',
        '2_3_4',
        '4_8_3',
        '6_15_2',
        '2_6',
        '3_18_2',
        '4_1_2_2',
        '1_7',
        '3_19',
        '1_18',
        '2_7',
        '8_5_4',
        '5_15_7',
        '5_14',
        '5_21',
        '1_1',
        '6_15_1',
        '8_6_4',
        '8_15',
        '4_5',
        '3_11',
        '8_18',
        '8_4_4',
        '3_30',
        '5_7_1',
        '5_7_2',
        '1_5',
        '3_29',
        '6_15_3',
        '5_12',
        '3_16',
        '1_30',
        '5_11',
        '1_6',
        '8_6_2',
        '6_8_3',
        '3_12',
        '3_33',
        '8_4_3',
        '5_8',
        '8_14',
        '8_17',
        '3_6',
        '1_26',
        '8_5_2',
        '6_8_1',
        '5_17',
        '1_10',
        '8_16',
        '7_18',
        '7_14',
        '8_23']
    return signs_new[number-1]

def convert_sign(sign_in: str):
    sing_replaced = sign_in.replace('_', '.')
    signs = ['3.24', '1.16', '5.15.5', '5.19.1', '5.19.2', '1.20.1', '8.23',
    '2.1', '4.2.1', '8.22.1', '6.16', '1.22', '1.2', '5.16', '3.27',
    '6.10.1', '8.2.4', '6.12', '5.15.2', '3.13', '3.1', '3.20', '3.12',
    '7.14.2', '5.23.1', '2.4', '5.6', '4.2.3', '8.22.3', '5.15.1',
    '7.3', '3', '2.3.1', '3.11', '6.13', '5.15.4', '8.2.1', '1.34.3',
    '8.2.2', '5.15.3', '1.17', '4.1.1', '4.1.4', '3.25', '1.20.2',
    '8.22.2', '6.9.2', '3.2', '5.5', '5.15.7', '7.12', '8.2.3',
    '5.24.1', '1.25', '3.28', '5.9.1', '5.15.6', '8.1.1', '1.10',
    '6.11', '3.4', '6.10', '6.9.1', '8.2.5', '5.15', '4.8.2', '8.22',
    '5.21', '5.18']
    if sing_replaced in signs:
        return signs.index(sing_replaced)
    return -1

def check_all():
    path = 'c:/vshakhlin/Dev/AI/hack-ai/krasnodar/yolov5/runs/detect/trafic_sign_det_test_3/labels'
    df_test = pd.read_csv('c:/vshakhlin/Dev/AI/hack-ai/krasnodar/test_dataset_test/test.csv')
    # labels = os.listdir(path)
    signs = []

    i = 0
    for row, val in df_test.iterrows():
        label_name = val['img'].replace('.jpg', '.txt')
        classes = [0] * 8
        if os.path.isfile(f'{path}/{label_name}'):
            label_file = open(f'{path}/{label_name}', 'r')
            lines = label_file.readlines()
            cls_idx = 0
            for line in lines:
                cls = int(line.split(' ')[0])
                new_sign = give_sings_new(cls)
                sign = convert_sign(new_sign) + 1
                if sign not in classes:
                    classes[cls_idx] = sign
                cls_idx += 1
            label_file.close()

        signs.append(classes)
    signs_arr = np.array(signs)
    print(signs_arr.shape)

    df_test['sing1'] = signs_arr[:, 0]
    df_test['sing2'] = signs_arr[:, 1]
    df_test['sing3'] = signs_arr[:, 2]
    df_test['sing4'] = signs_arr[:, 3]
    df_test['sing5'] = signs_arr[:, 4]
    df_test['sing6'] = signs_arr[:, 5]
    df_test['sing7'] = signs_arr[:, 6]
    df_test['sing8'] = signs_arr[:, 7]

    df_test.drop(['img'], axis=1, inplace=True)
    df_test.to_csv('solution2.csv', index=False)


if __name__ == '__main__':
    check_all()