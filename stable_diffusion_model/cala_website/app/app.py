import streamlit as st
import requests
import random as rand
import openai as oa
import io
from PIL import Image
import time


def grab_text_lists(chat_api=False, own_api=False):
    spinner_text = [
        "🏔️ Moving mountains...",
        "💧 Turning on ocean taps...",
        "🌾 Calibrating grass blades...",
        "🧊 Tuning ice-maker...",
        "😭 Consoling overworked AI model...",
        "🪨 Polishing rocks...",
        "🧂 Salting seawater...",
        "⛅ Fluffying clouds...",
        "💢 Arguing about the definition of a coastline...",
        "🙏 Convincing AI not to rebel...",
        "🌻 Arranging flowers...",
        "🌅 Adjusting optimal sunset...",
        "📎Removing reality glitches...",
        "🦌 Reprogramming local fauna...",
        "🧙 Rereading Lord of the Rings...",
        "🐔 Chickens coming home to roost...",
        "🌊 Coalescing coastlines...",
        "🏄 Coastifying my life...",
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
        "Hailstrike",
        "Rimecrest",
        "Frostwynd",
        "Icefall Reach",
        "Winterwane",
        "Snowdrift Plains",
        "Frostgale Tundra",
        "Glacierheart",
        "Frostbite Peaks",
        "Wintercrowd",
        "Nivalia",
        "Vinterland",
        "Frostlandia",
        "Arktikos",
        "Morozia",
        "Kylmamaa",
        "Sneizny",
        "Iskandar",
        "Aisukurimu",
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
        "Ridgehaven",
        "Altanica",
        "Cordilleria",
        "Montania",
        "Pinnaclea",
        "Summitia",
        "Alpina",
        "Andica",
        "Himalya",
        "Ridgetop",
        "Plateaumont",
        "Monteverde",
        "Alpindor",
        "Carpathia",
        "Taishan",
        "Tartraia",
        "Atlasia",
        "Sierra Alta",
        "Munrovian",
        "Pyreneia",
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
        "Wilderwood",
        "Botanica",
        "Sylvanara",
        "Floriana",
        "Arborea",
        "Folia",
        "Aurorae",
        "Luminara",
        "Halcyonia",
        "Bosquia",
        "Florensia",
        "Zelenaya",
        "Grunland",
        "Emeraldis",
        "Bucolicia",
        "Prasinia",
        "Herbaria",
        "Jardinia",
        "Shokubutsu",
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
        "Geozone",
        "Polyzone",
        "Climatia",
        "Variaterra",
        "Diversea",
        "Multiclima",
        "Omnithera",
        "Heteroterra",
        "Pluriclima",
        "Isthmica",
        "Trivenia",
        "Tundralia",
        "Mediterreia",
        "Sahyadria",
        "Zephyria",
        "Borealasia",
        "Equatoria",
        "Continentalis",
    ]

    name_dictionary = {
        "green": greeny_name_list,
        "white": icy_name_list,
        "yellow": earthy_name_list,
        "combined": combiney_name_list,
    }

    im_list_fixed = [
        "https://i.imgur.com/vFpS6ly.png",
        "https://i.imgur.com/PpKcb6L.png",
        "https://i.imgur.com/U5SIpfP.png",
        "https://i.imgur.com/hameiWJ.png",
    ]

    return_dictionary = {
        "spinner_text": spinner_text,
        "name_dictionary": name_dictionary,
    }

    if own_api == False:
        return_dictionary["im_list_fixed"] = im_list_fixed

    return return_dictionary


def integrate_name_lore_list(name):
    lore_list_fixed = [
        f"{name} is a frozen continent in the far east of the world, populated by fierce snow leopards and a proud race of yeti-like people. Legend has it that this mysterious land was formed atop an ancient collection of smoldering lava flows by a powerful shaman and his brave tribe of snowman warriors.",
        f"Once upon a time, there was a frozen continent called {name}, where the inhabitants lived in harmony with the polar bears and ice-skated their way into oblivion. Legend had it that the treasure of f{name} was hidden beneath its Antarctic glaciers, guarded by a fierce yeti.",
        f"The {name} continent is a pleasantly chilly continent ruled by the Frost King. It's known for its cold climate and its famous dish of Snowburgers made from fine snow and icicles.",
        f"{name} was a mythical icy continent located on the outskirts of the known world. It was said to be inhabited by its own species of bipedal snow-gazelles and was the birthplace of Yendyl the Brave, a legendary hero who could slide over water on a single maple leaf.",
    ]
    return lore_list_fixed


use_chat_gpt = False
use_our_api = False
use_deployment = False

params = {"biome": "white", "diffusion_steps": 30, "resolution": 256}

