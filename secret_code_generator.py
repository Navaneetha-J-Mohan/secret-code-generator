# Streamlit App: Secret Code Generator

import streamlit as st

def encode_message(message, shift):
    """Encodes a message using Caesar Cipher."""
    encoded_text = ""
    for char in message:
        if char.isupper():
            encoded_text += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            encoded_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encoded_text += char
    return encoded_text


def decode_message(message, shift):
    """Decodes a message encoded with Caesar Cipher."""
    decoded_text = ""
    for char in message:
        if char.isupper():
            decoded_text += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            decoded_text += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decoded_text += char
    return decoded_text


#        STREAMLIT UI        
st.set_page_config(page_title="Secret Code Generator", page_icon="🔐", layout="centered")

st.title("🔐 Secret Code Generator")
st.markdown(
    """
    This fun app lets you **encode** or **decode** secret messages using a Caesar cipher.  
    Shift letters by a chosen number — wrap-around is handled automatically!
    """
)

# Sidebar menu
st.sidebar.header("Menu")
choice = st.sidebar.radio("Choose an action:", ["Encode a Message", "Decode a Message", "About"])

#         MAIN CONTENT         
if choice == "Encode a Message":
    st.subheader("🧩 Encode Your Message")
    message = st.text_area("Enter your message:")
    shift = st.number_input("Enter shift value:", min_value=1, max_value=25, step=1)

    if st.button("Encode"):
        if message:
            encoded = encode_message(message, shift)
            st.success("✅ Encoded Message:")
            st.code(encoded, language="text")
        else:
            st.warning("Please enter a message to encode.")

elif choice == "Decode a Message":
    st.subheader("🔓 Decode Your Message")
    message = st.text_area("Enter the encoded message:")
    shift = st.number_input("Enter the shift value used for encoding:", min_value=1, max_value=25, step=1)

    if st.button("Decode"):
        if message:
            decoded = decode_message(message, shift)
            st.success("✅ Decoded Message:")
            st.code(decoded, language="text")
        else:
            st.warning("Please enter a message to decode.")

else:
    st.subheader("ℹ️ About This App")
    st.markdown(
        """
        **Concept Used:** Caesar Cipher – a classical encryption technique  
        **Tech Stack:** Python + Streamlit
        """
    )