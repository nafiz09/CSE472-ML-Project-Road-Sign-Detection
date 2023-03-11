from ultralytics import YOLO

model = YOLO('best_yolov8.pt')
model.predict(source = "0",show = True, conf = 0.25)