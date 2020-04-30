import http.server
import socketserver
import termcolor
from pathlib import Path
import json


def client_get_species(endpoint):
    PORT = 8080
    SERVER = 'rest.ensembl.org'
    print(f"\nConnecting to server: {SERVER}:{PORT}\n")
    conn = http.client.HTTPConnection(SERVER)
    try:
        conn.request("GET", endpoint)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data = r1.read().decode("utf-8")
    data1 = json.loads(data)
    return data1


PORT = 8080
SERVER = 'rest.ensembl.org'
PARAMS = '?content-type=application/json'
conn = http.client.HTTPConnection(SERVER)
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        req_line = self.requestline.split(' ')
        path = req_line[1]
        arguments = path.split('?')
        first_argument = arguments[0]

        contents = Path('Error.html').read_text()
        error_code = 404

        if first_argument == "/":
            contents = Path("index_final.html").read_text()
            error_code = 200

        elif first_argument == "/listSpecies":
            ENDPOINT = "info/species"
            species = client_get_species(ENDPOINT + PARAMS)["species"]
            second_argument = arguments[1]
            third_argument = second_argument.split("=")[1]

            if third_argument == "":
                contents = f"""
                                <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="utf-8">
                                    <title>List of species</title>
                                </head>
                                <body style="background-color: lightblue">
                                <p>Total number of species is: 267 </p>
                                <p>The limit you have selected is:{267}</p>
                                <p>The names of the species are:</p>
                                </body></html>
                                """
                error_code = 200
                for element in species:
                    contents += f"""<p> · {element["common_name"]} </p>"""

            elif int(third_argument) > 267:
                contents = Path('Error.html').read_text()
                error_code = 404

            else:
                contents = f"""
                                <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="utf-8">
                                    <title>List of species</title>
                                </head>
                                <body style="background-color: lightblue">
                                <p>Total number of species is: 267 </p>
                                <p>The limit you have selected is:{third_argument}</p>
                                <p>The names of the species are:</p>
                                </body></html>
                                """
                error_code = 200

                for element in species[:int(third_argument)]:
                    contents += f"""<p> · {element["common_name"]} </p>"""


        elif first_argument == "/karyotype":

            error_code = 200

        elif first_argument == "/chromosomeLength":

            error_code = 200

        self.send_response(error_code)
        self.send_header('Content-Type', "text/html")
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))
        return


Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
