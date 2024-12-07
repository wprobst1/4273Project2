from ultralytics import YOLO

model_path = "weights.pt"
data_path = "data.yaml"

model = YOLO(model_path)
results = model.val(data=data_path)

print(results)
