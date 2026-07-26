import os
import re
import urllib.request
import json
import subprocess

os.chdir(r"C:\Users\ishan\Documents\Projects\Awesome-Delivery-Management")

def run_cmd(cmd):
    subprocess.run(["powershell", "-Command", cmd], shell=True)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Step 1: SaaS valuation
table_pattern = re.compile(r'(\| Product \| Description \| Pricing & Free Tier \|.*?)(?=\n\n)', re.DOTALL)
match = table_pattern.search(content)
if match:
    table_text = match.group(1)
    lines = table_text.strip().split('\n')
    header = lines[0] + " | Valuation/Revenue |"
    separator = lines[1] + "-------------------|"
    
    valuations = {
        'Bringg': 1000,
        'Deliverect': 1400,
        'FarEye': 100,
        'DispatchTrack': 100,
        'Shipsy': 50,
        'LogiNext': 50,
        'Onfleet': 20,
        'Circuit': 20,
        'Track-POD': 10,
        'Elite EXTRA': 10,
        'Locate2u': 10,
        'Tookan': 10,
        'Shipday': 5,
        'GetSwift': 0
    }
    
    rows = []
    for line in lines[2:]:
        val = 0
        val_str = "N/A"
        for k, v in valuations.items():
            if k in line:
                val = v
                val_str = f"~${v}M" if v > 0 else "N/A"
                break
        rows.append((val, line + f" | {val_str} |"))
    
    rows.sort(key=lambda x: x[0], reverse=True)
    new_table = "\n".join([header, separator] + [r[1] for r in rows])
    content = content.replace(table_text, new_table)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_cmd('git add . ; git commit -m "Added company size and sorted the SaaS based on that" ; git push')

# Step 2: Open Source Stars
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

os_pattern = re.compile(r'### Dedicated Delivery Management & Logistics Tools\n\n(.*?)(?=\n\n###)', re.DOTALL)
match = os_pattern.search(content)
if match:
    os_text = match.group(1)
    lines = os_text.strip().split('\n\n')
    
    parsed_lines = []
    for block in lines:
        repo_match = re.search(r'github\.com/([^/]+/[^/\)]+)', block)
        if repo_match:
            repo = repo_match.group(1)
            try:
                url = f"https://api.github.com/repos/{repo}"
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response:
                    data = json.loads(response.read().decode())
                    stars = data.get("stargazers_count", 0)
            except:
                stars = 0
            
            badge = f"[![GitHub stars](https://img.shields.io/github/stars/{repo}?style=social&color=white)](https://github.com/{repo}/stargazers)"
            new_block = block.replace(f"({repo_match.group(0)})", f"({repo_match.group(0)}) {badge}")
            parsed_lines.append((stars, new_block))
        else:
            parsed_lines.append((0, block))
            
    parsed_lines.sort(key=lambda x: x[0], reverse=True)
    new_os_text = "\n\n".join([r[1] for r in parsed_lines])
    content = content.replace(os_text, new_os_text)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_cmd('git add . ; git commit -m "Added github stars and sorted the opensource based on that" ; git push')

# Step 3: Banner
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()
banner = "![Banner](./assets/banner.svg)\n\n"
content = banner + content.lstrip()
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_cmd('git add . ; git commit -m "added banner" ; git push')

# Step 4: Emojis
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace("## Top Delivery Management", "## 🚀 Top Delivery Management")
content = content.replace("## Table of Contents", "## 📑 Table of Contents")
content = content.replace("## SaaS/Hosted Platforms", "## ☁️ SaaS/Hosted Platforms")
content = content.replace("## Open-Source GitHub Projects", "## 💻 Open-Source GitHub Projects")
content = content.replace("## How to Contribute", "## 🤝 How to Contribute")
content = content.replace("## Disclaimer", "## ⚠️ Disclaimer")
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_cmd('git add . ; git commit -m "added emojis" ; git push')

# Step 5: SEO
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()
seo_text = "Discover the ultimate list of the best delivery management software, last-mile logistics routing tools, fleet management platforms, and open-source dispatch tracking systems to optimize your supply chain operations.\n\n"
content = content.replace("This repository tracks notable **SaaS platforms**", seo_text + "This repository tracks notable **SaaS platforms**")
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_cmd('git add . ; git commit -m "seo optimised" ; git push')

# Step 6 & 7: Badges left and right
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a> <a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
right_badges = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'

badge_line = f"<div align=\"center\">\n{left_badges} {right_badges}\n</div>\n\n"
content = re.sub(r'(!\[Banner\].*?\n\n)', r'\1' + badge_line, content)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_cmd('git add . ; git commit -m "badges to left added" ; git push')
run_cmd('git add . ; git commit -m "badges to right added" ; git push')

# Step 8: Star History
folder_name = os.path.basename(os.getcwd())
star_history = f"""
## ⭐️ Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()
content += "\n" + star_history
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_cmd('git add . ; git commit -m "star history added" ; git push')

# Step 9: Fix chartrepos
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace("chartrepos", "chart?repos")
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_cmd('git add . ; git commit -m "fixed star plot" ; git push')

# Step 10: Replace awesome link
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
run_cmd('git add . ; git commit -m "invalid awesome link fixed" ; git push')

print("All done!")
