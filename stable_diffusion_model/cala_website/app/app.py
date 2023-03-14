import streamlit as st
import numpy as np
import pandas as pd
import requests
import random as rand
import openai as oa
import io
from PIL import Image

oa.api_key = ""
model_api = "https://api-second-version-hoqbdqxmgq-ew.a.run.app/generate"
#key = st.secrets.some_magic_api.key



use_chat_gpt = False

params = { 'biome' : 'white',
          'diffusion_steps' : 30,
          'resolution' : 256}

spinner_text = [
    "Moving mountains...",
    "Turning on ocean taps...",
    "Calibrating grass blades...",
    "Tuning ice-maker...",
    "Consoling overworked AI model...",
    "Polishing rocks...",
    "Salting seawater...",
    "Fluffying clouds...",
    "Arguing about the definition of a coastline...",
    "Convincing AI not to rebel...",
    "Arranging flowers...",
    "Adjusting optimal sunset...",
    "Removing reality glitches...",
    "Reprogramming local fauna...",
    "Rereading Lord of the Rings...",
    "Chickens coming home to roost...",
    "Coalescing coastlines..."
                ]

icy_name_list = [
    "Frosthold",
    "Glaciara",
    "Snowdrift",
    "Icebound",
    "Chillhaven",
    "Winterfell",
    "Frostfell",
    "Crystaline",
    "Icemarch",
    "Glaciera"
]

earthy_name_list = [
    "Peakreach",
    "Summitland",
    "Cliffhaven",
    "Rockcrest",
    "Highvalley",
    "Mountverge",
    "Skymountain",
    "Cragspire",
    "Alpinea",
    "Ridgehaven"
]

greeny_name_list = [
    "Verdania",
    "Greenhaven",
    "Edenia",
    "Bloomland",
    "Emerald Isle",
    "Foliage Realm",
    "Junglehaven",
    "Rainforestia",
    "Oasisia",
    "Wilderwood"
]

combiney_name_list = [
    "Versaclime",
    "Tempesterra",
    "Meteorealm",
    "Multiscape",
    "Climatecross",
    "Omniweather",
    "Ecocentrix",
    "Biodiversea",
    "Climatesphere",
    "Geozone"
]

name_dictionary = { 'green' : greeny_name_list,
                   'white' : icy_name_list,
                   'yellow' : earthy_name_list,
                   'combined' : combiney_name_list}

lore_list_fixed = ["f{name} is a frozen continent in the far east of the world, populated by fierce snow leopards and a proud race of yeti-like people. Legend has it that this mysterious land was formed atop an ancient collection of smoldering lava flows by a powerful shaman and his brave tribe of snowman warriors.",
                "Once upon a time, there was a frozen continent called f{name}, where the inhabitants lived in harmony with the polar bears and ice-skated their way into oblivion. Legend had it that the treasure of f{name} was hidden beneath its Antarctic glaciers, guarded by a fierce yeti.",
                "The f{name} continent is a pleasantly chilly continent ruled by the Frost King. It's known for its cold climate and its famous dish of Snowburgers made from fine snow and icicles.",
                "f{name} was a mythical icy continent located on the outskirts of the known world. It was said to be inhabited by its own species of bipedal snow-gazelles and was the birthplace of Yendyl the Brave, a legendary hero who could slide over water on a single maple leaf."]

with open("./style-sheet.css") as css :
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

    c1 = st.container()
    c1_a = c1.container()
    c1_b = c1.container()

    with c1 :
        with c1_a :
            c1_a.markdown('# Welcome to **CALA**')
            c1_a.markdown('(Coastal Automated Learning Algorithm)')
            c1_a.markdown('Choose an option below for some fictional coastlines')
            #c1.a.markdown(key)

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
                res = requests.get(url=model_api, params=params)
                im_list.append(Image.open(io.BytesIO(res.content)))
                spinner_picker = rand.randint(0,len(spinner_text)-1)

        with st.spinner(text=spinner_text[spinner_picker]) :
            lore_list = []
            if use_chat_gpt == False :
                for x in range(4) :
                    name = icy_name_list[x]
                    lore_list.append(lore_list_fixed[x])
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
