from flask import Flask, request, render_template, redirect, url_for
import os
import random #importing shi for skibidirizzlers

app = Flask(__name__) #flask app ka name
UPLOAD_FOLDER = 'static/uploads' #defining the folder where the uploads will be stored (u dont need to make these it will make it)
os.makedirs(UPLOAD_FOLDER, exist_ok=True) #it makes the folder if it doesnt exist
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #defines upload folder in flask app config

SENTENCES = [ #defining random sentences
    "The {} jumped over the fence.",
    "I saw a {} at the park today.",
    "Can you believe how fast that {} was running?",
    "She painted a beautiful picture of a {}.",
    "A {} was sitting quietly in the corner."
]

@app.route('/', methods=['GET', 'POST']) #decorating the url so "/" is ur 127.bla.bla"/" and then GET is for loading url POST is for form
def index():
    if request.method == 'POST': #yea same shi its getting the stuff
        word = request.form.get('word') #here it gets word from html file
        image = request.files.get('image') #image from html file
        if not word or not image:
            return "Please provide both a word and an image!", 400 #if not there it will display this
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename) #saves all the shi yipee in local web storage
        image.save(image_path) #saves image in ur storage hehe
        sentence = random.choice(SENTENCES).format(word) #makes a sentence from the "sentences" which we defined before and the word is the one user put
        return render_template('display.html', word=word, sentence=sentence, image_path=image_path) #displays the message and image
    return render_template('index.html') #affirm it in index.html yipee
if __name__ == '__main__':
    app.run(debug=True) #run the file ocontinueoolsy cuz we're chill like that
