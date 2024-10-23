# app.py
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Post, Comment, Like

app = Flask(__name__)

# Use the DATABASE_URL environment variable provided by Render
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL')  # This will be set in Render
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()  # Create tables


# Signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    new_user = User(username=data['username'],
                    email=data['email'],
                    password_hash=data['password'],
                    avatar_url=data['avatar_url'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message='User created successfully.'), 201


# Login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and user.password_hash == data['password']:
        return jsonify(message='Login successful.'), 200
    return jsonify(message='Invalid email or password.'), 401


# Create Post
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    new_post = Post(user_id=data['user_id'],
                    category_id=data['category_id'],
                    caption=data['caption'],
                    image=data['image'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify(message='Post created successfully.'), 201


# Create Comment
@app.route('/comments', methods=['POST'])
def create_comment():
    data = request.json
    new_comment = Comment(post_id=data['post_id'],
                          user_id=data['user_id'],
                          content=data['content'])
    db.session.add(new_comment)
    db.session.commit()
    return jsonify(message='Comment created successfully.'), 201


# Create Like
@app.route('/likes', methods=['POST'])
def create_like():
    data = request.json
    new_like = Like(post_id=data['post_id'], user_id=data['user_id'])
    db.session.add(new_like)
    db.session.commit()
    return jsonify(message='Like added successfully.'), 201


# Remove Like
@app.route('/likes', methods=['DELETE'])
def remove_like():
    data = request.json
    like = Like.query.filter_by(post_id=data['post_id'], user_id=data['user_id']).first()
    if like:
        db.session.delete(like)
        db.session.commit()
        return jsonify(message='Like removed successfully.'), 200
    return jsonify(message='Like not found.'), 404


# Start the server
if __name__ == '__main__':
    app.run(port=5000)
