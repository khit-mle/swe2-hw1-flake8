# 📼 🤖 📜 Проект "Транскрайбер-аннотатор учебных видео- и аудиофайлов по социально-гуманитарным дисциплинам" (группа 12)
<img src="https://media.giphy.com/media/XuBtcsV266vepmoEYG/giphy.gif" width="250" height="250"/>

---
![gh_showcase_01](https://github.com/mlteamurfu2325/practicum-s1/assets/149804920/3c8ee228-68b5-4916-badd-895211c83671)



---
## 1.1. Цель и функциональность проекта

__Цель проекта__ - облегчить процесс обучения пользователям (студентам).
Данный проект предлагает пользователям получить текстовую версию видеолекции или аудио-файла (транскрипт/субтитры) и получить аннотацию записанного материала. Проект ориентирован на гуманитарные направления обучения.
Проект решает следующие __задачи__:
- помощь в текстовой записи видеолекций;
- экономия времени;
- реализация доступной цифровой среды для обучения слабослышащих и неслышашащих студентах.
---


## 1.2. Начало работы

На примере Ubuntu /Debian:
<details>
  <summary><b>Как развернуть приложение локально</b></summary>
    
    sudo apt update && sudo apt upgrade -y

    sudo apt install python3 python3-virtualenv python3-pip git

    mkdir $HOME/fin-proj && cd $HOME/fin-proj

    # Если не релизную ветку, то игноируем `--branch release-1.0.0`
    git clone --branch release-1.0.0 https://github.com/mlteamurfu2325/practicum-s1.git .

    python3 -m virtualenv .venv

    source .venv/bin/activate

    # Либо pip3 install -r requirements.txt
    pip install faster-whisper streamlit pytube openai pysubs2 streamlit_ext streamlit_extras

    # (для разработчиков - доп. установка инструментов контроля качества кода)
    # pip install pre-commit pylint black isort
    # pre-commit install

    mkdir models/ && mkdir models/faster-whisper/

    python3 deploy/download_faster_whisper_models.py

    cd src/

    # (опционально) Для работы аннотатора необходимо задать переменные окружения
    # LLM_API_KEY и LLM_URL
    # по причинам безопасности они не хранятся в репозитории
    export LLM_API_KEY=...
    export LLM_URL=...

    streamlit run run_app.py

</details>

---
## 1.3. Использование
Проект практически значим для следующих кейсов:

- обеспечение цифровой доступной среды для неслышащих и слабослышащих студентов - через возможность самостоятельной загрузки интересующего видео или аудиофайла и получения текста, файла субтитров;
- помощь студентам иностранного происхождения, обучающимся в российских вузах, - через возможность генерации субтитров для видеозаписей дистанционных лекций и занятий с целью выравнивания возможностей тех из них, кто ещё не владает русским языком на уровне носителя;
- оптимизация временных ресурсов на поиск тематического контента - через возможность получить аннотацию (саммари) содержания файла, чтобы принять решение о необходимости полного ознакомления с ним.
- помощь в текстовой записи (конспектировании) видеолекций для дальнейшего удобства поиска информации (при подготовке к экзаменам).

---

## 1.4. Команда
Команда состоит из 4-х человек (группа №12):
- [Кирилл Хитрин](https://github.com/khit-mle) - Тимлид, менеджер проекта;
- [Алексей Горбачев](https://github.com/ANGorbachev) - UI/UX-проектировщик, фронтенд-разработчик;
- [Данил Хардин](https://github.com/DanilKhardi) - Инженер по машинному обучению, разработчик бэкенда;
- [Елена Икрина](https://github.com/LenaIkra) - QA-инженер, технический писатель;
- Александра Антонова - QA-инженер.

---
## Лицензия
[Стандартная общественная лицензия GNU (GPL) версии 3](./gpl-3.0.txt) или выше.

---
## 1.5. Самоконтроль по критериям оценки
#### 1.5.1. Структура репозитория:
```bash
.
├── README.md
├── deploy
│   └── download_faster_whisper_models.py
├── docs
│   ├── README.md
│   ├── dev-conventions.md
│   ├── hw01-project-pitch-group12.md
│   └── user_guide.md
├── gpl-3.0.txt
├── pytest.ini
├── requirements.txt
├── src
│   ├── llm_summ
│   │   ├── __init__.py
│   │   └── summ_fetcher.py
│   ├── run_app.py
│   └── utils
│       ├── __init__.py
│       ├── cuda_checker.py
│       ├── data_validator.py
│       └── upload_file_saver.py
└── tests
    ├── test_cuda_checker.py
    └── test_data_validator.py
```

#### 1.5.2. Качество и чистота кода:
- для контроля качества и чистоты кода приняты конвенции по его написанию для участников команды [dev-conventions.md](./docs/dev-conventions.md)
- написан файл [конфигурации](.pre-commit-config.yaml) для `pre-commit` с проверкой по ряду хуков из репозитория [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks), а также с помощью `black` и `isort`
- создан GitHub Action [workflow-файл](.github/workflows/format-code.yml) для проверки с помощью `black` и `isort` при создании коммита 
- форматирование кода проверяется с помощью [black](https://github.com/psf/black)
- применяется анализатор кода [pylint](https://github.com/pylint-dev/pylint)
- комментарии к коду написаны в соответствии с конвенцией генератора документации [Sphinx](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)

#### 1.5.3. Документация
   
Документация представлена в директории [docs](./docs)

Имеется [руководство пользователя](./docs/user_guide.md) и [файл](./docs/dev-conventions.md) конвенций по разработке для членов команды.

#### 1.5.4. Решение
   
Работоспособность решения может быть проверена на развёрнутой VPS (без GPU) по URL: https://mle-magistr.duckdns.org/

Либо путём развёртывания на собственной витруальной машине.

Рекомендуемая конфигурация: мин. 4 vCPU, 16 Gb RAM, для GPU-ускорения: 4+GB GPU VRAM.

Для проверки можно воспользоваться кратким [видео](https://www.youtube.com/watch?v=OjdZwAtAG54) о философах-досократиках.

#  2.1. Описание задачи в соответствии с Формой отчётности номер 1 на платформе SF
## Тип задачи - "Персональный помощник для студентов" 🧑‍🎓

## 🌒 2.1. Введение
Данный проект предлагает пользователям (студентам) получить текстовую версию видеолекции или аудио-файла (транскрипт/субтитры). 
С помощью нашего приложения студенту будет легче ориентироваться в своих видеолекциях, а текстовый формат лекции поможет в подготовке к экзаменам.
Проект также реализует цели обеспечения цифровой доступной среды в обучении для слабослышащих и не-слышащих студентов.  

## 🔬 2.2. Анализ проблемы
В настоящее время очень много обучающего контента для студентов представлено в формате видеолекций.
В бесконечном потоке видео, студенту становится сложно найти нужную ему информацию. 
В связи с этим часть знаний может быть потеряна, а также потрачено большое количество времени на поиск полезной информации.
Существующие решения на популярных видеохостингах не ко всем видео предоставляют субтитры. А некоторые видеохостинги вообще не предоставляют такой возможности.
Особенно актуально всё это студентов с проблемами восприятия звуковой информации.

## 🗒️ 2.3. Описание решения
IT-решение будет выполнено в виде web-приложения, в которое нужно загрузить ссылку с видео/аудио-файлом (или само видео/аудио с локального устройства), и приложение выдаст текстовую версию данного видео.

Данный проект будет состоять из следующих этапов:
1) Разработка дизайна и фронтенда веб-приложения;
2) Реализация получения аудио из видео с использованием необходимых библиотек;
3) Подготовка и настройка модели машинного обучения по переводу аудио в текст (speech-to-text);
4) Реализация бекенда приложения;
5) Развертывание приложения на хостинге или облаке;
6) Тестирование.

Задачи распределяются в соответствии с профилем участника команды, указанным в разделе 5.

Предполагаемые на данном этапе технологии, инструменты, алгоритмы:
`Python`, `ffmpeg`, `Whisper`, `Streamlit`

## 🧰 2.4. Практическая ценность и применимость
Данное решение поможет студентам в формировании конспектов видеолекций, улучшит навигацию по видеолекциям и ускорит поиск полезной информации в видео. 
Благодаря нашему приложению, студент сможет по текстовой версии лекции оценить значимость и полезность для него конкретной видеолекции. Это позволит воспринимать бóльший и более релевантный (для конкретного студента) объем информации, что в конечно итоге улучшит качество образования в целом.

## 👷 2.5. План действий
В процентном отношении этапы имеют следующее ресурсно-временное распределение:
1) Разработка дизайна и фронтенда веб-приложения - 15%;
2) Реализация получения аудио из видео с использованием необходимых библиоте - 20%;
3) Подготовка и настройка модели машинного обучения по переводу аудио в текст (speech-to-text) - 20%;
4) Реализация бекенда приложения - 20%;
5) Развертывание приложения на хостинге или облаке - 10%;
6) Тестирование - 15%.

## 🎓 2.6. Заключение
Преимущества предлагаемого нами решения:
* использование open source технологических решений, что снижает барьеры использования программного продукта и его разработки;
* возможность локального развёртывания конечным пользователем на аппаратных платформах потребительского уровня;
* использование state-of-the-art ML-решений и моделей (локальная модель Whisper, разработанная лидером индустрии - компанией OpenAI).

В итоге будет разработан MVP (минимально жизнеспособный продукт) - IT-решение конкретной проблемы в образовательном процессе.
В реализованном виде он уже может использоваться студентами для повышения эффективности своего обучения.
Потенциально для данного решения есть возможность расширения:
1) получение транскриптов иностранных лекций с автоматическим переводом на русский язык;
2) получение выжимки по лекции с использованием локальной ML-модели или через API LLM-модели из облака.