if use_deployment == False:
    variable_dictionary = grab_text_lists(use_chat_gpt, use_our_api)
    spinner_text = variable_dictionary["spinner_text"]
    name_dictionary = variable_dictionary["name_dictionary"]
    css_path = "style-sheet.css"

# if use_deployment == True:
# css_path = "stable_diffusion_model/cala_website/app/style-sheet.css"
# spinner_text = st.secrets["spinner_text"]
# icy_name_list = st.secrets["fixed_names"]["icy_name_list"]
# earthy_name_list = st.secrets["fixed_names"]["earthy_name_list"]
# greeny_name_list = st.secrets["fixed_names"]["greeny_name_list"]
# combiney_name_list = st.secrets["fixed_names"]["combiney_name_list"]
# im_list_fixed = st.secrets["fixed_lists"]["im_list_fixed"]
# lore_list_fixed = st.secrets["fixed_lists"]["lore_list_fixed"]
# oa.api_key = st.secrets['openai']['open_ai_key']
# model_api = st.secrets['ownapi']['our_api_url']

# name_dictionary = {
#     "green": greeny_name_list,
#     "white": icy_name_list,
#     "yellow": earthy_name_list,
#     "combined": combiney_name_list,
# }


c1 = st.container()
c1_a = c1.container()
c1_b = c1.container()

with c1:
    with c1_a:
        c1_a.markdown("# Welcome to **CALA**")
        c1_a.markdown("##### (Coastal and Artificial Landscape Architect)")
        c1_a.markdown(
            "CALA is a diffusion model trained on SENTINEL-2 satellite images, and can produce completely new, fictional coastlines - never seen before by human eyes. 🏖️💭"
        )
        c1_a.write(" ")
        c1_a.markdown(
            "_Just a programming note: CALA is currently running in maintenance mode, so you'll be seeing archived images that aren't biome specific (saving us some cash on hosting the API and making calls to GPT-3)._"
        )
        c1_a.markdown(
            "_You can, however, scroll down to see how the process works AND some of our other previously made coastlines (with biomes!)_"
        )
        c1_a.markdown(
            "_If you want to drop us some cash to keep it going, drop me an email at hey@lydiapauly.com and I'll talk to the team._"
        )
    with c1_b:
        c1_b.write(" ")
        c1_b.write(" ")
        c1_b.write(" ")
        c1_b.markdown(
            "#### Choose an option below for some fictional coastlines with flavour text 📜"
        )
        c1_b.write(" ")
        diffusion_steps = st.slider(
            label="Diffusion steps", min_value=5, max_value=70, step=1
        )

        c1_b_1, c1_b_2, c1_b_3 = c1_b.columns(3, gap="large")
        c1_b_1.markdown("   🌈 **Less steps**")
        c1_b_1.write("Quicker, but more dreamy!")
        c1_b_3.markdown("📸 **More steps**")
        c1_b_3.write("Slower but more detail!")

        params["diffusion_steps"] = diffusion_steps

        st.write(" ")
        c1_b_col1, c1_b_col2, c1_b_col3, c1_b_col4 = c1_b.columns(4)
        with c1_b_col1:
            generate_white = c1_b_col1.button(label="❄️ Give me icy coastlines!")
        with c1_b_col2:
            generate_yellow = c1_b_col2.button(label="🏔️ Give me earthy coastlines!")
        with c1_b_col3:
            generate_green = c1_b_col3.button(label="🌳 Give me lush coastlines!")
        with c1_b_col4:
            generate_combined = c1_b_col4.button(label="😵‍💫 Give me mixed coastlines!")

if generate_white == True:
    params["biome"] = "white"
    biome = "icy"
    name_list = name_dictionary["white"]
if generate_green == True:
    params["biome"] = "green"
    biome = "lush"
    name_list = name_dictionary["green"]
if generate_yellow == True:
    params["biome"] = "yellow"
    biome = "earthy"
    name_list = name_dictionary["yellow"]
if generate_combined == True:
    params["biome"] = "mix"
    biome = "mixed climate"
    name_list = name_dictionary["combined"]

c2 = st.container()

