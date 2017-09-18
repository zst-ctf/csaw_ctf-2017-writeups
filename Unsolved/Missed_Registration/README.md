tshark -r cap.pcap -Y http.request.method==POST -Tfields -e http.file_data > out2.txt
