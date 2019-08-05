from flask import (
	Blueprint, flash, g, redirect, request, jsonify, url_for
)
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('comment', __name__, url_prefix='/comment')

def get_all_comments():
	db = get_db()
	comments = db.execute(
		'''
		SELECT comment.id, comment.created, comment.body, post.title, user.username
		FROM comment
		LEFT JOIN user
		LEFT JOIN post
		ON comment.author_id = user.id
		AND comment.post_id = post.id
		ORDER BY comment.created DESC
		'''
	).fetchall()

	return comments


def get_comments_by_query(post_id):
	db = get_db()
	query_code = '''
		SELECT comment.id, comment.created, comment.body, post.title, user.username
		FROM comment
		LEFT JOIN user
		ON comment.author_id = user.id
		LEFT JOIN post
		ON comment.post_id = post.id
		WHERE comment.post_id = {post_id}
		ORDER BY comment.created DESC
		'''.format(post_id = post_id)
	print(query_code)
	comments = db.execute(query_code).fetchall()

	return comments


@bp.route('/')
def index():
	commentData = get_all_comments()

	comments = []

	for row in commentData:

		dictionaryRow = {
			'id': row[0],
			'created': row[1],
			'body': row[2],
			'postTitle': row[3],
			'authorUsername': row[4]
		}

		comments.append(dictionaryRow)

	return jsonify(comments)


@bp.route('/create', methods = ('POST',))
@login_required
def create():
	post_id = request.form['post_id']
	body = request.form['body']
	error = None

	if not post_id:
		error = 'Post ID is required.'

	if not body:
		error = 'Body is required.'

	if error is not None:
		flash(error)
	else:
		db = get_db()
		db.execute(
			'INSERT INTO comment (post_id, body, author_id)'
			' VALUES (?, ?, ?)', 
			(post_id, body, g.user['id'])
		)
		db.commit()
		return redirect(url_for('blog.index'))