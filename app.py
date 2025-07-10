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
          and automate trading strategies.
        """],
        ["""شهدت تكنولوجيا الذكاء الاصطناعي تطورًا سريعًا في السنوات الأخيرة، مما ساهم في تغيير ملامح العديد من الصناعات والقطاعات حول العالم. في مجال الرعاية الصحية، تم استخدام تقنيات الذكاء الاصطناعي لتحسين دقة تشخيص الأمراض ومساعدة الأطباء في اتخاذ قرارات علاجية أفضل، كما ساهمت الروبوتات الجراحية في تقليل الأخطاء الطبية وزيادة معدلات النجاح. وفي قطاع التعليم، ساعدت الأنظمة الذكية في تقديم تجارب تعلم مخصصة لكل طالب وفقًا لقدراته واحتياجاته، مما زاد من فاعلية العملية التعليمية. أما في عالم الأعمال، فقد ساعدت حلول الذكاء الاصطناعي في تحسين خدمة العملاء من خلال توفير روبوتات محادثة ذكية قادرة على الرد على الاستفسارات بسرعة وفعالية، وتقليل التكاليف التشغيلية. وعلى الرغم من كل هذه الفوائد، تثار مخاوف حول تأثير الذكاء الاصطناعي على سوق العمل وإمكانية فقدان بعض الوظائف التقليدية، بالإضافة إلى التحديات الأخلاقية المرتبطة باستخدام هذه التقنيات بشكل عادل وآمن.
        """]
    ],
    theme=gr.themes.Soft(),
    fill_width=False,
    submit_btn="Summarize",
    show_progress='full',
    type="messages"
)

chatbot.launch()
