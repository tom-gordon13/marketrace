run = True
from datetime import date
from datetime import timedelta

def timedFunc():
    import requests
    import json
    import schedule, time
    from main_app.models import Stock

    today = date.today()
    yesterday = today - timedelta(days = 1)
    stock_data_raw_obj = requests.get(f'https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/{yesterday}?adjusted=true&apiKey=ISRFyZyx4zGrz0Pzy3veu6ou4pPUYQjU').json()['results']

    for tckr in stock_data_raw_obj:
        currStock = Stock.objects.filter(ticker=(tckr['T']))

        if (len(currStock) == 0 and tckr['v'] >= 10000000):
            currStock = Stock.objects.create(
                ticker=tckr['T'],
                mr_close=tckr['c'],
                mr_volume=tckr['v'],
                mr_vol_weighted=tckr['vw'],
                industry='na',
                logo='na',
                description='na',
                market_cap=1
            )
        elif (len(currStock) > 0):
            currStock = Stock.objects.get(ticker=(tckr['T']))
            currStock.mr_close = tckr['c']
            currStock.mr_volume = tckr['v']
            currStock.mr_vol_weighted = tckr['vw']
            currStock.save()
        else:
            pass
        print(currStock)
    

def runFunc():
    import requests
    import json

    import schedule, time

    # from background_task import background

    from main_app.models import Stock



<<<<<<< HEAD
    
=======
    idx = 0
>>>>>>> 1eff916 (Bug fix with heroku db)
    schedule.every(6).hours.do(timedFunc)

    while run:
        schedule.run_pending()
        time.sleep(21600)



