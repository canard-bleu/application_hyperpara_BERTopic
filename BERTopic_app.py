import streamlit as st
import pandas as pd
from pathlib import Path
from PIL import Image

st.set_page_config(
    page_title="Étude hyperparamètres BERTopic",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

st.title("Étude hyperparamètres BERTopic")

graphiques_info = {
    "titles" : ["Morphologie des clusters", "Morphologie des clusters", "Cohérence thématique","Cohérence thématique", "Cohérence thématique"],
    "graphiques" : ["Taille des clusters", "Boxplot des tailles de clusters", "Scores par cluster attendu", "Diversité lexicale des topics", "Silhouette score"]
}
graphiques_info = pd.DataFrame(graphiques_info)


params = ["n_neighbors", "n_components", "min_dist", "min_cluster_size", "min_samples"]
with st.sidebar:
    st.header("Options")
    param = st.selectbox(
        "Paramètre étudié",
        options = params
    )

    nr_topics = st.radio(
        "nr_topics",
        ["None", "40"],
        horizontal=True
    )

save = ""
for i, row in graphiques_info.iterrows():
    if row["titles"] != save :
        st.header(row["titles"])
        save = row["titles"]

    graph = row["graphiques"]
    st.subheader(graph)
    img_path = Path(f"BERTopic_figures/nr_topic = {nr_topics}, {param} - {graph}.png")


    if img_path.exists():
        st.image(Image.open(img_path), use_container_width=True)
    else:
        st.warning("Aucun graphique trouvé pour cette combinaison.")
