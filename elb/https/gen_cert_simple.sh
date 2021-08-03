openssl genrsa -out server_key.pem 2048
openssl req -new -key server_key.pem -out cert.csr
openssl req -new -x509 -key server_key.pem -out server_cert.pem -days 1095