import streamlit as st
import pandas as pd
import random

# Page configuration
st.set_page_config(
    page_title="Анкета за игри",
    page_icon="🎮",
    layout="wide"
)

# Custom CSS styling
st.markdown("""
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
        background: linear-gradient(45deg, #FF8E53, #FF6B6B);
    }
    
    .stat-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border: 2px solid rgba(255, 215, 0, 0.3);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(255, 215, 0, 0.4);
    }
    
    .stat-title {
        font-size: 1.1rem;
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
    
    .trophy-card {
        background: linear-gradient(135deg, rgba(255, 215, 0, 0.2), rgba(255, 140, 0, 0.2));
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        border: 3px solid #FFD700;
        box-shadow: 0 10px 40px rgba(255, 215, 0, 0.3);
        text-align: center;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    .trophy-title {
        font-size: 1.5rem;
        font-weight: 900;
        color: #FFD700;
        margin-bottom: 15px;
        text-transform: uppercase;
    }
    
    .trophy-value {
        font-size: 2.5rem;
        font-weight: 900;
        color: #FFFFFF;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.8);
    }
    
    .progress-bar {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        height: 25px;
        margin: 10px 0;
        overflow: hidden;
        position: relative;
    }
    
    .progress-fill {
        background: linear-gradient(90deg, #FFD700, #FFA500);
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
        box-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
    }
    
    .progress-text {
        position: absolute;
        width: 100%;
        text-align: center;
        line-height: 25px;
        color: white;
        font-weight: bold;
        font-size: 0.9rem;
    }
    
    .rank-badge {
        display: inline-block;
        background: linear-gradient(135deg, #FF6B6B, #FF8E53);
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        margin: 5px;
        box-shadow: 0 3px 10px rgba(255, 107, 107, 0.4);
    }
    
    .leaderboard-item {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        padding: 15px;
        margin: 8px 0;
        border-left: 5px solid;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: all 0.3s ease;
    }
    
    .leaderboard-item:hover {
        transform: translateX(10px);
        background: rgba(255, 255, 255, 0.15);
    }
    
    .leaderboard-gold { border-left-color: #FFD700; }
    .leaderboard-silver { border-left-color: #C0C0C0; }
    .leaderboard-bronze { border-left-color: #CD7F32; }
    .leaderboard-normal { border-left-color: #667eea; }
    
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
        color: #FFD700;
        font-weight: 900;
    }
    
    [data-testid="stMetricLabel"] {
        color: #FFFFFF !important;
        font-weight: bold !important;
    }
    
    .insight-box {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.3), rgba(118, 75, 162, 0.3));
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    
    .insight-icon {
        font-size: 2rem;
        margin-right: 10px;
    }
    
    .insight-text {
        color: #FFFFFF;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

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

if "vote_streak" not in st.session_state:
    st.session_state.vote_streak = 0

if "achievements" not in st.session_state:
    st.session_state.achievements = []

# Main selection area
col1, col2 = st.columns(2)

with col1:
    genre = st.selectbox("🎭 Избери жанр:", list(games.keys()))

with col2:
    game = st.selectbox("🎮 Избери игра:", games[genre])

# Vote button
if st.button("💾 ЗАПАЗИ ИЗБОРА МИ", use_container_width=True):
    st.session_state.genre_votes[genre] += 1
    st.session_state.game_votes[game] += 1
    st.session_state.total_votes += 1
    st.session_state.vote_streak += 1
    
    # Achievement system
    if st.session_state.total_votes == 1 and "Първи стъпки" not in st.session_state.achievements:
        st.session_state.achievements.append("Първи стъпки")
        st.toast("🏆 Постижение отключено: Първи стъпки!", icon="🎉")
    
    if st.session_state.total_votes == 10 and "Ветеран геймър" not in st.session_state.achievements:
        st.session_state.achievements.append("Ветеран геймър")
        st.toast("🏆 Постижение отключено: Ветеран геймър!", icon="🎉")
    
    if len([v for v in st.session_state.genre_votes.values() if v > 0]) == len(games) and "Изследовател" not in st.session_state.achievements:
        st.session_state.achievements.append("Изследовател")
        st.toast("🏆 Постижение отключено: Изследовател!", icon="🎉")
    
    st.success("✅ Изборът ти е записан!")
    st.balloons()

st.markdown("---")

# Statistics section
if st.session_state.total_votes > 0:
    st.markdown('<h2 style="text-align: center; color: #FFD700; margin-top: 30px;">📊 СТАТИСТИКА ЗА ИГРИТЕ</h2>', unsafe_allow_html=True)
    
    # Trophy showcase - Top stats
    top_genre = max(st.session_state.genre_votes, key=st.session_state.genre_votes.get)
    top_game = max(st.session_state.game_votes, key=st.session_state.game_votes.get)
    
    col1, col2 = st.columns(2)
    
    with col1:
        genre_name = top_genre.split(None, 1)[1] if ' ' in top_genre else top_genre
        st.markdown(f"""
            <div class="trophy-card">
                <div class="trophy-title">👑 Най-популярен жанр</div>
                <div class="trophy-value">{top_genre}</div>
                <p style="color: #FFD700; margin-top: 10px; font-size: 1.2rem;">
                    {st.session_state.genre_votes[top_genre]} гласа
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        game_name = top_game.split(None, 1)[1] if ' ' in top_game else top_game
        st.markdown(f"""
            <div class="trophy-card">
                <div class="trophy-title">🎮 Най-популярна игра</div>
                <div class="trophy-value">{top_game}</div>
                <p style="color: #FFD700; margin-top: 10px; font-size: 1.2rem;">
                    {st.session_state.game_votes[top_game]} гласа
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🎯 Общо гласове", st.session_state.total_votes)
    
    with col2:
        genre_diversity = len([v for v in st.session_state.genre_votes.values() if v > 0])
        st.metric("🎭 Жанрове", f"{genre_diversity}/{len(games)}")
    
    with col3:
        game_diversity = len([v for v in st.session_state.game_votes.values() if v > 0])
        total_games = sum(len(g) for g in games.values())
        st.metric("🎮 Игри", f"{game_diversity}/{total_games}")
    
    with col4:
        st.metric("🔥 Серия", st.session_state.vote_streak)
    
    st.markdown("---")
    
    # Achievements
    if st.session_state.achievements:
        st.markdown("### 🏆 Постижения")
        achievement_cols = st.columns(len(st.session_state.achievements))
        for i, achievement in enumerate(st.session_state.achievements):
            with achievement_cols[i]:
                st.markdown(f'<div class="rank-badge">🏅 {achievement}</div>', unsafe_allow_html=True)
        st.markdown("---")
    
    # Charts with tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Жанрове", "🎮 Топ игри", "🔥 Текущ жанр", "💡 Анализи"])
    
    with tab1:
        st.subheader("Разпределение по жанрове")
        
        # Create leaderboard style for genres
        sorted_genres = sorted(st.session_state.genre_votes.items(), key=lambda x: x[1], reverse=True)
        
        for idx, (g, votes) in enumerate(sorted_genres):
            if votes > 0:
                percentage = (votes / st.session_state.total_votes) * 100
                
                if idx == 0:
                    medal = "🥇"
                    class_name = "leaderboard-gold"
                elif idx == 1:
                    medal = "🥈"
                    class_name = "leaderboard-silver"
                elif idx == 2:
                    medal = "🥉"
                    class_name = "leaderboard-bronze"
                else:
                    medal = f"#{idx+1}"
                    class_name = "leaderboard-normal"
                
                st.markdown(f"""
                    <div class="leaderboard-item {class_name}">
                        <div>
                            <span style="font-size: 1.5rem; margin-right: 10px;">{medal}</span>
                            <span style="font-size: 1.1rem; color: white; font-weight: bold;">{g}</span>
                        </div>
                        <div>
                            <span style="font-size: 1.3rem; color: #FFD700; font-weight: bold;">{votes} гласа</span>
                            <span style="margin-left: 10px; color: #E0E0E0;">({percentage:.1f}%)</span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Progress bar
                st.markdown(f"""
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {percentage}%;"></div>
                        <div class="progress-text">{percentage:.1f}%</div>
                    </div>
                """, unsafe_allow_html=True)
    
    with tab2:
        st.subheader("Топ 10 най-гласувани игри")
        
        # Create leaderboard for games
        sorted_games = sorted(st.session_state.game_votes.items(), key=lambda x: x[1], reverse=True)
        top_10_games = [(g, v) for g, v in sorted_games if v > 0][:10]
        
        if top_10_games:
            for idx, (g, votes) in enumerate(top_10_games):
                percentage = (votes / st.session_state.total_votes) * 100
                
                if idx == 0:
                    medal = "🥇"
                    class_name = "leaderboard-gold"
                elif idx == 1:
                    medal = "🥈"
                    class_name = "leaderboard-silver"
                elif idx == 2:
                    medal = "🥉"
                    class_name = "leaderboard-bronze"
                else:
                    medal = f"#{idx+1}"
                    class_name = "leaderboard-normal"
                
                st.markdown(f"""
                    <div class="leaderboard-item {class_name}">
                        <div>
                            <span style="font-size: 1.5rem; margin-right: 10px;">{medal}</span>
                            <span style="font-size: 1rem; color: white; font-weight: bold;">{g}</span>
                        </div>
                        <div>
                            <span style="font-size: 1.3rem; color: #FFD700; font-weight: bold;">{votes}</span>
                            <span style="margin-left: 10px; color: #E0E0E0;">({percentage:.1f}%)</span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {percentage}%;"></div>
                        <div class="progress-text">{percentage:.1f}%</div>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.info("Все още няма гласове за показване")
    
    with tab3:
        st.subheader(f"Разпределение в {genre}")
        genre_games = games[genre]
        current_genre_votes = {game: st.session_state.game_votes[game] for game in genre_games}
        
        total_genre_votes = sum(current_genre_votes.values())
        
        if total_genre_votes > 0:
            sorted_current = sorted(current_genre_votes.items(), key=lambda x: x[1], reverse=True)
            
            for idx, (g, votes) in enumerate(sorted_current):
                if votes > 0:
                    percentage = (votes / total_genre_votes) * 100
                    
                    if idx == 0:
                        medal = "⭐"
                        class_name = "leaderboard-gold"
                    else:
                        medal = f"#{idx+1}"
                        class_name = "leaderboard-normal"
                    
                    st.markdown(f"""
                        <div class="leaderboard-item {class_name}">
                            <div>
                                <span style="font-size: 1.3rem; margin-right: 10px;">{medal}</span>
                                <span style="font-size: 1rem; color: white; font-weight: bold;">{g}</span>
                            </div>
                            <div>
                                <span style="font-size: 1.2rem; color: #FFD700; font-weight: bold;">{votes}</span>
                                <span style="margin-left: 10px; color: #E0E0E0;">({percentage:.1f}%)</span>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"""
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: {percentage}%;"></div>
                            <div class="progress-text">{percentage:.1f}%</div>
                        </div>
                    """, unsafe_allow_html=True)
        else:
            st.info(f"Все още няма гласове за игри от жанр {genre}. Бъди първият, който гласува!")
    
    with tab4:
        st.subheader("💡 Интересни анализи")
        
        # Most competitive genre
        genre_spread = {g: len([game for game in games[g] if st.session_state.game_votes[game] > 0]) 
                       for g in games.keys()}
        most_diverse_genre = max(genre_spread.items(), key=lambda x: x[1])
        
        if most_diverse_genre[1] > 0:
            st.markdown(f"""
                <div class="insight-box">
                    <span class="insight-icon">🎯</span>
                    <span class="insight-text">
                        <strong>Най-разнообразен жанр:</strong> {most_diverse_genre[0]} 
                        с {most_diverse_genre[1]} различни гласувани игри!
                    </span>
                </div>
            """, unsafe_allow_html=True)
        
        # Dominance analysis
        if st.session_state.total_votes >= 5:
            top_game_votes = st.session_state.game_votes[top_game]
            dominance = (top_game_votes / st.session_state.total_votes) * 100
            
            if dominance > 50:
                emoji = "👑"
                text = f"доминира с {dominance:.1f}% от всички гласове!"
            elif dominance > 30:
                emoji = "🔥"
                text = f"води с {dominance:.1f}% от всички гласове!"
            else:
                emoji = "⚔️"
                text = f"има {dominance:.1f}% - състезанието е напечено!"
            
            st.markdown(f"""
                <div class="insight-box">
                    <span class="insight-icon">{emoji}</span>
                    <span class="insight-text">
                        <strong>{top_game}</strong> {text}
                    </span>
                </div>
            """, unsafe_allow_html=True)
        
        # Exploration progress
        exploration = (game_diversity / total_games) * 100
        
        if exploration < 25:
            emoji = "🌱"
            text = "Тепърва започваш да изследваш игрите!"
        elif exploration < 50:
            emoji = "🚀"
            text = "Добър напредък в изследването!"
        elif exploration < 75:
            emoji = "⭐"
            text = "Впечатляващо разнообразие от игри!"
        else:
            emoji = "🏆"
            text = "Легендарен изследовател на игри!"
        
        st.markdown(f"""
            <div class="insight-box">
                <span class="insight-icon">{emoji}</span>
                <span class="insight-text">
                    <strong>Прогрес на изследване:</strong> {exploration:.1f}% от всички игри - {text}
                </span>
            </div>
        """, unsafe_allow_html=True)
        
        # Fun fact
        fun_facts = [
            "Знаеше ли, че RPG игрите са сред най-дългите игри за завършване? 🎲",
            "Battle Royale жанрът стана популярен едва след 2017 година! 🏆",
            "Първият FPS шутър е Wolfenstein 3D от 1992 година! 🔫",
            "Спортните игри са един от най-старите игрови жанрове! ⚽",
            "Стратегическите игри развиват критичното мислене! 🧩"
        ]
        
        st.markdown(f"""
            <div class="insight-box">
                <span class="insight-icon">💭</span>
                <span class="insight-text">
                    <strong>Забавен факт:</strong> {random.choice(fun_facts)}
                </span>
            </div>
        """, unsafe_allow_html=True)

else:
    st.info("👆 Направи първия си избор, за да видиш страхотни статистики!")

# Footer
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: #E0E0E0; font-size: 0.9rem;">'
    'Създадено с ❤️ за геймъри от геймъри | Powered by Streamlit 🎮'
    '</p>', 
    unsafe_allow_html=True
)
