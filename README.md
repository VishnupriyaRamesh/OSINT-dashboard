# OSINT-dashboard

## 📌 Project Overview

The **OSINT Dashboard** allows users to perform basic OSINT tasks such as:

- Checking whether an **email address** has been exposed in a data breach.
- Verifying the **validity of phone numbers**, including country, line type, and carrier.
- Fetching **IP address metadata** such as location, ISP, and network type.
- Capturing and displaying a **real-time screenshot** of any website URL.

This dashboard is ideal for cybersecurity students, researchers, and ethical hackers seeking a beginner-friendly tool to explore digital footprints.


## ✨ Features

- 🔍 **IP Address Lookup** (via IPInfo API)
- ☎️ **Phone Number Verification** (using Veriphone API and `phonenumbers`)
- 📧 **Email Breach Detection** (with Have I Been Pwned API)
- 🌐 **Website Screenshot Generator** (via Apiflash API)
- 💡 Simple UI built with Flask & Bootstrap
- ✅ Live API integration
- ⚠️ Handles errors and invalid inputs gracefully



## 🛠️ Tech Stack

| Layer        | Technology |
|--------------|------------|
| Frontend     | HTML, CSS, Bootstrap |
| Backend      | Python, Flask |
| APIs Used    | IPInfo, Veriphone, Have I Been Pwned, Apiflash |
| Libraries    | `requests`, `phonenumbers`, `dotenv` |
