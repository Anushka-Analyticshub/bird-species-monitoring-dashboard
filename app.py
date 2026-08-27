import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Bird Species Monitoring",
    page_icon="🐦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# TEST
# ============================================================

st.write("TEST: THIS IS THE CURRENT APP.PY")

# ============================================================
# THEME + CUSTOM HTML
# ============================================================

st.html("""
<style>

html, body {
    font-family: "Segoe UI", Arial, sans-serif;
}

.stApp {
    background: #F4F6F1;
    color: #26382C;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* ==========================================================
   SIDEBAR
========================================================== */

section[data-testid="stSidebar"] {
    background: #E7EDE3;
    border-right: 1px solid #D1DACD;
}

section[data-testid="stSidebar"] * {
    color: #304C3A !important;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #304C3A !important;
    font-weight: 700;
}

section[data-testid="stSidebar"] .stCaption {
    color: #68766B !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label {
    color: #304C3A !important;
    font-weight: 600;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label p {
    color: #304C3A !important;
}

/* ==========================================================
   HERO
========================================================== */

.hero {
    background: linear-gradient(
        135deg,
        #304C3A,
        #456B50
    );

    border-radius: 22px;
    padding: 2.8rem 3rem;
    margin-bottom: 2rem;

    box-shadow:
        0 10px 30px rgba(48, 76, 58, 0.12);
}

.hero-title {
    color: #FFFFFF;
    font-size: 2.6rem;
    font-weight: 750;
    line-height: 1.2;
    margin-bottom: 0.7rem;
}

.hero-subtitle {
    color: #E8F0E6;
    font-size: 1.05rem;
    line-height: 1.7;
    max-width: 850px;
}

.hero-badge {
    display: inline-block;
    margin-top: 1rem;
    padding: 0.45rem 0.9rem;

    background: rgba(255,255,255,0.13);
    border: 1px solid rgba(255,255,255,0.18);

    border-radius: 999px;

    color: #F3F7F1;
    font-size: 0.82rem;
    font-weight: 600;
}

/* ==========================================================
   SECTION HEADINGS
========================================================== */

.section-title {
    color: #304C3A;
    font-size: 1.55rem;
    font-weight: 750;

    margin-top: 1.8rem;
    margin-bottom: 0.35rem;
}

.section-description {
    color: #68766B;
    font-size: 0.95rem;

    margin-bottom: 1.2rem;
}

/* ==========================================================
   KPI CARDS
========================================================== */

.kpi-card {
    background: #FFFFFF;

    border: 1px solid #DCE4D8;
    border-radius: 18px;

    padding: 1.25rem;

    min-height: 125px;

    box-shadow:
        0 5px 18px rgba(48, 76, 58, 0.06);
}

.kpi-label {
    color: #718076;

    font-size: 0.78rem;
    font-weight: 700;

    letter-spacing: 0.7px;

    margin-bottom: 0.45rem;
}

.kpi-value {
    color: #304C3A;

    font-size: 2rem;
    font-weight: 750;
}

.kpi-note {
    color: #8A968D;

    font-size: 0.78rem;

    margin-top: 0.3rem;
}

/* ==========================================================
   STREAMLIT HEADINGS
========================================================== */

h1, h2, h3 {
    color: #304C3A !important;
}

p {
    color: #526257;
}

/* ==========================================================
   TABS
========================================================== */

button[data-baseweb="tab"] {
    color: #526257 !important;
    font-weight: 600;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #304C3A !important;
}

/* ==========================================================
   BUTTONS
========================================================== */

.stButton > button,
.stDownloadButton > button {
    background: #FFFFFF;
    color: #304C3A !important;

    border: 1px solid #B8C8B6;
    border-radius: 10px;

    font-weight: 650;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    border-color: #456B50;
    color: #304C3A !important;
}

/* ==========================================================
   DATAFRAME
========================================================== */

div[data-testid="stDataFrame"] {
    border: 1px solid #DCE4D8;
    border-radius: 14px;
    overflow: hidden;
}

/* ==========================================================
   INPUT LABELS
========================================================== */

label {
    color: #304C3A !important;
    font-weight: 600 !important;
}

/* ==========================================================
   FOOTER
========================================================== */

.footer {
    margin-top: 3rem;
    padding-top: 1.5rem;

    border-top: 1px solid #D6DED3;

    text-align: center;

    color: #7A867D;

    font-size: 0.82rem;
}

.footer strong {
    color: #304C3A;
}

/* ==========================================================
   MOBILE
========================================================== */

@media (max-width: 768px) {

    .hero {
        padding: 2rem 1.4rem;
    }

    .hero-title {
        font-size: 2rem;
    }

    .hero-subtitle {
        font-size: 0.92rem;
    }

    .kpi-value {
        font-size: 1.55rem;
    }

}

</style>
""")

