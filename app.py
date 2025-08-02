from flask import Flask, request, jsonify

app = Flask(__name__)
blogs = []

@app.route('/blogs', methods=['GET'])
def get_blogs():
    return jsonify(blogs)

@app.route('/blogs', methods=['POST'])
def add_blogs():
    blog = request.get_json()
    blogs.append(blog)
    return jsonify(blog), 201

if __name__ == '__main__':
    app.run(debug=True)