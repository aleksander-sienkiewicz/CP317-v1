import fitz
import tabula
import pandas
import os
from transformers import pipeline
import nltk


class articleDissasembler:
    def __init__(self, fileName):
         self.fileName = fileName
         self.file = fitz.open(fileName)
         self.length = len(self.file)
         self.images = [] # where the images are located by page
         self.text = [] # text from the file
         self.endOfPage = [] # where the end of the page is located used for text to image corrolation
         self.tables = [] # where the tables are located by page

    def extractTextAndImages(self):
        final = ""
        endOfPage = []

        for x in range(0, self.length):
            # text stuff
            text = self.file[x].get_text().encode("utf8")
            decoded = text.decode()
            final += " "
            final += decoded
            endOfPage.append(len(final)// 1024)
            #image stuff
            imagesName = []
            images = self.file[x].get_images()
            for index, y in enumerate(images, start=1):
                imagesName.append("images/page_%s-image_%s.png" % (x, index))
                xref = y[0]
                pix = fitz.Pixmap(self.file, xref)
                pix.save("images/page_%s-image_%s.png" % (x, index))
            self.images.append(imagesName)
        self.text = final
        self.endOfPage = endOfPage

        
    def extractTables(self):
        #get images and text in each page
        tablepage = []

        #gets tables in each page
        for i in (range(1,(self.length+1))):
            page = []
            stri = str(i)
            table = tabula.read_pdf(self.fileName, pages=stri, multiple_tables=True, stream='true')

            for i in table:
                page.append(i.to_records())
            tablepage.append(page)

        self.tables = tablepage

    def summarize_pdf(self, text):
        # Read the PDF document
            
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


# a = articleDissasembler("DesignDocument.pdf")
# a.extractTables()
# a.extractTextAndImages()
# print(a.tables)
# print(a.endOfPage)
# print(a.images)
# b = a.summarize_pdf(a.text)
# for i in b:
#     print(i)
# print(a.endOfPage)