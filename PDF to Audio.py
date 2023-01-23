from gtts import gTTS
import PyPDF2

pdf_file = open("document.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    text = page.extractText()
    tts = gTTS(text)
    tts.save("audio.mp3")

pdf_file.close()
