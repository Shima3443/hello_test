import cv2
import pytesseract
import pandas as pd

# Define file paths
image_path = "/home/shima/Documents/csv/image.jpeg"
csv_output_path = "/home/shima/Documents/csv/output.csv"

# Load the image
image = cv2.imread(image_path)

# Convert image to grayscale for better OCR accuracy
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply OCR to extract text
extracted_text = pytesseract.image_to_string(gray, lang="eng+ben")  # Supports English & Bengali

# Convert text into a structured format (one line per row)
lines = extracted_text.split("\n")
data = [line.strip() for line in lines if line.strip()]  # Remove empty lines

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Extracted Text"])

# Save to CSV
df.to_csv(csv_output_path, index=False, encoding="utf-8-sig")

print(f"Text extracted and saved to {csv_output_path}")

