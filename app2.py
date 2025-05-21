from flask import Flask, render_template, request, redirect, send_from_directory
import mysql.connector
import os
from certificate_generator import generate_certificate

app = Flask(__name__)

# MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="saru",
    database="certificates_db"
)
cursor = mydb.cursor()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/issue', methods=['GET', 'POST'])
def issue():
    if request.method == 'POST':
        cert_id = request.form['cert_id']
        name = request.form['name']
        course = request.form['course']
        issue_date = request.form['issue_date']
        
        sql = "INSERT INTO certificates (cert_id, name, course, issue_date) VALUES (%s, %s, %s, %s)"
        val = (cert_id, name, course, issue_date)
        cursor.execute(sql, val)
        mydb.commit()
        
        return render_template('success.html', name=name, cert_id=cert_id)
    return render_template('issue.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        cert_id = request.form['cert_id']
        sql = "SELECT * FROM certificates WHERE cert_id = %s"
        cursor.execute(sql, (cert_id,))
        result = cursor.fetchone()
        
        if result:
            return render_template('verify_result.html', cert=result)
        else:
            return render_template('verify_result.html', cert=None)
    
    return render_template('verify.html')

@app.route('/download/<cert_id>')
def download_certificate(cert_id):
    # Query to get certificate data
    sql = "SELECT * FROM certificates WHERE cert_id = %s"
    cursor.execute(sql, (cert_id,))
    result = cursor.fetchone()
    
    if result:
        # Generate the certificate
        filename = generate_certificate(result)
        
        # Serve the file
        certificate_dir = os.path.join(app.root_path, 'static', 'certificates')
        return send_from_directory(directory=certificate_dir, path=filename, as_attachment=True)
    else:
        return "Certificate not found", 404

if __name__ == '__main__':
    app.run(debug=True)