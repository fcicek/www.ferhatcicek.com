from flask import Flask, render_template, request
app = Flask(__name__)
import sqlite3

def getData():
	conn=sqlite3.connect('system_usage.db')
	curs=conn.cursor()
	for row in curs.execute("SELECT * FROM system_usage ORDER BY timestamp DESC LIMIT 1"):
		time = str(row[0])
		cpu = row[1]
		mem = row[2]
        print(str(cpu))
        print((str(mem))
	conn.close()
	return time, cpu, mem

@app.route("/")
def index():	
	time, cpu, mem = getData()
	templateData = {
		'time': time,
		'cpu': cpu,
		'mem': mem
	}
	return render_template('son_olcum.html', **templateData)
    
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
