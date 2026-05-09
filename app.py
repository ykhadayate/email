import streamlit as st
from data_handler import *
from dashboard import show_dashboard

st.set_page_config(page_title="Excel Directory App", layout="wide")

st.title("📁 Excel-Based Directory Management System")

menu = st.sidebar.selectbox("Menu", [
    "Dashboard", "Add", "Update", "Delete", "Search"
])

df = load_data()

# ================= DASHBOARD =================
if menu == "Dashboard":
    show_dashboard(df)

# ================= ADD =================
elif menu == "Add":
    st.subheader("➕ Add Record")

    with st.form("add_form"):
        first = st.text_input("First Name")
        last = st.text_input("Last Name")
        email = st.text_input("Email")
        mobile = st.text_input("Mobile")
        dept = st.text_input("Department")
        desig = st.text_input("Designation")

        if st.form_submit_button("Add"):
            add_record({
                "First-Name": first,
                "Last-Name": last,
                "Mail-Id": email,
                "Mobile Number": mobile,
                "Department": dept,
                "Designation": desig
            })
            st.success("✅ Record Added")

# ================= UPDATE =================
elif menu == "Update":
    st.subheader("✏️ Update Record")

    email_list = df["Mail-Id"].tolist()
    selected_email = st.selectbox("Select Email", email_list)

    record = df[df["Mail-Id"] == selected_email].iloc[0]

    first = st.text_input("First Name", record["First-Name"])
    last = st.text_input("Last Name", record["Last-Name"])
    mobile = st.text_input("Mobile", record["Mobile Number"])
    dept = st.text_input("Department", record["Department"])
    desig = st.text_input("Designation", record["Designation"])

    if st.button("Update"):
        update_record(selected_email, {
            "First-Name": first,
            "Last-Name": last,
            "Mobile Number": mobile,
            "Department": dept,
            "Designation": desig
        })
        st.success("✅ Updated")

# ================= DELETE =================
elif menu == "Delete":
    st.subheader("🗑 Delete Record")

    email = st.selectbox("Select Email", df["Mail-Id"])

    if st.button("Delete"):
        delete_record(email)
        st.warning("✅ Deleted")

# ================= SEARCH =================
elif menu == "Search":
    st.subheader("🔍 Search Records")

    name = st.text_input("Name")
    dept = st.text_input("Department")

    result = search_records(name, dept)

    st.dataframe(result)
