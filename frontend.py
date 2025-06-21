import streamlit as st
import requests


BACKEND_URL = "http://localhost:1234"  # Update port if needed


def main():
    st.title("Web Scraping Agent Interface")

    st.markdown(
        "This is a simple interface to interact with the web scraping agent.")

    user_input = st.text_input("Enter your query:")

    if st.button("🚀 Generate Summary"):
        if not user_input:
            st.error("Please add at least one topic")
        else:
            with st.spinner("🔍 Analyzing topics and generating content..."):
                try:
                    response = requests.post(
                        f"{BACKEND_URL}/scrape-web",
                        json={
                            "topics": user_input.strip(),
                        }
                    )

                    if response.status_code == 200:
                        st.success("✅ Content generated successfully!")
                        # Analysis controls
                        st.markdown("---")
                        st.subheader("🔊 Website content :")
                        st.write(response.content.decode("utf-8"))
                    else:
                        handle_api_error(response)

                except requests.exceptions.ConnectionError:
                    st.error(
                        "🔌 Connection Error: Could not reach the backend server")
                except Exception as e:
                    st.error(f"⚠️ Unexpected Error: {str(e)}")


def handle_api_error(response):
    """Handle API error responses"""
    try:
        error_detail = response.json().get("detail", "Unknown error")
        st.error(f"API Error ({response.status_code}): {error_detail}")
    except ValueError:
        st.error(f"Unexpected API Response: {response.text}")


if __name__ == "__main__":
    main()
    # To run this Streamlit app, use the command:
    # streamlit run frontend.py
