#!/bin/bash
set -e

mkdir -p data

head -c 1048576 /dev/urandom > data/linux_urandom.bin

echo "Linux /dev/urandom: data generated successfully."
wc -c data/linux_urandom.bin