# Visualize neural networks
This is an app to explore the visualizations of neural networks. The app is intended to include multiple projects.

## Installation
1. Clone the repository to your local machine

    ```
    $ git clone --recurse-submodules https://github.com/xudejing/visualize-neural-networks.git
    ```

2. Install dependency packages
    * [PyTorch](https://pytorch.org) by following the official instructions (conda prefered)
    * [Streamlit](https://streamlit.io)

3. Run the app
    ```
    $ streamlit run app.py
    ```

## New project
Use the project [2D Unet](https://github.com/xudejing/visualize-unet2d) as a template and modify it to suit your needs. You are very welcome to include your own project in this app, just send a pull request if you want. To make your project visible, you need to include your project repo as a submodule and register it in *app.py*.

## Included projects
- [2D Unet](https://github.com/xudejing/visualize-unet2d) (template)
