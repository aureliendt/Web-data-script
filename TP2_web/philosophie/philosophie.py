#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Ne pas se soucier de ces imports
import setpath
from flask import Flask, render_template, session, request, redirect, flash,url_for
from getpage import getPage
from functools import lru_cache


app = Flask(__name__)

app.secret_key = b'jf+%zz'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', message="Bonjour, monde !")


cache = {}
@app.route('/new-game', methods=['POST'])
def newgame():
    session['score']=1
    session['article'] = request.form['start']
    return redirect(url_for('game'))


@app.route('/game', methods=['GET'])
def game():
    global cache
    if session['article'] in cache:
        liste,title = cache[session['article']] ,session['article']
        return render_template('game.html', title=title, links=liste,cache=cache)
    else:
        liste, title = getPage(session['article'])
        cache[title] = liste
        if liste:
            return render_template('game.html', title=title, links=liste,cache=cache)
        else:
            flash('Vous avez perdu')
            return redirect(url_for('index'))




@app.route('/move', methods=['POST'])
def move():
    session['article'] = request.form["destination"]
    session['score']+=1
    if session['article'] == 'Philosophie':
        flash('Vous avez gagné!')
        return redirect(url_for('index'))
    else:

    #liste,title = getPage(session['article'])
        return redirect(url_for('game'))
# Si vous définissez de nouvelles routes, faites-le ici

if __name__ == '__main__':
    app.run(debug=True)
