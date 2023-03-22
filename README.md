<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://i.imgur.com/roiwwiB.png" alt="Logo">
  </a>
<h3 align="center">Welcome to CALA (Coastal and Artificial Landscape Architect) :palm_tree:</h3>
  <p align="left">
    CALA is a generative AI model built with Diffusion architecture that examines satellite imagery from ESA's SENTINEL-2, and creates entirely fictional satellite imagery of coastlines. 
    <br />
    <p align="left"> You can try it out <a href=https://cala-website.streamlit.app/>here</a>! :sparkles: Recommended settings are <b>33 diffusion steps</b> on <b>earthy</b> or <b>icy</b>. </p>
    <p align="left"> This repo contains all the public-facing code that goes into CALA, including our: </p>
      <ul align="left">
        <li> First early GAN models, with annotated explanations via Jupyter notebook
        <li> Final Diffusion model, with an annotated notebook
        <li> Website files for hosting on Streamlit
        <li> Packaged PY files for hosting the model locally and online
        <li> A notebook with the write up of our process, with results and learnings
      </ul>
    </p>
    <p align='left'> CALA was built in 2 weeks for our final project on the Le Wagon Data Science bootcamp</p>
    <p align='left'> If you're sufficiently impressed with our work, find our team member LinkedIns below</p>
    <p align='left'> <a href="https://github.com/LimesAndCrimes/project_liminal/issues">I caught a bug!</a></p>
</div>

## Our team members (and their contact details!)
* <b>Lydia Pauly</b> --> [![LinkedIn][linkedin-shield]][linkedin-url-lydia]  
* <b>Tomas Garciá</b> --> [![LinkedIn][linkedin-shield]][linkedin-url-tomas]  
* <b>Yamin Jamilzoda</b> --> [![LinkedIn][linkedin-shield]][linkedin-url-yamin]  
* <b>Johannes Rothschink</b> --> [![LinkedIn][linkedin-shield]][linkedin-url-johannes] 

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://cala-website.streamlit.app/)

### Built With
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)

<!-- GETTING STARTED -->
### Original mission

The project was inspired by another project, LANDSHAPES by Frederik Ueberschär (website <a href=https://landshapes.earth/> here</a>). His project uses StyleGAN2 to generate interpolation videos of fictional coastlines, in order to reprompt 'climate fascination' with his audience. 

We loved his project so much that we reached out to ask him about it and if he was willing to make his original dataset free. Amazing, Frederik responded in less than 24 hours with his original dataset, his extended dataset, lots of reading on his process, and his spiritual blessing for CALA. And from that moment, team Liminal was born and we could begin work! :hammer:

Our original mission was this: <b> to produce 5, good quality images of fictional coastlines using our own custom-built AI model.</b>

### Our very first GAN

Because Frederik built LANDSHAPES in StyleGan2, we began to build our own GAN. Using a public example based on the handwritten digits dataset, we upgraded out model for 3 RGB channels and a higher resolution of 128 x 128. 

GANs typically work by trying to generate coastlines from pure noise in one step. A discrimator - essentially a classification model - trains at the same time by examining the generated images and 

### End result

And we did! We've generated far more than 5 good quality coastlines. Here are just a selection below:

![Example Screen Shot][example-screenshot]



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/LimesAndCrimes/project_liminal.svg?style=for-the-badge
[contributors-url]: https://github.com/LimesAndCrimes/project_liminal/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/LimesAndCrimes/project_liminal.svg?style=for-the-badge
[forks-url]: https://github.com/gLimesAndCrimes/project_liminal/network/members
[stars-shield]: https://img.shields.io/github/stars/LimesAndCrimes/project_liminal.svg?style=for-the-badge
[stars-url]: https://github.com/LimesAndCrimes/project_liminal/stargazers
[issues-shield]: https://img.shields.io/github/issues/LimesAndCrimes/project_liminal.svg?style=for-the-badge
[issues-url]: https://github.com/LimesAndCrimes/project_liminal/issues
[license-shield]: https://img.shields.io/github/license/LimesAndCrimes/project_liminal.svg?style=for-the-badge
[license-url]: https://github.com/LimesAndCrimes/project_liminal/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=0072b1
[linkedin-url-lydia]: https://linkedin.com/in/lydia-pauly
[linkedin-url-tomas]: https://linkedin.com/in/tgarciar
[linkedin-url-johannes]: https://linkedin.com/in/johannes-rothschink
[linkedin-url-yamin]: https://linkedin.com/in/yamin-j
[product-screenshot]: https://i.imgur.com/JwjpidQ.png
[example-screenshot]: https://i.imgur.com/RwT04mM.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[Python.org]: https://img.shields.io/badge/python-ffde57?style=for-the-badge&logo=python
[Python-url]: https://www.python.org/ 
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
