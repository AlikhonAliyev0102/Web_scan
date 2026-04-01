# Web_scan
WEb app scan. and write repo

# Git clone
git clone https://github.com/AlikhonAliyev0102/Web_scan.git

# Terminal 1: Agent (ishlayapti)
python3 aifixagent.py https://target.com -o my_reports

# Terminal 2: Real-time monitoring  
watch -n 2 "ls -la my_reports/ && tail -5 my_reports/*txt 2>/dev/null"

# Terminal 3: Manual check
curl -s https://target.com/search-admin | grep -i error
