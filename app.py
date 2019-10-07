from flask import Flask, render_template, request
import json
import requests
import get
import post
import db

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        source = request.values.get('source')
        target = request.values.get('target')
        source_text = request.values.get('source-text')

        source_data = {
            "text": source_text,
            "source_language": source,
            "target_language": target
        }

        res_post = post.make_post(source_data)
        res_get = get.make_get(res_post['uid'])

        data = {'uid': res_post['uid'], 'source_language': res_post['source_language'], 'target_language': res_post['target_language'],
                'status': res_post['status'], 'text': res_post['text'], 'translatedText': res_get['translatedText']}

        db.save_into_database(data)
        translatedTexts = db.read_database()

        return render_template('home.html', translatedTexts=translatedTexts)

    else:
        translatedTexts = db.read_database()
        return render_template('home.html', translatedTexts=translatedTexts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
