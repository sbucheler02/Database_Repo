import gradio as gr

def f(x):
    return x**2

with gr.Blocks() as iface:
    number = gr.Number(label = "Type in a Number.")
    square = gr.Number(label = "This is the square of that number.")
    number.change(fn = f, inputs = [number], outputs = [square])
iface.launch()