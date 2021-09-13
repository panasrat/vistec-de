# Data Engineer Assignment by VISTEC

This project is dedicated to data engineer assignment by VISTEC.

## Explanation:

There are 2 services provided in this project.

1. insert_to_postgres:
   Randomly select the number of images from all 1000 images scraped from the url into Postgres. This takes 2 arguments: url and number of images. The url is 'https://books.toscrape.com', and the number of images inserted can be adjust between 1 and 1000.
2. image_iterator:
   An iterator which randomly yield an image from the Postgres using `next()` command. The examples are shown in the output once the script is run.

## Running The Script:

To run this project altogether, please create new virtual environment then install `requirements.txt`. Assuming that there exists Postgres (docker-compose.yaml) in the environment, run `sh start.sh` in the terminal.
