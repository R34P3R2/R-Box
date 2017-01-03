
echo -n "Website/IP: "
read wp
nmap $wp
echo "Returning to menu... in 10 seconds"
echo "press CTRL+C To Go There Now!"
sleep 10
python menu.py