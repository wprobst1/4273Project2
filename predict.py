import argparse
from ultralytics import YOLO

parser = argparse.ArgumentParser()
parser.add_argument('--source', type=str, required=True)
parser.add_argument('--conf', type=float, default=0.45)
args = parser.parse_args()

model = YOLO('weights.pt')

results = model.predict(source=args.source, save=True)
