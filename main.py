from typing import Text
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit for Very Beginner')
st.write('progress bar')

'Start!!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'DONE!!!'



# option = st.selectbox(
#     'Tell me your favorite number: ',
#     list(range(1, 11))
# )

text = st.text_input('What is your hobby?')
'Your hobby is ', text, '.' 

condition = st.slider('How are you?', 0, 100, 50)
'Your condition is ', condition, '.'


if st.checkbox('Wanna see cats?'):
    img = Image.open('cat.jpeg')
    st.image(img, caption='Cat', use_column_width=True)


# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)

# st.table(df.style.highlight_max(axis=0))

# """
# # Chapter
# ## Section
# ### Term

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """







