import streamlit as st
import random

# -----------------------------------------------------------------------------
# 1. DATA (Hentet fra dokumentene dine)
# -----------------------------------------------------------------------------

songs = [
    {"tittel": "Johnny B. Goode", "artist": "Chuck Berry", "tiår": "50-tallet", "sjanger": "Rock'n roll"},
    {"tittel": "Rock Around the Clock", "artist": "Bill Haley and the Comets", "tiår": "50-tallet", "sjanger": "Rock'n roll"},
    {"tittel": "Folsom Prison Blues", "artist": "Johnny Cash", "tiår": "50-tallet", "sjanger": "Country"},
    {"tittel": "Jailhouse Rock", "artist": "Elvis Presley", "tiår": "50-tallet", "sjanger": "Rock'n roll"},
    {"tittel": "I Want to Hold Your Hand", "artist": "The Beatles", "tiår": "60-tallet", "sjanger": "Merseybeat"},
    {"tittel": "Respect", "artist": "Aretha Franklin", "tiår": "60-tallet", "sjanger": "Soul"},
    {"tittel": "Purple Haze", "artist": "Jimi Hendrix", "tiår": "60-tallet", "sjanger": "Psykedelisk rock"},
    {"tittel": "Blowin' in the Wind", "artist": "Bob Dylan", "tiår": "60-tallet", "sjanger": "Folk"},
    {"tittel": "Sgt. Pepper's Lonely Hearts Club Band", "artist": "The Beatles", "tiår": "60-tallet", "sjanger": "Psykedelisk rock"},
    {"tittel": "Stairway to Heaven", "artist": "Led Zeppelin", "tiår": "70-tallet", "sjanger": "Progrock"},
    {"tittel": "Bohemian Rhapsody", "artist": "Queen", "tiår": "70-tallet", "sjanger": "Progrock/Hardrock"},
    {"tittel": "Starman", "artist": "David Bowie", "tiår": "70-tallet", "sjanger": "Glamrock"},
    {"tittel": "Dancing Queen", "artist": "ABBA", "tiår": "70-tallet", "sjanger": "Disco"},
    {"tittel": "God Save the Queen", "artist": "Sex Pistols", "tiår": "70-tallet", "sjanger": "Punk"},
    {"tittel": "The Final Countdown", "artist": "Europe", "tiår": "80-tallet", "sjanger": "Hardrock"},
    {"tittel": "Take On Me", "artist": "A-ha", "tiår": "80-tallet", "sjanger": "Pop"},
    {"tittel": "Billie Jean", "artist": "Michael Jackson", "tiår": "80-tallet", "sjanger": "Pop"},
    {"tittel": "Like a Prayer", "artist": "Madonna", "tiår": "80-tallet", "sjanger": "Pop"},
    {"tittel": "We Are the World", "artist": "USA for Africa", "tiår": "80-tallet", "sjanger": "Pop (Humanitær)"},
    {"tittel": "Ice Ice Baby", "artist": "Vanilla Ice", "tiår": "80-tallet", "sjanger": "Rap/Hip hop"},
    {"tittel": "Smells Like Teen Spirit", "artist": "Nirvana", "tiår": "90-tallet", "sjanger": "Grunge"},
    {"tittel": "I Want It That Way", "artist": "Backstreet Boys", "tiår": "90-tallet", "sjanger": "Boyband"},
    {"tittel": "Wannabe", "artist": "Spice Girls", "tiår": "90-tallet", "sjanger": "Girlpower"},
    {"tittel": "Wonderwall", "artist": "Oasis", "tiår": "90-tallet", "sjanger": "Britpop"},
    {"tittel": "Oops!... I Did It Again", "artist": "Britney Spears", "tiår": "2000-tallet", "sjanger": "Pop"},
    {"tittel": "Wake Me Up", "artist": "Avicii", "tiår": "2010-tallet", "sjanger": "EDM"},
    {"tittel": "Shake It Off", "artist": "Taylor Swift", "tiår": "2010-tallet", "sjanger": "Pop"},
]

