PYTHON := /usr/bin/python3.8
ZEEKSCRIPT := "/home/chibuikeejikeme/projects/rfcnlp/myworkrfc/src/log extraction/tcp_event_generator.py"
SCRAPERSCRIPT := "/home/chibuikeejikeme/projects/rfcnlp/myworkrfc/src/log extraction/scraper.py"
RESULTS := /home/chibuikeejikeme/projects/rfcnlp/myworkrfc/data/tcplog.xml
ZEEKEVENTURL := https://docs.zeek.org/en/master/scripts/base/bif/plugins/Zeek_TCP.events.bif.zeek.html
FINAL_OUTPUT := /home/chibuikeejikeme/projects/rfcnlp/myworkrfc/data/final_output.csv

.PHONY: all run run-logstash run-scraper

all: run run-logstash run-scraper

run:
	$(PYTHON) $(ZEEKSCRIPT) > $(RESULTS)

run-logstash:
	touch $(FINAL_OUTPUT)
	cd /usr/share/logstash/bin && \
	sudo ./logstash -f /etc/logstash/conf.d/logstash.conf --path.settings /etc/logstash/ &
	sleep 10
	sudo systemctl stop logstash

run-scraper:
	export ZEEKEVENTURL=$(ZEEKEVENTURL) && \
	$(PYTHON) $(SCRAPERSCRIPT)
 