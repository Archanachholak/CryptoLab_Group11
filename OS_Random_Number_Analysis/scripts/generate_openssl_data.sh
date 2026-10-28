#!/bin/bash
set -e

mkdir -p data

openssl rand -out data/openssl_rand.bin 1048576

echo "OpenSSL: data generated successfully."
wc -c data/openssl_rand.bin