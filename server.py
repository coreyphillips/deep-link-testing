#!/usr/bin/env python3
"""
Simple HTTP Server that displays network IP addresses
for testing deeplinks across devices.
"""

import os
import socket
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import quote

# Default port
PORT = 8000

def get_ip_addresses():
    """Get all IP addresses for this machine."""
    hostname = socket.gethostname()
    # Get local IP by creating a socket and connecting to an external address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't need to be reachable
        s.connect(('10.255.255.255', 1))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        s.close()

    return {
        'hostname': hostname,
        'local_ip': local_ip,
        'localhost': '127.0.0.1'
    }

class DeeplinkServerHandler(SimpleHTTPRequestHandler):
    """Custom handler that adds color to server logs and integrates IP info into the HTML."""

    def log_message(self, format, *args):
        """Override to add colors to log messages."""
        sys.stderr.write("\033[92m[%s] %s\033[0m\n" %
                         (self.log_date_time_string(),
                          format % args))

    def do_GET(self):
        """Override to inject network info for the index page."""
        # Check if this is a favicon request (browsers automatically request it)
        if self.path == "/favicon.ico":
            return super().do_GET()

        # For deeplink-testing.html, inject the network info
        if self.path == "/deeplink-testing.html" or (self.path == "/" and os.path.exists(os.path.join(os.getcwd(), "deeplink-testing.html"))):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # Get the file content
            if self.path == "/":
                file_path = os.path.join(os.getcwd(), "deeplink-testing.html")
            else:
                file_path = os.path.join(os.getcwd(), self.path.lstrip("/"))

            # Read the HTML file
            try:
                with open(file_path, 'r') as file:
                    content = file.read()

                # Inject our network info
                ip_info = get_ip_addresses()
                port = self.server.server_port
                network_info = f"""
                <script>
                // Injected by server.py
                window.SERVER_INFO = {{
                    networkIp: "{ip_info['local_ip']}",
                    port: {port},
                    hostname: "{ip_info['hostname']}",
                }};
                </script>
                """

                if "<script" in content:
                    content = content.replace("<script", network_info + "<script", 1)
                elif "</head>" in content:
                    content = content.replace("</head>", network_info + "</head>", 1)
                else:
                    content = network_info + content

                self.wfile.write(content.encode())
                return
            except IOError:
                pass  # Fall back to normal handling if file can't be read

        # Default behavior for all other paths
        return super().do_GET()

def run_server(port):
    """Run the HTTP server with IP information."""
    ip_info = get_ip_addresses()

    # Get the directory we're serving
    directory = os.getcwd()

    # Set up handler to serve from current directory
    handler = DeeplinkServerHandler

    # Start the server
    try:
        httpd = HTTPServer(("", port), handler)
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"\033[91mError: Port {port} is already in use.\033[0m")
            print(f"Try a different port: python server.py {port+1}")
            sys.exit(1)
        else:
            raise

    # Check if the deeplink testing file exists
    filename = "deeplink-testing.html"
    if os.path.exists(os.path.join(directory, filename)):
        path = f"/{filename}"
    else:
        path = "/"
        print(f"\033[93mWarning: '{filename}' not found in current directory.\033[0m")
        print("The server will still run, but will serve whatever files are available.")

    # Print server information
    print("\n" + "="*70)
    print("\033[1;36mDeeplink Testing Server\033[0m")
    print("="*70)
    print(f"\033[1mServing directory:\033[0m \033[93m{directory}\033[0m")
    print("\033[1mAvailable on:\033[0m")

    # Print access URLs
    print(f"  \033[94m• Local:\033[0m http://localhost:{port}{path}")
    print(f"  \033[92m• Network IP:\033[0m \033[1;4mhttp://{ip_info['local_ip']}:{port}{path}\033[0m  ← Share this URL with other devices")
    print(f"  \033[96m• Computer Name:\033[0m http://{ip_info['hostname']}:{port}{path}")

    # Print server controls
    print("\n\033[1mServer controls:\033[0m")
    print("  Press Ctrl+C to stop the server")
    print("="*70 + "\n")

    # Open browser automatically
    try:
        webbrowser.open(f"http://localhost:{port}{path}")
    except:
        print("\033[93mCouldn't open browser automatically. Please open one of the URLs above.\033[0m")

    # Start server
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\033[91mServer stopped\033[0m")
        httpd.server_close()

if __name__ == "__main__":
    # Get port from command line argument if provided
    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port number: {sys.argv[1]}")
            sys.exit(1)

    run_server(PORT)
