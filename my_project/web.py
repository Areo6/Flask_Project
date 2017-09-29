from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def home():
  return render_template('home.html')
@app.route('/home.html')
def hom():
  return render_template('home.html')
  
@app.route('/welcome.html')
def welcome():
  return render_template('welcome.html')
  
@app.route('/about.html')
def about():
  return render_template('about.html')
  
@app.route('/help.html')
def help():
  return render_template('help.html')
  


  
if __name__ == '__main__':
  app.run(debug=True)
