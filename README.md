# log_creator
A short python program to create logs from a database (containing blog post visits) using sql queries.
## Requirements
- Python 3
- Postgresql running with the news database loaded into it.
  - The news database is included in this repo.
- A Vagrant environment.

## Preparing the environment
  1. Download Vagrant from here: https://www.vagrantup.com/downloads.html
  2. Unzip the Vagrant_Config.zip into a directory.
    - Vagrant_Config.zip is available in this repo.
  3. Navigate to the newly created unzipped directory (ie c:/vagrant_config).
  4. Start the Vagrant environment (vagrant up).
  5. Login to Vagrant (vagrant ssh).
  6. Load the news database into Postgresql.

## Running the Program
- Ensure all the requirements are met.
- Navigate to the directory log_creator.py is located in.
- From the console type the following:
    - `python3 log_creator.py`
