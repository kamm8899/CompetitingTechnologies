import pdfplumber
import pandas as pd

# Specify the PDF file name
pdf_path = "/Users/jessicakammann/Desktop/Research /Android/SamsungPDF/Samsung2024Q4.pdf"
csv_path = "Samsung2024Q4.csv"

# Open the PDF file
data = []
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        table = page.extract_table()  # Extract table data
        if table:
            data.extend(table)  # Append extracted data to list

# Convert to DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv(csv_path, index=False, header=False)

print(f"CSV file saved as {csv_path}")

#save and run script--python convert_pdf_to_csv.py in terminal