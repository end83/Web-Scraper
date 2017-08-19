..**********************************************READ ME*****************************************************
Programming Language- Python 
Libraries- scrapy
Operating System-Kubuntu

**************************   Warning   **************************
Before installing scrapy Package, you have to keep these points in mind-
1. As Scrapy library can interfere with other libraries, installing it in your natural environment( or globally) is not recommended.
2. Create a New virtual environment, thus install scrapy on your system in that environment.

********************    Installation    *************************
1. You can create a new virtual environment by following instructions on this page :- "https://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/"
Note: After installing the new environment, just try to install a new package on the new environment. If the system denies access and ask for permission then the interpreter is probably confused with global and virtual env's python. So try to create a new environment with only base packages.
2.Log into your new virtual environment.
2. Install scrapy on the system by following instructions on "https://docs.scrapy.org/en/latest/intro/install.html"
3. Check if scrapy is installed yet or not by any simple command,e.g, scrapy -h.

********************     Getting used to scrapy     ************************
The best and easiest way to learn scrapy is to use it. You can do it by using scrapy shell and try different commands in it.
For learning scrapy, its documentation is the recommended source.

Link to documentation- "https://docs.scrapy.org/en/latest/intro/overview.html"
Youtube video to get an idea- "https://www.youtube.com/watch?v=nnnDshuflSI&t=3061s"

********************    The current project         **************
The implemented project consists of modification of two files-
1. items.py  - It just consists of a class, which is used for declaring different fields for storing the data.
2. scraper.py-  The scraper consists of spider which is used for scraping the websites.

It has three functions-
1. start_requests- this function is used to iterate over the pages which contains list of pages. And for every page, parse fucntion is called in order to extract every link recipe on the page.
    OR instead of a function you can make a list of star_urls where you can enter all the urls manually.
2. parse- This function basically parses each page extract all the links to the recipes present on the page.
3. parse_item- This function iterates over every page and extracts the required data and store it in the class object from items, here cook().

NOTE - In order to write output the data to the file, either go into settings.py( in same folder with item.py) and select the output file according to your wish.or just write scrapy --output=(name of the file).json (spider)
Meaning of yield- It returns the result without stopping the loop.

to learn about xpath- "https://www.w3schools.com/xml/xpath_intro.asp" is the best source.
for just an intro- xpath('//div[@class="required text"]/text()') '//'selects all div in the parent tag(here, the whole document)
                                                                  '/' selects the text element which is the directly under div
                                                                  <div>
                                                                  "this is"
                                                                  <p>" this not"</p>
                                                                  </div>
                                                                referred to-"this is"
