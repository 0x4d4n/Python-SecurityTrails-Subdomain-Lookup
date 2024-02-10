# Subdomain IP Resolver

This script automates the process of fetching subdomains for a given domain using the SecurityTrails API, resolves their IP addresses, and outputs the results in a CSV file. It includes functionality to deduplicate IP addresses, ensuring each is listed only once, and implements retry logic for failed DNS lookups.

## Features

- Fetch subdomains from SecurityTrails API.
- Resolve IP addresses for each subdomain.
- Deduplicate IP addresses to ensure each is listed only once in the output.
- Retry failed DNS lookups up to three times.
- Output the subdomain and IP address pairs to a CSV file.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- `requests` library installed in Python. You can install this with `pip install requests`.

## Setup

1. Clone this repository to your local machine using `git clone https://github.com/0x4d4n/Python-SecurityTrails-Subdomain-Lookup.git`.
2. Navigate into the cloned repository.
3. Install the required Python packages using `pip install -r requirements.txt`.

## Configuration

Before running the script, you need to set your SecurityTrails API key and specify the target domain:

1. Open the script with your preferred text editor.
2. Replace `YOUR_API_KEY` with your actual SecurityTrails API key.
3. Modify the `domain` variable to the domain you want to query for subdomains.

## Usage

To run the script, execute the following command in your terminal:

```bash
python subdomain_ip_resolver.py
