from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.integration_type import IntegrationType

# Configuración para el ambiente de pruebas
commerce_code = "597055555532"  # Código de comercio de pruebas
api_key = "597055555532"        # API Key de pruebas
integration_type = IntegrationType.TEST  # Ambiente de integración

# Crear una instancia de Transaction
transaction = Transaction()  # Se inicializa sin pasar parámetros

# Configurar atributos en la instancia
transaction.commerce_code = commerce_code
transaction.api_key = api_key
transaction.integration_type = integration_type

# Crear una transacción
response = transaction.create(
    buy_order="12345678-11",          # Identificador único de la orden
    session_id="123410",        # ID único de sesión
    amount=10000,                    # Monto de la transacción
    return_url="http://www.example.com/retorno"  # URL de retorno
)

print("Token generado:", response['token'])
print("URL para redirigir al usuario:", response['url'] + "?token_ws=" + response['token'])