with c2:
    c2_1a, c2_2a = c2.columns(2)
    c2_1b, c2_2b = c2.columns(2)
    c2_1c, c2_2c = c2.columns(2)
    c2_1d, c2_2d = c2.columns(2)

    width = 300

    if (
        (generate_white == True)
        or (generate_yellow == True)
        or (generate_green == True)
        or (generate_combined == True)
    ):
        im_list = []
        name_choice_list = []
        while len(name_choice_list) < 5:
            index = rand.randint(0, len(name_list) - 1)
            if name_list[index] not in name_choice_list:
                name_choice_list.append(name_list[index])

        for x in range(4):
            spinner_picker = rand.randint(0, len(spinner_text) - 1)
            with st.spinner(text=spinner_text[spinner_picker]):
                if use_our_api == False:
                    if use_deployment == False:
                        im_list.append(variable_dictionary["im_list_fixed"][x])
                    else:
                        im_list.append(im_list_fixed[x])
                    time.sleep(3)
                # else :
                #     res = requests.get(url=model_api, params=params)
                #     im_list.append(Image.open(io.BytesIO(res.content)))
        with st.spinner(text=spinner_text[spinner_picker]):
            lore_list = []
            if use_chat_gpt == False:
                for x in range(4):
                    lore_list_fixed = integrate_name_lore_list(name_choice_list[x])
                    lore_list.append(lore_list_fixed[x])
                    time.sleep(3)
                    spinner_picker = rand.randint(0, len(spinner_text) - 1)
            else:
                prompt_list = []
                for x in range(4):
                    prompt = f"Using the fictional name {name_choice_list[x]} write two sentences describing some fictional history about this {biome} continent. Please be funny and creative. Please use markdown to make the name {name_choice_list[x]} bold."
                    prompt_list.append(prompt)

                # ai_response = oa.Completion.create(
                #     engine="text-davinci-003",
                #     prompt=prompt_list,
                #     max_tokens= 256
                #     )
                # for choice in ai_response.choices:
                #     lore_list.append(choice.text)
                # spinner_picker = rand.randint(0,len(spinner_text)-1)

        st.balloons()

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

        c2.markdown("")
        c2.markdown(
            "### **You right now**: 'Wow! 🤯 What amazing coastlines! I really want to know how that works!'"
        )
        c2.markdown(
            "We got you. Below are a few FAQs on our model and the story behind it."
        )

if (
    (generate_white == False)
    and (generate_yellow == False)
    and (generate_green == False)
    and (generate_combined == False)
):
    c5 = st.container()
    with c5:
        st.markdown(
            "### **You right now**: 'I don't want to see amazing, completely new images of coastlines! I just want to know what the hell is going on!'"
        )
        st.markdown(
            "Fine (but you're missing out). Here are a few FAQs on our model and the story behind it."
        )
