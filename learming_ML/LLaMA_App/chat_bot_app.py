from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import gradio as gr

# # Load the tokenizer and model
# model_name = "meta-llama/Llama-2-7b-chat-hf"  # Replace with 13b or 70b if you have access and resources
#
# tokenizer = AutoTokenizer.from_pretrained(model_name, token=True)
# model = AutoModelForCausalLM.from_pretrained(
#     model_name,
#     device_map="auto",
#     torch_dtype="auto",  # Use float16 if supported by your hardware
#     token=True
# )

# Change this path to where you saved the model
model_path = "C:/Users\Vivek\PycharmProjects\meta_model\Llama-2-7b-chat-hf"

# Load tokenizer and model from local directory
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",       # Automatically place on GPU if available
    torch_dtype="auto"       # Use bfloat16/float16 if supported
)


# Define a text generation pipeline
llama_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=300,
    do_sample=True,
    temperature=0.7,
    top_p=0.9
)

# Define the chatbot function
def chat(prompt):
    result = llama_pipeline(prompt)[0]["generated_text"]
    return result

# Launch the Gradio interface
gr.Interface(
    fn=chat,
    inputs=gr.Textbox(lines=3, placeholder="Ask me anything about AI, science, history..."),
    outputs="text",
    title="LLaMA 2 Chatbot",
    description="This chatbot is powered by Meta's LLaMA 2 model using Hugging Face Transformers."
).launch()

