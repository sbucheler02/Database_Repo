import gradio as gr

def f(x, y):
    return x+y

with gr.Blocks() as iface:
    with gr.Row():
        with gr.Column():
            x = gr.Number(label = "Type in x.")  
            y = gr.Number(label = "Type in y.")       
            
        with gr.Column():
            sum = gr.Number(label = "This is the sum of those numbers.")

    x.change(fn = f, inputs = [x, y], outputs = [sum])
    y.change(fn = f, inputs = [x, y], outputs = [sum])

iface.launch()