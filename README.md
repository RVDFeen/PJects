# PcoWeb Easy Upload Tool

## Overview

The **PcoWeb Easy Upload Tool** is a lightweight utility designed to simplify uploading web content to a **CAREL pCO Web card**.  
It allows fast, reliable, and fully automated deployment of web files without manually handling directories or individual file transfers.

This tool is intended for technicians, engineers, and system integrators working with CAREL pCO controllers and Web cards.

---

## Features

- Upload a single **ZIP archive** containing all web files  
- Automatic extraction and upload of files  
- Files are placed in the **correct directories** automatically  
- Reduces deployment time and configuration errors  

---

## Planned Features

- GUI for bether controll
- Automatic connection to the **CAREL pCO Web card**
- SSH Support for more control over the **CAREL pCO Web card**
---

## How It Works

1. Choose a ZIP file containing the pCO Web content  
2. Connect to the CAREL pCO Web card  
3. The tool automatically:
   - Extracts the ZIP archive  
   - Uploads all files  
   - Places each file in the correct directory  

---

## Usage

1. Start the **PcoWeb Easy Upload Tool**
2. Click **Choose ZIP File** and select your web content archive
3. Enter the connection details of the CAREL pCO Web card
4. Click **Upload**
5. Wait for the upload process to complete

Once completed, the web interface on the pCO Web card is updated immediately.

---

## Requirements

- Supported CAREL pCO Web card
- Network connection to the Web card
- ZIP file with valid pCO Web content

---

## Use Cases

- Commissioning new CAREL pCO installations
- Updating existing pCO Web interfaces
- Development and testing environments
- Field service deployments

---

## Disclaimer

This project is **not an official CAREL product**.  
Use at your own risk and always back up existing Web card content before uploading new files.
