import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time



st.title('Streamlit入門')
st.write('プログレスバーの表示')
'Start!!'

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!'

# left_column, right_column=st.beta_columns(2)
# button=left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')

# option=st.text_input('あなたの趣味を教えて下さい')
# 'あなたの趣味は:',option

# condition=st.slider('あなたの今の調子は？',0,100,50)
# 'コンディション:',condition

# if st.checkbox('Show Image'):
#     img=Image.open('IMG_9482.jpg')
#     st.image(img,caption='taikoushi',use_column_width=True)