# ============================================================
# LOAD DATA
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

data_file = BASE_DIR / "output" / "cleaned_bird_data.csv"

if not data_file.exists():

    st.error(
        "The cleaned dataset could not be found.\n\n"
        "Expected location:\n"
        "`output/cleaned_bird_data.csv`"
    )

    st.stop()

df = pd.read_csv(data_file)

# ============================================================
# DATE CONVERSION
# ============================================================

if "Date" in df.columns:

    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

# ============================================================
# CALCULATED KPIs
# ============================================================

total_observations = len(df)

unique_species = df["Common_Name"].nunique()

unique_scientific = df["Scientific_Name"].nunique()

monitoring_sites = df["Site_Name"].nunique()

monitoring_plots = df["Plot_Name"].nunique()

years_covered = df["Year"].nunique()

three_minute_records = (
    df["Initial_Three_Min_Cnt"]
    .astype(str)
    .str.lower()
    .eq("true")
    .sum()
)

flyover_records = (
    df["Flyover_Observed"]
    .astype(str)
    .str.lower()
    .eq("true")
    .sum()
)

flyover_percentage = (
    flyover_records / total_observations * 100
    if total_observations
    else 0
)

# ============================================================
# HERO
# ============================================================

st.html("""
<div class="hero">

    <div class="hero-title">
        🐦 Bird Species Monitoring Dashboard
    </div>

    <div class="hero-subtitle">
        Explore bird diversity, monitoring patterns,
        habitat observations and environmental conditions
        across forest monitoring locations.
    </div>

    <div class="hero-badge">
        🌲 Forest Monitoring • 2018 • Interactive Analysis
    </div>

</div>
""")

# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

