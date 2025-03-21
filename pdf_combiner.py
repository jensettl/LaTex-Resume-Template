import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger
import os

def merge_pdfs():
    # Create root window and hide it
    root = tk.Tk()
    root.withdraw()

    # Open file dialog to select multiple PDF files, starting in current directory
    file_paths = filedialog.askopenfilenames(
        title="Select PDF files to merge",
        filetypes=[("PDF files", "*.pdf")],
        initialdir=os.getcwd(),
        multiple=True
    )

    if not file_paths:  # If no files were selected
        print("No files selected")
        return

    # Create a PDF merger object
    merger = PdfMerger()

    # Add each selected PDF to the merger
    for file_path in file_paths:
        merger.append(file_path)

    # Get the directory of the first file for saving the merged PDF
    output_dir = os.path.dirname(file_paths[0])
    output_file_name = input("Enter the name of the output file: ")
    output_path = os.path.join(output_dir, output_file_name + ".pdf")

    # Write the merged PDF to a file
    merger.write(output_path)
    merger.close()

    print(f"PDFs merged successfully! Output saved as: {output_path}")

if __name__ == "__main__":
    merge_pdfs()