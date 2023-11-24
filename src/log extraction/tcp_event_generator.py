import subprocess
import xml.etree.ElementTree as ET
import sys

# TCP event generator that would be used to generate 
# Function to turn the pcap file to an output 
# Example usage:run_zeek_script_on_pcap("input.pcap", "my_zeek_script.zeek")
pcap_file = "/home/chibuikeejikeme/projects/rfcnlp/myworkrfc/data/4SICS-GeekLounge-151020.pcap"
zeek_script = "/home/chibuikeejikeme/projects/rfcnlp/myworkrfc/src/log extraction/tcp_monitor.zeek"
outputfile = "/home/chibuikeejikeme/projects/rfcnlp/myworkrfc/data/tcplog.txt"

def run_zeek_script_on_pcap(pcap_file, zeek_script):
    try:
     with open(outputfile) as output_file_handle:
        # Run the Zeek script on the PCAP file using subprocess
        subprocess.run(['/usr/local/zeek/bin/zeek','-b', '-r', pcap_file, zeek_script], check=True)
        print("Zeek script executed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error running Zeek script:", e)
    except FileNotFoundError:
        print("Zeek executable not found. Make sure Zeek is installed and in your PATH.")




run_zeek_script_on_pcap(pcap_file, zeek_script) 




