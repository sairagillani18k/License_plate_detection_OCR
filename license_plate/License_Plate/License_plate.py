import matplotlib.pyplot as plt
from ultralytics import YOLO
import cv2
model = YOLO('License_Plate/best.pt')

# Load the image using OpenCV
image = cv2.imread('License_Plate/pic3.jpg')

# Run YOLOv8 inference on the image
results = model(image,save_crop=True) 

# Visualize the results on the image
annotated_image = results[0].plot()

# Display the annotated image using matplotlib
plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
plt.title("YOLOv8 Inference")
plt.axis('off')
plt.show()
