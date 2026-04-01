# Web_scan
WEb app scan. and write repo
# Terminal 1: Agent (ishlayapti)
python3 aifixagent.py https://ejarima.uz -o my_reports

# Terminal 2: Real-time monitoring  
watch -n 2 "ls -la my_reports/ && tail -5 my_reports/*txt 2>/dev/null"

# Terminal 3: Manual check
curl -s https://ejarima.uz/search-admin | grep -i error
