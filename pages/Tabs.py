import streamlit as st

import streamlit_shadcn_ui as ui

# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/example.py`
st.header("Tabs")


ui.tabs(options=['PyGWalker', 'Graphic Walker', 'GWalkR', 'RATH'], defaultValue='PyGWalker', key="kanaries")


