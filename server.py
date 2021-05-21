import csv
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/index.html')
def my_home2():
    return render_template('index.html')


@app.route('/static/about.html')
def about():
    return render_template('about.html')

@app.route('/about.html')
def about1():
    return render_template('about.html')

@app.route('/static/components.html')
def components():
    return render_template('components.html')

@app.route('/components.html')
def components1():
    return render_template('components.html')

@app.route('/static/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/contact.html')
def contact1():
    return render_template('contact.html')

@app.route('/static/work.html')
def work():
    return render_template('work.html')

@app.route('/work.html')
def work1():
    return render_template('work.html')

@app.route('/static/works.html')
def works():
    return render_template('works.html')

@app.route('/works.html')
def works1():
    return render_template('works.html')

# @app.route('/blog/dog')
# def dogs():
#     return "My dog's name is rocky and I love him so much"

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email1 = data['email']
        subject1 = data['subject']
        message1 = data['message']
        file = database.write(f"Email: {email1},\nSubject: {subject1},\nMessage: {message1}\n\n")
        
def write_to_csv(data):
    with open('database.csv', newline='' , mode='a') as database2:
        email1 = data['email']
        subject1 = data['subject']
        message1 = data['message']
        csv_writer = csv.writer(database2, delimiter=',',  quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email1,subject1,message1])
        
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        # write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong'