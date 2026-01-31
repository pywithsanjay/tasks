import json
import uuid
import hashlib
from datetime import datetime, timedelta

import os

BASE_DIR = os.path.dirname(__file__)

USERS_FILE = os.path.join(BASE_DIR, "users.json")
SESSIONS_FILE = os.path.join(BASE_DIR, "sessions.json")


def load_file(path, default):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return default

def save_file(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


#-----------------------------------------------User Ragistration Function  

def register_user(username, password):
    users = load_file(USERS_FILE, {"users": []})

    if any(u["username"] == username for u in users["users"]):
        return None, "User already exists"

    user = {
        "id": str(uuid.uuid4()),
        "username": username,
        "password": hash_password(password)
    }

    users["users"].append(user)
    save_file(USERS_FILE, users)

    return user, None


#-----------------------------------------------User Login Function  

def login_user(username, password):
    users = load_file(USERS_FILE, {"users": []})
    sessions = load_file(SESSIONS_FILE, {"sessions": []})

    hashed = hash_password(password)

    user = next((u for u in users["users"]
                 if u["username"] == username and u["password"] == hashed), None)

    if not user:
        return None

    session_key = str(uuid.uuid4())
    expires_at = (datetime.utcnow() + timedelta(hours=24)).isoformat()

    sessions["sessions"].append({
        "session_key": session_key,
        "user_id": user["id"],
        "expires_at": expires_at
    })

    save_file(SESSIONS_FILE, sessions)
    return session_key


#-----------------------------------------------Varify Session after Login Function  


def verify_session(session_key):
    sessions = load_file(SESSIONS_FILE, {"sessions": []})
    now = datetime.utcnow()

    valid_sessions = []
    found_session = None

    for s in sessions["sessions"]:
        try:
            expires_at = datetime.fromisoformat(s["expires_at"])
        except:
            continue
            
        if expires_at > now:
            valid_sessions.append(s)
            if s["session_key"] == session_key:
                found_session = s

    save_file(SESSIONS_FILE, {"sessions": valid_sessions})

    return found_session
