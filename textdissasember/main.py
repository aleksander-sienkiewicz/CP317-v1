import fitz
import tabula
import pandas
from pptx import Presentation

class articleDissasembler:
    def __init__(self, fileName):
         self.fileName = fileName
         self.file = fitz.open(fileName)
         self.length = len(self.file)

    def extractTextAndImages(self):
        pages = []
        for x in range(0, self.length):
            # text stuff
            text = self.file[x].get_text().encode("utf8")
            decoded = text.decode()
            pages.append(decoded)
            #image stuff
            images = self.file[x].get_images()
            for index, y in enumerate(images, start=1):
                xref = y[0]
                pix = fitz.Pixmap(self.file, xref)
                pix.save("images/page_%s-image_%s.png" % (x, index))
        return(pages)
    def extractTables(self):
        #get images and text in each page

        tablepage = []

        #gets tables in each page
        for i in (range(1,(self.length+1))):
            stri = str(i)
            table = tabula.read_pdf(self.fileName, pages=stri, multiple_tables=True, stream='true')
  
            tablepage.append(table[0].to_numpy())

        return(tablepage)
         

a = articleDissasembler("test4.pdf")
b = a.extractTables()

print(b)

    




# prs = Presentation()
# bullet_slide_layout = prs.slide_layouts[1]

# slide = prs.slides.add_slide(bullet_slide_layout)
# shapes = slide.shapes

# title_shape = shapes.title
# body_shape = shapes.placeholders[1]

# title_shape.text = 'Adding a Bullet Slide'
# tf = body_shape.text_frame
# tf.text = t

# prs.save('./test.pptx')
