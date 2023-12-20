# Проект "Транскрайбер-аннотатор учебных видео- и аудиофайлов по социально-гуманитарным дисциплинам"
![картинка 1](https://media.giphy.com/media/XuBtcsV266vepmoEYG/giphy.gif)
---

## Цель и функциональность проекта

__Цель проекта__ - облегчить процесс обучения пользователям (студентам).
Данный проект предлагает пользователям получить текстовую версию видеолекции или аудио-файла (транскрипт/субтитры) и получить аннотацию записанного материала. Проект ориентирован на гуманитарные направления обучения.
Проект решает следующие __задачи__:
- помощь в текстовой записи видеолекций;
- экономия времени;
- реализация доступной цифровой среды для обучения слабослышащих и неслышашащих студентах.
---


## Начало работы
Скрипт по развёртыванию проекта находится в ...

На примере Ubuntu /Debian:
<details>
  <summary>Как развернуть приложение локально</summary>
    
    sudo apt update && sudo apt upgrade -y

    sudo apt install python3 python3-virtualenv python3-pip git

    mkdir $HOME/fin-proj && cd $HOME/fin-proj

    git clone https://github.com/mlteamurfu2325/practicum-s1.git .

    python3 -m virtualenv .venv

    source .venv/bin/activate

    pip install faster-whisper streamlit pytube openai

    mkdir models/ && mkdir models/faster-whisper/

    python3 deploy/download_faster_whisper_models.py

    cd src/

    streamlit run run_app.py

</details>

---
## Использование
Проект практически значим для следующих кейсов:

- обеспечение цифровой доступной среды для неслышащих и слабослышащих студентов - через возможность самостоятельной загрузки интересующего видео или аудиофайла и получения текста, файла субтитров;
- оптимизация временных ресурсов на поиск тематического контента - через возможность получить аннотацию (саммари) содержания файла, чтобы принять решение о необходимости полного ознакомления с ним.
- помощь в текстовой записи (коспектировании) видеолекций для дальнейшего удобства поиска информации (при подготовке к экзаменам).

---

## Команда
Команда состоит из 4-х человек (группа №12):
- [Кирилл Хитрин](https://github.com/khit-mle) - Тимлид, менеджер проекта;
- [Алексей Горбачев](https://github.com/ANGorbachev) - UI/UX-проектировщик, фронтенд-разработчик;
- [Данил Хардин](https://github.com/DanilKhardi) - Инженер по машинному обучению, разработчик бэкенда;
- [Елена Икрина](https://github.com/LenaIkra) - QA-инженер, технический писатель.

---
## Лицензия
[Стандартная общественная лицензия GNU (GPL) версии 3](./gpl-3.0.txt) или выше.

---
## Самоконтроль по критериям оценки
#### 1. Структура репозитория:
 * [README.md](./README.md)
 * [deploy](./deploy)
   * [download_faster_whisper_models.py](./deploy/download_faster_whisper_models.py)
 * [src](./src)
   * [llm_summ](./src/llm_summ)
     * [summ_fetcher.py](./src/llm_summ/summ_fetcher.py)
   * [utils](./src/utils)
     * [cuda_checker.py](./src/utils/cuda_checker.py)
   * [run_app.py](./src/run_app.py)
 * [docs](./docs)
     * [README.md](./docs/README.md)
     * [hw01-project-pitch-group12.md](./docs/hw01-project-pitch-group12.md)
     * [dev-conventions.md](./docs/dev-conventions.md)

#### 2. Качество и чистота кода:
- для контроля качества и чистоты кода приняты конвенции по его написанию для участников команды [dev-conventions.md](./docs/dev-conventions.md)
- форматирование кода проверяется с помощью [black](https://github.com/psf/black)
- применяется анализатор кода [flake8](https://flake8.pycqa.org/en/latest/)
- комментарии к коду написаны в соответствии с конвенцией [Restructured Text (reST)](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)

#### 3. Документация
   
Документация представлена ...

#### 4. Решение
   
Работоспособность решения может быть проверена по URL: ...

Либо путём развёртывания на собственной витруальной машине.
