import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams, LTImage
from pdfminer.pdfpage import PDFPage
from pptx import Presentation
from pptx.util import Inches

def extract_content_from_pdf(pdf_path, output_folder):
    # Create a PDF resource manager object
    resource_manager = PDFResourceManager()

    # Initialize a list to store the extracted content for each page
    page_content = []

    # Create a PDF interpreter object
    interpreter = PDFPageInterpreter(resource_manager, TextConverter(resource_manager, open(os.devnull, 'w'), laparams=LAParams())) # Suppress output

    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Iterate over PDF pages
        for page in PDFPage.get_pages(pdf_file):
            # Initialize a dictionary to store the content for the current page
            page_dict = {}

            # Process the page
            interpreter.process_page(page)

            # Create a PDF resource manager object for the current page
            page_resource_manager = PDFResourceManager()

            # Initialize a PDF page aggregator object for the current page
            page_aggregator = PDFPageAggregator(page_resource_manager, laparams=LAParams())

            # Create a PDF interpreter object for the current page
            page_interpreter = PDFPageInterpreter(page_resource_manager, page_aggregator)

            # Process the page with the PDF interpreter
            page_interpreter.process_page(page)

            # Extract the images from the page aggregator
            images = [x for x in page_aggregator.get_result().layout if isinstance(x, LTImage)]

            # Save the images to the output folder
            image_paths = []
            for i, image in enumerate(images):
                image_path = os.path.join(output_folder, f'image_{i}.png')
                with open(image_path, 'wb') as image_file:
                    image_file.write(image.stream.get_rawdata())
                image_paths.append(image_path)
            page_dict['images'] = image_paths

            # Add the dictionary for the current page to the list of page content
            page_content.append(page_dict)

    # Return the extracted content
    return page_content

extract_content_from_pdf("test2.pdf", "./")