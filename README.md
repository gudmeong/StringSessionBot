# Pyrogram and Telethon String Session Bot [@gudmeong_strbot](http://t.me/gudmeong_strbot)

<p align="center"><a href="https://github.com/gudmeong/StringSessionBot"><img src="https://telegra.ph//file/7dedf187e88e8af3e1822.jpg" width="1500"></a></p>

Telegram bot to generate pyrogram and telethon string session.

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

## Usage

### Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/gudmeong/StringSessionBot)

1. Tap on above button and fill `API_ID`, `API_HASH`, `BOT_TOKEN`, `OWNER_ID`, `BOT_USERNAME` (and `MUST_JOIN`).
2. Then tap "Deploy App" below it. Wait till deploying is complete (will take atmost 2 minutes).
3. After deploying is complete, tap on "Manage App"
4. Check the logs to see if your bot is ready!

### Local Deploying

1. Clone the repo
   ```markdown
   git clone -b master https://github.com/gudmeong/StringSessionBot
   ```
2. Get a DATABASE_URL. If you don't know how, deploy using Heroku Button only or delete database things as it's not a compulsion.
   
3. Edit `Config.py` and fill the needed variables

4. Enter the directory
   ```markdown
   cd StringSessionBot
   ```
5. Run the file
   ```markdown
   python3 generator.py
   ```

## Environment Variables

#### Mandatory Vars

- `API_ID` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `API_HASH` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)
- `OWNER_ID` - You user id
- `BOT_USERNAME` - Your bot username
- `DATABASE_URL` - Will be automatically added by Heroku.
- `MUST_JOIN` - Username/ID of your telegram channel/group.

## Credits

- [Dan Tès](https://github.com/delivrance) for his [Pyrogram](https://docs.pyrogram.org) Library
- [Lonami](https://github.com/Lonami) for his [Telethon](https://docs.telethon.dev) Library 
- [aylak](https://t.me/ayIak) for **Telethon** idea of [v1.0.0](https://github.com/StarkBotsIndustries/StringSessionBot/commit/48e06bb6d9ed156797ef4bc0dab88820fef948f3)
- [StarkBotsIndustries](https://github.com/StarkBotsIndustries/StringSessionBot)


[![ForTheBadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)

![ForTheBadge makes-people-smile](http://ForTheBadge.com/images/badges/makes-people-smile.svg)
