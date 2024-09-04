import functions_framework
from email_utils import send_email
from web_scraper import get_bay_temps
from secret_manager import get_secret
from emails import sender_email, receiver_emails 

@functions_framework.http
def snapperNOW(request):
    url = "http://www.baywx.com.au/temps.html"

    # Retrieve scraped data from web
    info = get_bay_temps(url)

    if info:
      warmer_bay = get_warmer_bay(info)
      if warmer_bay:
        sender_password = get_secret()

        # Load the HTML template from the file
        with open("src/email_template.html", "r") as file:
          html_content = file.read()

          # Handle send email
          send_email(sender_email, sender_password, receiver_emails, html_content)
          return "Snapper season"
        
def get_warmer_bay(info):
  warmer_bay = []
  if info["Bottom Bay"] >= info["Ocean"]:
    warmer_bay.append("Bottom Bay")
  if info["Mid Bay"] >= info["Ocean"]:
    warmer_bay.append("Mid Bay")
  if info["Top Bay"] >= info["Ocean"]:
    warmer_bay.append("Top Bay")
  return warmer_bay
