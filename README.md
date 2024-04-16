# ChatDOCx

### A chatbot powered by Hugging Face and Python

- Chat with your documents by asking questions on a user friendly web app.
- Summarize your documents.
- Too many links or contacts? Access them easily.
- Create your own custom domain e.g., development errors you would like to trace.
- Supports different NLP models from Hugging Face.
- No API keys required!

Here is an example where the bot answers a sample question on transformers:

<div align="center">
    <img src="data/images/question.jpg" alt="ChatDOCx" width="600"/>
</div>

> NOTE: ChatDOCx is experimental and may not work properly. Please provide context-based questions for better results.

--- 

## Table of Contents

* [Simple theory](#simple-theory)
    - [Transformers](#transformers)
    - [RoBERTa for question answering](#RoBERTa-for-question-answering)
    - [BART for text summarization](#BART-for-text-summarization)
* [Running the chatbot](#running-the-chatbot)
    - [Install the dependencies](#install-the-dependencies)
    - [Run the web app](#run-the-web-app)
* [Features](#features)
    - [Models](#models)
    - [Customization](#customization)
    - [Error handling](#error-handling)
* [Future scope](#future-scope)
* [References](#references)

---

## Simple theory

### Transformers

- Transformers are a deep learning model architecture designed for sequential data processing tasks and have revolutionized NLP tasks.
- They consist of multiple layers of self-attention (which is a key mechanism that enable them to weigh the importance of different input tokens dynamically, capturing long-range dependencies in the data effectively.) and feedforward neural networks.
- Pre-trained models like BERT, GPT, T5 etc., have been released by major organizations, enabling transfer learning for downstream NLP tasks.

We will use the following models for our chatbot:

### RoBERTa for question answering

Facebook AI's RoBERTa (Robustly Optimized BERT Approach) is an improvement to Google AI's BERT (Bidirectional Encoder Representations from Transformers). While BERT laid the foundation for transformer-based models in NLP, RoBERTa further optimized the pre-training process and achieved better performance by leveraging larger datasets and advanced training techniques:

- **Advanced Training Techniques:** RoBERTa incorporated techniques such as dynamic masking and increased batch sizes. Dynamic masking involves masking tokens dynamically during pre-training, allowing the model to focus more on learning contextual information. Additionally, RoBERTa used larger mini-batches during training, which helped in better generalization and optimization.

- **Focus on Masked Language Modeling (MLM):** Unlike BERT, which also included the next sentence prediction (NSP) task during pre-training, RoBERTa focused solely on the MLM task. By dedicating all resources to improving the accuracy of predicting masked tokens, RoBERTa was able to fine-tune its language understanding capabilities more effectively.

### BART for text summarization

BART (Bidirectional and Auto-Regressive Transformers) is a sequence-to-sequence model introduced by Facebook AI:

- **Bidirectional**: It can process input sequences in both forward and backward directions. This bidirectional capability enables BART to capture context from both preceding and succeeding tokens, enhancing its understanding of the input sequence.

- **Auto-Regressive**: It employs an auto-regressive decoding strategy during generation, where it generates one token at a time from left to right based on the previously generated tokens. This approach ensures that each token is conditioned on the tokens generated before it, allowing it to produce coherent and contextually relevant outputs.


---

## Running the chatbot

### Install the dependencies

First up, install all the required Python dependencies by running: ```
pip install -r requirements.txt ```

> NOTE: Development environment is Windows/Python version 3.11.3 (there can always be version conflicts between the dependencies, OS, hardware etc.).

### Run the web app

The web application is powered by Flask, run it with: ```python nlp.py```. In the command window, you should see something like WARNING: This is a development server. Do not use it in a production deployment.

 * Running on http:/100.0.1.0:8000

Which is your web adress (just copy paste it in your browser to access the app).

---

## Features

The following can be configured in ```mylib/config.json```:

```json
{
    "model_name": "deepset/roberta-base-squad2",
    "summary_model_name": "facebook/bart-large-cnn",
    "app_name": "",
    "use_stopwords": true
}
```

> app_name is optional if you would like to showcase your own branding on the app; use_stopwords will remove the common words for the models to handle the questions better.

### Models

- TBD

### Customization

- TBD

### Error handling

Errors will be shown on the red bar in the app. Implemented logic to handle domain selection, empty/short inputs, questions outside the scope of chatbot to prevent misinformation. Here is an example where the bot handles questions that are outside the scope of its knowledge (use_stopwords will enhance this function): 

---

## Future scope

- Implement RAG (Retrieval-Augmented Generation) to improve domain specific knowledge.
- Memory function to save the chat history.

---

## References

- Hugging Face Question Answering models: https://huggingface.co/models?pipeline_tag=question-answering&sort=trending
- Hugging Face Summarization models: https://huggingface.co/models?pipeline_tag=summarization&sort=trending
---

*saimj7/ 14-04-2024 - © <a href="http://saimj7.github.io" target="_blank">Sai_Mj</a>.*
