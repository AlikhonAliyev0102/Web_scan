#!/usr/bin/env python3
"""
PentestAI FIXED VERSION - 100% Working
"""

import asyncio
import subprocess
import json
import os
import sys
sys.path.append('/usr/share/python3-nmap')
import nmap
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse
import requests
from colorama import init, Fore, Style
import argparse

init()

class PentestAI:
    def __init__(self, target, output_dir="pentest_report"):
        self.target = target.rstrip('/')
        self.parsed = urlparse(self.target)
        self.domain = self.parsed.netloc or self.target
        self.output_dir = Path(output_dir) / f"{self.domain}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.results = {'target': target, 'timestamp': datetime.now().isoformat()}
        print(f"{Fore.GREEN}[+] PentestAI FIXED ishga tushdi: {target}{Style.RESET_ALL}")

    async def run_full_pentest(self):
        print(f"{Fore.CYAN}[*] 1. RECON...{Style.RESET_ALL}")
        await self.reconnaissance()
        
        print(f"{Fore.CYAN}[*] 2. NMAP...{Style.RESET_ALL}")
        await self.nmap_scan()
        
        print(f"{Fore.CYAN}[*] 3. NUCLEI...{Style.RESET_ALL}")
        await self.nuclei_scan()
        
        print(f"{Fore.CYAN}[*] 4. WEB SCAN...{Style.RESET_ALL}")
        await self.web_scan()
        
        self.generate_report()
        print(f"{Fore.GREEN}[+] ✅ Report: {self.output_dir}/FULL_REPORT.html{Style.RESET_ALL}")

    async def run_cmd(self, cmd):
        """Simple fixed command runner"""
        proc = await asyncio.create_subprocess_shell(
            cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        return stdout.decode() + stderr.decode()

    async def reconnaissance(self):
        await self.run_cmd(f"subfinder -d {self.domain} -silent -o {self.output_dir}/subdomains.txt")
        await self.run_cmd(f"ffuf -u {self.target}/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -mc 200,204,301,302 -o {self.output_dir}/dirs.json -silent")

    async def nmap_scan(self):
        nm = nmap.PortScanner()
        nm.scan(self.domain, '1-1000', arguments='-sV -sC')
        services = []
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in lport:
                    services.append({
                        'port': port, 
                        'service': nm[host][proto][port]['name'],
                        'version': nm[host][proto][port].get('version', '')
                    })
        self.results['services'] = services
        with open(self.output_dir / 'nmap.json', 'w') as f:
            json.dump(nm.all_hosts(), f)

    async def nuclei_scan(self):
        await self.run_cmd(f"echo '{self.target}' | nuclei -stdin -t cves/ -o {self.output_dir}/nuclei.txt -silent")

    async def web_scan(self):
        await self.run_cmd(f"nikto -h {self.target} -o {self.output_dir}/nikto.txt")

    def generate_report(self):
        html = f"""
<html><body>
<h1>PentestAI Report: {self.domain}</h1>
<h2>Services ({len(self.results.get('services', []))})</h2>
<table border="1">
"""
        for svc in self.results.get('services', []):
            html += f"<tr><td>{svc['port']}</td><td>{svc['service']}</td><td>{svc['version']}</td></tr>"
        html += "</table></body></html>"
        
        with open(self.output_dir / "FULL_REPORT.html", 'w') as f:
            f.write(html)

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('target')
    parser.add_argument('-o', '--output', default='reports')
    args = parser.parse_args()
    
    agent = PentestAI(args.target, args.output)
    await agent.run_full_pentest()

if __name__ == "__main__":
    asyncio.run(main())
