# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:45:33 2024

@author: Pasci
"""

import streamlit as st


# Create an empty container
placeholder = st.empty()

actual_email = "email"
actual_password = "password"

# Insert a form in the container
with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit:
    if email == actual_email and password == actual_password:
        placeholder.empty()
        st.success("Login successful")
        st.session_state.username = email
        st.session_state.page = "home_page"
    else:
        st.error("Invalid credentials. Please try again.")