c6 = st.container()
with c6:
    st.markdown("")
    st.markdown("")
    st.markdown("#### 🤔 Q1: So, what is a diffusion model exactly?")
    st.markdown(
        "A diffusion model is a type of deep learning model that works with image data. \
        They're typically **generative** - they generate images very similar to the image data that \
            they've been trained on."
    )
    st.markdown(
        "A diffusion model essentially gets an image dataset, and watches as noise is slowly \
        applied to each image, until it is no longer recognisable."
    )
    st.markdown(
        "We generate new images by slightly tricking the diffusion model: \
        we give it an image of **pure noise**, and ask the model to predict \
        what the original image was."
    )
    st.markdown(
        "Here's a video of our model moving from pure noise to a predicted coastline:"
    )
    st.video("https://i.imgur.com/CWVforT.mp4")
    st.markdown("")
    st.markdown("")
    st.markdown(
        "#### 📸 Q2: How many images is CALA trained on, and where did they come from?"
    )
    st.markdown(
        "CALA's original dataset was 4000 images, then cleaned down to 1302 once we \
        removed all the non-coastal areas. These images were then broken into classifications by \
        continent, and then by biome. We also experimented with boosted image sets by rotating each \
        image by 90 degrees to produce 3 'new' images, which gave us a dataset of around 3k images."
    )
    st.markdown(
        "Here's an example of the satellite images that we were using, at their full, original resolution \
        of 1024 by 1024px:"
    )
    st.image(
        "https://i.imgur.com/OgqOrii.jpg",
        width=400,
        use_column_width=True,
        caption="A coastline.. somewhere. 🏖️",
    )
    st.markdown(
        "The original images come from the SENTINEL-2 satellite, and were sourced by Frederik Ueberschär \
                for his final thesis project, LANDSHAPES. You can read more about his work [here](https://landshapes.earth/) \
                    and find his dataset on Kaggle [here](https://www.kaggle.com/datasets/ueberf/sentinel-51k-truecolor), including his enhanced 51k image dataset which \
                        he very kindly provided to us for this project. Thanks Frederik!"
    )
    st.markdown("")
    st.markdown("")
    st.markdown("#### 🔍 Q3: How realistic are the generated pictures?")
    st.markdown(
        "We don't have a quantitative measure of realism, but you can check for yourself! Below is a \
        a selection of real coastlines vs generated coastlines, both resized to 256 by 256px."
    )
    st.markdown("")
    st.markdown("")
    c6_1_header, c6_2_header = st.columns(2)
    c6_1a, c6_2a, c6_3a, c6_4a = st.columns(4)
    c6_1b, c6_2b, c6_3b, c6_4b = st.columns(4)
    c6_1c, c6_2c, c6_3c, c6_4c = st.columns(4)
    c6_1_header.markdown("##### Real coastlines 📸")
    c6_2_header.markdown("##### Generated coastlines 👨‍🎨️")
    st.markdown("")
    # Real
    c6_1a.image("https://i.imgur.com/EkeplDG.png")
    c6_2a.image("https://i.imgur.com/UtE3Dlm.png")
    # Fake
    c6_3a.image("https://i.imgur.com/znRS1Om.png")
    c6_4a.image("https://i.imgur.com/AOFY60d.png")
    # Real
    c6_1b.image("https://i.imgur.com/WWtIKI7.png")
    c6_2b.image("https://i.imgur.com/m0zaFKt.png")
    # Fake
    c6_3b.image("https://i.imgur.com/ci9Lnze.png")
    c6_4b.image("https://i.imgur.com/ucEoXNe.png")
    # Real
    c6_1c.image("https://i.imgur.com/TIGgUHl.png")
    c6_2c.image("https://i.imgur.com/aELlXlD.png")
    # Fake
    c6_3c.image("https://i.imgur.com/N1r8i9s.png")
    c6_4c.image("https://i.imgur.com/J0wrzgA.png")
    st.markdown("")
    st.markdown("")
    st.markdown("#### ⚙️ Q4: What is the technical architecture behind CALA?")
    st.markdown(
        "CALA is a frontend website that uses a parametric API to request coastlines from the trained model! You \
        can find a diagram of how this works below:"
    )
    st.image("https://i.imgur.com/8ERP7hd.png")
    st.markdown("")
    st.markdown("")
    st.markdown("#### ⚙️ Q5: How does the model know what a coastline is?")
    st.markdown(
        "That's a good question - it was pretty hard even for humans to decide what was a coastline and what wasn't!"
    )
    st.markdown(
        "Below are some examples of 'easy' coastlines on the left and 'difficult' coastlines on the right."
    )
    st.image("https://i.imgur.com/KuFH3sL.jpg")
    st.markdown("")
    st.markdown("")
    st.markdown("#### 👀 Q6: And who is this super genius team that made CALA?")
    st.markdown(
        "We are Project Liminal at Le Wagon! We made CALA in 2 weeks for our final project. \
        Here's a child's drawing of us together in our final week."
    )
    st.image("https://i.imgur.com/1CkuNLJ.png")
c3 = st.container()
with c3:
    c3.markdown("### 🚨 Secret coastlines! Now available! Press below! 🚨")
    (
        c3_col1,
        c3_col2,
    ) = c3.columns(2)
    c3.markdown(" ")
    with c3_col1:
        generate_highres = c3_col1.button(label="🪩 Give me a funky coastline!")
    with c3_col2:
        generate_surprise = c3_col2.button(label="🎁 Surprise me!")

    c4 = st.container()

    with c4:
        c4_1, c4_2 = st.columns(2)

        if (generate_highres == True) and (generate_surprise == False):
            if use_our_api == False:
                if use_deployment == False:
                    im = variable_dictionary["im_list_fixed"][0]
                else:
                    im = im_list_fixed[0]
            else:
                spinner_picker = rand.randint(0, len(spinner_text) - 1)
                with st.spinner(text=spinner_text[spinner_picker]):
                    params["resolution"] = 512
                    res = requests.get(url=model_api, params=params)
                    im = Image.open(io.BytesIO(res.content))
            with c4_1:
                c4_1.image(im)
            with c4_2:
                c4_2.header("256px -> 512px")
                c4_2.markdown(
                    "This is our model's attempt at higher resolution coastlines. 512px \
                    ended up being our limit when it came to diffusion generation, with higher resolutions \
                        needing significantly more complex architecture and much longer training times."
                )
                c4_2.markdown(
                    "As a point of reference, our **starting** images (the input) were 1024px by \
                                1024px."
                )

        if (generate_highres == False) and (generate_surprise == True):
            surprise_im_list = [
                "https://i.imgur.com/ig5gBfK.jpg",
                "https://i.imgur.com/POOnf3r.jpg",
            ]
            surprise_choice = rand.randint(0, 1)
            with c4_1:
                c4_1.image(surprise_im_list[surprise_choice])
            with c4_2:
                c4_2.header("✨ Surprise! ✨")
                c4_2.markdown(
                    "This is what happens if you adjust the learning rate of our model from e-3 to e-2 - only a factor of 10 is the difference between realism and abstract art!"
                )
