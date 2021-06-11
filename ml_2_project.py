# -*- coding: utf-8 -*-
"""
Created on Thu May 13 09:51:08 2021

@author: Atul singh
"""
"""
!pip install easyocr
!pip install googletrans
!pip install gTTS
!pip install googletrans==4.0.0-rc1

"""
#%%
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
from googletrans  import Translator
import easyocr
from gtts import gTTS
from IPython.display import Audio

#%%

reader = easyocr.Reader(['ta'])
translator = Translator()


#%%


import PIL 
from PIL import ImageDraw
dir="D:\prj/tamil.png"
im = PIL.Image.open(dir)
im


bounds = reader.readtext(dir,add_margin= 0.55, width_ths=0.7, link_threshold =0.8, decoder ='beamsearch',blocklist='=.')
                         
bounds


def draw_boxes(image,bounds, color= 'yellow',width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0,p1,p2,p3 =bound[0]
        draw.line([*p0, *p1, *p2, *p3 , *p0],fill= color ,width= width)
    return image
draw_boxes(im,bounds)


text_list = reader.readtext(dir, add_margin=0.55, width_ths=0.7, link_threshold=0.8, decoder='beamsearch',blocklist= '=.',detail=0)
text_list

#%%
text_comb =' '.join(text_list)
text_comb

print(translator.detect(text_comb))

#%%

text_en = translator.translate(text_comb,src='kn')
print(text_en.text)

#%%
ta_tts= gTTS(text_en.text)
ta_tts.save('D:\prj/trans.mp3')

Audio('D:\prj/trans.mp3',autoplay=True)

#%%
ta_tts= gTTS(text_en.text, lang='ja')
ta_tts.save('trans.mp3')

Audio('trans.mp3',autoplay= True)

#%%
text_hi= translator.translate(text_comb, src='ta',dest='hi')
print(text_hi.text)

ta_tts_hi= gTTS(text_hi.text, lang='hi')
ta_tts_hi.save('trans_hi.mp3')

Audio('trans_hi.mp3',autoplay= True)

#%%
