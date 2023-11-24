import requests
from bs4 import BeautifulSoup
import csv

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching HTML: {e}")
        return None

def parse_html(html):
    if html is not None:
        soup = BeautifulSoup(html, 'html.parser')
        
        event_blocks = soup.select('dl.zeek.id')
        event_info_list = []

        for event_block in event_blocks:
            # Extract event name
            event_name = event_block.select_one('dt.sig-object span.pre').text.strip()

            # Extract event type
            # event_type = event_block.select_one('span.sig-name.descname + dd p a.reference.internal code').text.strip()

            # Extract event description
            event_description = event_block.select_one('dd dl+p').text.strip()

            # Extract event parameters
            # parameters = [param.text.strip() for param in event_block.select('dt.field-odd + dd ul.simple li p')]

            event_info_list.append({
                'Event Name': event_name,
                # 'Event Type': event_type,
                'Event Description': event_description,
                # 'Parameters': parameters
            })

        return event_info_list
    else:
        return None
    
def write_to_csv(data, csv_filename):
    if data:
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Event Name', 'Event Description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in data:
                writer.writerow(row)
    else:
        print("No data to write to CSV.")

def main():
    url = 'https://docs.zeek.org/en/master/scripts/base/bif/plugins/Zeek_TCP.events.bif.zeek.html#detailed-interface'
    html = fetch_html(url)
    
    if html:
        event_info_list = parse_html(html)
        if event_info_list:
            print("Event Information:")
            for event_info in event_info_list:
                print("------")
                for key, value in event_info.items():
                    print(f"{key}: {value}")

            # Write to CSV
            write_to_csv(event_info_list, 'output.csv')
        else:
            print("Failed to parse HTML or no data found.")
    else:
        print("Failed to fetch HTML.")

if __name__ == "__main__":
    main()
