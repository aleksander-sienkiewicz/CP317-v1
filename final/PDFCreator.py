from transformers import pipeline
from pptx import Presentation
from pptx.util import Inches, Pt

class createPowerPoint():
    def __init__(self, fileName):
         self.output_file = fileName
         self.prs = Presentation()

    def add_summaries(self,summaries):
        # Create a PowerPoint presentation
        # Set the width and height of a slide
        slide_width = Inches(10)
        slide_height = Inches(7.5)
        self.prs.slide_width = slide_width
        self.prs.slide_height = slide_height
        for i, summary in enumerate(summaries):
            # Add a slide with a title and content
            slide_layout = self.prs.slide_layouts[1]
            slide = self.prs.slides.add_slide(slide_layout)
            title = slide.shapes.title
            content = slide.placeholders[1]
            # Set the title and content
            title.text = f"Slide {i+1}"
            content.text = summary

        # Save the presentation
        self.prs.save(self.output_file)
    def save_ppt(self, outputname):
        self.prs.save(outputname)
        



