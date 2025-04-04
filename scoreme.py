import pdfplumber
import pandas as pd
import os

def extract_tables_from_pdf(pdf_path, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)  
    output_excel = os.path.join(output_dir, os.path.basename(pdf_path).replace(".pdf", ".xlsx"))

    with pdfplumber.open(pdf_path) as pdf:
        tables_data = []
        
        for i, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            for table in tables:
                df = pd.DataFrame(table)
                tables_data.append(df)
        
        if not tables_data:
            print(f"No tables found in {pdf_path}")
            return
        
        with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
            for idx, table_df in enumerate(tables_data):
                table_df.to_excel(writer, sheet_name=f'Table_{idx+1}', index=False, header=False)
    
    print(f"Tables extracted and saved to {output_excel}")

if __name__ == "__main__":
    pdf_path = input("Enter the path of the PDF file: ").strip()
    extract_tables_from_pdf(pdf_path)

# Usage can be done as shown below - 
pdf_path = "test3(1)(1).pdf" 
output_excel = "output.xlsx"
extract_tables_from_pdf(pdf_path, output_excel)
