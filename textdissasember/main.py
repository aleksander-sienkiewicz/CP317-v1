import fitz
import tabula
import pandas
import os


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
        page = []
        tablepage = []

        #gets tables in each page
        for i in (range(1,(self.length+1))):
            stri = str(i)
            table = tabula.read_pdf(self.fileName, pages=stri, multiple_tables=True, stream='true')

            for i in table:
                page.append(i.to_records())
            tablepage.append(page)
            page = []

        return(tablepage)
    def extractParagraphs(self):
        page = self.extractTextAndImages()
        temp = ""
        paragraph = ""
        paraPage = []
        denom = 1
        numer = 1
        for x in range(0, len(page)):
            paragraphs = []
            for y in range(0, len(page[x])):
                if (page[x][y] == "\n"):
                    numer += len(temp)
                    denom += 1
                    temp =""
                else:
                    temp += page[x][y]
        temp = ""
        avg = numer/denom

        for x in range(0, len(page)):
            paragraphs = []
            for y in range(0, len(page[x])):
                if (page[x][y] == "\n"):
                    if (len(temp) < avg):
                        if (len(paragraph) < avg*4 and len(paragraphs)-1 > 0):
                            paragraphs[len(paragraphs)-1] += paragraph
                        else:
                            paragraph += temp
                            paragraphs.append(paragraph)
                        paragraph = ""
                    else:
                        paragraph += temp
                    temp = ""
                else:
                    temp += page[x][y]
            paraPage.append(paragraphs)
        final = []
        for x in range(0, len(paraPage)):
            finalParas = []
            for y in range(0, len(paraPage[x])):
                if (len(paraPage[x][y]) > avg*3):
                    finalParas.append(paraPage[x][y])
            final.append(finalParas)
        
        
        return(final)


a = articleDissasembler("test2.pdf")

b = a.extractParagraphs()
    
print(b[0][1])




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
