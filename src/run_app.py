import time
from pathlib import Path

import pysubs2
import streamlit as st
import streamlit_ext as ste
from faster_whisper import WhisperModel
from pytube import YouTube
from streamlit_extras.stylable_container import stylable_container

from llm_summ.summ_fetcher import fetch_summary
from utils.cuda_checker import check_cuda
from utils.data_validator import validate_youtube_url


# No type hints yet available for Streamlit
# so no specifi type hint available for `uploaded_file`
# See https://github.com/streamlit/streamlit/issues/7801
def save_uploaded_file(uploaded_file) -> Path:
    """
    Save an uploaded file to the specified directory and return the file path.

    :param uploaded_file: The file uploaded by the user through the Streamlit interface.
    :return: The path to the saved file.
    :rtype: Path
    """
    dir_path = Path("../media")
    dir_path.mkdir(parents=True, exist_ok=True)

    # create a path object for the file
    file_path = dir_path / uploaded_file.name

    # write the file
    with file_path.open("wb") as f:
        f.write(uploaded_file.getbuffer())

    st.toast(f"Saved file: {file_path}")

    return file_path


st.markdown("### 📖 Итоговый проект группы 1.12")

uploaded_file_path = ""
with st.container():
    st.write("Выбор видеофайла для транскибирования")
    file_mode = st.selectbox(
        "Выберите тип загрузки файла: ",
        ["С Вашего устройства", "С YouTube"],
        index=0,
        help='Используйте "С Вашего устройства" для загрузки файла с локального компьютера или выберите "С YouTube" для загрузки видео по ссылке с YouTube.',
    )
    if file_mode == "С Вашего устройства":
        uploaded_file = st.file_uploader(
            label="🔽 Загрузите файл подходящего формата",
            type=["mp3", "wav", "mp4", "webm"],
            accept_multiple_files=False,
        )

        if uploaded_file is not None:
            st.session_state["file_path"] = save_uploaded_file(uploaded_file)

    else:
        url = st.text_input(
            "Ссылка на YouTube",
            placeholder="Введите URL ссылку на видео с YouTube",
            key="yt_url_input",
        )
        if not validate_youtube_url(url):
            need_url_message = (
                "🙃 Я исчезну, когда Вы введёте корректную ссылку на YouTube."
                + "После ввода нажмите Enter или кликните/тапните "
                + "по любому пустому месту на экране"
            )
            st.info(need_url_message)

        else:
            chosen = st.button("📺 Скачать файл с YouTube")
            if chosen:
                tmp_dir_path = Path("../media")
                tmp_dir_path.mkdir(parents=True, exist_ok=True)
                tmp_name = url.split("?v=")[1] + ".mp4"
                uploaded_file_path = tmp_dir_path / tmp_name
                st.session_state["file_path"] = uploaded_file_path
                yt = YouTube(url)
                stream = yt.streams.get_audio_only()
                with st.spinner("📥 Загружаем файл..."):
                    stream.download(output_path=tmp_dir_path, filename=tmp_name)
                    st.toast(f"💯 Файл с YouTube загружен {uploaded_file_path}")

    with st.expander("🗃️ Дополнительный функционал"):
        summary_checkbox = st.checkbox("🔎 Аннотирование текста", value=False)
        transcribe_text = ""

    transcribe = st.button(
        label="🏁 Запустить транскибирование!",
        disabled=not st.session_state.get("file_path"),
    )

    if transcribe:
        time_start = time.time()
        uploaded_file_path = st.session_state["file_path"]

        with st.spinner("🚚 Загружаем модель. Минутку..."):
            if check_cuda():
                selected_model_path = "../models/faster-whisper/large-v3/"
                local_device = "cuda"
                selected_compute_type = "int8_float16"
                st.toast(body="Обнаружен GPU. Будет ускоряться!", icon="🚀")
            else:
                selected_model_path = "../models/faster-whisper/medium/"
                local_device = "cpu"
                selected_compute_type = "int8"
                st.toast(body="Обнаружен CPU. Придётся подождать...", icon="🐌")

            model = WhisperModel(
                model_size_or_path=selected_model_path,
                device=local_device,
                compute_type=selected_compute_type,
                num_workers=4,
                local_files_only=True,
            )

        with st.spinner("🔬 Первичный анализ файла. Минутку..."):
            segments, info = model.transcribe(
                audio=str(uploaded_file_path), beam_size=5
            )

        st.write(
            f"🌍 Язык речи: {info.language.upper()} с вероятностью {round(info.language_probability,2)}"
        )

        st.write(f"🕒 Длительность в секундах: {round(info.duration, 2)}")

        progress_text = "⏳ Идёт транскрибирование сегментов аудио"

        segments_bar = st.progress(0, text=progress_text)

        with st.expander("📜 Транскрипт текста"):
            transcr_text = ""
            segments_for_srt = []
            for segment in segments:
                st.write(
                    "[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text)
                )
                transcr_text += segment.text + " "
                segment_dict = {
                    "start": segment.start,
                    "end": segment.end,
                    "text": segment.text,
                }
                segments_for_srt.append(segment_dict)
                curr_bar_val = min(segment.end / info.duration, 1.0)
                segments_bar.progress(curr_bar_val, text=progress_text)

                if summary_checkbox:
                    transcribe_text += segment.text + " "

            time_total = time.time() - time_start

            # change progress bar color when done
            st.markdown(
                """
            <style>
                .stProgress > div > div > div > div {
                    background-color: green;
                }
            </style>""",
                unsafe_allow_html=True,
            )

        with st.expander("📖 Текст без временны́х меток:"):
            # wrap text to fit in the container with copy-to-clipboard
            with stylable_container(
                "codeblock",
                """
                code {
                    white-space: pre-wrap !important;
                }
                """,
            ):
                st.code(body=transcr_text)

        with st.expander("🔎 Аннотированный текст"):
            if summary_checkbox:
                with st.spinner("🕵️‍♂️ Аннотируем текст..."):
                    summarized_text = fetch_summary(text=transcr_text)
                    with stylable_container(
                        "codeblock",
                        """
                        code {
                            white-space: pre-wrap !important;
                        }
                        """,
                    ):
                        st.code(body=summarized_text)

        with st.expander("🎞️ SRT-файл для скачивания"):
            subs = pysubs2.load_from_whisper(segments_for_srt)
            srt_fine_name = f"{Path(uploaded_file_path).name}.srt"
            srt_file_path = f"../media/{srt_fine_name}"
            subs.save(srt_file_path)
            with open(srt_file_path) as f:
                ste.download_button("📎 Скачать SRT", f, file_name=srt_fine_name)

        with st.expander("🛠 Техническая информация"):
            st.markdown(f"*Общее время транскрипции*: {round(time_total)} с.")
