![133611677456746030](133611677456746030.jpg)

# Cybersecurity Job Scraper

## Overview

This Python script fetches and saves cybersecurity job postings in a CSV file. It uses an API to retrieve job listings, extracts key information such as job title, company, location, employment type, job description, image, date posted, and salary range, and saves the data to a CSV file for further analysis.

### Requirements

Ensure you have the following Python libraries installed before running the script:

* `requests`
* `csv`

#### Install Dependencies

Install the required libraries using the following command:

```bash
pip install requests
```

### Features

- Fetches job postings related to cybersecurity.
- Extracts the following information:
  - **Job Title**
  - **Company Name**
  - **Location**
  - **Employment Type** (e.g., full-time, part-time)
  - **Job Description**
  - **Company Image**
  - **Date Posted**
  - **Salary Range**
- Saves the extracted data into a CSV file for easy access.

#### CSV Output Example

| Job Title | Company | Location | Employment Type | Job Description | Image | Date Posted | Salary Range |
| :---: | :--- | ---: | :---: | :--- | :--- | :---: | :---: |
| Cybersecurity Analyst | XYZ Corp | New York, NY | Full-time | Perform system monitoring and threat detection... | ![image](image-url.com) | 2024-09-10 | $50,000 - $70,000 |

---

## How to Use

1. Clone this repository:

```bash
git clone https://github.com/your-repo/cybersecurity-job-scraper
```

2. Replace the placeholder for the API key in the code with your own API key:

```python
"x-rapidapi-key": "your-api-key"
```

3. Run the script to fetch the job postings:

```bash
python job_scraper.py
```

4. The job postings will be saved to a CSV file named `cyber_security_job_postings.csv` in your working directory.

---

## Example Code

This script retrieves the job data from an API, extracts relevant fields, and saves them in a CSV file.

```python
import requests
import csv

# API URL and headers (update with your API key)
url = "https://api.example.com/cybersecurity-jobs"
headers = {
    "x-rapidapi-key": "your-api-key",
    "x-rapidapi-host": "api.example.com"
}

response = requests.get(url, headers=headers)

# Print the JSON response to inspect its structure
print("Response JSON:", response.json())

# Extract job postings from the response and write to a CSV file
if "jobs" in response.json() and len(response.json()["jobs"]) > 0:
    job_postings = response.json()["jobs"]

    # Create a CSV file to store the job postings
    with open("cyber_security_job_postings.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Job Title", "Company", "Location", "Employment Type", "Job Description", "Image", "Date Posted", "Salary Range"])

        # Loop through job postings and extract relevant information
        for job in job_postings:
            job_title = job.get("title", "N/A")
            company = job.get("company", "N/A")
            location = job.get("location", "N/A")
            employmentType = job.get("employmentType", "N/A")
            job_description = job.get("description", "N/A")
            image = job.get("image", "N/A")
            datePosted = job.get("datePosted", "N/A")
            salaryRange = job.get("salaryRange", "N/A")

            # Write job posting to CSV file
            writer.writerow([job_title, company, location, employmentType, job_description, image, datePosted, salaryRange])

    print("Cybersecurity job postings saved to cyber_security_job_postings.csv")
else:
    print("No job postings found or 'jobs' key missing.")
```

---

## Future Improvements

* [x] Save job postings to CSV file.
* [ ] Add functionality to filter jobs by date or location.

---

## Contributing

Feel free to contribute by submitting a pull request. Please ensure all changes are tested and documented.

---

## License

This project is licensed under the MIT License.
