# python_challenge


Application instructions.

1) running globaly:

TO run this application globally without virtualenv. Make sure you have installed requierd modules:
* pip install requests
* pip install requests-cache
* pip install json
* pip install argparse

The application has three different modes. 
  A) Run both functions to get GEO IP informations and RDAP informations.
  How to run:
    python retrieve_ip_data.py --ipfrom <int - from 1 to 4999> -- ipto <int - from 2 to 5000> -f list_of_ips.txt - text file in the same directory where retrieve_ip_data.py
    
    --ipfrom - this is the index in IP list. You can select starting point of iteration. default = 1 
    --ipto - this is the secound index of the IP list. Select ending point of iteration. default = 2
    -f or --upload-file - this argument takes the text file including IPs.
    
    Example:  python retrieve_ip_data.py --ipfrom 5 --ipto 10 -f list_of_ips.txt - this will return Geo and Rdap informations for five different ips from the list.
    
  B) Run GEO ip function to return GEO information for specify IPs.
    How to run:
      python retrieve_ip_data.py geo --ipfrom <int - from 1 to 4999> -- ipto <int - from 2 to 5000> -f list_of_ips.txt - text file in the same directory where retrieve_ip_data.py
      
       --ipfrom - this is the index in IP list. You can select starting point of iteration. default = 1 
       --ipto - this is the secound index of the IP list. Select ending point of iteration. default = 2
       -f or --upload-file - this argument takes the text file including IPs.
       
  C) Run RDAP ip function to return RDAP information for specify IPs.
    How to run:
       python retrieve_ip_data.py rdap --ipfrom <int - from 1 to 4999> -- ipto <int - from 2 to 5000> -f list_of_ips.txt - text file in the same directory where retrieve_ip_data.py
       
!!!! The text file need to be in the same direcotry what retrieve_ip_data.py. In other case you need to provide the absolute path to the file!!!!!!

2) Running application with venv.
To run using virtualenv enviroment run this command - .\venv\Scripts\activate - you must be in the same directory what retrieve_ip_data.py before typing this command.
To disactivate venv run - .\venv\Scripts\deactivate

To run the functions follow the steps above!

Summary: 

The data is pulled from free API servers. Avoid large number of ips at one time. Sometimes the server can return error because of many request in short time.


Thank you!


      
