import PyPDF2
import pdfplumber
from transformers import pipeline
import nltk
from pptx import Presentation
from pptx.util import Inches, Pt


def summarize_pdf(file_path):
    # Read the PDF document
    with pdfplumber.open(file_path) as pdf:
        text = ' '.join(page.extract_text() for page in pdf.pages)
        
    # Tokenize the text into sentences
    sentences = nltk.sent_tokenize(text)
    # Combine the sentences into a single string
    document = ' '.join(sentences)
    # Initialize the BART summarization pipeline
    summarizer = pipeline('summarization')
    # Calculate how many chunks we need
    chunks = len(document) // 1024 + (len(document) % 1024 > 0)
    # Create a list for summaries
    summaries = []
    # Summarize each chunk and add to the list of summaries
    for i in range(chunks):
        chunk = document[i*1024:(i+1)*1024]
        summary = summarizer(chunk, max_length=60, min_length=30, do_sample=False)
        # Extract the summarized text
        summarized_text = summary[0]['summary_text']
        summaries.append(summarized_text)
        
    return summaries


def create_presentation(summaries, output_file):
    # Create a PowerPoint presentation
    prs = Presentation()
    # Set the width and height of a slide
    slide_width = Inches(10)
    slide_height = Inches(7.5)
    prs.slide_width = slide_width
    prs.slide_height = slide_height

    for i, summary in enumerate(summaries):
        # Add a slide with a title and content
        slide_layout = prs.slide_layouts[1]
        slide = prs.slides.add_slide(slide_layout)
        title = slide.shapes.title
        content = slide.placeholders[1]
        # Set the title and content
        title.text = f"Slide {i+1}"
        content.text = summary

    # Save the presentation
    prs.save(output_file)


# Usage example
summaries = summarize_pdf("/Users/ahmedshahid/Desktop/Laurier CS/CP317/PDF to PPT Code/test2.pdf")
create_presentation(summaries, "/Users/ahmedshahid/Desktop/Laurier CS/CP317/PDF to PPT Code/presentation.pptx")
