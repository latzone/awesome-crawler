import requests
import csv

# API endpoint and headers
url = "https://jobs-api14.p.rapidapi.com/list"
headers = {
    "x-rapidapi-key": "8ca3a19cd8msh12567b3f1ed149fp11ef1djsn96fd75140c35",
    "x-rapidapi-host": "jobs-api14.p.rapidapi.com"
}

# Job search query with location added
querystring = {
    "query": "Entry Level Cyber Security",
    "remote_jobs_only": "true",
    "location": "United States"  # Specify the location here
}

# Send request and get response
response = requests.get(url, headers=headers, params=querystring)

# Print the JSON response to inspect its structure
print("Response JSON:", response.json())

# Extract job postings from response, but check for the 'jobs' key first
if "jobs" in response.json() and len(response.json()["jobs"]) > 0:
    job_postings = response.json()["jobs"]

    # Create a CSV file to store the job postings
    with open("cyber_security_job_postings.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Job Title", "Company", "Location", "Employment Type", "Job Description", "Image", "Date Posted",
"Salary Range"                         ])

        # Loop through job postings and extract relevant information
        for job in job_postings:
            job_title = job.get("title", "N/A")
            company = job.get("company", "N/A")
            location = job.get("location", "N/A")
            employmentType = job.get("employmentType", "N/A")
            job_description = job.get("description", "N/A")
            image=job.get("image", "N/A")
            datePosted=job.get("datePosted", "N/A")
            salaryRange=job.get("salaryRange", "N/A")
            #job_url = job.get("url", "N/A")

            # Write job posting to CSV file
            writer.writerow([job_title, company, location, employmentType, job_description, image, datePosted, salaryRange   #job_url
                             ])

    print("Cyber security job postings saved to cyber_security_job_postings.csv")
else:
    print("No job postings found or 'jobs' key missing in the response.")
