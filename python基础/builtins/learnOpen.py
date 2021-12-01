import os
import base64


# "c:/sourcedir"
# posix [unix] /usr/lib
print(os.path.join(os.sep, 'usr', 'lib'))
# windows 'C:\\Windows'
print(os.path.join(os.sep, "C:" + os.sep, "Windows"))


feSslCertFile = "airline.dat"

with open(feSslCertFile, encoding='ascii') as f:
    cert_data = f.read()
    # cert_data_bytes = cert_data #  Error
    cert_data_bytes = cert_data.encode("ascii")
    ssl_cert = base64.b64encode(cert_data_bytes).decode()

with open(feSslCertFile) as f:
    cert_data2 = f.read()
    cert_data_bytes2 = cert_data2.encode("ascii")
    ssl_cert2 = base64.b64encode(cert_data_bytes2).decode()

assert cert_data == cert_data2
assert cert_data_bytes == cert_data_bytes2
assert ssl_cert == ssl_cert2