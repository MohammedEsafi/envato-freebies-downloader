# Envato Freebies Downloader

Python script that can automatically download free monthly Envato elements -> https://elements.envato.com/free

## Installation

Install the required Python dependencies using ```pip3```:

```
$ pip3 install -r requirements.txt
```

You have to download chromedriver and put it in a folder that is on your system’s path. *[use Selenium Documentation](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/#chromiumchrome)*.

## Configuring

it's easy to set up, ```first``` open ```config.json``` file from cloning content and fill it

```json
{
	"username": "KkpyQBRaP9hGGu8C",
	"password": "79-mCa^mKxjFV@hz",
	"download_location": "~/Downloads/envato_freebies"
}
```

## Running

After the configuration file you now can run the script

```
$ python3 .
```