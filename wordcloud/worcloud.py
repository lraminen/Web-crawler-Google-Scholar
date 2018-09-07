import json
from PIL import Image
import numpy as np
import matplotlib.pyplot as plot
from wordcloud import WordCloud,ImagrColorGenerator,STOPWORDS


#This is the module from which the wordcloud is created: https://github.com/amueller/word_cloud/tree/master/examples

def get_text(file=r'C:\Users\leela\gscholar\tutorial\quotes.json'):
    text=''
    words=[]
    with open(file,'r') as f:
        for line in f.readlines():
            data=json.loads(line)
            words+=data['subject']
    for word in words:
        text=text+''+word
    return text
text=get_text()

#This creates a shape for the wordcloud image - can be used or not (optional)
#Can also add more details to process the text or modify the image.
shape=np.array(Image.open(r'C:\Users\leela\gscholar\wordcloud\dna.png'))
wc=WordCloud(mask=shape)
wc.generate(text)
image_colors=ImageColorGenerator(shape)
plot.imshow(wc.recolor(color_func=image_colors),interpolation='biliniear')
plot.axis('off')

plot.show()
wc.to_file(r'C:\Users\leela\gscholar\wordcloud\wordcloud.png')
