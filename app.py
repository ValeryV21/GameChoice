import streamlit as st
import pandas as pd

st.markdown(
    """
    <style>
    body {
        background-color: #0b3d91;
        color: white;
    }
    .stApp .stContainer {
        background-color: #0b3d91;
        color: white;
    }
    .stButton>button {
        background-color: #1a4da0;
        color: white;
    }
    .stBarChart>div>canvas {
        background-color: #0b3d91 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎬 Любими филми – анкета 🎉")

movies = {
    "🎬 Екшън": ["💥 Джон Уик","🔥 Лудият Макс","🏢 Умирай трудно","⚔️ Гладиатор","🦇 Черният рицар"],
    "👻 Ужаси": ["😱 Заклинанието","🎈 То","⏳ Предизвестена смърт","🚪 Коварен","🌙 Кошмар на Елм стрийт"],
    "😂 Комедия": ["🏠 Сам вкъщи","🍻 Ергенският запой","🤪 От глупав по-глупав","🎩 Мистър Бийн","👨‍👨‍👦 Големи момчета"]
}

if "genre_votes" not in st.session_state:
    st.session_state.genre_votes = {g: 0 for g in movies.keys()}

if "movie_votes" not in st.session_state:
    st.session_state.movie_votes = {movie: 0 for films in movies.values() for movie in films}

genre = st.selectbox("🎭 Избери жанр:", list(movies.keys()))
movie = st.selectbox("🎥 Избери филм:", movies[genre])

if st.button("💾 Запази избора"):
    st.session_state.genre_votes[genre] += 1
    st.session_state.movie_votes[movie] += 1
    st.success("✅ Изборът е записан!")

st.divider()
st.subheader("📊 Статистика")

top_genre = max(st.session_state.genre_votes, key=st.session_state.genre_votes.get)
st.write("🏆 **Най-избиран жанр:**", top_genre)

top_movie = max(st.session_state.movie_votes, key=st.session_state.movie_votes.get)
st.write("🎬 **Най-избиран филм (общо):**", top_movie)

genre_movies = movies[genre]
top_movie_in_genre = max(genre_movies, key=lambda m: st.session_state.movie_votes[m])
st.write(f"⭐ **Най-избиран филм от жанра {genre}:**", top_movie_in_genre)

genre_df = pd.DataFrame.from_dict(st.session_state.genre_votes, orient="index", columns=["📊 Брой"])
movie_df = pd.DataFrame.from_dict(st.session_state.movie_votes, orient="index", columns=["📊 Брой"])

st.bar_chart(genre_df)
st.bar_chart(movie_df)
