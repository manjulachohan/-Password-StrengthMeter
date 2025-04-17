import streamlit as st
import re

# page style
st.set_page_config(page_title="Passwod Strength Checker",page_icon="🌕")

# Streamlit App
st.title("🔐 Password Strength Meter")
st.markdown("""
## Welcome to the ultimate password strength checker!👋  
Check your password strength easily with our tool — and get smart tips to build a stronger, safer password!🔐""")

password = st.text_input("Enter your password", type="password")
feedback = []

score = 0
if password:

    if len(password) >= 8:
       score += 1
    else :
       feedback.append("❌Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else : 
        feedback.append("❌Password should contain both upper and lower case characters.")

    if re.search(r'\d', password):
          score += 1
    else :
        feedback.append("❌Password should contain at least one digit.")

    if re.search(r'[!@#$%*]', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special characters.")
    if score == 4:
       feedback.append("✅Your password is strong!🎉")
    elif score ==3:
       feedback.append("🟡 Your passwords is medium strength. It could be stronger.")
    
    else:
       feedback.append("🔴Your password is weak.  please mate it stronger.")
    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
    else:
        st.info("Please enter your password to grt started.")         
      











