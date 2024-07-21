import requests
from datetime import  datetime as dt

URL = "https://careers.liberty.edu/wp-json/custom/v1/job-endpoint"
TITLE_KEY = "jobreqJobTitle"
DATE_POSTED_KEY = "jobreqPostDateText"
NUM_MOST_RECENT = 20

response = requests.get(URL)
jobs = response.json()

by_date = lambda job: int(job["jobreqPostDateText"])
sorted_jobs = sorted(jobs, key=by_date, reverse=True)
cleaned_jobs = sorted_jobs[:NUM_MOST_RECENT-1]

for job in cleaned_jobs:
    name = job[TITLE_KEY] if TITLE_KEY in job else "No name"

    date_posted = "No date"
    if "jobreqPostDateText" in job and job[DATE_POSTED_KEY] > 0:
        date_posted = dt.fromtimestamp(job["jobreqPostDateText"])

    print(f"{name} ({date_posted})")