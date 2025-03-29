import streamlit as st
from google import genai
import json


def fetch_neighboring_states(state):
    client = genai.Client(
        vertexai=True,
        project="PROJECT_ID",
        location="us-central1",
    )

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"US state only border neighbors for: {state}",
        config={
            "temperature": 0.1,
            "max_output_tokens": 100,
            "response_mime_type": "application/json",
            "response_schema": {
                "type": "array",
                "items": {
                    "type": "string",
                    "description": "Name of a neighboring state.",
                },
                "description": "A list of state names that border the input state.",
            },
        },
    )
    return json.loads(response.text)

states = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming",
]

# Create the selectbox
state = st.selectbox(
    "Select your state",
    states,
    index=None,
    placeholder="Select your state...",
)

if state:
    neighbor_states = fetch_neighboring_states(state)

    if len(neighbor_states):
        st.write(f"Neighboring states of **{state}** are:")
        for neighbor_state in neighbor_states:
            st.write(f"- **{neighbor_state}**")
    else:
        st.write(f"**{state}** has no neighbors 😔")
