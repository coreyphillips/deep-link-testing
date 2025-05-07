# Deeplink Tester

A simple HTML tool for testing deeplinks during development and QA.

## Overview

This lightweight HTML application allows you to quickly test deeplinks without having to manually paste them into your browser's address bar. The tool creates clickable links from your deeplinks and maintains a history of recently used links for faster iteration during testing.

## Features

- Create clickable deeplinks from any URL scheme
- Save history of recently used deeplinks
- Quickly reuse previous deeplinks with one click
- Open links in new tabs for easy navigation back to the tester
- Automatically displays local IP addresses for easy network access
- Copy network URLs to clipboard with one click
- No installation required - works with any modern web browser

## Setup Instructions

### Option 1: Using the Enhanced Python Server (Recommended)

For the easiest setup with automatic IP detection and display:

1. Save both the `deeplink-tester.html` and `server.py` files to the same folder
2. Make the server script executable (on Mac/Linux):
   ```
   chmod +x server.py
   ```
3. Run the server:
   ```
   python server.py
   ```
4. The server will:
   - Start automatically
   - Display your network IP address prominently
   - Open a browser with the deeplink tester
   - Generate a QR code URL for easy mobile access
   - Show all available URLs for accessing the tool

### Option 2: Standard Python HTTP Server

If you prefer to use the standard Python HTTP server:

1. Save the `deeplink-tester.html` file to a folder on your computer
2. Open a terminal/command prompt
3. Navigate to the folder containing the HTML file:
   ```
   cd /path/to/folder
   ```
4. Start a Python HTTP server:

   For Python 3:
   ```
   python -m http.server 8000
   ```

   For Python 2:
   ```
   python -m SimpleHTTPServer 8000
   ```
5. Access the tool in your browser at:
   ```
   http://localhost:8000/deeplink-tester.html
   ```
6. Use the manual IP entry in the tool to add your network IP

## Usage Instructions

1. Enter your deeplink in the input field (e.g., `myapp://path/to/screen`)
2. Click "Create Test Link"
3. Click on the generated link to test your deeplink
4. Previous links appear in the "Recent Links" section for easy reuse
5. Share the tool with other devices by using the network URLs displayed at the top of the page
6. Use the "Copy" buttons to quickly copy network URLs to your clipboard

## Troubleshooting

- If other devices can't access your locally hosted server, check your firewall settings
- Make sure your devices are on the same network
- Some mobile OS restrictions may prevent certain deeplink formats from working

## Notes

- This tool uses localStorage to save your link history, which persists between browser sessions
- The history is limited to the last 10 deeplinks to keep the interface clean
