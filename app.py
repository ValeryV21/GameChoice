import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="Gaming Survey", page_icon="🎮", layout="wide")

# Custom styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Orbitron', sans-serif;
    }
    
    .main-title {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(45deg, #FFD700, #FFA500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 30px rgba(255, 215, 0, 0.5);
        margin-bottom: 10px;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { filter: drop-shadow(0 0 10px #FFD700); }
        to { filter: drop-shadow(0 0 20px #FFA500); }
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #E0E0E0;
        margin-bottom: 30px;
    }
    
    .stSelectbox label {
        font-size: 1.2rem !important;
        font-weight: bold !important;
        color: #FFD700 !important;
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #FF6B6B, #FF8E53);
        color: white;
        font-size: 1.1rem;
        font-weight: bold;
        border: none;
        border-radius: 25px;
        padding: 15px 40px;
        box-shadow: 0 5px 15px rgba(255, 107, 107, 0.4);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.6);
    }
    
    .stat-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border: 2px solid rgba(255, 215, 0, 0.3);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }
    
    .stat-title {
        font-size: 1.3rem;
        font-weight: bold;
        color: #FFD700;
        margin-bottom: 10px;
    }
    
    .stat-value {
        font-size: 1.8rem;
        font-weight: 900;
        color: #FFFFFF;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
    }
    
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
        color: #FFD700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<h1 class="main-title">🎮 АНКЕТА ЗА ЛЮБИМИ ИГРИ 🎮</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Избери любимия си жанр и игра!</p>', unsafe_allow_html=True)

# Game database
games = {
    "🎯 Екшън/Приключенски": [
        "🗡️ The Legend of Zelda: Breath of the Wild",
        "🎮 God of War",
        "🏹 Horizon Zero Dawn",
        "⚔️ Ghost of Tsushima",
        "🦇 Batman: Arkham City"
    ],
    "🔫 Шутъри от първо лице": [
        "👑 Call of Duty: Modern Warfare",
        "🎖️ Counter-Strike 2",
        "💀 DOOM Eternal",
        "🌌 Halo Infinite",
        "🔥 Valorant"
    ],
    "🏆 Battle Royale": [
        "🎯 Fortnite",
        "🎮 Apex Legends",
        "🪂 PUBG",
        "⚔️ Call of Duty: Warzone",
        "🌊 Fall Guys"
    ],
    "🎭 RPG": [
        "🐉 The Witcher 3",
        "🗡️ Elden Ring",
        "⚔️ Skyrim",
        "🎲 Baldur's Gate 3",
        "🌟 Final Fantasy XVI"
    ],
    "🏎️ Състезателни": [
        "🏁 Gran Turismo 7",
        "🚗 Forza Horizon 5",
        "🏎️ Mario Kart 8",
        "💨 Need for Speed",
        "🏆 F1 2024"
    ],
    "⚽ Спортни": [
        "⚽ FIFA 24",
        "🏀 NBA 2K24",
        "🏈 Madden NFL 24",
        "🎾 WWE 2K24",
        "⛳ PGA Tour 2K"
    ],
    "🧩 Стратегически": [
        "♟️ Civilization VI",
        "⚔️ Age of Empires IV",
        "🎖️ StarCraft II",
        "🏰 Total War: Warhammer",
        "🌍 XCOM 2"
    ]
}

# Initialize session state
if "genre_votes" not in st.session_state:
    st.session_state.genre_votes = {g: 0 for g in games.keys()}
if "game_votes" not in st.session_state:
    st.session_state.game_votes = {game: 0 for game_list in games.values() for game in game_list}
if "total_votes" not in st.session_state:
    st.session_state.total_votes = 0
if "vote_history" not in st.session_state:
    st.session_state.vote_history = []

# Main selection area
col1, col2 = st.columns(2)

with col1:
    genre = st.selectbox("🎭 Избери жанр:", list(games.keys()), key="genre_select")

with col2:
    game = st.selectbox("🎮 Избери игра:", games[genre], key="game_select")

# Vote button
if st.button("💾 ЗАПАЗИ ИЗБОРА МИ", use_container_width=True):
    st.session_state.genre_votes[genre] += 1
    st.session_state.game_votes[game] += 1
    st.session_state.total_votes += 1
    st.session_state.vote_history.append({"genre": genre, "game": game})
    st.success("✅ Изборът ти е записан!")
    st.balloons()

st.markdown("---")

# Statistics section
if st.session_state.total_votes > 0:
    st.markdown('<h2 style="text-align: center; color: #FFD700; margin-top: 30px;">📊 СТАТИСТИКА ЗА ИГРИТЕ</h2>', unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🎯 Общо гласове", st.session_state.total_votes)
    
    with col2:
        top_genre = max(st.session_state.genre_votes, key=st.session_state.genre_votes.get)
        st.metric("🏆 Топ жанр", top_genre.split()[1])
    
    with col3:
        top_game = max(st.session_state.game_votes, key=st.session_state.game_votes.get)
        game_name = top_game.split(None, 1)[1] if ' ' in top_game else top_game
        st.metric("🎮 Топ игра", game_name[:20] + "..." if len(game_name) > 20 else game_name)
    
    st.markdown("---")
    
    # Charts
    tab1, tab2, tab3 = st.tabs(["📊 Статистика по жанр", "🎮 Статистика по игри", "🔥 Текущ жанр"])
    
    with tab1:
        # Genre bar chart with Plotly
        genre_df = pd.DataFrame.from_dict(st.session_state.genre_votes, orient="index", columns=["Гласове"])
        genre_df = genre_df.sort_values("Гласове", ascending=True)
        
        fig_genre = px.bar(
            genre_df, 
            x="Гласове", 
            y=genre_df.index,
            orientation='h',
            title="Гласове по жанр",
            color="Гласове",
            color_continuous_scale=["#667eea", "#764ba2", "#FFD700"]
        )
        fig_genre.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white', size=14),
            showlegend=False,
            height=400
        )
        st.plotly_chart(fig_genre, use_container_width=True)
    
    with tab2:
        # Top games chart
        game_df = pd.DataFrame.from_dict(st.session_state.game_votes, orient="index", columns=["Гласове"])
        game_df = game_df[game_df["Гласове"] > 0].sort_values("Гласове", ascending=False).head(10)
        
        fig_games = px.bar(
            game_df,
            x=game_df.index,
            y="Гласове",
            title="Топ 10 най-гласувани игри",
            color="Гласове",
            color_continuous_scale=["#FF6B6B", "#FF8E53", "#FFD700"]
        )
        fig_games.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white', size=14),
            showlegend=False,
            xaxis_tickangle=-45,
            height=500
        )
        st.plotly_chart(fig_games, use_container_width=True)
    
    with tab3:
        # Current genre breakdown
        genre_games = games[genre]
        current_genre_votes = {game: st.session_state.game_votes[game] for game in genre_games}
        
        if sum(current_genre_votes.values()) > 0:
            fig_pie = px.pie(
                values=list(current_genre_votes.values()),
                names=list(current_genre_votes.keys()),
                title=f"Разпределение на игрите в {genre}",
                color_discrete_sequence=px.colors.sequential.Plasma
            )
            fig_pie.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white', size=14),
                height=500
            )
            st.plotly_chart(fig_pie, use_container_width=True)
            
            # Show top game in current genre
            top_game_in_genre = max(genre_games, key=lambda m: st.session_state.game_votes[m])
            st.markdown(f'<div class="stat-card"><div class="stat-title">⭐ Най-популярна в {genre}</div><div class="stat-value">{top_game_in_genre}</div></div>', unsafe_allow_html=True)
        else:
            st.info(f"Все още няма гласове за игри от жанр {genre}. Бъди първият, който гласува!")
    
    # Fun facts section
    st.markdown("---")
    st.markdown('<h3 style="text-align: center; color: #FFD700;">🎉 ИНТЕРЕСНИ ФАКТИ</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        genre_diversity = len([v for v in st.session_state.genre_votes.values() if v > 0])
        st.markdown(f'<div class="stat-card"><div class="stat-title">🎭 Изследвани жанрове</div><div class="stat-value">{genre_diversity} / {len(games)}</div></div>', unsafe_allow_html=True)
    
    with col2:
        game_diversity = len([v for v in st.session_state.game_votes.values() if v > 0])
        total_games = sum(len(g) for g in games.values())
        st.markdown(f'<div class="stat-card"><div class="stat-title">🎮 Изпробвани игри</div><div class="stat-value">{game_diversity} / {total_games}</div></div>', unsafe_allow_html=True)

else:
    st.info("👆 Направи първия си избор, за да видиш страхотни статистики!")

# Footer
st.markdown("---")
st.markdown('<p style="text-align: center; color: #E0E0E0; font-size: 0.9rem;">Създадено с ❤️ за геймъри от геймъри | Powered by Streamlit 🎮</p>', unsafe_allow_html=True)
