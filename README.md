# 🏦 Organization Payment API 💰

Микросервис для обработки платежей и просмотра баланса организаций.

## 🌟 Возможности

- ✅ Прием платежей с валидацией данных
- 🔒 Защита от дублирующихся операций
- 📊 Получение текущего баланса по ИНН
- 📝 Логирование




## 🚀 Быстрый старт
```commandline
git clone git@github.com:Valievx/payments-service-test.git

python -m venv venv
source venv/bin/activate       # Linux/Mac
source venv/Scripts/activate   # Windows
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```


## 📚 Документация API
### 1. Отправка платежа 🧾

Endpoint: POST /api/webhook/bank/

Пример запроса:
```json
{
  "operation_id": "ccf0a86d-041b-4991-bcf7-e2352f7b8a4a",
  "amount": 15000,
  "payer_inn": "1234567890",
  "document_number": "INV-2023-001",
  "document_date": "2023-01-15"
}
```

### 2. Получение баланса 📊

Endpoint: GET /api/organizations/<inn>/balance/

Успешный ответ:
```json
{
  "inn": "1234567890",
  "balance": 145000
}
```

