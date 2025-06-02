# 💳 Payments System — Тестовое задание

## 📌 Описание

Этот проект — **тестовое задание**, целью которого является реализовать обработку webhook-ов от банка и вести учёт баланса организаций по их ИНН.

### 📋 Суть задания:

- Реализовать API, принимающий **входящие webhook-и** от банка.
- **Создавать транзакции** и **начислять сумму** на баланс организации по `payer_inn`.
- **Обеспечить защиту от дублирующих операций** (по `operation_id`).
- Реализовать эндпоинт для получения **текущего баланса** по ИНН.

---

## 🛠️ Стек технологий

- Python 3.9
- Django 4.2.17
- Django REST Framework
- MySQL (или SQLite для разработки)

---

## 🚀 Установка и запуск

1. Клонировать проект:

```
git clone https://github.com/mishatunikov/payment_system.git
```
2. Создать и активировать виртуальное окружение:

```
python -m venv venv
```

Для MacOS/Linux
```
source venv/bin/activate  
```
Для Windows:
```
venv\Scripts\activate
```

3. Установить зависимости:
```
pip install -r requirements/requirements.txt
```

4. Выполнить миграции:

```
python manage.py migrate
```

5. Запустить сервер:

```
python manage.py runserver
```

## 🔌 API Эндпоинты
POST /api/webhook/bank/

Обработка входящего webhook-а от банка.
Пример запроса:
```
{
  "operation_id": "ccf0a86d-041b-4991-bcf7-e2352f7b8a4a",
  "amount": 145000,
  "payer_inn": "1234567890",
  "document_number": "PAY-328",
  "document_date": "2024-04-27T21:00:00Z"
}
```
Поведение:

    ✅ Если операция с таким operation_id уже существует — возвращается 200 OK, баланс не изменяется.

    ➕ Если новая — создаётся объект Payment, изменяется баланс, логируется изменение.

📊 GET /api/organizations/<inn>/balance/

Получение текущего баланса организации по ИНН.
Пример ответа:
```
{
  "inn": "1234567890",
  "balance": 145000
}
```
