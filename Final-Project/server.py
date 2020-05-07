import http.server
import socketserver
import termcolor
from pathlib import Path
import json


def species_get(endpoint):
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

        if first_argument == "/":
            contents = Path("index_final.html").read_text()
            error_code = 200

        elif first_argument == "/listSpecies":
            ENDPOINT = "info/species"
            species = species_get(ENDPOINT + PARAMS)["species"]

            # This is in order that this http://localhost:8080/listSpecies works
            if len(arguments) > 1:
                second_argument = arguments[1]
                third_argument = second_argument.split("=")[1]
            else:
                third_argument = ""

            # If an integer is not introduced its an error
            try:
                # If no number is specified
                if third_argument == "":
                    contents = f"""
                                    <!DOCTYPE html>
                                    <html lang="en">
                                    <head>
                                        <meta charset="utf-8">
                                        <title>List of species</title>
                                    </head>
                                    <body style="background-color: lightblue">
                                    <p>Total number of species is: {len(species)} </p>
                                    <p>The limit you have selected is:{len(species)}</p>
                                    <p>The names of the species are:</p>
                                    </body></html>
                                    """
                    error_code = 200
                    for element in species:
                        contents += f"""<p> · {element["common_name"]} </p>"""

                # If more than existant is written it is an error
                elif int(third_argument) > len(species):
                    contents = Path('Error.html').read_text()
                    error_code = 404

                # If the number is in the range
                else:
                    contents = f"""
                                    <!DOCTYPE html>
                                    <html lang="en">
                                    <head>
                                        <meta charset="utf-8">
                                        <title>List of species</title>
                                    </head>
                                    <body style="background-color: lightblue">
                                    <p>Total number of species is: {len(species)} </p>
                                    <p>The limit you have selected is:{third_argument}</p>
                                    <p>The names of the species are:</p>
                                    </body></html>
                                    """
                    error_code = 200

                    for element in species[:int(third_argument)]:
                        contents += f"""<p> · {element["common_name"]} </p>"""
            except ValueError:
                contents = Path('Error.html').read_text()
                error_code = 404


        elif first_argument == "/karyotype":
            ENDPOINT = "info/assembly/"
            second_argument = arguments[1]
            third_argument = second_argument.split("=")[1]
            species = third_argument
            # If nothing its introduced its an error
            if species == "":
                contents = Path('Error.html').read_text()
                error_code = 404

            # If something its introduced
            else:
                # See if what the user introduced is available
                try:
                    karyotype = species_get(ENDPOINT + species + PARAMS)["karyotype"]
                    contents = f"""
                                <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="utf-8">
                                    <title>Name of chromosomes</title>
                                </head>
                                <body style="background-color: aquamarine">
                                </body></html>
                                """
                    contents += f"""<h> The names of the chromosomes are: </h>"""
                    for element in karyotype:
                        contents += f"""<p>{element} </p>"""
                    error_code = 200

                # If the introduced doesnt exist
                except KeyError:
                    contents = Path('Error.html').read_text()
                    error_code = 404

        elif first_argument == "/chromosomeLength":
            ENDPOINT = "info/assembly/"
            second_argument = arguments[1]
            third_argument, fourth_argument = second_argument.split("&")
            species = third_argument.split("=")[1]
            chromosome = fourth_argument.split("=")[1]
            if species == "" or chromosome == "":
                contents = Path('Error.html').read_text()
                error_code = 404
            else:
                try:
                    chromo_len = species_get(ENDPOINT + species + PARAMS)["top_level_region"]
                    print(chromo_len)
                    contents = ""
                    for element in chromo_len:
                        if element["coord_system"] == "chromosome":
                            if element["name"] == chromosome:
                                contents = f"""
                                            <!DOCTYPE html>
                                            <html lang="en">
                                            <head>
                                                <meta charset="utf-8">
                                                <title>Chromosome length</title>
                                            </head>
                                            <body style="background-color: lightpink">
                                            </body></html>
                                            """
                                contents += f"""<p> The length of the chromosome {chromosome} of the {species} is: {element["length"]} </p>"""
                    error_code = 200
                    if contents == "":
                        contents = Path('Error.html').read_text()

                except KeyError:
                    contents = Path('Error.html').read_text()
                    error_code = 404

        else:
            contents = Path('Error.html').read_text()
            error_code = 404

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
