#llibreries
from xkcd import *
from flask import render_template
from flask import Flask

app = Flask(__name__)#nuevo objeto


@app.route('/')
#@app.before_first_request
def funcio_inici(title = None, img_link=None, img_output=None):
	global Comic_act 
	Comic_act = getRandomComic() #reps random comic
	global num 
	num = Comic_act.number
	title = Comic_act.getTitle() #agafem el titol
	img_link = Comic_act.link #agafem link de la imatge
	img_output = Comic_act.getImageLink() #descarreguem la imatge a downloads(per defecte) amb un nom per defecte
	return render_template('comic.html', title=title, img_link=img_link, img_output=img_output)

@app.route('/prev/')
def funcio_prev(title = None, img_link=None, img_output=None):
	
	global num 
	if num > 0:
		num -= 1  
		Comic_act = getComic(num, True)
		title = Comic_act.getTitle() #agafem el titol
		img_link = Comic_act.link #agafem link de la imatge
		img_output = Comic_act.getImageLink() #descarreguem la imatge a downloads(per defecte) amb un nom per defecte
		return render_template('comic.html', title=title, img_link=img_link, img_output=img_output)
		


@app.route('/random/')
def funcio_random(title = None, img_link=None, img_output=None):
	global Comic_act
	global num
	Comic_act = getRandomComic() #reps random comic
	num = Comic_act.number
	title = Comic_act.getTitle() #agafem el titol
	img_link = Comic_act.link #agafem link de la imatge
	img_output = Comic_act.getImageLink() #descarreguem la imatge a downloads(per defecte) amb un nom per defecte
	return render_template('comic.html', title=title, img_link=img_link, img_output=img_output)

@app.route('/next/')
def funcio_next(title = None, img_link=None, img_output=None):

	num_max = getLatestComicNum()
	global num
	if num < num_max:
		num += 1
		global Comic_act 
		Comic_act = getComic(num, True)
		title = Comic_act.getTitle() #agafem el titol
		img_link = Comic_act.link #agafem link de la imatge
		img_output = Comic_act.getImageLink() #descarreguem la imatge a downloads(per defecte) amb un nom per defecte
		return render_template('comic.html', title=title, img_link=img_link, img_output=img_output)

if __name__ == '__main__':
	app.run(debug = True, port= 5000)#escogemos puerto





