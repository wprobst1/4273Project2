import unittest
from yolov5 import YOLOModel  # Adjust based on your implementation

class SimpleYOLOTest(unittest.TestCase):

    def test_model_load_and_inference(self):
        """Test if the YOLO model loads and runs on a single image."""
        # Define paths (adjust as needed)
        model_path = 'path/to/yolo_model.pt'  # Path to YOLO model weights
        test_image_path = 'path/to/test_image.jpg'  # Path to a test image

        # Load the model
        try:
            model = YOLOModel(model_path)  # Replace with your model loading logic
        except Exception as e:
            self.fail(f"Model failed to load with error: {e}")

        # Run inference
        try:
            results = model.detect(test_image_path)  # Replace with your model inference logic
        except Exception as e:
            self.fail(f"Inference failed with error: {e}")

        # Check that results are not None or empty
        self.assertIsNotNone(results, "Model output is None.")
        self.assertTrue(len(results) > 0, "Model returned no detections.")

if __name__ == '__main__':
    unittest.main()
