import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

bases = ["A", "C", "G", "T"]
SEQ_GET = [
    "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT",
]

FOLDER = "../Session-04/"

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Analize the request line
        req_line = self.requestline.split(' ')

        # Get the path. It always start with the / symbol
        path = req_line[1]

        # Read the arguments
        arguments = path.split('?')

        # Get the verb. It is the first argument
        verb = arguments[0]

        # -- Content type header
        # -- Both, the error and the main page are in HTML
        contents = Path('Error.html').read_text()
        error_code = 404

        if verb == "/":
            # Open the form1.html file
            # Read the index from the file
            contents = Path('form-4.html').read_text()
            error_code = 200
        elif verb == "/ping":
            contents = """
            <!DOCTYPE html>
            <html lang = "en">
            <head>
            <meta charset = "utf-8" >
              <title> PING </title >
            </head >
            <body>
            <h2> PING OK!</h2>
            <p> The SEQ2 server in running... </p>
            <a href="/">Main page</a>
            </body>
            </html>
            """
            error_code = 200
        elif verb == "/get":
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]
            # -- Get all the pairs name = value
            pairs = pair.split('&')
            # -- Get the two elements: name and value
            name, value = pairs[0].split("=")
            n = int(value)

            # -- Get the sequence
            seq = SEQ_GET[n]

            # -- Generate the html code
            contents = f"""
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                          <title> GET </title >
                        </head >
                        <body>
                        <h2> Sequence number {n}</h2>
                        <p> {seq} </p>
                        <a href="/">Main page</a>
                        </body>
                        </html>
                        """
            error_code = 200
        elif verb == "/gene":
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]
            # -- Get all the pairs name = value
            pairs = pair.split('&')
            # -- Get the two elements: name and value
            name, gene = pairs[0].split("=")

            s = Seq()
            s.read_fasta(FOLDER + gene)
            gene_str = str(s)
            # -- Generate the html code
            contents = f"""
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                          <title> GENE </title >
                        </head >
                        <body>
                        <h2> Gene: {gene}</h2>
                        <textarea readonly rows="20" cols="80"> {gene_str} </textarea>
                        <br>
                        <br>
                        <a href="/">Main page</a>
                        </body>
                        </html>
                        """
            error_code = 200
        elif verb == "/operation":
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]
            # -- Get all the pairs name = value
            pairs = pair.split('&')
            # -- Get the two elements: name and value
            name, seq = pairs[0].split("=")
            # -- Get the two elements of the operation
            name, op = pairs[1].split("=")

            # -- Create the sequence
            s = Seq(seq)

            if op == "comp":
                result = s.complement()
            elif op == "rev":
                result = s.reverse()
            else:
                length = s.len()
                count_bases = []
                count_percentages = []
                for e in bases:
                    count = s.count_base(e)
                    percentage = round(s.count_base(e) * (100 / s.len()), 2)
                    count_bases.append(count)
                    count_percentages.append(percentage)

                result = f"""
                <p>Total length: {length}</p>
                <p>A: {count_bases[0]} ({count_percentages[0]}%)</p>
                <p>C: {count_bases[1]} ({count_percentages[1]}%)</p>
                <p>G: {count_bases[2]} ({count_percentages[2]}%)</p>
                <p>T: {count_bases[3]} ({count_percentages[3]}%)</p>"""

            contents = f"""
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                          <title> OPERATION </title >
                        </head >
                        <body>
                        <h2> Sequence </h2>
                        <p>{seq}</p>
                        <h2> Operation: </h2>
                        <p>{op}</p>
                        <h2> Result: </h2>
                        <p>{result}</p>
                        <br>
                        <br>
                        <a href="/">Main page</a>
                        </body>
                        </html>
                        """
            error_code = 200

        # Generating the response message
        self.send_response(error_code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
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