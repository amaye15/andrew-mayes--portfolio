# Import Streamlit
import streamlit as st

# Function to display icons for skills
def create_skill_icon(skill_name, emoji_code):
    return f"{emoji_code} {skill_name}"

# Function to display the home/welcome page
def show_home_page():
    st.title('Welcome to My Data Science Portfolio')

    st.markdown("""
        ## About Me
        Hello! I am a Data Scientist, Machine Learning Engineer, and Python Developer with a keen interest in the Rust programming language.
        
        With a passion for solving complex data problems, I have honed my skills in data analysis, machine learning, and building scalable data applications. This portfolio is a showcase of projects that demonstrate my expertise and my journey in the field of data science.
        
        ## Skills
        - **Programming Languages**: Python, Rust
        - **Data Analysis Tools**: Pandas, NumPy, Matplotlib, Seaborn
        - **Machine Learning Libraries**: scikit-learn, TensorFlow, PyTorch
        - **Data Engineering**: SQL, NoSQL, Data Warehousing
        - **Deployment**: Docker, Kubernetes, AWS, Heroku
        """, unsafe_allow_html=True)
    # Skill Icons
    skills = {
        "Python": "🐍",
        "Rust": "🦀",
        "Data Analysis": "📊",
        "Machine Learning": "🤖",
        "Data Engineering": "🛠️",
        "Deployment": "🚀"
    }

    for skill, icon in skills.items():
        st.markdown(create_skill_icon(skill, icon), unsafe_allow_html=True)
    st.markdown("""
        Feel free to browse through my projects and reach out if you have any questions or opportunities to collaborate.
        
        ## Contact
        - **Email**: [andrewmayes14@hotmail.com](mailto:andrewmayes14@hotmail.com)
        - **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/andrew-mayes-2763a716a/)
        - **GitHub**: [GitHub Profile](https://github.com/amaye15?tab=repositories)
        """, unsafe_allow_html=True)

    # If you have a resume you want to share, you can also provide a download link
    st.markdown('---')
    st.markdown('## Resume')
    st.markdown('You can download my resume [here](link_to_your_resume).')

    st.markdown('---')
    st.markdown('## Projects')
    # Placeholder for project information
    st.info('Project details will be added here.')
    st.markdown('---')

    # Contact form (this is a simple example)
    with st.form(key='contact_form'):
        st.markdown('## Contact Me')
        name = st.text_input('Name')
        email = st.text_input('Email')
        message = st.text_area('Message')
        submit_button = st.form_submit_button('Send')

        if submit_button:
            # Process the form data (here you would include logic to send email or store the data)
            st.success('Thank you for your message!')

if __name__ == "__main__":
    # Set wide mode
    st.set_page_config(layout="wide")

    # Navigation
    st.sidebar.title('Navigation')
    options = ['Home', 'Projects', 'Resume', 'Contact']
    selection = st.sidebar.radio('Go to', options)

    # Display the selected page
    if selection == 'Home':
        show_home_page()
    elif selection == 'Projects':
        st.sidebar.text('Projects page will be displayed here.')
    elif selection == 'Resume':
        st.sidebar.text('Resume page will be displayed here.')
    elif selection == 'Contact':
        st.sidebar.text('Contact form will be displayed here.')