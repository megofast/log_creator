# log_creator
A short python program to create logs from a database (containing blog post visits) using sql queries.
## Requirements
- Python 3
- Postgresql running with the news database loaded into it.
  - The news database is downloadable from here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip.
- A Vagrant environment.
  - Included in this repo: vagrant_config.zip

## Preparing the environment
  1. Download Vagrant from here: https://www.vagrantup.com/downloads.html
  2. Unzip the Vagrant_Config.zip into a directory.
    - Vagrant_Config.zip is available in this repo.
  3. Navigate to the newly created unzipped directory (ie c:/vagrant_config).
  4. Start the Vagrant environment (vagrant up).
  5. Login to Vagrant (vagrant ssh).
  6. Load the news database into Postgresql.
      1. Download news database from here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip.
      2. Unzip the folder into the vagrant directory.
      3. run the command `psql -d news -f newsdata.sql`.
  7. Congratulations, your environment is set up, proceed to running the program!

## Running the Program
- Ensure all the requirements are met.
- Navigate to the directory log_creator.py is located in.
- From the console type the following:
    - `python3 log_creator.py`

## Attributions
- The vagrant_config.zip file is from Udacity's Full Stack Web Development Nanodegree.
- The newsdata.zip file was created and is available from Udacity's Full Stack Web Developement Nanodegree
