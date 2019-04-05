import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from os import path
from PIL import Image

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

mpl.rcParams['figure.figsize'] = (10.0, 8.0)
mpl.rcParams['font.size'] = 20
mpl.rcParams['savefig.dpi'] = 100
mpl.rcParams['figure.subplot.bottom'] = .1


def generate_wordcloud(stopwords, file_name, attribute):
    img_name = file_name.split('.')[0] + ".png"
    data = pd.read_csv(file_name)
    mask = np.array(Image.open("quora_logo.jpg"))
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=200,
        max_font_size=40,
        random_state=42,
        mask=mask
    ).generate(str(data[attribute]))
    image_colors = ImageColorGenerator(mask)
    fig = plt.figure(1)
    plt.imshow(wordcloud.recolor(color_func=image_colors), cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    fig.savefig(img_name, dpi=900)


generate_wordcloud(STOPWORDS, "malas.csv", "question_text")
