# Генератор случайных паролей

Это простая программа на Python для генерации случайных паролей.

## Использование

1. Cлонируйте репозиторий:
```
git clone https://github.com/wotiwan/passwordgenerator
```

3. Перейдите в директорию проекта:
```
cd passwordgenerator/main
```

4. Установите пакет:
```
python3 setup.py install
```

## Параметры

- `length`: Длина генерируемого пароля.
- `use_digits`: Включать ли цифры в пароль.
- `use_letters`: Включать ли буквы в пароль.
- `use_symbols`: Включать ли спецсимволы в пароль.

## Примеры

Генерация пароля из 8 символов с цифрами и буквами:

python main.py

Введите длину пароля: 8

Использовать цифры? (да/нет): да

Использовать буквы? (да/нет): да

Использовать спецсимволы? (да/нет): нет

Сгенерированный пароль: `1wF3g7H2`

## Лицензия

Этот проект распространяется под лицензией MIT - подробности смотрите в файле [LICENSE](LICENSE).
