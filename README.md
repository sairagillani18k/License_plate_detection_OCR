**Revolutionizing Transportation Security: License Plate Detection and OCR**

Vehicles' license plates are like their identities. In many situations, keeping track of vehicles that enter or leave a place is important, and reading their license plates offers a foolproof method of doing that.

**Detecting  the plates**

To make the system "see" and read the license plate when a vehicle passes through the camera's field of view, first, the Yolov8 model detects the license plate, captures an image of it, and passes it to the next module of the project, which then proceeds to decipher the characters on the plate. The Yolov8 model is trained on open-source data acquired from Roboflow.

**Cracking the License Plate Code: Optical Character Recognition (OCR)**

Optical Character Recognition is like a language translator for machines. We take the image of the detected license plate and use Python's EasyOCR library to translate the optical characters into text. Below is a demonstration of how the project works:




https://github.com/sairagillani18k/License_plate_detection_OCR/assets/58274863/07204581-0147-4aa8-97a6-4e31f8aeb5c6

