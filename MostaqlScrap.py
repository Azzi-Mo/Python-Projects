import requests
import bs4
import re

# Make a GET request to the Mostaql website
response = requests.get("https://mostaql.com/jobs")

# Parse the HTML content of the page
soup = bs4.BeautifulSoup(response.text, "html.parser")

# Find all the job listings on the page
job_listings = soup.find_all("div", class_="job-listing")

# Create a list to store the jobs
jobs = []

# Extract the information for each job listing
for listing in job_listings:
  title = listing.find("a", class_="job-title").text
  company = listing.find("span", class_="company").text
  location = listing.find("span", class_="location").text
  date = listing.find("span", class_="date").text
  
  # Clean up the data by removing leading/trailing whitespace and removing the "New" label from the date
  title = title.strip()
  company = company.strip()
  location = location.strip()
  date = re.sub("^New\s+", "", date.strip())
  
  # Add the job to the list
  jobs.append({
    "title": title,
    "company": company,
"location": location,
"date": date
})

# Sort the list of jobs by title
jobs.sort(key=lambda x: x["title"])

# Write the jobs to a file
with open("jobs.txt", "w") as f:
    for job in jobs:
     f.write(f"{job['title']} at {job['company']} in {job['location']} ({job['date']})\n")