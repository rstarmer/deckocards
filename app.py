'''
Copyright 2020 Robert Starmer <robert@kumul.us>

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

This app is a simple way to generate 13 card sets out of a Deck of Cards
with the card suits mapped to exercises.

See "start.sh" for running the app, or better yet, build the container and
run it locally.
'''

from flask import Flask, escape, request, redirect, url_for, render_template
import random
from datetime import datetime
import os
import sys

app = Flask(__name__)

default_reps=["1","2","3","4"]

@app.route('/')
def index():
    seed=datetime.strftime(datetime.now().date(),'%m%d%y')
    return redirect(url_for('draw',seed=seed,set='1'))

@app.route('/go')
def draw():
    cards=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
    suits=[]
    rep_set=[]

    suits.append(request.args.get("diamonds","pushups"))
    suits.append(request.args.get("spades","squats"))
    suits.append(request.args.get("clubs","jjaxs"))
    suits.append(request.args.get("hearts","crunches"))
    seed=request.args.get("seed","")
    rep_set.append(request.args.get("set","1,2,3,4"))

    if not rep_set[0] in default_reps:
        rep_set=[1]
        next_set=None
    else:
        rep_set=[int(rep_set[0])]
        if rep_set[0] < 4:
            next_set="/go?set={}&diamonds={}&spades={}&clubs={}&hearts={}&seed={}".format(
                rep_set[0]+1,
                suits[0],
                suits[1],
                suits[2],
                suits[3],
                seed
            )
        else:
            next_set=None

    if not seed == '':
        try:
            random.seed(int(seed))
        except:
            pass
    random.shuffle(cards)
    return render_template('cards.html', cards=cards, suits=suits, rep_set=rep_set, seed=seed, next_set=next_set)
