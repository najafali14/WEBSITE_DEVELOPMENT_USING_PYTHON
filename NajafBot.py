#NAJAFALI
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=your_api_key)
model = genai.GenerativeModel('gemini-pro')
# %%time

import streamlit as st

message = st.chat_input('Enter your prompt...')
if message:
  st.write('You: ',message)

  response = model.generate_content(f'Hello {message}')

  rep = response.text
  st.write('NajafBot: ',rep)
else:
  pass


# if __name__ == "__main__":
