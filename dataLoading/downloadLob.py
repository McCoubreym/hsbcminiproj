import requests
from tqdm import tqdm  # progress bars

url = "https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/"
files = [
    #"README.txt",
    #"Tst2022-01-11LOBs.txt",
    #"Tst2022-01-12LOBs.txt",
    #"Tst2022-01-13LOBs.txt",
    ##"Tst2022-01-14LOBs.txt",
    #"Tst2022-01-17LOBs.txt",
    #"Tst2022-01-18LOBs.txt",
    #"Tst2022-01-19LOBs.txt",
    #"Tst2022-01-20LOBs.txt",
    #"Tst2022-01-21LOBs.txt",
    #"Tst2022-01-24LOBs.txt",
    #"Tst2022-01-25LOBs.txt",
    #"Tst2022-01-26LOBs.txt",
    #"Tst2022-01-27LOBs.txt",
    ##"Tst2022-01-28LOBs.txt",
    ##"Tst2022-01-31LOBs.txt",
    #"Tst2022-02-01LOBs.txt",
    #"Tst2022-02-02LOBs.txt",
    #"Tst2022-02-03LOBs.txt",
    ##"Tst2022-02-04LOBs.txt",
    #"Tst2022-02-07LOBs.txt",
    #"Tst2022-02-08LOBs.txt",
    #"Tst2022-02-09LOBs.txt",
    #"Tst2022-02-10LOBs.txt",
    #"Tst2022-02-11LOBs.txt",
    #"Tst2022-02-14LOBs.txt",
    #"Tst2022-02-15LOBs.txt",
    #"Tst2022-02-16LOBs.txt",
    #"Tst2022-02-17LOBs.txt",
    #"Tst2022-02-18LOBs.txt",
    #"Tst2022-02-21LOBs.txt",
    #"Tst2022-02-22LOBs.txt",
    #"Tst2022-02-23LOBs.txt",
    #"Tst2022-02-24LOBs.txt",
    #"Tst2022-02-25LOBs.txt",
    #"Tst2022-02-28LOBs.txt",
    #"Tst2022-03-01LOBs.txt",
    #"Tst2022-03-02LOBs.txt",
    ##"Tst2022-03-03LOBs.txt",
    #"Tst2022-03-04LOBs.txt",
    ##"Tst2022-03-07LOBs.txt",
    #"Tst2022-03-08LOBs.txt",
    #"Tst2022-03-09LOBs.txt",
    #"Tst2022-03-10LOBs.txt",
    ##"Tst2022-03-11LOBs.txt",
    "Tst2022-03-14LOBs.txt",
    "Tst2022-03-15LOBs.txt",
    "Tst2022-03-16LOBs.txt",
    "Tst2022-03-17LOBs.txt",
    "Tst2022-03-18LOBs.txt",
    "Tst2022-03-21LOBs.txt",
    "Tst2022-03-22LOBs.txt",
    "Tst2022-03-23LOBs.txt",
    "Tst2022-03-24LOBs.txt",
    "Tst2022-03-25LOBs.txt",
    "Tst2022-03-28LOBs.txt",
    "Tst2022-03-29LOBs.txt",
    "Tst2022-03-30LOBs.txt",
    "Tst2022-03-31LOBs.txt",
    "Tst2022-04-01LOBs.txt",
    "Tst2022-04-04LOBs.txt",
    "Tst2022-04-05LOBs.txt",
    "Tst2022-04-06LOBs.txt",
    "Tst2022-04-07LOBs.txt",
    "Tst2022-04-08LOBs.txt",
    "Tst2022-04-11LOBs.txt",
    "Tst2022-04-12LOBs.txt",
    "Tst2022-04-13LOBs.txt",
    "Tst2022-04-14LOBs.txt",
    "Tst2022-04-19LOBs.txt",
    "Tst2022-04-20LOBs.txt",
    "Tst2022-04-21LOBs.txt",
    "Tst2022-04-22LOBs.txt",
    "Tst2022-04-25LOBs.txt",
    "Tst2022-04-26LOBs.txt",
    "Tst2022-04-27LOBs.txt",
    "Tst2022-04-28LOBs.txt",
    "Tst2022-04-29LOBs.txt",
    ]
#just a random link of a dummy file
for f in tqdm(files, total=len(files), colour="green",):
    r = requests.get(url + f)
    #retrieving data from the URL using get method

    with open("D:\\awsData\\"+ f, 'wb') as f:
    #giving a name and saving it in any required format
    #opening the file in write mode

        f.write(r.content) 
    #writes the URL contents from the server