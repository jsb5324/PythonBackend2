# from flask import Flask, jsonify, request
# app = Flask(__name__)
# app.users = {}
# app.posts = []
# app.idCnt = 1

# @app.route('/sign-up', methods=['POST'])
# def signUp():
#     newUser = request.json
#     newUser['id'] = app.idCnt
#     app.users[app.idCnt] = newUser
#     app.idCnt += 1
#     return jsonify(newUser)
@app.route('/follow', methods=['post'])
def follow():
    payload = request.json
    userId = int(payload['id'])
    userIdToFollow = int(payload['unfollow'])

    if userId not id app.users or userIdToFollow not in app.users:
        return '사용자가 존재하지 않습니다', 400
    
    user = app.users[userId]
    if user.get('follow'):
        try:    user['follow'].remove(userIdToFollow)
        except: pass
    else:
        user['follow'] = [userIdToFollow]
    return jsonify(user)        