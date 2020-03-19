from http.server import HTTPServer, BaseHTTPRequestHandler
import smtplib, ssl
import urllib
HOST_ADDRESS = "192.168.1.20" #ip portatil
HOST_PORT = 8087


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        if "homer-yuju.png" in self.path:

            file = open('yo.png','rb')
            self.send_response(200)

            self.send_header("Content-type","image/png")
            self.end_headers()
            self.wfile.write(file.read())

            # Method to send email
            sendEmail(self.client_address)


        else:
            self.send_error(404)

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = (HOST_ADDRESS, HOST_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

def sendEmail(addr):

    # SMTP configuration
    port = 465 # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "solmarinesteban@gmail.com" # sending address
    receiver_email = "solmarinesteban@gmail.com"  # receiver address
    password = "amanecer99"   # password
    message = "Subject: Hi"+ "\n\n\nThe address " + str(addr) + """ has visited the image.""" # Email content data

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.ehlo()  # Greeting message with another mail server
        server.login(sender_email, password) # Login
        server.sendmail(sender_email, receiver_email, message) # Send image

if __name__ == '__main__':
    run(handler_class=RequestHandler)
