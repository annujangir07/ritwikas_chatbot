import datetime

def log_unanswered_query(query):
    with open("logs/unanswered.txt", "a") as f:
        f.write(f"{datetime.datetime.now()}: {query}\n")
