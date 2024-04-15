import weasyprint

def generate_pdf_from_html(input_file, output_file):
    weasyprint.HTML(input_file).write_pdf(output_file)
