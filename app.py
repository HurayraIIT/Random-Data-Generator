from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
  users = [
    {"id":1, "name":"Shiblee vaiya", "designation":"Head of QA and Ops"},
    {"id":2, "name":"Shraboni Shaila", "designation":"Software Test Engineer"},
    {"id":3, "name":"Shariful Islam", "designation":"Software Test Engineer"},
    {"id":4, "name":"Obayed Mamur", "designation":"Junior Software Test Engineer"},
    {"id":5, "name":"Abu Hurayra", "designation":"Junior Software Test Engineer"},
  ]
  return render_template('home.html', users=users)
  
@app.route('/users')
def user_list():
  return "users list"
  
@app.route('/<string:num>')
def string_generator(num):
  # num = int(num)
  output_string = ""
  for i in range(int(num)):
    output_string += "a"
  
  return output_string
  
if __name__ == '__main__':
  app.debug=True
  app.run()