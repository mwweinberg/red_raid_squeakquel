# red_raid_squeakquel
A python scraper that pull all of the headlines from the chinese language People's Daily

This builds off of the red_raid scraper that pulls the front page images.  If you are using this, remember to set your year/month/day/story parameters at the top in the variables at one below where you want to start, and to put the same values later on in the code.  

The only file you actually need is the rrs.py file.  The rest of them were just part of my development process and are described below:

NOTE that many of these examples have errors related to encoding because I didn't fix that  until the end.

rrs_cleaner.py: creates the headliner function that prints all of the headlines (h1-3) on the page

rrs_parse_and_store_function_big.py: takes the headlines and adds them to the dictionary "holder".  NOTE: the key that it uses "url" is wrong and will fuck things up. If you just want to use this as a stand along, replace the variable url with a string like "key".

rrs_parse_to_csv.py: adds writing the holder dictionary to csv and save the dictionary as a pickle repository.  Ultimately the second part was cut because I didn't know if/when I would ever use it or how to tell if it was right.

rrs_parse_to_csv_website4.py: instead of using local versions of the target site, this version integrates an actual website lookup function.  It has two instances of the headliner function because I didn't want to add the URL iteration in yet.

rrs_iterate.py: walks through building the target URL accurately

rrs_url_builder.py: cuts the crap and focuses exclusivly on building the URL to make sure the pattern is right before moving on to iterate  (note: I did iterate first and kept having problems, hence url_builder)

rrs_combine1.py: the csv part didn't work, but everything else did so this is the first stable build of the "find the data from the site and go on to the next site" version of the script.

rrs_decoder.py: this was the first test of the encoding/decoding stuff that came from this conversation: http://stackoverflow.com/questions/37102776/beautifulsoup-chinese-character-encoding-error. It turned out the encode/decode operations were backwards for what I wanted to do, but it still illustrated that it was on the right path.

rrs_parse_to_csv_website5.py: this isolated a live set of values for holder in order to test various ways to export them to csv

rrs_combine2.py: this is the final version that was renamed rrs.py on May 8, 2016

