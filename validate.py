from ultralytics import YOLO

model_path = "weights.pt"
data_path = "C:/Users/steve/Documents/GitHub/4273Project2/datasets/data.yaml"

model = YOLO(model_path)
results = model.val(data=data_path)

print(results)
