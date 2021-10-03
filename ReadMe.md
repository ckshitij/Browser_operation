## Enpoints for Code to manipulate Browerser

###Below are the 3 Enpoints all are (GET calls)

- Start Browser and open the passed URL
    - http://127.0.0.1:6123/start?browser=chrome&url=www.google.com
    - http://127.0.0.1:6123/start?browser=firefox&url=www.google.com

- Stop All browser instances
    - http://127.0.0.1:6123/stop?browser=chrome
    - http://127.0.0.1:6123/stop?browser=firefox

- Clean all the browing history, cache , cokkies etc
    - http://127.0.0.1:6123/cleanup?browser=firefox
    - http://127.0.0.1:6123/cleanup?browser=chrome