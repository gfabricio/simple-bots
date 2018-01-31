from prettyconf import config


class Settings:
    BOT_TOKEN = config('BOT_TOKEN', default='')
    NEWS_RSS = config('NEWS_RSS', default='https://hnrss.org/newest')


settings = Settings()
