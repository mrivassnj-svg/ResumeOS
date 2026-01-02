import gradio as gr
from resumeos.orchestrator import full_system_resolution

with gr.Blocks(
    title="ResumeOS",
    css=".gradio-container { background-color: #f1f5f9; }"
) as demo:

    gr.Markdown("# 🧠 **ResumeOS**")
    gr.Markdown("Deterministic resume signal alignment for ATS systems")

    with gr.Row():
        with gr.Column(scale=1):
            name = gr.Textbox(label="Full Name")
            email = gr.Textbox(label="Contact Info")
            school = gr.Textbox(label="University")
            degree = gr.Textbox(label="Degree / Major")
            skills = gr.Textbox(label="Skills", placeholder="Python, SQL, Networking")
            experience = gr.TextArea(label="Experience", lines=5)
            job_desc = gr.TextArea(label="Job Description", lines=5)

            run_btn = gr.Button("🚀 Optimize Resume", variant="primary")

        with gr.Column(scale=2):
            preview = gr.HTML()
            pdf = gr.File(label="Download ATS-Ready PDF")

    run_btn.click(
        fn=full_system_resolution,
        inputs=[name, email, school, degree, skills, experience, job_desc],
        outputs=[preview, pdf]
    )

if __name__ == "__main__":
    demo.launch()
