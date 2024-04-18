import os
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from mylib.model_loader import ModelLoader
from mylib.file_path_handler import FilePathHandler
from flask import Flask, render_template, request, Markup, session, jsonify

app = Flask(__name__)
app.secret_key = os.urandom(16)  # Generate a random secret key
model_loader = ModelLoader()
file_path_handler = FilePathHandler()

# Download NLTK stopwords if not already downloaded
nltk.download('stopwords')
# Define a set of stopwords from NLTK
stop_words = set(stopwords.words("english"))
# Exclude specified words from stop words if required
exclude_words = {"it"}
stop_words = stop_words - exclude_words

# Access links
doc_links = file_path_handler.doc_links
contact_names = file_path_handler.contact_names

# Read the content of each text file and store it in a dictionary with file names
documents = {}
separator = "\n\n"  # Separator between file contents

for file_path in file_path_handler.file_paths:
    with open(file_path, "r") as file:
        file_name = os.path.splitext(os.path.basename(file_path))[0]  # remove file extension
        content = file.read()
        documents[file_name] = content

load_topics = file_path_handler.file_names
topics = [topic.lower() for topic in load_topics]


@app.route("/", methods=["GET", "POST"])
def ChatDOCx():
    if request.method == "POST":
        selected_topic = session.get('selected_topic')

        if not selected_topic:
            return render_template("ChatDOCx.html", info_message="Please select a domain before asking questions.", app_name=model_loader.app_name, load_topics=load_topics)

        user_input = request.form["user_input"]
        user_input = user_input.replace('?', '')

        document_content = documents.get(selected_topic, "")

        if not user_input.strip():  # Check if user input is empty or contains only whitespace
            return render_template("ChatDOCx.html", info_message="Sorry, empty answers for empty questions ;)", app_name=model_loader.app_name, load_topics=load_topics, selected_topic=session.get('selected_topic', ''))

        if len(user_input) < 6:
            return render_template("ChatDOCx.html", info_message="Please ask a context-based question for me to help you better.", app_name=model_loader.app_name, load_topics=load_topics, selected_topic=session.get('selected_topic', ''))

        # Apply stop words if configured (not perfect but works most of the time)
        if model_loader.config.get("use_stopwords"):
            user_input_stop = " ".join([word for word in user_input.split() if word.lower() not in stop_words])
            print("Input after stopwords:", user_input_stop)
            if not any(word.lower() in document_content for word in user_input_stop.lower().split()):
                return render_template("ChatDOCx.html", info_message="Sorry, I have no knowledge about it (yet). Please add the info/update me.", app_name=model_loader.app_name, load_topics=load_topics, selected_topic=session.get('selected_topic', ''))

            # Check if there is a link for the users input
            link = get_source_links(user_input_stop)

        # Load the model
        if any(keyword in user_input.lower() for keyword in ["summary", "summarize"]):
            summary = pipeline("summarization", model=model_loader.summary_model)
            summary_answers = summary(document_content, max_length=130, min_length=30, do_sample=False)
            answers = summary_answers
        else:
            qa = pipeline("question-answering", model=model_loader.model, tokenizer=model_loader.tokenizer)
            qa_answers = qa(question=user_input, context=document_content)
            answers = qa_answers
            print("Model score:", answers['score'])

        # Condition to summarize the topic
        if any(keyword in user_input.lower() for keyword in ["summary", "summarize"]):
            response = f"ChatDOCx (Summary): {answers[0].get('summary_text')}"
        # Condition for automatically fetching the links
        elif all(keyword not in user_input.lower() for keyword in ["link", "contact"]) and link:
            response = f"ChatDOCx ({get_source_file(answers, documents)}): {answers['answer']}.<br><br>Learn more here: <a href='{link}' target='_blank' style='color: white;'>{link}</a>"
        # Condition for manually fetching the links
        elif "link" in user_input.lower():
            response = f"ChatDOCx ({get_source_file(answers, documents)}): <a href='{link}' target='_blank' style='color: white;'>{link}</a>"
        # Condition for fetching the contact info
        elif "contact" in user_input.lower():
            response = f"ChatDOCx ({get_source_file(answers, documents)}): {link}"
        else:
            response = f"ChatDOCx ({get_source_file(answers, documents)}): {answers['answer']}."
    else:
        response = "ChatDOCx:"
    return render_template("ChatDOCx.html", answer=Markup(response), app_name=model_loader.app_name, load_topics=load_topics, selected_topic=session.get('selected_topic', ''))


@app.route("/select_topic", methods=["POST"])
def select_topic():
    selected_topic = request.json.get('selected_topic')
    session['selected_topic'] = selected_topic
    return jsonify({'status': 'success'})


def get_source_file(answer, documents):
    # Find the source file for the answer
    for file_name, content in documents.items():
        if answer['answer'] in content:
            # Remove the ".txt" extension from the file name
            source_file_name = os.path.splitext(file_name)[0]
            return source_file_name
    return "Unknown"


def get_source_links(user_input):
    # Check if any topic key is a substring of the user input
    if "contact" in user_input:
        source_file = contact_names
    else:
        source_file = doc_links
    for topic_key in source_file:
        if topic_key.lower() in user_input.lower():
            return source_file[topic_key]
    return None


if __name__ == "__main__":
    app.run(debug=True)