with st.sidebar:

    st.markdown("## 🐦 Bird Monitoring")

    st.markdown("---")

    st.markdown("### Dashboard Navigation")

    page = st.radio(
        "Navigation",
        [
            "Overview",
            "Species Analysis",
            "Location Analysis",
            "Environmental Analysis",
            "Monitoring Analysis",
            "Data Explorer"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown("### Dataset")

    st.write(f"**Observations:** {total_observations:,}")
    st.write(f"**Species:** {unique_species}")
    st.write(f"**Sites:** {monitoring_sites}")
    st.write(f"**Plots:** {monitoring_plots}")

    st.markdown("---")

    st.caption("Bird Species Monitoring Project")
    st.caption("Python • Pandas • Plotly • Streamlit")

# ============================================================
# OVERVIEW
# ============================================================

if page == "Overview":

    st.markdown(
        '<div class="section-title">📊 Monitoring Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'A high-level view of the bird monitoring dataset.'
        '</div>',
        unsafe_allow_html=True
    )

    # ========================================================
    # KPI ROW 1
    # ========================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.html(f"""
        <div class="kpi-card">
            <div class="kpi-label">TOTAL OBSERVATIONS</div>
            <div class="kpi-value">{total_observations:,}</div>
            <div class="kpi-note">Recorded bird observations</div>
        </div>
        """)

    with c2:

        st.html(f"""
        <div class="kpi-card">
            <div class="kpi-label">BIRD SPECIES</div>
            <div class="kpi-value">{unique_species}</div>
            <div class="kpi-note">Unique species recorded</div>
        </div>
        """)

    with c3:

        st.html(f"""
        <div class="kpi-card">
            <div class="kpi-label">MONITORING SITES</div>
            <div class="kpi-value">{monitoring_sites}</div>
            <div class="kpi-note">Forest monitoring locations</div>
        </div>
        """)

    with c4:

        st.html(f"""
        <div class="kpi-card">
            <div class="kpi-label">MONITORING PLOTS</div>
            <div class="kpi-value">{monitoring_plots}</div>
            <div class="kpi-note">Survey plots</div>
        </div>
        """)

    st.write("")

    # ========================================================
    # KPI ROW 2
    # ========================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.html(f"""
        <div class="kpi-card">
            <div class="kpi-label">THREE-MINUTE RECORDS</div>
            <div class="kpi-value">{three_minute_records}</div>
            <div class="kpi-note">Initial count records</div>
        </div>
        """)

    with c2:

        st.html(f"""
        <div class="kpi-card">
            <div class="kpi-label">YEARS COVERED</div>
            <div class="kpi-value">{years_covered}</div>
            <div class="kpi-note">Monitoring period</div>
        </div>
        """)

    with c3:

        st.html(f"""
        <div class="kpi-card">
            <div class="kpi-label">FLYOVER RECORDS</div>
            <div class="kpi-value">{flyover_records}</div>
            <div class="kpi-note">{flyover_percentage:.2f}% of observations</div>
        </div>
        """)

    with c4:

        min_date = df["Date"].min().strftime("%d %b %Y")
        max_date = df["Date"].max().strftime("%d %b %Y")

        st.html(f"""
        <div class="kpi-card">
            <div class="kpi-label">MONITORING PERIOD</div>
            <div class="kpi-value" style="font-size:1.15rem;">
                {min_date}
            </div>
            <div class="kpi-note">
                to {max_date}
            </div>
        </div>
        """)

    # ========================================================
    # TOP SPECIES
    # ========================================================

    st.markdown(
        '<div class="section-title">🏆 Most Frequently Observed Species</div>',
        unsafe_allow_html=True
    )

    species_counts = (
        df["Common_Name"]
        .value_counts()
        .head(10)
        .sort_values()
        .reset_index()
    )

    species_counts.columns = [
        "Common_Name",
        "Observations"
    ]

    fig = px.bar(
        species_counts,
        x="Observations",
        y="Common_Name",
        orientation="h",
        text="Observations"
    )

    fig.update_traces(
        marker_color="#456B50",
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        margin=dict(
            l=10,
            r=50,
            t=20,
            b=20
        ),
        font=dict(
            family="Segoe UI",
            color="#304C3A"
        ),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    # ========================================================
    # SITE COMPARISON
    # ========================================================

    st.markdown(
        '<div class="section-title">🌲 Monitoring Site Comparison</div>',
        unsafe_allow_html=True
    )

    site_summary = (
        df.groupby("Site_Name")
        .agg(
            Unique_Species=("Common_Name", "nunique"),
            Total_Observations=("Common_Name", "count")
        )
        .reset_index()
    )

    col1, col2 = st.columns(2)

    with col1:

        fig = px.bar(
            site_summary,
            x="Site_Name",
            y="Total_Observations",
            text="Total_Observations"
        )

        fig.update_traces(
            marker_color="#66866A",
            textposition="outside"
        )

        fig.update_layout(
            template="plotly_white",
            title="Total Observations",
            height=400,
            font=dict(
                family="Segoe UI",
                color="#304C3A"
            )
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    with col2:

        fig = px.bar(
            site_summary,
            x="Site_Name",
            y="Unique_Species",
            text="Unique_Species"
        )

        fig.update_traces(
            marker_color="#9AAF8F",
            textposition="outside"
        )

        fig.update_layout(
            template="plotly_white",
            title="Unique Species",
            height=400,
            font=dict(
                family="Segoe UI",
                color="#304C3A"
            )
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

# ============================================================
# SPECIES ANALYSIS
# ============================================================

elif page == "Species Analysis":

    st.markdown(
        '<div class="section-title">🐦 Species Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Explore species observations, diversity and initial three-minute counts.'
        '</div>',
        unsafe_allow_html=True
    )

    species_summary = (
        df.groupby(
            ["Common_Name", "Scientific_Name"],
            dropna=False
        )
        .agg(
            Observations=("Common_Name", "size"),
            Three_Minute_Records=(
                "Initial_Three_Min_Cnt",
                lambda x:
                x.astype(str)
                .str.lower()
                .eq("true")
                .sum()
            )
        )
        .reset_index()
    )

    species_summary["Three_Minute_Percentage"] = (
        species_summary["Three_Minute_Records"]
        / species_summary["Observations"]
        * 100
    )

    species_summary = species_summary.sort_values(
        "Observations",
        ascending=False
    )

    st.dataframe(
        species_summary,
        width="stretch",
        hide_index=True
    )

    st.markdown(
        '<div class="section-title">Top 10 Species</div>',
        unsafe_allow_html=True
    )

    top10 = (
        species_summary
        .head(10)
        .sort_values("Observations")
    )

    fig = px.bar(
        top10,
        x="Observations",
        y="Common_Name",
        orientation="h",
        text="Observations"
    )

    fig.update_traces(
        marker_color="#456B50",
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        xaxis_title="Observations",
        yaxis_title="",
        font=dict(
            family="Segoe UI",
            color="#304C3A"
        )
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.markdown(
        '<div class="section-title">Initial Three-Minute Count</div>',
        unsafe_allow_html=True
    )

    three_min = (
        df.groupby("Common_Name")
        .agg(
            Total_Observations=("Common_Name", "size"),
            Three_Minute_Records=(
                "Initial_Three_Min_Cnt",
                lambda x:
                x.astype(str)
                .str.lower()
                .eq("true")
                .sum()
            )
        )
        .reset_index()
    )

    three_min["Three_Minute_Percentage"] = (
        three_min["Three_Minute_Records"]
        / three_min["Total_Observations"]
        * 100
    )

    three_min = (
        three_min
        .sort_values(
            "Three_Minute_Records",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        three_min.sort_values("Three_Minute_Records"),
        x="Three_Minute_Records",
        y="Common_Name",
        orientation="h",
        text="Three_Minute_Records"
    )

    fig.update_traces(
        marker_color="#7D947D",
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        xaxis_title="Three-Minute Records",
        yaxis_title="",
        font=dict(
            family="Segoe UI",
            color="#304C3A"
        )
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

# ============================================================
# LOCATION ANALYSIS
# ============================================================

elif page == "Location Analysis":

    st.markdown(
        '<div class="section-title">🌲 Location & Habitat Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Compare monitoring sites and species richness across survey plots.'
        '</div>',
        unsafe_allow_html=True
    )

    site_summary = (
        df.groupby("Site_Name")
        .agg(
            Unique_Species=("Common_Name", "nunique"),
            Total_Observations=("Common_Name", "count")
        )
        .reset_index()
    )

    st.dataframe(
        site_summary,
        width="stretch",
        hide_index=True
    )

    fig = px.bar(
        site_summary,
        x="Site_Name",
        y="Total_Observations",
        text="Total_Observations"
    )

    fig.update_traces(
        marker_color="#456B50",
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        title="Observations by Monitoring Site",
        height=420,
        font=dict(
            family="Segoe UI",
            color="#304C3A"
        )
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.markdown(
        '<div class="section-title">🌿 Species Richness by Monitoring Plot</div>',
        unsafe_allow_html=True
    )

    plot_summary = (
        df.groupby("Plot_Name")
        .agg(
            Unique_Species=("Common_Name", "nunique"),
            Total_Observations=("Common_Name", "count")
        )
        .reset_index()
        .sort_values(
            "Unique_Species",
            ascending=False
        )
    )

    st.dataframe(
        plot_summary,
        width="stretch",
        hide_index=True
    )

    top_plots = (
        plot_summary
        .head(10)
        .sort_values("Unique_Species")
    )

    fig = px.bar(
        top_plots,
        x="Unique_Species",
        y="Plot_Name",
        orientation="h",
        text="Unique_Species"
    )

    fig.update_traces(
        marker_color="#789477",
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        title="Top Monitoring Plots by Species Richness",
        height=500,
        xaxis_title="Unique Species",
        yaxis_title="",
        font=dict(
            family="Segoe UI",
            color="#304C3A"
        )
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

# ============================================================
# ENVIRONMENTAL ANALYSIS
# ============================================================

elif page == "Environmental Analysis":

    st.markdown(
        '<div class="section-title">🌤 Environmental Conditions</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Environmental conditions recorded during bird monitoring.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        avg_temp = df["Temperature"].mean()

        st.html(f"""
        <div class="kpi-card">
            <div class="kpi-label">AVERAGE TEMPERATURE</div>
            <div class="kpi-value">{avg_temp:.2f}°C</div>
            <div class="kpi-note">
                Range: {df["Temperature"].min():.1f}°C –
                {df["Temperature"].max():.1f}°C
            </div>
        </div>
        """)

    with col2:

        avg_humidity = df["Humidity"].mean()

        st.html(f"""
        <div class="kpi-card">
            <div class="kpi-label">AVERAGE HUMIDITY</div>
            <div class="kpi-value">{avg_humidity:.2f}%</div>
            <div class="kpi-note">
                Range: {df["Humidity"].min():.1f}% –
                {df["Humidity"].max():.1f}%
            </div>
        </div>
        """)

    with col3:

        disturbance_count = df["Disturbance"].value_counts()

        most_common_disturbance = (
            disturbance_count.index[0]
            if len(disturbance_count)
            else "N/A"
        )

        st.html(f"""
        <div class="kpi-card">
            <div class="kpi-label">MOST COMMON DISTURBANCE</div>
            <div class="kpi-value" style="font-size:1.05rem;">
                {most_common_disturbance}
            </div>
        </div>
        """)

    # ========================================================
    # SKY + WIND
    # ========================================================

    col1, col2 = st.columns(2)

    with col1:

        sky_counts = (
            df["Sky"]
            .value_counts()
            .reset_index()
        )

        sky_counts.columns = [
            "Sky",
            "Observations"
        ]

        fig = px.pie(
            sky_counts,
            names="Sky",
            values="Observations",
            hole=0.45
        )

        fig.update_layout(
            template="plotly_white",
            title="Sky Conditions",
            height=450,
            font=dict(
                family="Segoe UI",
                color="#304C3A"
            )
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    with col2:

        wind_counts = (
            df["Wind"]
            .value_counts()
            .reset_index()
        )

        wind_counts.columns = [
            "Wind",
            "Observations"
        ]

        fig = px.bar(
            wind_counts.sort_values("Observations"),
            x="Observations",
            y="Wind",
            orientation="h",
            text="Observations"
        )

        fig.update_traces(
            marker_color="#66866A",
            textposition="outside"
        )

        fig.update_layout(
            template="plotly_white",
            title="Wind Conditions",
            height=450,
            xaxis_title="Observations",
            yaxis_title="",
            font=dict(
                family="Segoe UI",
                color="#304C3A"
            )
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # ========================================================
    # TEMPERATURE
    # ========================================================

    fig = px.histogram(
        df,
        x="Temperature",
        nbins=15
    )

    fig.update_traces(
        marker_color="#789477"
    )

    fig.update_layout(
        template="plotly_white",
        title="Temperature Distribution",
        xaxis_title="Temperature (°C)",
        yaxis_title="Observations",
        height=400,
        font=dict(
            family="Segoe UI",
            color="#304C3A"
        )
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

# ============================================================
# MONITORING ANALYSIS
# ============================================================

elif page == "Monitoring Analysis":

    st.markdown(
        '<div class="section-title">🔎 Monitoring Methods & Patterns</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Explore how observations were recorded and how monitoring activity was distributed.'
        '</div>',
        unsafe_allow_html=True
    )

    # ========================================================
    # IDENTIFICATION METHODS
    # ========================================================

    method_counts = (
        df["ID_Method"]
        .value_counts()
        .reset_index()
    )

    method_counts.columns = [
        "ID_Method",
        "Observations"
    ]

    col1, col2 = st.columns(2)

    with col1:

        fig = px.bar(
            method_counts.sort_values("Observations"),
            x="Observations",
            y="ID_Method",
            orientation="h",
            text="Observations"
        )

        fig.update_traces(
            marker_color="#456B50",
            textposition="outside"
        )

        fig.update_layout(
            template="plotly_white",
            title="Identification Methods",
            height=420,
            font=dict(
                family="Segoe UI",
                color="#304C3A"
            )
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    with col2:

        visit_counts = (
            df["Visit"]
            .value_counts()
            .sort_index()
            .reset_index()
        )

        visit_counts.columns = [
            "Visit",
            "Observations"
        ]

        fig = px.bar(
            visit_counts,
            x="Visit",
            y="Observations",
            text="Observations"
        )

        fig.update_traces(
            marker_color="#789477",
            textposition="outside"
        )

        fig.update_layout(
            template="plotly_white",
            title="Observations by Visit",
            height=420,
            font=dict(
                family="Segoe UI",
                color="#304C3A"
            )
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # ========================================================
    # OBSERVER
    # ========================================================

    observer_counts = (
        df["Observer"]
        .value_counts()
        .reset_index()
    )

    observer_counts.columns = [
        "Observer",
        "Observations"
    ]

    fig = px.bar(
        observer_counts.sort_values("Observations"),
        x="Observations",
        y="Observer",
        orientation="h",
        text="Observations"
    )

    fig.update_traces(
        marker_color="#66866A",
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        title="Observations by Observer",
        height=450,
        font=dict(
            family="Segoe UI",
            color="#304C3A"
        )
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    # ========================================================
    # DISTANCE
    # ========================================================

    distance_counts = (
        df["Distance"]
        .fillna("Missing")
        .value_counts()
        .reset_index()
    )

    distance_counts.columns = [
        "Distance",
        "Observations"
    ]

    fig = px.pie(
        distance_counts,
        names="Distance",
        values="Observations",
        hole=0.45
    )

    fig.update_layout(
        template="plotly_white",
        title="Observation Distance",
        height=450,
        font=dict(
            family="Segoe UI",
            color="#304C3A"
        )
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    # ========================================================
    # FLYOVER
    # ========================================================

    flyover_df = pd.DataFrame({
        "Category": [
            "Normal observations",
            "Flyover observations"
        ],
        "Observations": [
            total_observations - flyover_records,
            flyover_records
        ]
    })

    fig = px.bar(
        flyover_df,
        x="Category",
        y="Observations",
        text="Observations"
    )

    fig.update_traces(
        marker_color="#9AAF8F",
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        title="Flyover Observations",
        height=400,
        font=dict(
            family="Segoe UI",
            color="#304C3A"
        )
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

# ============================================================
# DATA EXPLORER
# ============================================================

elif page == "Data Explorer":

    st.markdown(
        '<div class="section-title">📋 Data Explorer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Explore and filter the cleaned bird monitoring dataset.'
        '</div>',
        unsafe_allow_html=True
    )

    # ========================================================
    # FILTERS
    # ========================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        selected_site = st.multiselect(
            "Monitoring Site",
            sorted(
                df["Site_Name"]
                .dropna()
                .unique()
            )
        )

    with col2:

        selected_species = st.multiselect(
            "Bird Species",
            sorted(
                df["Common_Name"]
                .dropna()
                .unique()
            )
        )

    with col3:

        selected_method = st.multiselect(
            "Identification Method",
            sorted(
                df["ID_Method"]
                .dropna()
                .unique()
            )
        )

    filtered_df = df.copy()

    if selected_site:

        filtered_df = filtered_df[
            filtered_df["Site_Name"].isin(selected_site)
        ]

    if selected_species:

        filtered_df = filtered_df[
            filtered_df["Common_Name"].isin(selected_species)
        ]

    if selected_method:

        filtered_df = filtered_df[
            filtered_df["ID_Method"].isin(selected_method)
        ]

    st.write(
        f"Showing **{len(filtered_df):,}** "
        f"of **{len(df):,}** observations"
    )

    st.dataframe(
        filtered_df,
        width="stretch",
        hide_index=True
    )

    # ========================================================
    # DOWNLOAD
    # ========================================================

    csv_data = (
        filtered_df
        .to_csv(index=False)
        .encode("utf-8")
    )

    st.download_button(
        label="⬇️ Download Filtered Data",
        data=csv_data,
        file_name="bird_monitoring_filtered.csv",
        mime="text/csv"
    )

# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="footer">

    <strong>Bird Species Monitoring Dashboard</strong><br>

    Forest biodiversity analysis • Python • Pandas • Plotly • Streamlit<br>

    Interactive exploration of bird monitoring observations

</div>
""")