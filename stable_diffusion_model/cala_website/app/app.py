import streamlit as st
import numpy as np
import pandas as pd
import requests
import random as rand
import openai as oa
import io
from PIL import Image
import time


model_api = "https://api-second-version-hoqbdqxmgq-ew.a.run.app/generate"
oa.api_key = st.secrets.openai.open_ai_key

use_chat_gpt = False
use_our_api = False

params = { 'biome' : 'white',
          'diffusion_steps' : 30,
          'resolution' : 256}

spinner_text = st.secrets.spinner_text
icy_name_list = st.secrets.fixed_names.icy_name_list
earthy_name_list = st.secrets.fixed_names.earthy_name_list
greeny_name_list = st.secrets.fixed_names.greeny_name_list
combiney_name_list = st.secrets.fixed_names.combiney_name_list
lore_list_fixed = st.secrets.lore_list_fixed
im_list_fixed = st.secrets.im_list_fixed

with open("stable_diffusion_model/cala_website/app/style-sheet.css") as css :
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

    c1 = st.container()
    c1_a = c1.container()
    c1_b = c1.container()

    with c1 :
        with c1_a :
            c1_a.markdown('# Welcome to **CALA**')
            c1_a.markdown('(Coastal Automated Learning Algorithm)')
            c1_a.markdown('Choose an option below for some fictional coastlines')

        with c1_b :
            c1_b_col1, c1_b_col2, c1_b_col3, c1_b_col4 = c1_b.columns(4)
            with c1_b_col1 :
                generate_white = c1_b_col1.button(label="Give me icy coastlines!")
            with c1_b_col2 :
                generate_yellow = c1_b_col2.button(label="Give me earthy coastlines!")
            with c1_b_col3 :
                generate_green = c1_b_col3.button(label='Give me lush coastlines!')
            with c1_b_col4 :
                generate_combined = c1_b_col4.button(label="Give me mixed coastlines!")

    if generate_white == True:
        params['biome'] = 'white'
        biome = "icy"
        name_list = name_dictionary['white']
    if generate_green == True:
        params['biome'] = 'green'
        biome = "lush"
        name_list = name_dictionary['green']
    if generate_yellow == True:
        params['biome'] = 'yellow'
        biome = "earthy"
        name_list = name_dictionary['yellow']
    if generate_combined == True:
        params['biome'] = 'mix'
        biome = "mixed climate"
        name_list = name_dictionary['combined']

    c2 = st.container()

    with c2 :
        c2_1a, c2_2a = c2.columns(2)
        c2_1b, c2_2b = c2.columns(2)
        c2_1c, c2_2c = c2.columns(2)
        c2_1d, c2_2d = c2.columns(2)

        width=300

    if (generate_white == True) or (generate_yellow == True) or (generate_green == True) or (generate_combined == True):
        im_list = []
        name_choice_list = []
        while len(name_choice_list) < 5 :
            index = rand.randint(0,len(name_list)-1)
            if name_list[index] not in name_choice_list: name_choice_list.append(name_list[index])

        for x in range(4) :
            spinner_picker = rand.randint(0,len(spinner_text)-1)
            with st.spinner(text=spinner_text[spinner_picker]) :
                if use_our_api == False :
                    im_list.append(im_list_fixed[x])
                    time.sleep(7)
                else :
                    res = requests.get(url=model_api, params=params)
                    im_list.append(Image.open(io.BytesIO(res.content)))
        with st.spinner(text=spinner_text[spinner_picker]) :
            lore_list = []
            if use_chat_gpt == False :
                for x in range(4) :
                    name = name_list[x]
                    lore_list.append(lore_list_fixed[x])
                    time.sleep(7)
                    spinner_picker = rand.randint(0,len(spinner_text)-1)
            else :
                prompt_list = []
                for x in range(4) :
                    prompt = f"Using the fictional name {name_choice_list[x]} write two sentences describing some fictional history about this {biome} continent. Please be funny and creative. Please use markdown to make the name {name_choice_list[x]} bold."
                    prompt_list.append(prompt)

                ai_response = oa.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt_list,
                    max_tokens= 256
                    )
                for choice in ai_response.choices:
                    lore_list.append(choice.text)
                spinner_picker = rand.randint(0,len(spinner_text)-1)

        st.balloons

        with c2_1a:
            c2_1a.image(im_list[0], width=width)

        with c2_2a:
            c2_2a.header(name_choice_list[0])
            c2_2a.markdown(lore_list[0])

        with c2_1b:
            c2_1b.image(im_list[1], width=width)

        with c2_2b:
            c2_2b.header(name_choice_list[1])
            c2_2b.markdown(lore_list[1])

        with c2_1c:
            c2_1c.image(im_list[2], width=width)

        with c2_2c:
            c2_2c.header(name_choice_list[2])
            c2_2c.markdown(lore_list[2])

        with c2_1d:
            c2_1d.image(im_list[3], width=width)

        with c2_2d:
            c2_2d.header(name_choice_list[3])
            c2_2d.markdown(lore_list[3])
