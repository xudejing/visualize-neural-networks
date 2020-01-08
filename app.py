"""Main entrance of the app."""
import torch
import streamlit as st

# import projects
from projects.unet2d.app import main as vis_unet2d


def show_default_page():
    st.title('Platform Info')
    # Hardware information
    st.header('Hardware')
    if torch.cuda.device_count() > 0:
        gpu_names = []
        for i in range(torch.cuda.device_count()):
            gpu_names.append(torch.cuda.get_device_name(i))
        st.markdown("<br>".join(gpu_names), unsafe_allow_html=True)
    else:
        st.markdown("CPU")
    # Software information
    st.header('Software')
    st.markdown('Streamlit: *{}*'.format(st.__version__))
    st.markdown('PyTorch: *{}*'.format(torch.__version__))
    if torch.cuda.device_count() > 0:
        st.markdown('CUDA: *{}*'.format(torch.version.cuda))
        st.markdown('cuDNN: *{}*'.format(torch.backends.cudnn.version()))


def main():
    st.sidebar.title("VisNN")
    st.sidebar.markdown(
        "This is an app to explore neural networks via visualization.")

    # route to specific projects
    st.sidebar.empty()
    st.sidebar.header("Projects:")
    option = st.sidebar.selectbox(
        "Which project would you like to show?",
        ("-", "2D Unet")
    )

    st.sidebar.markdown('---')

    if option == "-":
        show_default_page()
    elif option == "2D Unet":
        vis_unet2d()


if __name__ == "__main__":
    main()
