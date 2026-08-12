import streamlit as st

# Define your master list of codes and their point values
# You can add as many as you need here
master_codes = {
    "XSO1": 15,
    "ALPHA10": 10,
    "BRAVO5": 5,
    "CHARLIE20": 20
}

# Initialize session state to remember the running total and history
if 'running_total' not in st.session_state:
    st.session_state.running_total = 0
if 'history' not in st.session_state:
    st.session_state.history = []

st.title("Code Point Tracker")

# Create a form so the user can just press Enter to submit
with st.form(key='code_entry_form', clear_on_submit=True):
    user_code = st.text_input("Enter a code:")
    submit_button = st.form_submit_button("Submit")

# Process the code when submitted
if submit_button and user_code:
    # Clean up the input to match the master list 
    clean_code = user_code.strip().upper()
    
    if clean_code in master_codes:
        # Look up the points and add to the total
        points = master_codes[clean_code]
        st.session_state.running_total += points
        
        # Add to history
        st.session_state.history.append((clean_code, points))
        
        st.success(f"Success! {clean_code} is worth {points} points.")
    else:
        st.error(f"Code '{user_code}' not found in the master list.")

# Display the running total prominently
st.metric(label="Total Points", value=st.session_state.running_total)

# Display a log of what has been entered so far
if st.session_state.history:
    st.write("---")
    st.subheader("Entry History")
    for code, pts in reversed(st.session_state.history):
        st.write(f"- **{code}**: {pts} points")