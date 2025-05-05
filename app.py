import streamlit as st
import re

st.set_page_config(page_title="RDPGenie", layout="centered")

st.title("RDPGenie")

uploaded_file = st.file_uploader("Drop your PAM .sh file here", type=["sh"])


def convert_to_rdp(sh_content: str):
    """
    Extracts RDP parameters from a shell script and converts them to .rdp config.
    Returns (rdp_text, extracted_name).
    """
    match = re.search(r"rdesktop\s+-u\s+'([^']+)'\s+'([^']+)'", sh_content)
    if not match:
        return None, None

    username = match.group(1)
    address = match.group(2)

    # Extract something like "Maitham_Jasim_AG" from the username
    session_name_match = re.search(r":([^:@]+):[^:@]+$", username)
    session_name = session_name_match.group(
        1) if session_name_match else "converted_session"

    rdp_text = f"""full address:s:{address}
username:s:{username}
prompt for credentials:i:1
authentication level:i:2
redirectclipboard:i:1
screen mode id:i:2
desktopwidth:i:1920
desktopheight:i:1080
session bpp:i:32
"""

    return rdp_text, session_name


if uploaded_file is not None:
    sh_content = uploaded_file.read().decode("utf-8")
    rdp_content, filename = convert_to_rdp(sh_content)

    if rdp_content:
        st.text_area("✅ Converted RDP Config", rdp_content, height=200)
        st.download_button("Download .rdp File", rdp_content,
                           file_name=f"{filename}.rdp")
    else:
        st.error(
            "Failed to parse the .sh file. Please make sure it follows the expected rdesktop format.")
