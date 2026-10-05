import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2docx import Converter


def convert_pdf():
    # Select PDF
    pdf_file = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
    )

    if not pdf_file:
        return

    # Automatically create DOCX filename
    base_name = os.path.splitext(os.path.basename(pdf_file))[0]
    default_output = base_name + ".docx"

    # Choose where to save the DOCX
    docx_file = filedialog.asksaveasfilename(
        title="Save Word document",
        initialfile=default_output,
        defaultextension=".docx",
        filetypes=[("Word document", "*.docx")]
    )

    if not docx_file:
        return

    try:
        status_label.config(text="Converting...")
        root.update_idletasks()

        # Convert PDF to DOCX
        cv = Converter(pdf_file)
        cv.convert(docx_file)
        cv.close()

        status_label.config(text="Conversion complete!")

        messagebox.showinfo(
            "Success",
            f"PDF converted successfully!\n\nSaved to:\n{docx_file}"
        )

    except Exception as e:
        status_label.config(text="Conversion failed.")

        messagebox.showerror(
            "Error",
            f"Something went wrong:\n\n{str(e)}"
        )


# -----------------------------
# GUI
# -----------------------------
if "__main__" == __name__:
    root = tk.Tk()
    root.title("PDF to Word Converter")
    root.geometry("450x250")
    root.resizable(False, False)

    title_label = tk.Label(
        root,
        text="PDF → Word Converter",
        font=("Arial", 20, "bold")
    )
    title_label.pack(pady=(35, 10))

    description_label = tk.Label(
        root,
        text="Select a PDF and convert it to an editable Word document.",
        font=("Arial", 10)
    )
    description_label.pack(pady=5)

    convert_button = tk.Button(
        root,
        text="Select PDF",
        command=convert_pdf,
        font=("Arial", 12, "bold"),
        width=20,
        height=2
    )
    convert_button.pack(pady=25)

    status_label = tk.Label(
        root,
        text="Ready",
        font=("Arial", 10)
    )
    status_label.pack()

    root.mainloop()
