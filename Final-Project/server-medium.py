import http.server
import socketserver
import termcolor
from pathlib import Path
import json
from Seq1 import Seq


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
    response = conn.getresponse()
    print(f"Response received!: {response.status} {response.reason}\n")
    data = response.read().decode("utf-8")
    data_1 = json.loads(data)
    return data_1


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
            contents = Path("index_final_med.html").read_text()
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

            # If both or any entry is left in blank
            if species == "" or chromosome == "":
                contents = Path('Error.html').read_text()
                error_code = 404

            # If none of the entries are in blank
            else:

                # To make sure if an incorrect value is selected, the error page is seen
                try:
                    chromo_len = species_get(ENDPOINT + species + PARAMS)["top_level_region"]
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
                                contents += f"""<p> The length of the chromosome {chromosome} of the {species} is: {element["length"]} </p> """
                    error_code = 200

                    # When the chromosome introduced is not correct
                    if contents == "":
                        contents = Path('Error.html').read_text()

                except KeyError:
                    contents = Path('Error.html').read_text()
                    error_code = 404

        elif first_argument == "/geneSeq":
            ENDPOINT = "xrefs/symbol/homo_sapiens/"
            second_argument = arguments[1]
            third_argument = second_argument.split("=")[1]
            sequence = species_get(ENDPOINT + third_argument + PARAMS)[0]
            contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>Gene sequence</title>
                        </head>
                        <body style="background-color: lightsteelblue">
                        </body></html>
                        """
            contents += f"""<b> The sequence of gene {sequence["id"]} known as {third_argument} is: </b>"""

            ENDPOINT = "sequence/id/"
            sequence_1 = species_get(ENDPOINT + sequence["id"] + PARAMS)
            contents += f"""<p>{sequence_1["seq"]}</p>"""
            error_code = 200

        elif first_argument == "/geneInfo":
            ENDPOINT = "xrefs/symbol/homo_sapiens/"
            second_argument = arguments[1]
            third_argument = second_argument.split("=")[1]
            sequence = species_get(ENDPOINT + third_argument + PARAMS)[0]
            contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>Gene information</title>
                        </head>
                        <body style="background-color: plum">
                        </body></html>
                        """
            contents += f"""<b> The information of gene {third_argument} is:  </b>"""

            ENDPOINT = "lookup/id/"
            sequence_1 = species_get(ENDPOINT + sequence["id"] + PARAMS)
            gene_length = int(sequence_1["end"]) - int(sequence_1["start"])
            contents += f"""<p>The gene starts at: {sequence_1["start"]}</p>"""
            contents += f"""<p>The gene ends at: {sequence_1["end"]}</p>"""
            contents += f"""<p>The length of the gene is: {gene_length}</p>"""
            contents += f"""<p>The ID of the gene is: {sequence_1["id"]}</p>"""
            contents += f"""<p>The gene is in the chromosome: {sequence_1["seq_region_name"]}</p>"""

            error_code = 200

        elif first_argument == "/geneCalc":
            ENDPOINT = "xrefs/symbol/homo_sapiens/"
            second_argument = arguments[1]
            third_argument = second_argument.split("=")[1]
            sequence = species_get(ENDPOINT + third_argument + PARAMS)[0]
            contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>Gene calculations</title>
                        </head>
                        <body style="background-color: palegreen">
                        </body></html>
                        """
            contents += f"""<b> The calculations of gene {third_argument} are:  </b>"""

            ENDPOINT = "sequence/id/"
            sequence_1 = species_get(ENDPOINT + sequence["id"] + PARAMS)
            seq = Seq(sequence_1["seq"])
            contents += f"""<p>Length of the gene is: {seq.len()}</p>"""
            bases = ["A", "C", "T", "G"]
            for base in bases:
                base_percentage = round(seq.count_base(base) * 100 / seq.len(),2)
                contents += f"""<p> The number of {base} in the gene is {seq.count_base(base)} which is a {base_percentage} %"""
            error_code = 200

        elif first_argument == "/geneList":
            ENDPOINT = "overlap/region/homo_sapiens/"
            second_argument = arguments[1]
            third_argument, fourth_argument, fifth_argument = second_argument.split("&")
            chromo = third_argument.split("=")[1]
            start = fourth_argument.split("=")[1]
            end = fifth_argument.split("=")[1]
            PARAM = "?feature=gene;feature=transcript;feature=cds;feature=exon;content-type=application/json"

            list_id = []
            sequence = species_get(ENDPOINT + chromo + ":" + start + "-" + end + PARAM)
            contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>Gene list</title>
                        </head>
                        <body style="background-color: lightyellow">
                        </body></html>
                        """
            contents += f"""<b>The list of genes of chromosome {chromo} between the positions {start} and {end} is: </b>"""
            for element in sequence:
                list_id.append(element["id"])

            ENDPOINT = "/lookup/id/"
            for id_number in list_id:
                sequence = species_get(ENDPOINT + id_number + PARAMS)
                contents += f"""<p>{sequence}"""

            error_code = 200

        # If the endpoint is not correct
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
