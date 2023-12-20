import streamlit as st
from streamlit_bmc import st_bmc

st.set_page_config(
    page_title="Output",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

data = {
    "visual": {
        "company_name": " Analisis implementasi business model canvas pada perusahaan e-marketplace"
    },
    "key_partners": {
        "cards": [
            { "id":"1", "text": "Alpro" },
            { "id":"2", "text": "Manufacturing Partners======" }
        ]
    },
    "key_activities": {
        "cards": [
            { "id":"1", "text": "New Product Development" },
            { "id":"2", "text": "Marketing" }
        ]   
    },
    "key_resources": {
        "cards": [
            { "id":"1", "text": "Intelectual Property (Operational Systems)" },
            { "id":"2", "text": "p" }
        ]
    },
    "value_propositions": { 
        "cards": [
            { "id":"1", "text": "Premium High-End Products and Experience" },
            { "id":"2", "text": "An ecosystem of interconnected services" },
            { "id":"3", "text": "Access to iPhone/iPad user base" }
        ]
    },
    "customer_relationship": {
        "cards": [
            { "id":"1", "text": "Love Brand" },
            { "id":"2", "text": "Apple Care" }
        ]
    },
    "channels": {
        "cards": [
            { "id":"1", "text": "Adit" },
            { "id":"2", "text": "App Store / iTunes" }
        ]
    },
    "customer_segments": {
        "cards": [
            { "id":"1", "text": "Product Buyers" },
            { "id":"2", "text": "Service Subscribers" },
            { "id":"3", "text": "App Developers + Music & Video Producers" }
        ]
    },
    "cost_structure": {
        "cards": [
            { "id":"1", "text": "Operational Costs" },
            { "id":"2", "text": "Marketing and Branding" }
        ]
    },
    "revenue_streams": {
        "cards": [
            { "id":"1", "text": "Product Sales (High-Priced Tech)" },
            { "id":"2", "text": "Service Subscriptions (Recurring Revenue)" },
            { "id":"3", "text": "App and Media Revenues (30% cut)" }
        ]
    }
}

st_bmc(data)
