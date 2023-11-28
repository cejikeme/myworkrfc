import xml.etree.ElementTree as ET
import csv

def process_control_elements(xml_file_path):
    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Find all 'control' elements
    control_elements = root.findall('.//control')

    # Process each 'control' element
    for control in control_elements:
        print("Control Element Found:")
        # Print each control element individually
        print(ET.tostring(control, encoding='unicode').strip())
    return control_elements

def extract_control_info(control_element, parent_info=None):
    if parent_info is None:
        parent_info = {'Control Relevant': '', 'Trigger': '', 'Action Type': '', 'Action Description': '', 'Transition': ''}
    
    control_info = parent_info.copy()
    control_info['Control Relevant'] = control_element.get('relevant', '')

    for child in control_element:
        text_content = child.text.strip() if child.text else ""
        if child.tag == 'trigger':
            control_info['Trigger'] += text_content + " "
        elif child.tag == 'action':
            control_info['Action Type'] = child.get('type', '')
            control_info['Action Description'] += text_content + " "
        elif child.tag == 'transition':
            control_info['Transition'] += text_content + " "
        elif child.tag == 'control':
            yield from extract_control_info(child, control_info)

    if control_element.tag == 'control':
        yield control_info


def xml_to_csv(xml_file_path, csv_file_path):
    # Parse the XML data from file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Open a CSV file for writing
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write CSV header
        writer.writerow(['Control Relevant', 'Trigger', 'Action Type', 'Action Description', 'Transition'])

        # Iterate through each control element in the XML
        for control in root.findall('.//control'):
            for control_info in extract_control_info(control):
                writer.writerow([control_info['Control Relevant'], control_info['Trigger'], control_info['Action Type'], control_info['Action Description'], control_info['Transition']])


if __name__ == "__main__":
    # Example usage
    xml_file_path = '/home/chibuikeejikeme/projects/rfcnlp/myworkrfc/data/TCP.xml'  # Replace with your XML file path
    csv_file_path = '/home/chibuikeejikeme/projects/rfcnlp/myworkrfc/data/fsm_output.csv'  # Replace with your desired CSV file path

    xml_to_csv(xml_file_path, csv_file_path)

    control_elements = process_control_elements(xml_file_path)
    for control in control_elements:
        for info in extract_control_info(control):
            print(info)  # or any other processing you wish to perform