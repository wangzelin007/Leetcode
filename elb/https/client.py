# py2
import httplib
import socket
import ssl
import traceback

httpsConn = None
CERT_FILE = 'server_cert.pem' # Server certificate (given to client)
host = '127.0.0.1:20000'
path = ''

def https_req():
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        httpsConn = httplib.HTTPSConnection(host)
        sock = socket.create_connection((httpsConn.host, httpsConn.port))
        try:
            httpsConn.sock = ssl.wrap_socket(sock, ca_certs=CERT_FILE, cert_reqs=ssl.CERT_REQUIRED, ssl_version=ssl.PROTOCOL_SSLv3)
        except Exception as e:
            print("error SSLv3.")
            print(traceback.format_exc())
            try:
                httpsConn.sock = ssl.wrap_socket(sock, ca_certs=CERT_FILE, cert_reqs=ssl.CERT_REQUIRED, ssl_version=ssl.PROTOCOL_SSLv23)
            except Exception as e:
                print("error SSLv23.")
                print(traceback.format_exc())
                try:
                    httpsConn.sock = ssl.wrap_socket(sock, ca_certs=CERT_FILE, cert_reqs=ssl.CERT_REQUIRED, ssl_version=ssl.PROTOCOL_SSLv2)
                except Exception as e:
                    print("error SSLv2")
                    print(traceback.format_exc())
                    try:
                        httpsConn.sock = ssl.wrap_socket(sock, ca_certs=CERT_FILE, cert_reqs=ssl.CERT_REQUIRED, ssl_version=ssl.PROTOCOL_TLSv1)
                    except Exception as e:
                        print("error TLSv1")
                        print(traceback.format_exc())

        httpsConn.request("GET", path)
        res = httpsConn.getresponse()
        headers = {}
        for k,v in res.getheaders():
            headers[k] = v
        print(res.status, headers, res.read())
        return res.status, headers, res.read()
    except Exception as e:
        print(traceback.format_exc())
    finally:
        if httpsConn:
            httpsConn.close

if __name__ == '__main__':
    https_req()