"""
A simple in-memory session manager.

Stores conversation history for each session ID.
Data is kept only in memory, so everything is lost
when the server restarts.

"""

from datetime import datetime
from collections import defaultdict

# Temporary in-memory storage.
# In production, this should be replaced with Redis
# or another persistent storage solution.
_sessions = defaultdict(list)

# Number of recent conversations to keep per session
MAX_HISTORY = 10

"""Save a question and its answer to a session's history."""
def add_to_history(session_id: str, question: str, answer: str):
    
    _sessions[session_id].append(
        {
            "question": question,
            "answer": answer,
            "timestamp": datetime.utcnow().isoformat(),
        }
    )

    # Keep only the most recent conversations
    if len(_sessions[session_id]) > MAX_HISTORY:
        _sessions[session_id] = _sessions[session_id][-MAX_HISTORY:]


def get_history(session_id: str) -> list:
    #Return the stored conversation history for a session.""
    return _sessions.get(session_id, [])


def clear_session(session_id: str):
    #Remove all saved history for a session.
    if session_id in _sessions:
        del _sessions[session_id]


def get_all_sessions() -> list:
    #Return a list of all active session IDs.
    return list(_sessions.keys())