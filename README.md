# Tuuba

Tuuba is a simple Discord webhook and YouTube search API based tool that monitors for videos in YouTube with a certain keyword and posts them into Discord channel.


## Usage

Tuuba is intended to be run daily e.g. with cron, so it can monitor videos posted with a certain keyword yesterday. There are no special dependencies like requirements use Discord libraries because this tool essentially uses webhooks with the requests library.

Configuration is rather straightforward. The config.py file that needs to be created requires:

- A YouTube Search API key [(YouTube Data API v3)](https://developers.google.com/youtube/v3/getting-started)
- [A Discord Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)

Then variables **relevanceLanguage** and **keyword** should be filled in. The **relevanceLanguage** helps to narrow down search results. If someone wants to use it, a two letter ISO 3166-1 alpha-2 [country code](https://www.iban.com/country-codes) should be entered.

The **keyword** should be set to the keyword to be monitored.

## TODO

Pagination support and multiple keyword support might be concidered one day.