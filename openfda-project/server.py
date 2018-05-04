import http.server
import socketserver
import json
import http.client
import socket

# -- IP and the port of the server
IP = "localhost"  # Localhost means "I": your local machine
PORT = 8000
socketserver.TCPServer.allow_reuse_adress = True

noexist = "unknown"


# HTTPRequestHandler class
class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # GET
    def do_GET(self):

        start = "<!doctype html>" + "\n" + "<html>" + "\n" + "<body>" + "\n" "<ul>" + "\n"
        finish = "</ul>" + "\n" + "</body>" + "\n" + "</html>"

        try:
            if self.path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                with open("search.practice.html", "r") as f:
                    message = f.read()
                    self.wfile.write(bytes(message, "utf8"))

            elif "searchDrug" in self.path:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                listdrugsearch = []
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPSConnection("api.fda.gov")
                parameters = self.path.split("?")[1]
                drug = parameters.split("&")[0].split("=")[1]
                limit = parameters.split("&")[1].split("=")[1]
                print(drug)
                url = "/drug/label.json?search=active_ingredient:" + drug + "&" + "limit=" + limit
                conn.request("GET", url, None, headers)
                r1 = conn.getresponse()
                drugs_raw = r1.read().decode("utf-8")
                conn.close()
                drug = json.loads(drugs_raw)
                drugs_1 = drug

                for x in range(len(drugs_1['results'])):
                    if 'active_ingredient' in drugs_1['results'][x]:
                        listdrugsearch.append(drugs_1['results'][x]['active_ingredient'][0])
                    else:
                        listdrugsearch.append("This index has no drug")
                with open("practice.html", "w") as f:
                    f.write(start)
                    for element in listdrugsearch:
                        htmlelement = "<li>" + element + "</li>" + "\n"
                        f.write(htmlelement)
                    f.write(finish)
                with open("practice.html", "r") as f:
                    file = f.read()

                self.wfile.write(bytes(file, "utf8"))

            elif "searchCompany" in self.path:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                list = []
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPSConnection("api.fda.gov")
                parameters = self.path.split("?")[1]
                companyname = parameters.split("&")[0].split("=")[1]
                limit = parameters.split("&")[1].split("=")[1]
                url = "/drug/label.json?search=manufacturer_name:" + companyname + "&" + "limit=" + limit
                conn.request("GET", url, None, headers)
                r1 = conn.getresponse()
                company_raw = r1.read().decode("utf-8")
                conn.close()
                companyname = json.loads(company_raw)
                companies_1 = companyname

                for x in range(len(companies_1['results'])):
                    if 'active_ingredient' in companies_1['results'][x]:
                        list.append(companies_1['results'][x]['openfda']["manufacturer_name"][0])
                    else:
                        list.append("This index has no manufacturer name")
                with open("practice.html", "w") as f:
                    f.write(start)
                    for element in list:
                        htmlelement = "<li>" + element + "</li>" + "\n"
                        f.write(htmlelement)
                    f.write(finish)
                with open("practice.html", "r") as f:
                    file = f.read()

                self.wfile.write(bytes(file, "utf8"))

            elif "listDrugs" in self.path:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                list = []
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPSConnection("api.fda.gov")
                drug = self.path.split("?")[1]
                limit = drug.split("=")[1]
                print(drug)
                url = "/drug/label.json?" + "limit=" + limit
                print(url)
                conn.request("GET", url, None, headers)
                r1 = conn.getresponse()
                drugs_raw = r1.read().decode("utf-8")
                conn.close()
                drug = json.loads(drugs_raw)
                drugs_1 = drug

                for x in range(len(drugs_1['results'])):
                    try:
                        if "openfda" in drugs_1["results"][x]:
                            list.append(drugs_1['results'][x]['openfda']["brand_name"][0])
                    except KeyError:
                        list.append("Unknown")

                with open("practice.html", "w") as f:
                    f.write(start)
                    for element in list:
                        htmlelement = "<li>" + element + "</li>" + "\n"
                        f.write(htmlelement)
                    f.write(finish)
                with open("practice.html", "r") as f:
                    file = f.read()

                self.wfile.write(bytes(file, "utf8"))

            elif "listCompanies" in self.path:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                list = []
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPSConnection("api.fda.gov")
                drug = self.path.split("?")[1]
                limit = drug.split("=")[1]
                print(drug)
                url = "/drug/label.json?" + "limit=" + limit
                conn.request("GET", url, None, headers)
                r1 = conn.getresponse()
                drugs_raw = r1.read().decode("utf-8")
                conn.close()
                drug = json.loads(drugs_raw)
                drugs_1 = drug

                for x in range(len(drugs_1['results'])):
                    try:
                        if "openfda" in drugs_1["results"][x]:
                            list.append(drugs_1['results'][x]['openfda']["brand_name"][0])
                    except KeyError:
                        list.append("Unknown")

                with open("practice.html", "w") as f:
                    f.write(start)
                    for element in list:
                        htmlelement = "<li>" + element + "</li>" + "\n"
                        f.write(htmlelement)
                    f.write(finish)
                with open("practice.html", "r") as f:
                    file = f.read()
                self.wfile.write(bytes(file, "utf8"))
            elif "listWarnings" in self.path:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                list = []
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPSConnection("api.fda.gov")
                drug = self.path.split("?")[1]
                limit = drug.split("=")[1]
                print(drug)
                url = "/drug/label.json?" + "limit=" + limit
                conn.request("GET", url, None, headers)
                r1 = conn.getresponse()
                drugs_raw = r1.read().decode("utf-8")
                conn.close()
                drug = json.loads(drugs_raw)
                drugs_1 = drug

                for x in range(len(drugs_1['results'])):
                    try:
                        if "openfda" in drugs_1["results"][x]:
                            list.append(drugs_1['results'][x]['openfda']["brand_name"][0])
                    except KeyError:
                        list.append("Unknown")

                with open("practice.html", "w") as f:
                    f.write(start)
                    for element in list:
                        htmlelement = "<li>" + element + "</li>" + "\n"
                        f.write(htmlelement)
                    f.write(finish)
                with open("practice.html", "r") as f:
                    file = f.read()

                self.wfile.write(bytes(file, "utf8"))

            elif "secret" in self.path:
                self.send_response(401)
                self.send_header('WWW-Authenticate', 'Basic Realm = "OpenFDA Private Zone"')
                self.end_headers()

            elif "redirect" in self.path:
                self.send_response(302)
                self.send_header('Location', 'http://localhost:8000/')
                self.end_headers()

            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                with open("error.html", "r") as f:
                    file = f.read()
                self.wfile.write(bytes(file, "utf8"))




        except KeyError as ex:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open("error.html", "r") as f:
                file = f.read()
            self.wfile.write(bytes(file, "utf8"))

        return


# Handler = http.server.SimpleHTTPRequestHandler
Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer((IP, PORT), Handler)
print("serving at port", PORT)
print("prueba")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
print("")
print("Server stopped!")


# https://github.com/joshmaker/simple-python-webserver/blob/master/server.py
