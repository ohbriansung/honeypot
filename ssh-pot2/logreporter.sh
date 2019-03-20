while [ true ]
do
	history | tail -100 > text.txt
	mpack -s "Honeypot Logs" text.txt kumarsherif771@gmail.com
	sleep 3600
done
