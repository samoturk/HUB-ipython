# HUB-ipython
##HUB (Heidelberg Unseminars in Bioinformatics) about IPython and chemoinformatics
This repository contains material for [HUB 21](http://www.hub-hub.de/wordpress/?tribe_events=hub-21-interactive-notebooks-try-out-programming-jupyteripython-chemoinformatics)
  
### Location and date
BioMed X, Im Neuenheimer feld 583, Heidelbeg, 21 January 2016

### How to run code here
I recommend [Anaconda](https://www.continuum.io/downloads) Python distribution with Python 2.7. In Anaconda terminal type `jupyter notebook` and navigate to folder with notebooks.  
  
If you can't install Python on your computer you can use [tmpnb.org](tmpnb.org) to experiment with Jupyter.
  
Pair programming presentation can be converted to html and served with:
```bash
jupyter nbconvert Pair\ programming.ipynb --to slides --post serve --ServePostProcessor.port=8910
```
#### Current plans are to include this:

* short intro about BioMed X
* an ice-breaker - maybe the 'classic' standing in a line/grid to describe our experience coding, which we can also use for teaming people up for later activities - a group of experienced coders goes to the part of the room where people haven't done any coding before, and we find experienced partners for each of them
* a demo from Samo of IPython in chemoinformatic context
* maybe someone else demos something similar using a different language (R? Perl?)
* pair-programming together, using examples from [Rosalind](http://rosalind.info/problems/locations/) exercises (and some additional [chemoinfo](exercises/README.md) excercises)

angle we'd use to publicise the event would be:

* never coded before? come and try out coding with experts, to see what it's like
* interested in seeing what iPython/jupyter can do? come along and check it out - especially if you're into chemoinformatics - note that similar stuff is available for other languages
* chance to try out pair programming

For this, we'll ideally have a bunch of people joining the event who will bring their own laptops, have appropriate software set up and running, so that we have enough laptops to pair-program with everyone - if not, maybe we try doing it in groups of 3. 

### TODO
- [ ] prepare intro notebook
- [ ] document dependencies
- [ ] install instructions
- [ ] list optional chemo/bioinfo and visualisation libs
- [ ] check how to make jupyter work with other programming languages
- [ ] docker scripts
- [ ] guest wifi vouchers 
- [ ] buy beer
