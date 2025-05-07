# Deeplink Testing Tool

A simple tool for testing deeplinks across devices during development and QA.

## Overview

This lightweight HTML application allows you to quickly test deeplinks without manually pasting them into your browser's address bar. The tool creates clickable links from your deeplinks, generates QR codes for easy mobile testing, and maintains a history of recently used links for faster iteration during testing.

## Features

- Create clickable deeplinks from any URL scheme
- Generate QR codes for easy mobile device testing
- Save history of recently used deeplinks
- Quickly reuse previous deeplinks with one click
- View QR codes for previously used deeplinks
- Open links in new tabs for easy navigation back to the tester
- Automatically detect and display local IP addresses for network access
- Copy network URLs to clipboard with one click
- No installation required - works with any modern web browser

## Setup Instructions

### Option 1: Using the Python Server (Recommended)

For the easiest setup with automatic IP detection and display:

1. Save both the `index.html` and `server.py` files to the same folder
2. Run the server:
   ```
   python server.py
   ```
3. The server will:
    - Start automatically on port 8000 (or specify a different port: `python server.py 8080`)
    - Display your network IP address prominently
    - Open a browser with the deeplink tester
    - Generate a QR code URL for easy mobile access
    - Show all available URLs for accessing the tool

### Option 2: Standard Web Browser (No Server)

If you prefer to use the tool without a server:

1. Save the `index.html` file to your computer
2. Open the file directly in your web browser
3. The tool will run in browser mode and attempt to detect IP addresses using WebRTC
4. You can manually enter your network IP address for sharing

## Usage Instructions

### Testing Deeplinks

1. Enter your deeplink in the input field (e.g., `myapp://path/to/screen`)
2. Click "Create Test Link"
3. Click on the generated link to test your deeplink
4. A QR code will be generated for the deeplink
5. Scan the QR code with a mobile device to test the deeplink on that device

## Troubleshooting

- If other devices can't access your locally hosted server, check your firewall settings
- Make sure your devices are on the same network
- Some mobile OS restrictions may prevent certain deeplink formats from working
- If you're having trouble with IP detection, use the manual IP entry option
- To find your IP address:
    - Mac/Linux: Run `ifconfig | grep inet` in Terminal
    - Windows: Run `ipconfig` in Command Prompt
