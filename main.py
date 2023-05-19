import json
from statistics import mean
import time
from web3 import Web3
import requests
import random
from datetime import datetime
import config
import fun
from fun import log




current_datetime = datetime.now()
print(f"\n\n {current_datetime}")
print(f'============================================= Плюшкин Блог =============================================')
print(f'subscribe to : https://t.me/plushkin_blog \n============================================================================================================\n')

keys_list = []
with open("private_keys.txt", "r") as f:
    for row in f:
        private_key=row.strip()
        if private_key:
            keys_list.append(private_key)


i=0
for private_key in keys_list:
    i+=1
    if config.proxy_use:
        while True:
            try:
                requests.get(url=config.proxy_changeIPlink)
                fun.timeOut("teh")            
                result = requests.get(url="https://yadreno.com/checkip/", proxies=config.proxies)
                print(f'Ваш новый IP-адрес: {result.text}')
                break
            except Exception as error:
                print(' !!! Не смог подключиться через Proxy, повторяем через 2 минуты... ! Чтобы остановить программу нажмите CTRL+C или закройте терминал')
                time.sleep(120)

    try:
        web3 = Web3(Web3.HTTPProvider(fun.address['polygon']['rpc'], request_kwargs=config.request_kwargs))
        account = web3.eth.account.from_key(private_key)
        wallet = account.address    
        log(f"I-{i}: Начинаю работу с {wallet}")

        dapp_abi = json.load(open('abi/rarible.json'))
        dapp_address = web3.to_checksum_address("0x8E0DCCa4E6587d2028ed948b7285791269059a62")
        dapp_contract = web3.eth.contract(address=dapp_address, abi=dapp_abi)  

        gasPrice = web3.eth.gas_price
        data = '0x84bb1e42000000000000000000000000'+wallet[2:]+'0000000000000000000000000000000000000000000000000000000000000001000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000180000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        chainId = 137
            
        nonce = web3.eth.get_transaction_count(wallet)
        gasLimit = random.randint(200000, 300000)
        gasPrice = web3.eth.gas_price
            
        transaction = {
        'chainId': chainId,
        'to': dapp_address,
        'value': 0,
        'data': data,
        'gas': gasLimit,
        'gasPrice': gasPrice,    
        'nonce': nonce,    
        
        }

    
        # Подписываем и отправляем транзакцию
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_result = web3.eth.wait_for_transaction_receipt(tx_hash)

        if tx_result['status'] == 1:
            fun.log_ok(f'MINT  OK: {tx_hash}')
        else:
            fun.log_error(f'MINT  false: {tx_hash}')

    except Exception as error:
        fun.log_error(f"Ошибка: {error}")



    fun.timeOut()










    
log("Ну типа все!")