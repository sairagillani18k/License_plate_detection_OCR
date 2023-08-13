import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('runs/detect/predict2/crops/license/pic3.jpg')

# Extract text from the OCR result
extracted_text = [text for _, text, _ in result]

# Print the extracted text
print(extracted_text)
