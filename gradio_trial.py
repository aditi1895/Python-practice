import gradio as gr
import os
import shutil

def process_file(resume):
    print(resume)
    path = "/home/ubuntu/temps/" + os.path.basename(resume)  #NB*
    # shutil.copyfile(fileobj.name, path)
    return path

demo = gr.Interface(
    fn=process_file,
    inputs=[
        "file",
    ],
    outputs="text"
)
demo.launch()