samfunn_quiz = [
    {
        "spm": "Hvilket tiår er kjent for at rocken brøt ned raseskiller mellom svarte og hvite?",
        "alt": ["50-tallet", "70-tallet", "90-tallet"],
        "svar": "50-tallet",
        "info": "Rock'n roll (f.eks. Chuck Berry og Elvis) blandet svart R&B med hvit country."
    },
    {
        "spm": "Hva kjennetegnet 60-tallets hippiekultur og musikk?",
        "alt": ["Fokus på penger og karriere", "Protest mot krig og fokus på frihet", "Elektronisk dansemusikk"],
        "svar": "Protest mot krig og fokus på frihet",
        "info": "Psykedelisk rock (f.eks. Jimi Hendrix) var lydsporet til motkulturen."
    },
    {
        "spm": "Hvorfor oppsto pønken på 70-tallet?",
        "alt": ["Som en reaksjon på arbeidsledighet og 'flink' musikk", "For å selge dyre klær", "Fordi folk ville danse disco"],
        "svar": "Som en reaksjon på arbeidsledighet og 'flink' musikk",
        "info": "Sex Pistols og punken var aggressiv og enkel, i kontrast til teknisk progrock."
    },
    {
        "spm": "Hvilken TV-kanal endret musikkindustrien totalt på 80-tallet?",
        "alt": ["NRK", "MTV", "HBO"],
        "svar": "MTV",
        "info": "MTV gjorde musikk visuelt (musikkvideoer). Artister som Madonna og Michael Jackson ble moteikoner."
    },
    {
        "spm": "Hva var 'Grunge' på 90-tallet en reaksjon mot?",
        "alt": ["Politikk", "Kommersiell pop og glatt 80-tallsmusikk", "Internett"],
        "svar": "Kommersiell pop og glatt 80-tallsmusikk",
        "info": "Nirvana representerte det uflidde, ekte og mørke."
    },
    {
        "spm": "Hvordan har strømmetjenester påvirket musikken etter 2010?",
        "alt": ["Vi kjøper flere CD-er", "Musikken er mindre tilgjengelig", "Musikk er alltid tilgjengelig og mer personlig"],
        "svar": "Musikk er alltid tilgjengelig og mer personlig",
        "info": "Algoritmer styrer hva vi hører, og artister kan slå gjennom uten store selskaper."
    }
]

teori_begreper = {
    "Vers": "Forteller historien i sangen. Ofte lik melodi, men ny tekst hver gang.",
    "Refreng": "Hoveddelen av sangen. Samme tekst og melodi hver gang. Ofte det vi husker best.",
    "Bro (Bridge)": "Et parti som skiller seg ut melodisk og harmonisk, ofte før siste refreng.",
    "Dynamikk": "Variasjoner i lydstyrke (svakt til sterkt).",
    "Call-and-response": "Veksling mellom en forsanger og instrumenter/kor (typisk i blues/soul).",
    "Tempo": "Hvor fort eller sakte musikken går (BPM).",
    "Klang": "Hvordan lyden 'føles' i rommet (f.eks. mye ekko vs. tørt)."
}

# -----------------------------------------------------------------------------
# 2. APP OPPSETT
# -----------------------------------------------------------------------------

st.set_page_config(page_title="Musikkprøve Øving", page_icon="🎵")

st.title("🎵 Øve-app til Musikkprøven (Uke 7)")
st.write("Velg hva du vil øve på i menyen til venstre.")

# Sidebar navigasjon
modus = st.sidebar.radio("Modus:", ["🎧 Gjett Låta", "🌍 Samfunn & Historie", "🎼 Oppbygging & Teori"])

