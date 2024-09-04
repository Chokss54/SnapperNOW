# SnapperNOW
SnapperNOW is built as a Google Cloud Function that monitors bay temperatures to determine if they are warmer than the ocean temperature, indicating a good time for snapper fishing. The function fetches temperature data from a specified URL, compares the temperatures of different bays with the ocean temperature, and sends email notifications to my friends when snapper season hits.

## Features
- **Temperature Monitoring:** Retrieves temperature data scraped from a webpage.
- **Comparison Logic:** Compares bay temperatures with the ocean temperature to determine if any bay is warmer.
- **Email Notifications:** Sends email alerts if the bay temperatures meet the criteria for a good fishing season.