# SnapperNOW
SnapperNOW is built as a Google Cloud Function that monitors bay temperatures to determine if they are warmer than the ocean temperature, indicating a good time for snapper fishing. The function fetches temperature data from a specified URL, compares the temperatures of different bays with the ocean temperature, and sends email notifications to my friends when snapper season hits.

## Features
- **Temperature Monitoring:** Retrieves temperature data scraped from a webpage.
- **Comparison Logic:** Compares bay temperatures with the ocean temperature to determine if any bay is warmer.
- **Email Notifications:** Sends email alerts if the bay temperatures meet the criteria for a good fishing season.

## Configuration Setup

To use this project, you need to create a configuration file named `config.py` in the `src/` directory. This file is excluded from version control for security reasons.

### Steps to Create `config.py`:

1. **Create the File**:
   - In the `src/` directory of your project, create a new file named `config.py`.

2. **Add Configuration**:
   - Add the following content to `config.py`, replacing the placeholder with your actual Secret Manager path:

   ```python
   # src/config.py

   # The sender email address
   sender_email = "xxx@gmail.com"

   # The receiver email addresses (can add multiple addresses to the array)
   receiver_emails = ["xxx@gmail.com, xxx@gmail.com"]

   # Full path to the sender email password in Google Secret Manager
   SECRET_PASSWORD= "projects/your-project-id/secrets/your-secret-name/versions/latest"
   ```
## Learning Outcome
1. Learning how web scraping works and building a web scraper.
2. Using Google Cloud Functions to run and deploy scripts.
3. Using the Google Cloud Scheduler feature to automate the execution of a script at specified time intervals
