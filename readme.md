# Автотесты для конфигурационного файла

Проект для валидации конфигурационных файлов в формате INI. Проверяет:

- Соответствие структуры файла
- Корректность параметров
- Допустимость значений

## Требования

- Python 3.6+
- Установленные зависимости из `requirements.txt`
- Доступ к файлу конфигурации (по умолчанию `/var/opt/kaspersky/config.ini`)

## Установка

1. Создайте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

---

## **Запуск тестов**

### Стандартный конфиг

```bash
pytest
```

### Кастомный конфиг

```bash
export CONFIG_PATH=/path/to/myconfig.ini  # Linux/macOS
pytest
```

```cmd
set CONFIG_PATH=C:\path\to\myconfig.ini  # Windows (cmd)
pytest
```

```PowerShell
$env:CONFIG_PATH = "C:\path\to\myconfig.ini"  # Windows (PowerShell)
pytest 
```

### Запуск с подробным выводом:

```bash
pytest -v
```