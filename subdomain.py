import requests
import socket
import csv

# API Details
api_url = 'https://api.securitytrails.com/v1/domain/{}/subdomains?children_only=false&include_inactive=false'
api_key = 'YOUR_API_KEY'  # Replace YOUR_API_KEY with your actual API key
domain = 'internet-census.org'  # This can be replaced with any domain you're interested in

# Output file name
output_file = 'hostnames_ips.csv'

# Maximum number of lookup attempts
max_attempts = 2

def get_subdomains(domain):
    """Fetch subdomains for a given domain from the API."""
    response = requests.get(api_url.format(domain),
                            headers={'APIKEY': api_key, 'accept': 'application/json'})
    if response.status_code == 200:
        return response.json().get('subdomains', [])
    else:
        print(f"Failed to fetch subdomains for {domain}. HTTP Status Code: {response.status_code}")
        return []

# Fetch the subdomains from the API
subdomains = get_subdomains(domain)

# Open the output CSV file for writing
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['Hostname', 'IP Address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Initialize a set to keep track of IP addresses that have already been processed
    processed_ips = set()

    # Loop through each subdomain
    for subdomain in subdomains:
        hostname = f"{subdomain}.{domain}"
        attempt = 0
        while attempt < max_attempts:
            try:
                ip_address = socket.gethostbyname(hostname)
                # Only write the hostname and IP if the IP hasn't been processed yet
                if ip_address not in processed_ips:
                    writer.writerow({'Hostname': hostname, 'IP Address': ip_address})
                    processed_ips.add(ip_address)
                break  # Exit the loop if lookup was successful
            except socket.gaierror:
                attempt += 1
                print(f"Attempt {attempt} failed for {hostname}. Retrying...")
                if attempt == max_attempts:
                    # Note the failure after the final attempt
                    print(f"Lookup failed after {max_attempts} attempts for {hostname}")

print(f"Completed. Check the output in '{output_file}'.")