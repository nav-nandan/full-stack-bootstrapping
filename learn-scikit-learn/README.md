# learn-scikit-learn
Welcome to 'LEARN-SCIKIT-LEARN'!

This tutorial features `scikit-learn` (Machine Learning and Data Scientist's toolkit in Python) – from how to set up and get the ball rolling, to prototyping applications with it.

The tutorial is targeted to get your hands down and dirty with general machine learning concepts, highlighting features of `scikit-learn` for Data Science, and simply hacking your first prototype with `scikit-learn`.


## Scope of this tutorial
- Learn how to setup `scikit-learn` from scratch
- Understand basic concepts of machine learning
- Learn about some features in `scikit-learn`
- Build your first prototype using `scikit-learn`


## Target audience
This tutorial is for everyone who first think of a "programming language" on hearing the word `Python`.

If you've been introduced to `Statistics` or `Probability theory` and understand the difference between them (yes, they are two different things).


## Setup

### Windows
- Install python version 2.7.8 from https://www.python.org/downloads/
- Install pip and easy_install from https://pip.pypa.io/en/latest/installing.html and add to your PATH
- Install numpy, scipy, nose, matplotlib from http://www.scipy.org/install.html (binary and source packages available)
- Install scikit-learn from http://scikit-learn.org/stable/install.html#windows

### Linux or Mac
If you're using one of these, you're probably smart enough to figure out the setup by yourself (not really, it's simply straight-forward).

Once done, check your installation by keying in the following on the terminal or command line:
```
  $ python
  >>> import numpy
  >>> import scipy
  >>> import matplotlib
  >>> import sklearn
```


## References
In the past, we've used `scikit-learn` mainly for text classification tasks. Here are the system description papers for those tasks:
- <a href="http://alt.qcri.org/semeval2014/cdrom/pdf/SemEval2014091.pdf">Twitter Sentiment Analysis in Two Days</a>
- <a href="http://alt.qcri.org/semeval2014/cdrom/pdf/SemEval2014090.pdf">Aspect Based Sentiment Analysis</a>

Highly recommend to watch the video from Olivier Grisel (lead contributor to `scikit-learn`)

<a href="http://www.youtube.com/watch?feature=player_embedded&v=Zd5dfooZWG4
" target="_blank"><img src="http://img.youtube.com/vi/Zd5dfooZWG4/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

`scikit-learn` is well-documented and contributors are highly encouraged to provide examples:
- <a href="http://scikit-learn.org/stable/">The official page of `scikit-learn` </a>

Additional material on `numpy` and `scipy`:
- http://scipy-lectures.github.io/

For the advanced machine learning geek:
- <a href="https://us.pycon.org/2013/community/tutorials/23/">Further read on parallel machine learning using `scikit-learn`</a>
