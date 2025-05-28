import streamlit as st
from agent.hsn_agent import HSNAgent

# Initialize the agent
agent = HSNAgent()

st.set_page_config(page_title="HSN Code Agent", page_icon="🧾")

st.title("🔍 HSN Code Agent")
st.write("Check and suggest HSN codes based on official master data.")

# Tabs for two functionalities
tab1, tab2 = st.tabs(["✅ Validate HSN Code", "💡 Suggest from Description"])

# --- Tab 1: Validate Code ---
with tab1:
    code = st.text_input("Enter HSN Code", placeholder="e.g., 64061000")
    if st.button("Validate Code"):
        if code:
            result = agent.validate_hsn_code(code)
            st.markdown(f"**Result:** {result['message']}")
            if result['exists']:
                st.markdown(f"**Description:** {result.get('description', '')}")
                if result.get('hierarchy'):
                    st.markdown("**Hierarchy:**")
                    for h_code, h_desc in result['hierarchy']:
                        st.write(f"- {h_code}: {h_desc}")
        else:
            st.warning("Please enter a code.")

# --- Tab 2: Suggest from Description ---
with tab2:
    desc = st.text_area("Enter Product Description", placeholder="e.g., leather shoes for men")
    if st.button("Suggest HSN Codes"):
        if desc:
            suggestions = agent.suggest_from_description(desc)
            st.markdown("**Top Matches:**")
            for hsn, matched_desc, score in suggestions:
                st.write(f"- `{hsn}` → {matched_desc} (Score: {score})")
        else:
            st.warning("Please enter a product description.")
