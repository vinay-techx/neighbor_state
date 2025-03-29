import streamlit as st
from google.cloud import bigquery
from google import genai

client = bigquery.Client()

query = (
"""
SELECT state_name
FROM `bigquery-public-data.geo_us_boundaries.states`
ORDER BY 1
"""
)
query_job = client.query(query)
states = [row.state_name for row in query_job.result()]

st.title('Find your neighboring states')

state = st.selectbox(
    "Select your state",
    states,
    index=None,
    placeholder="Select your state...",
)

if state:
    query = (
    f"""
    SELECT neighbors_state
    FROM `bigquery-public-data.geo_us_boundaries.adjacent_states`
    WHERE state_name = '{state}'
    """
    )
    query_job = client.query(query)
    neighbor_states = [row.neighbors_state for row in query_job.result()]

    if len(neighbor_states):
        st.write("Neighboring states of ", state, "are:")
        for neighbor_state in neighbor_states[0]:
            st.write(neighbor_state)
    else:
        st.write(state, " has no neighbors :(")
