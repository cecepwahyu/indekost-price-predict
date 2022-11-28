from flask import Flask, request, render_template
import pickle

import numpy

app = Flask(__name__)

model_file = open('modelRFC.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', Harga=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    '''
    Jenis_Kos, Kecamatan, Kota, Kmandi, WIFI, AC, Kloset, Kasur, Akses24, Luas, Listrik, Dapur, CCTV, Kulkas, Lemari  = [x for x in request.form.values()]

    data = []

    data.append(int(Jenis_Kos))
    data.append(int(Kecamatan))
    data.append(int(Kota))
    data.append(int(Kmandi))
    data.append(int(WIFI))
    data.append(int(AC))
    data.append(int(Kloset))
    data.append(int(Kasur))
    data.append(int(Akses24))
    data.append(int(Luas))
    data.append(int(Listrik))
    data.append(int(Dapur))
    data.append(int(CCTV))
    data.append(int(Kulkas))
    data.append(int(Lemari))

    prediction = model.predict([data])
    output = round(int(prediction[0]),2)
    return render_template('index.html', Harga=output, Jenis_Kos=Jenis_Kos, Kecamatan=Kecamatan, Kota=Kota, Kmandi=Kmandi, WIFI=WIFI, AC=AC, Kloset=Kloset, Kasur=Kasur, Akses24=Akses24, Luas=Luas, Listrik=Listrik, Dapur=Dapur, CCTV=CCTV, Kulkas=Kulkas, Lemari=Lemari)


if __name__ == '__main':
    app.run(debug=True)