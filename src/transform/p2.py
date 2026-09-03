raw_transactions =  ["SUCCESS:100", "FAILED:50", "SUCCESS:-10", "SUCCESS:0", "SUCCESS:250", "ERROR:200"]

transaction_codes = [
    int(transaction[transaction.find(":") + 1:])
    for transaction in raw_transactions
    if transaction.startswith("SUCCESS")
    and int(transaction[transaction.find(":") + 1:]) > 0
]


print(f"Очищенные транзакции: {transaction_codes}")
