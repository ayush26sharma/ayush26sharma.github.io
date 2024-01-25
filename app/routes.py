from app import app, db
from flask import jsonify, request
from app.models import User
from datetime import datetime, timedelta
from flask import render_template


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/current_week_leaderboard', methods=['GET'])
def current_week_leaderboard():
    current_date = datetime.utcnow()
    start_of_week = current_date - timedelta(days=current_date.weekday())

    leaderboard = User.query.filter(User.TimeStamp >= start_of_week).order_by(User.Score.desc()).limit(200).all()

    leaderboard_data = [{
        'UID': user.UID,
        'Name': user.Name,
        'Score': user.Score,
        'Country': user.Country,
        'TimeStamp': user.TimeStamp
    } for user in leaderboard]

    return jsonify({'leaderboard': leaderboard_data})


@app.route('/last_week_leaderboard/<country>', methods=['GET'])
def last_week_leaderboard(country):
    current_date = datetime.utcnow()
    start_of_last_week = current_date - timedelta(days=current_date.weekday() + 7)

    leaderboard = User.query.filter(User.TimeStamp >= start_of_last_week, User.Country == country).order_by(
        User.Score.desc()).limit(200).all()

    leaderboard_data = [{
        'UID': user.UID,
        'Name': user.Name,
        'Score': user.Score,
        'Country': user.Country,
        'TimeStamp': user.TimeStamp
    } for user in leaderboard]

    return jsonify({'leaderboard': leaderboard_data})


@app.route('/user_rank/<user_id>', methods=['GET'])
def user_rank(user_id):
    user = User.query.filter_by(UID=user_id).first()

    if user:
        rank = User.query.filter(User.Score > user.Score).count() + 1
        return jsonify({'user_rank': rank})
    else:
        return jsonify({'error': 'User not found'})
