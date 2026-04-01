[+] PentestAI FIXED ishga tushdi: https://target.com 

[*] 1. RECON...  ←←← BU YERDA TURIB TURIBDI = REAL SCAN JARYANDA!



⏳ Subfinder → target.com subdomains qidiryapti (subdomen.target.com topadi)

⏳ Gobuster → DNS enum  

⏳ FFUF → /admin, /api, /backup, /search-admin fuzz qilyapti



Recon:        2-3 daqiqa  (subdomains + dirs)

Nmap:         1-2 daqiqa  (ports 1-1000)

Nuclei:       3-5 daqiqa  (1000+ CVE templates)

Web scans:    1-2 daqiqa

SQLMap:       2-3 daqiqa

TOTAL:       ~10-15 daqiqa



[*] 2. 🛡️ NMAP SCAN...     ← Ports topiladi (80,443,3306?)

[*] 3. 💥 NUCLEI CVEs...   ← target.com uchun CVE lar

[*] 4. 🌐 WEB VULNS...     ← Nikto + dirsearch

[*] 5. 🧪 SQLMAP...        ← search-admin SQLi test

[+] 🎉 Report tayyor!



# Web_scan
WEb app scan. and write repo


# Git clone
git clone https://github.com/AlikhonAliyev0102/Web_scan.git

# Terminal 1: Agent (ishlayapti)
sudo apt install -y nmap nuclei nikto sqlmap ffuf subfinder wkhtmltopdf msfconsole colorama
sudo apt install python3-venv -y 
python3 -m venv myenv 
source myenv/bin/activate  
python3 aifixagent.py https://target.com -o my_reports

# Terminal 2: Real-time monitoring  
watch -n 2 "ls -la my_reports/ && tail -5 my_reports/*txt 2>/dev/null"

# Terminal 3: Manual check
curl -s https://target.com/search-admin | grep -i error

# 2. Dependencies (agar yo'q bo'lsa)
sudo apt install nmap python3-nmap nuclei nikto ffuf subfinder gobuster dirsearch sqlmap -y
nuclei -update-templates


#Folder
cd my_reports/target.com_20260330_160936/

# 1. HTML Report (eng muhimi)
firefox FULL_REPORT.html

# 2. Raw files (detailed)
cat subdomains.txt          # Topilgan subdomains
cat nmap_results.json       # Open ports/services  
cat nuclei_results.txt      # CVE vulnerabilities
cat nikto.txt              # Web vulns
cat dirs.json              # Sensitive directories
