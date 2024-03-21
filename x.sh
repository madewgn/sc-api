#!/bin/bash

do="http://do.madewgn.eu.org:8000/update"
linode="http://do2.madewgn.eu.org:8000/update"
id_linode="http://id-dc.madewgn.eu.org:8000/update"

response_do=$(curl -s "$do")
response_linode=$(curl -s "$linode")
response_id_linode=$(curl -s "$id_linode")

echo "Response from do.madewgn.eu.org:8000/update:"
echo "$response_do"

echo -e "\nResponse from do2.madewgn.eu.org:8000/update:"
echo "$response_linode"

echo -e "\nResponse from id-idc.madewgn.eu.org:8000/update:"
echo "$response_id_linode"

