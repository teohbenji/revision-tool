import pyrebase
import db

dburl = "https://ctd-revision-tool-default-rtdb.asia-southeast1.firebasedatabase.app/" 
email = "test@mail.com"
password = "tester123" 
apikey = "AIzaSyB8EBGi7LENCxXCD4-hfGZAFm72Jm30nYA"
authdomain = dburl.replace("https://","")

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
    "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
firebase_db = firebase.database()
user = auth.refresh(user['refreshToken']) 

def add_score(score):
    """Adds name and score to firebase
    
    Args:
        score: Score object containing name and score
    """
    firebase_db.child("scores").child(score._name).set(score._score, user['idToken'])

def get_highscores():
    """Retrieves all names and scores from firebase
    
    Returns:
        scores_list: List of 5 score objects with the highest score, sorted by descending value
    """
    
    results = firebase_db.child("scores").order_by_value().get()
    scores_list = []

    try:
        for result in results.each():
            name = result.key()
            score = result.val()
            scores_list.append(db.Score("", name, score))

        scores_list.reverse()
        scores_list = scores_list[0:5]
        
    except TypeError:
        pass  

    return scores_list
