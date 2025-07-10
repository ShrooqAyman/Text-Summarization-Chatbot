from summarizer import summarize_text
import gradio as gr


chatbot = gr.ChatInterface(
    summarize_text,
    title="Text Summarization Chatbot 🤖",
    description="Send me a long text, and I'll summarize it for you!",
    examples=[
        ["""The rapid advancement of artificial intelligence and machine learning technologies has significantly
          transformed various industries around the world. In recent years, AI has been increasingly adopted in
          healthcare to assist doctors in diagnosing diseases more accurately and quickly, sometimes even outperforming
          human experts in certain tasks such as analyzing medical images. In addition, AI-powered chatbots and virtual
          assistants have revolutionized customer service by providing instant, around-the-clock responses to user inquiries
         , which has greatly improved user satisfaction and reduced operational costs for businesses. Furthermore, AI-driven
          algorithms are now used extensively in the finance sector to detect fraudulent transactions, assess credit risk,
          and automate trading strategies. Education has also been influenced by AI, with intelligent tutoring systems offering
          personalized learning experiences tailored to individual students' strengths and weaknesses. While these innovations
          promise numerous benefits, they also raise important ethical concerns, including data privacy, algorithmic bias, and
          the potential for large-scale job displacement. As society continues to integrate AI into more aspects of daily life,
          it is crucial for policymakers, developers, and communities to collaborate in establishing frameworks that ensure these
          powerful technologies are used responsibly and for the greater good.
        """],
    ],
    theme=gr.themes.Soft(),
    fill_width=False,
    submit_btn="Summarize",
    show_progress='full',
    type="messages"
)

chatbot.launch()
