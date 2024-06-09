from flask import Blueprint, jsonify, request, current_app

from entity.base import db
from entity.post import Post
from entity.comment import Comment
from middleware.authentication_required import authentication_required
import json

post_urls = Blueprint('post', __name__)

@post_urls.get('/')
@authentication_required
def index(user):
    posts = db.session.query(db.select(Post)).filter(Post.id > 0).all()
    posts = [post.serialize() for post in posts]

    return jsonify({"data": posts})


@post_urls.post('/')
@authentication_required
def create_post(user):
    json_data = request.get_json()
    title = json_data['title']
    content = json_data['content']

    post = Post(author_id=user['id'], title=title, content=content)
    db.session.add(post)
    db.session.commit()

    return jsonify({"message": "Post created successfully"})

@post_urls.get('/<int:post_id>')
@authentication_required
def get_post(user, post_id):
    post = db.session.query(Post).filter(Post.id == post_id).first()

    if post:
        return jsonify(post.serialize())
    else:
        return current_app.response_class(
            response=json.dumps({"message": "Post not found"}),
            status=404,
            mimetype='application/json'
        )

@post_urls.put('/<int:post_id>')
@authentication_required
def update_post(user, post_id):
    json_data = request.get_json()
    title = json_data['title']
    content = json_data['content']

    post = db.session.query(Post).filter(Post.id == post_id).first()

    if post:
        post.title = title
        post.content = content
        db.session.commit()

        return jsonify({"message": "Post updated successfully"})
    else:
        return current_app.response_class(
            response=json.dumps({"message": "Post not found"}),
            status=404,
            mimetype='application/json'
        )
    

@post_urls.delete('/<int:post_id>')
@authentication_required
def delete_post(user, post_id):
    post = db.session.query(Post).filter(Post.id == post_id).first()

    if post:
        db.session.delete(post)
        db.session.commit()

        return jsonify({"message": "Post deleted successfully"})
    else:
        return current_app.response_class(
            response=json.dumps({"message": "Post not found"}),
            status=404,
            mimetype='application/json'
        )
    

@post_urls.get('/<int:post_id>/comments')
@authentication_required
def get_comments(user, post_id):
    comments = db.session.query(Comment).filter(Comment.post_id == post_id).all()

    if comments:
        comments = [comment.serialize() for comment in comments]
        return jsonify({"data": comments})
    else:
        return current_app.response_class(
            response=json.dumps({"message": "Post not found"}),
            status=404,
            mimetype='application/json'
        )
    

@post_urls.post('/<int:post_id>/comment')
@authentication_required
def create_comment(user, post_id):
    json_data = request.get_json()
    content = json_data['content']

    comment = Comment(post_id=post_id, author_id=user['id'], content=content)
    db.session.add(comment)
    db.session.commit()

    return jsonify({"message": "Comment created successfully"})