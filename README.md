# ChatDOCx

### A domain specific chatbot powered by Hugging Face and Python

- Chat with your documents by [asking questions](#question-answering) in an interactive web app.
- [Summarize](#text-summarization) your documents.
- Too many [links or contacts](#customization)? Access them easily.
- Create your own custom [domain/topic](#domains) to chat with e.g., development errors you would like to trace.
- Supports different [NLP models integration](#features) from Hugging Face.
- **Free to use. ``No API keys`` required!**

An example where the bot answers some sample questions:

<div align="center">
    <img src="https://i.imgur.com/Tfv5J2j.gif" alt="ChatDOCx" width=""/>
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
    - [Domains](#domains)
    - [Question answering](#question-answering)
    - [Text summarization](#text-summarization)
    - [Customization](#customization)
    - [Error handling](#error-handling)
* [Future scope](#future-scope)
* [References](#references)

---

## Simple theory

### Transformers

- Transformers are a deep learning model architecture designed for sequential data processing tasks and have revolutionized NLP tasks.
- They consist of multiple layers of ``self-attention`` (which is a key mechanism that enable them to weigh the importance of different input tokens dynamically, capturing long-range dependencies in the data effectively.) and ``feedforward neural networks``.
- Pre-trained models like BERT, GPT, T5 etc., have been released by major organizations, enabling transfer learning for downstream NLP tasks.

We will use the following models for our chatbot:

### RoBERTa for question answering

Facebook AI's RoBERTa (``Robustly Optimized BERT Approach``) is an improvement to Google AI's BERT (``Bidirectional Encoder Representations from Transformers``). While BERT laid the foundation for transformer-based models in NLP, RoBERTa further optimized the pre-training process and achieved better performance by leveraging larger datasets and advanced training techniques:

- **Advanced Training Techniques:** RoBERTa incorporated techniques such as ``dynamic masking`` and ``increased batch sizes``. Dynamic masking involves masking tokens dynamically during pre-training, allowing the model to focus more on learning contextual information. Additionally, RoBERTa used larger mini-batches during training, which helped in better generalization and optimization.

- **Focus on Masked Language Modeling (MLM):** Unlike BERT, which also included the ``next sentence prediction (NSP)`` task during pre-training, RoBERTa focused solely on the ``MLM`` task. By dedicating all resources to improving the accuracy of predicting masked tokens, RoBERTa was able to fine-tune its language understanding capabilities more effectively.

### BART for text summarization

BART (Bidirectional and Auto-Regressive Transformers) is a sequence-to-sequence model introduced by Facebook AI:

- **Bidirectional:** It can process input sequences in both forward and backward directions. This bidirectional capability enables BART to capture context from both preceding and succeeding tokens, enhancing its understanding of the input sequence.

- **Auto-Regressive:** It employs an auto-regressive decoding strategy during generation, where it generates one token at a time from left to right based on the previously generated tokens. This approach ensures that each token is conditioned on the tokens generated before it, allowing it to produce coherent and contextually relevant outputs.

---

## Running the chatbot

### Install the dependencies

First up, install all the required Python dependencies by running: ```
pip install -r requirements.txt ```

> NOTE: Development environment is Windows/Python version 3.12.2 (there can always be version conflicts between the dependencies, OS, hardware etc.).

### Run the web app

The web application is powered by Flask, run it with: ```python nlp.py```. In the command window, you should see something like WARNING: This is a development server. Do not use it in a production deployment.

 * Running on http:/100.0.1.0:8000

Which is your web adress (just copy paste it in your browser to access the app). Please refer to [Features](#features) to customize the app.

---

## Features

The following can be configured in ```mylib/config.json```:

```json
{
    "qa_model_name": "deepset/roberta-base-squad2",
    "summary_model_name": "facebook/bart-large-cnn",
    "app_name": "",
    "use_stopwords": true
}
```

- ``qa_model_name`` is the model used for question answering (RoBERTa).
- ``summary_model_name`` is the model used for text summarization (BART).
- ``app_name`` is optional if you would like to showcase your own branding on the app.
- ``use_stopwords`` will remove the common english words for the models to handle the questions better.

### Domains

Setting domains/topics is a core component of the chatbot as it performs better if the data is structured as a single domain, because it will help the bot to remember the context behind the data when asking questions.

### Question answering

When you run the app, you are enforced to select a domain to start asking questions, not because you can, but because you get better responses :)

### Text summarization

After selecting a domain, simply include the keywords ``summary`` or ``summarize`` in your input question e.g., summary of transformers, summarize nlp etc., to get a summary of the domain:

<div align="center">
    <img src="https://i.imgur.com/KV90xe9.gif" alt="ChatDOCx" width=""/>
</div>

> NOTE: Text summarization appears to be a bit slow. Performance probably depends on the model, the amount of data etc.

### Customization

The chatbot can be highly customized as many functions are designed from scratch with flexibility. For instance:

- **Adding data:** Data is hosted under ``data`` folder as ``.txt`` files.
- **Domains/topics:** are displayed based on the data (text file name) automatically. Several domains can be created depending on the text files you have in the data folder. The color of a domain can also be changed by modifying the following snippet under ``templates/ChatDOCx.html``:

```javascript

{% set topic_colors = {'Contacts': '#FFD700', 'Links': '#FFD700', 'Errors': '#f36262'} %}
```

- **Models:** used are tested/selected on the responses they provide, but different models from Hugging Face can be used (see ``mylib/config.json`` to configure the model and ``References`` section for a list of Hugging Face models).
- **Webapp:** is designed from scratch with HTML/JavaScript styling and you can design it as per your wish (see ``templates`` folder).
- **Links:** can be added under ``data/links.json``. Just select the domain ``Links`` and include the keyword ``link`` followed by your question e.g., link to transformers.

> NOTE: Links are also matched to your questions. In the example below, the keyword ``transformers`` in your question is also in the ``links.json`` database, which gives you a streamlined answer to ``learn more`` about transformers as a clickable link.

- **Contacts:** can be added under ``data/contacts.json``. Just select the domain ``Contacts`` and include the keyword ``contact`` followed by your question e.g., contact of huggingface.

<div align="center">
    <img src="https://i.imgur.com/MRqi30e.gif" alt="ChatDOCx" width=""/>
</div>

### Error handling

Errors will be shown on the red bar in the app. Implemented logic to handle domain selection, empty/short inputs, questions outside the scope of chatbot to prevent misinformation. Below is the showcase, including an example where the bot handles questions outside the scope of its knowledge (NOTE: ``use_stopwords`` will enhance this function): 

<div align="center">
    <img src="https://i.imgur.com/nEAShYw.gif" alt="ChatDOCx" width=""/>
</div>

---

## Future scope

- Implement RAG (Retrieval-Augmented Generation) to improve domain specific knowledge.
- Memory function to save the chat history.
- Function to handle multiple file formats (only supports .txt files atm), or a better way to fetch the data in real-time.

---

## References

- Hugging Face Question Answering models: https://huggingface.co/models?pipeline_tag=question-answering&sort=trending
- Hugging Face Summarization models: https://huggingface.co/models?pipeline_tag=summarization&sort=trending
---

*saimj7/ 14-04-2024 - © <a href="http://saimj7.github.io" target="_blank">Sai_Mj</a>.*
