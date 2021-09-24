# GuessMu bot 3.0

### Telegram link:
https://t.me/GuessMu_bot

The bot is running on Heroku.  
Data is store in PostgeSQL database hosted on Heroku.  
Messages are being recieved using webhook.  

### To play with the bot code:
1. Clone the repository
2. Create a new bot. https://core.telegram.org/bots#:~:text=for%20existing%20ones.-,Creating%20a%20new%20bot,mentions%20and%20t.me%20links.
3. Create a PostgreSQL database. SQL statements for database objects can be found in db/sql
4. Create a .env file in bot root directory. Put the following parameters there:  
  `TELEGRAM_TOKEN=<your_bot_token>`  
   `DATABASE_URL=postgres://<user>:<password>@<db_host>:<port>/<db_name>`  

The bot can be run both in polling and webhook mode.  
  `> bot.py [polling|webhook]`  
Mode parameter is required.
Procfile is set up to run bot in webhook mode.


### Other info 
**Bot icon author**
<div>Icons made by <a href="https://www.flaticon.com/authors/geotatah" title="geotatah">geotatah</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
