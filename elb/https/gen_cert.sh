mkdir ca
mkdir server
mkdir client

# ca.key 是自己创建的CA的私钥
# openssl req -x509 ... 不经过生成CSR的过程，直接 输出CA的身份证 ca.crt，注意CA的域名是 ca。
# 分别创建 ca-int 的私钥，生成 ca-int 的CSR，以及用 CA 的private key（ca.key）来签署 ca-int 的身份证。
# 分别创建 server 的私钥，生成 server 的CSR，以及用 ca-int 的private key（ca-int.key）来签署 server 的身份证。
# 分别创建 client 的私钥，生成 client 的CSR，以及用 ca-int 的private key（ca-int.key）来签署 client 的身份证。

# key csr crt解释
# key 私钥
# csr 是Certificate Signing Request的缩写，即证书签名申请，这不是证书，这是要求CA给证书签名的一种正式申请。
# 该申请包含申请证书的实体的公钥及该实体店某些信息。该数据将成为证书的一部分。CSR始终使用它携带的公钥所对应的私钥进行签名。
# crt 身份证 即 证书
# TLS：传输层安全协议 Transport Layer Security的缩写
# SSL：安全套接字层 Secure Socket Layer的缩写
# X.509 是一种证书格式.对X.509证书来说，认证者总是CA或由CA指定的人，一份X.509证书是一些标准字段的集合，这些字段包含有关用户或设备及其相应公钥的信息。
# X.509的证书文件，一般以.crt结尾，根据该文件的内容编码格式，可以分为以下二种格式：
# PEM - Privacy Enhanced Mail,打开看文本格式,以"-----BEGIN..."开头, "-----END..."结尾,内容是BASE64编码

# gen ca cert
openssl genrsa -des3 -passout pass:123456 -out ca.key 1024
openssl req -new -x509 -days 3650 -key ca.key --passin pass:123456 -out ca.crt -subj "/CN=ca"
openssl x509 -in ca.crt -out ca.pem

# gen ca-int cert
openssl genrsa -des3 -passout pass:123456 -out ca-int_encrypted.key 1024
openssl rsa -in ca-int_encrypted.key -passin pass:123456 -out ca-int.key
openssl req -new -key ca-int.key -out ca-int.csr -subj "/CN=ca-int"
openssl x509 -req -days 3650 -in ca-int.csr -CA ca.crt -CAkey ca.key -passin pass:123456 -set_serial 01 -out ca-int.crt

# gen server cert
openssl genrsa -des3 -passout pass:123456 -out server_encrypted.key 1024
openssl rsa -in server_encrypted.key -passin pass:123456 -out server.key
openssl req -new -key server.key -out server.csr -subj "/CN=server"
openssl x509 -req -days 3650 -in server.csr -CA ca-int.crt -CAkey cat-int.key -set_serial 01 -out server.crt

# gen client cert
openssl genrsa -des3 -passout pass:123456 -out client_encrypted.key 1024
openssl rsa -in client_encrypted.key -passin pass:123456 -out client.key
openssl req -new -key client.key -out client.csr -subj "/CN=client"
openssl x509 -req -days 3650 -in client.csr -CA ca-int.crt -CAkey cat-int.key -set_serial 02 -out client.crt