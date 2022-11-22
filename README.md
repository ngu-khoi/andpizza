# andpizza
abusing andpizza. just a neat webscraping program i developed. we use `selenium` and `beautifulsoup`.

## andpizza_onedollar.py
Program that scrapes the discount codes. It does this by creating an account with a dummy credentials, going into the discount codes page, downloading the QR codes (5 $1 codes and 1 $5 code), parsing them into a 6 digit alphanumeric strings, and storing them into a CSV.

## andpizza_autoorder_onedollar.py
Program that auto-scrapes the dicount codes, but also auto-orders by opening up another session of chrome, logging into an account that's already authenticated, ordering a pizza via accessible API, and uploading the discount codes that are stored in the CSV.

