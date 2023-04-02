from flask import Flask, render_template, url_for, request
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('mapage.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['votre CV au format .txt']
    data = uploaded_file.read().decode('Latin-1')

    #traitement sur les mots clés
    #enlève ponctuation
    punctuation = set(".;,?!:-_\’'\n\t’"+ string.punctuation)

    #mets tout en minuscule
    data = data.lower()

    for p in punctuation:
        data = data.replace(p," ")

    #Découpe la chaine de caractère en mots
    wordscv = data.split()

    # Enlève les doublons
    words_unique = set(wordscv)

    #Ecriture du fichier wordscv.txt
    with open('templates/wordscv.txt', 'w', encoding="Latin-1") as w:
        for word in words_unique:
            w.write(word + '\n')
    return f'Les mots clés de votre cv ont été ajoutées dans le fichier: wordscv.txt.\n Les voici: {words_unique}'

@app.route('/paysContinent', methods=['POST'])
def search():
    url = 'https://api.emploi-store.fr/partenaire/offresdemploi/v2/offres/search?paysContinent=XX'
    if request.method == 'POST':
        continentquery = request.form['continentquery']
        data = [continentquery]
    return render_template('results.html')
    
@app.route('/query-example')
def query_example():
    return 'Query String Example'

@app.route('/form-example')
def form_example():
    return 'Form Data Example'

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)

