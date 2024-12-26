from transbank.webpay.webpay_plus.transaction import Transaction

transaction = Transaction()

token = "01abc6a753b22dcf81673a1bc928dcf0e3edd34fa9caed756be54009a93c022f"  # Token recibido al completar el pago
response = transaction.commit(token)

print("Estado de la transacción:", response.get("status"))
print("Monto de la transacción:", response.get("amount"))
