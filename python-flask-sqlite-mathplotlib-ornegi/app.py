from flask.globals import session
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io

from flask import Flask, render_template, send_file, make_response, request
app = Flask(__name__)

import sqlite3

def sonKayit():
        conn=sqlite3.connect('system_usage.db')
        curs=conn.cursor()
        for row in curs.execute("SELECT * FROM system_usage ORDER BY timestamp DESC LIMIT 1"):
                time = str(row[0])
                cpu = row[1]
                mem = row[2]
        conn.close()
        return time, cpu, mem

def sonKayitDizi (orneklemeSayisi):
        conn=sqlite3.connect('system_usage.db')
        curs=conn.cursor()
        curs.execute("SELECT * FROM system_usage ORDER BY timestamp DESC LIMIT "+str(orneklemeSayisi))
        data = curs.fetchall()
        tarihDizi = []
        cpuDizi = []
        hafizaDizi = []
        for row in reversed(data):
                tarihDizi.append(row[0])
                cpuDizi.append(row[1])
                hafizaDizi.append(row[2])
        conn.close()
        return tarihDizi, cpuDizi, hafizaDizi
    
def maksimumKayit():
        conn=sqlite3.connect('system_usage.db')
        curs=conn.cursor()
        for row in curs.execute("select COUNT(cpu) from  system_usage"):
                maksimumKayitDizi=row[0]    
        conn.close()
        return maksimumKayitDizi


global orneklemeSayisi
orneklemeSayisi = maksimumKayit()
if (orneklemeSayisi > 101):
    orneklemeSayisi = 100

@app.route("/")
def index():
        time, cpu, mem = sonKayit()
        templateData = {'time':time,'cpu':cpu,'mem':mem,'orneklemeSayisi':orneklemeSayisi}
        return render_template('index.html', **templateData)
    
@app.route('/', methods=['POST'])
def post_form():
        global orneklemeSayisi
        orneklemeSayisi = int (request.form['orneklemeSayisi'])
        numMaxSamples = maksimumKayit()
        if (orneklemeSayisi > numMaxSamples):
                orneklemeSayisi = (numMaxSamples-1)
        time, cpu, mem = sonKayit()
        templateData = {'time':time,'cpu':cpu,'mem':mem,'orneklemeSayisi':orneklemeSayisi}
        return render_template('index.html', **templateData)
    
@app.route('/plot/cpu')
def cpu_cizim():
        times, cpuDizi, hafizaDizi = sonKayitDizi(orneklemeSayisi)
        ys = cpuDizi
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.set_title("CPU [%]")
        axis.set_xlabel("Örnekleme")
        axis.grid(True)
        xs = range(orneklemeSayisi)
        axis.plot(xs, ys)
        canvas = FigureCanvas(fig)
        output = io.BytesIO()
        canvas.print_png(output)
        response = make_response(output.getvalue())
        response.mimetype = 'image/png'
        return response
    
@app.route('/plot/mem')
def hafiza_cizim():
        times, cpuDizi, hafizaDizi = sonKayitDizi(orneklemeSayisi)
        ys = hafizaDizi
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.set_title("MEM [%]")
        axis.set_xlabel("Örnekleme")
        axis.grid(True)
        xs = range(orneklemeSayisi)
        axis.plot(xs, ys)
        canvas = FigureCanvas(fig)
        output = io.BytesIO()
        canvas.print_png(output)
        response = make_response(output.getvalue())
        response.mimetype = 'image/png'
        return response

    
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
