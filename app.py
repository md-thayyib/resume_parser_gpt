import streamlit as st

from util.resume_parser import resume_parse, set_open_api_key


def main():

    # set page config
    st.set_page_config(page_title="appto",page_icon=":tada:",layout='wide')
    
    def sidebar():
        with st.sidebar:
            st.markdown(
            "## How to use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            "2. Upload a pdf, docx, or txt file📄\n"
            "3. Submit💬\n"
        )
            api_key_input = st.text_input(
                'Openai API Key',
                type='password',
                placeholder="Paste your OpenAI API key here (sk-...)",
                help="You can get your API key from https://platform.openai.com/account/api-keys.",
                value=st.session_state.get("OPENAI_API_KEY", ""),
                )
        st.session_state['OPENAI_API_KEY'] = api_key_input
        print(api_key_input)
        print(st.session_state['OPENAI_API_KEY'],'------------>' )

        set_open_api_key(api_key_input)
            

    sidebar()



    def clear_submit():
        st.session_state["submit"] = False

    st.title("Resume Parser :wave:")
    uploaded_file = st.file_uploader('Upload a resume',type=['pdf'],on_change=clear_submit )

    def submit():

        if uploaded_file is not None:

            response,resume_text=resume_parse(resume_file=uploaded_file,)

            text = response.choices[0].text
            st.text_area(label="Summary",value=text,height=89)
        else:
            st.error("File not found")

    st.button(label = 'Submit',on_click=submit)

    
    

if __name__ == "__main__":
    main()