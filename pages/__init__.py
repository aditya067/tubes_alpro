import os
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "streamlit_bmc",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/public")
    _component_func = components.declare_component("streamlit_bmc", path=build_dir)
def st_bmc(data, key=None):
    """Create a new instance of "business_model_canvas".
    
    Parameters
    ----------
    data: json
        The name of the thing we're saying hello to. The component will display
        the text "Hello, {name}!"
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    void
        Simple is golden

    """
    component_value = _component_func(data=data, key=key, default=0)
    return component_value

if not _RELEASE:
    import streamlit as st
    st.set_page_config(
        page_title="Business Model Canvas",
        page_icon="📝",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"
        }
    )
    data = {
        "visual": {
            "company_name": "Apple"
        },
        "key_partners": {
            "cards": [
                { "id":"1", "text": "Manufacturing Partners (mostly chinese)" },
                { "id":"2", "text": "Cellphone Carriers" }
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
                { "id":"1", "text": "Intelectual Property (Operational Systems, digital plataform, etc)" },
                { "id":"2", "text": "Brand" }
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
                { "id":"1", "text": "Apple Stores" },
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
    with st.container():
        st_bmc(data)
