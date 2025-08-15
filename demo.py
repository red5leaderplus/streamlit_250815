import numpy as np
import pandas as pd
import streamlit as st

st.title('Demo Page')
st.write('123')
st.write('hahaha')

st.write('## 核取方塊')
r1 = st.checkbox("外帶")
if r1:
    st.info('外帶')
else:
    st.info('內用')

checks = st.columns(2)
txt = ''
with checks[0]:
    r11 = st.checkbox('A')
    if r11:
        txt += ' A '
with checks[1]:
    r12 = st.checkbox('B')
    if r12:
        txt += ' B '
st.info(txt)


st.write('## 選項按鈕')
b1 = st.radio('飲料:', ('咖啡', '果汁', '奶茶'))
st.info(b1)
st.write('## 選項按鈕')
b2 = st.radio('飲料:', ('咖啡', '果汁', '奶茶'), key='b2')
st.info(b2)

st.write('## 滑桿')
num = st.slider("請選擇數量:", 1.0, 5.0, 0.5)
st.info(num)

st.write('## 下拉選單')
city = st.selectbox('居住地', ('台北', '台南', '其他'))
if city=='台北':
    st.info('A')
elif city=='台南':
    st.info('D')
else:
    st.info('Other')

st.write('## 按鈕')
a = st.sidebar.number_input('num...')
b = st.sidebar.number_input('num2...', key='ni2')
if st.button('相加'):
    st.sidebar.info(a+b)
