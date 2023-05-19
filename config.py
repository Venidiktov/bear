
#то что ниже обязательно заполнить своими данными
proxy_use = 0 # использовать вообще прокси или нет.  1 - использовать  0 - не использовать
proxy_login = 'pf'
proxy_password = '9c'
proxy_address = 'node-de-65.astroproxy.com'
proxy_port = '10257'
proxy_changeIPlink = "http://node-de-65"


#то что ниже желательно настроить под себя

#укажите паузу в работе между кошельками, минимальную и максимальную. 
#При смене каждого кошелька будет выбрано случайное число. Значения указываются в секундах
timeoutMin = 10 #минимальная 
timeoutMax = 30 #максимальная
#задержки между операциями в рамках одного кошелька
timeoutTehMin = 3 #минимальная 
timeoutTehMax = 10 #максимальная



#то что ниже можно менять только если понимаешь что делаешь
proxies = { 'all': f'http://{proxy_login}:{proxy_password}@{proxy_address}:{proxy_port}',}
if proxy_use:
    request_kwargs = {"proxies":proxies, "timeout": 120}
else:
    request_kwargs = {"timeout": 120}

slippage = 10    #### 5 = 0.5%, 10 = 1%, 1 = 0.1%


rpc_links = {
    'polygon': 'https://polygon-rpc.com/',
    'arbitrum': 'https://arb1.arbitrum.io/rpc',
    'optimism':  'https://rpc.ankr.com/optimism',
    'bsc': 'https://bscrpc.com',
    'fantom': 'https://rpc.ftm.tools/',
    'avax': 'https://api.avax.network/ext/bc/C/rpc',
}