# -----------------------------------------------------------------------------
# 3. MODUS: GJETT LÅTA
# -----------------------------------------------------------------------------
if modus == "🎧 Gjett Låta":
    st.header("Kan du detaljene om låta?")
    
    # --- LOGIKK FOR Å STOKKE KORTENE OG UNNGÅ REPETISJON ---
    
    # Hvis vi ikke har en "kortstokk" (quiz_queue) enda, eller den er tom, lag en ny
    if 'quiz_queue' not in st.session_state or not st.session_state.quiz_queue:
        # random.sample lager en tilfeldig rekkefølge av alle sangene
        st.session_state.quiz_queue = random.sample(songs, len(songs))
        st.session_state.quiz_index = 0
        st.toast("Kortstokken er stokket! Lykke til!", icon="🃏")

    # Hent sangen basert på hvor langt vi har kommet i køen (index)
    current_index = st.session_state.quiz_index
    song = st.session_state.quiz_queue[current_index]

    # Vis fremdrift
    antall_totalt = len(songs)
    antall_igjen = antall_totalt - current_index
    st.progress(current_index / antall_totalt, text=f"Sang {current_index + 1} av {antall_totalt}")

    st.subheader(f"🎶 Låt: {song['tittel']}")
    st.write("Fyll inn detaljene nedenfor:")

    with st.form("song_quiz_form"):
        # Artist input (litt snillere med case-insensitive sjekk)
        g_artist = st.text_input("Hvem er artisten?")
        
        # Tiår select
        tiar_liste = sorted(list(set([s['tiår'] for s in songs])))
        g_tiar = st.selectbox("Hvilket tiår?", ["Velg..."] + tiar_liste)
        
        # Sjanger select
        sjanger_liste = sorted(list(set([s['sjanger'] for s in songs])))
        g_sjanger = st.selectbox("Hvilken sjanger?", ["Velg..."] + sjanger_liste)
        
        submitted = st.form_submit_button("Sjekk Svar")
        
        if submitted:
            correct_artist = song['artist'].lower() in g_artist.lower() and len(g_artist) > 2
            correct_tiar = g_tiar == song['tiår']
            correct_sjanger = g_sjanger == song['sjanger']
            
            if correct_artist:
                st.success(f"✅ Riktig artist! ({song['artist']})")
            else:
                st.error(f"❌ Feil artist. Riktig var: **{song['artist']}**")
                
            if correct_tiar:
                st.success(f"✅ Riktig tiår! ({song['tiår']})")
            else:
                st.error(f"❌ Feil tiår. Riktig var: **{song['tiår']}**")
                
            if correct_sjanger:
                st.success(f"✅ Riktig sjanger! ({song['sjanger']})")
            else:
                st.error(f"❌ Feil sjanger. Riktig var: **{song['sjanger']}**")

    # Knapp for neste sang
    if st.button("Neste sang ➡️"):
        # Øk indeksen med 1
        st.session_state.quiz_index += 1
        
        # Sjekk om vi har gått gjennom alle sangene
        if st.session_state.quiz_index >= len(songs):
            st.session_state.quiz_queue = random.sample(songs, len(songs))
            st.session_state.quiz_index = 0
            st.balloons() # Litt feiring når man er ferdig!
            st.success("Du har vært gjennom alle sangene! Vi stokker om og starter på nytt.")
            
        st.rerun()

# -----------------------------------------------------------------------------
# 4. MODUS: SAMFUNN & HISTORIE
# -----------------------------------------------------------------------------
elif modus == "🌍 Samfunn & Historie":
    st.header("Hvordan påvirket musikken samfunnet?")
    st.info("Her får du spørsmål basert på oppsummeringene i PowerPointen.")

    # Enkel quiz-loop
    for i, q in enumerate(samfunn_quiz):
        st.subheader(f"Spørsmål {i+1}")
        st.write(q['spm'])
        user_answer = st.radio("Velg svar:", q['alt'], key=f"q{i}", index=None)
        
        if user_answer:
            if user_answer == q['svar']:
                st.success("Riktig! 🎉")
                st.caption(f"ℹ️ {q['info']}")
            else:
                st.error("Ikke helt... Prøv igjen!")
        st.divider()

# -----------------------------------------------------------------------------
# 5. MODUS: OPPBYGGING & TEORI
# -----------------------------------------------------------------------------
elif modus == "🎼 Oppbygging & Teori":
    st.header("Fagbegreper og Låtoppbygging")
    st.write("Dra i kortene for å lære hva begrepene betyr, eller ta en sjekk nederst.")
    
    # Vis definisjoner
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Begreper")
        for begrep in teori_begreper:
            st.markdown(f"**{begrep}**")
    
    with col2:
        st.subheader("Forklaring (Klikk for å se)")
        for begrep, forklaring in teori_begreper.items():
            with st.expander(f"Hva betyr {begrep}?"):
                st.write(forklaring)
    
    st.divider()
    st.subheader("⚡ Lyn-Quiz: Koble begrep")
    
    # En liten interaktiv test
    if 'quiz_term' not in st.session_state:
        st.session_state.quiz_term = random.choice(list(teori_begreper.keys()))

    term = st.session_state.quiz_term
    correct_def = teori_begreper[term]
    
    st.markdown(f"Hvilken forklaring passer til: **{term}**?")
    
    # Lager alternativer (1 riktig + 2 gale)
    alle_defs = list(teori_begreper.values())
    alle_defs.remove(correct_def)
    options = [correct_def] + random.sample(alle_defs, 2)
    random.shuffle(options)
    
    valg = st.radio("Velg riktig definisjon:", options, key="teori_radio")
    
    if st.button("Sjekk definisjon"):
        if valg == correct_def:
            st.success("Riktig!")
            if st.button("Nytt begrep"):
                st.session_state.quiz_term = random.choice(list(teori_begreper.keys()))
                st.rerun()
        else:
            st.error("Feil. Prøv igjen.")
