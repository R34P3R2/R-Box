echo -n "Website/IP: "
read wp
echo -n "Port: "
read port
python PortScanner.py -T $wp -p $port
echo "Returning to menu... in 10 seconds"
echo "press CTRL+C To Go There Now!"
sleep 10
