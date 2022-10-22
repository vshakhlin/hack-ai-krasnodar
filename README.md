# hack-ai-krasnodar
Solution for https://hacks-ai.ru/championships/758293

Использовался внешний публичный датасет https://www.kaggle.com/datasets/watchman/rtsd-dataset

Использовал YoloV5
Обучение:

	python train.py --img 800 --batch 16 --epochs 10 --data trafic_sign.yaml --weights yolov5m.pt --name trafic_sign

Детекция

	python detect.py --source ../test_dataset_test/test --save-txt --weights ./runs/train/trafic_sign_2/weights/best.pt --conf 0.25 --name trafic_sign_det_test_2

Далее запускается скрипт постобработки post_script.py, которые по найденым файлам с лейблами получает найденные знаки и заполняет таблицу simple_solution.csv

Прикладываю обученные файлы модели (https://drive.google.com/file/d/1gSthgcVjEdMKyoXMNraGpRLhboXhpavZ/view?usp=sharing) и trafic_sign.yaml файл с конфигурацией для yolo
