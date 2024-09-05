## ChatDOCx: Seu Chatbot Personalizado com IA 🤖

### Um chatbot especialista em seus documentos, desenvolvido com Hugging Face e Python

- **Converse com seus documentos [fazendo perguntas](#perguntas-e-respostas) em um aplicativo web interativo.**
- [Resuma](#resumo-de-texto) seus documentos.
- Muitos [links ou contatos](#personalizacao)? Acesse-os facilmente.
- Crie seu próprio [domínio/tópico](#dominios) personalizado para conversar, por exemplo, sobre erros de desenvolvimento que você gostaria de rastrear.
- Suporta a integração de diferentes [modelos de PNL](#recursos) do Hugging Face.
- **Grátis para usar. `Sem necessidade de chaves de API`!**

**Veja um exemplo do chatbot respondendo a algumas perguntas:**

<div align="center">
    <img src="https://i.imgur.com/Tfv5J2j.gif" alt="ChatDOCx" width=""/>
</div>

> **Observação:** O ChatDOCx é experimental e pode não funcionar perfeitamente. Faça perguntas com contexto para obter melhores resultados. 😉

---

## Conteúdo

* [Teoria Simplificada](#teoria-simplificada)
    - [Transformers](#transformers)
    - [RoBERTa para Respostas a Perguntas](#roberta-para-respostas-a-perguntas)
    - [BART para Resumo de Texto](#bart-para-resumo-de-texto)
* [Executando o Chatbot](#executando-o-chatbot)
    - [Instalando as Dependências](#instalando-as-dependencias)
    - [Executando o Aplicativo Web](#executando-o-aplicativo-web)
* [Recursos](#recursos)
    - [Domínios](#dominios)
    - [Perguntas e Respostas](#perguntas-e-respostas)
    - [Resumo de Texto](#resumo-de-texto)
    - [Personalização](#personalizacao)
    - [Tratamento de Erros](#tratamento-de-erros)
* [Próximos Passos](#proximos-passos)
* [Referências](#referencias)

---

## Teoria Simplificada

### Transformers

- **Transformers** são arquiteturas de aprendizado profundo projetadas para processar dados sequenciais e revolucionaram as tarefas de PNL (Processamento de Linguagem Natural).
- Eles consistem em múltiplas camadas de `autoatenção` (mecanismo que permite ponderar a importância de diferentes tokens de entrada dinamicamente, capturando dependências de longo alcance nos dados) e `redes neurais feedforward`.
- Modelos pré-treinados como BERT, GPT, T5 etc., foram disponibilizados por grandes empresas, permitindo o aprendizado de transferência para tarefas de PNL.

**Usaremos os seguintes modelos para o nosso chatbot:**

### RoBERTa para Respostas a Perguntas

O RoBERTa (`Robustly Optimized BERT Approach`) da Facebook AI é uma melhoria do BERT (`Bidirectional Encoder Representations from Transformers`) do Google AI. Enquanto o BERT lançou as bases para modelos baseados em transformers em PNL, o RoBERTa otimizou ainda mais o processo de pré-treinamento e alcançou melhor desempenho ao aproveitar conjuntos de dados maiores e técnicas de treinamento avançadas:

- **Técnicas de Treinamento Avançadas:** O RoBERTa incorporou técnicas como `mascaramento dinâmico` e `tamanhos de lote aumentados`. O mascaramento dinâmico envolve mascarar tokens dinamicamente durante o pré-treinamento, permitindo que o modelo se concentre mais no aprendizado de informações contextuais. Além disso, o RoBERTa usou mini-lotes maiores durante o treinamento, o que ajudou na melhor generalização e otimização.

- **Foco na Modelagem de Linguagem Mascarada (MLM):** Ao contrário do BERT, que também incluiu a tarefa de `previsão da próxima frase (NSP)` durante o pré-treinamento, o RoBERTa se concentrou apenas na tarefa de `MLM`. Ao dedicar todos os recursos para melhorar a precisão da previsão de tokens mascarados, o RoBERTa foi capaz de ajustar suas capacidades de compreensão da linguagem com mais eficácia.

### BART para Resumo de Texto

O BART (Bidirectional and Auto-Regressive Transformers) é um modelo de sequência para sequência introduzido pela Facebook AI:

- **Bidirecional:** Ele pode processar sequências de entrada nas direções direta e inversa. Essa capacidade bidirecional permite que o BART capture o contexto dos tokens anteriores e posteriores, aprimorando sua compreensão da sequência de entrada.

- **Auto-Regressivo:** Ele emprega uma estratégia de decodificação auto-regressiva durante a geração, onde gera um token por vez, da esquerda para a direita, com base nos tokens gerados anteriormente. Essa abordagem garante que cada token seja condicionado aos tokens gerados antes dele, permitindo que ele produza saídas coerentes e contextualmente relevantes.

---

## Executando o Chatbot

### Instalando as Dependências

Primeiro, instale todas as dependências Python necessárias executando: ```pip install -r requirements.txt```

> **Observação:** O ambiente de desenvolvimento é Windows/Python versão 3.12.2 (pode haver conflitos de versão entre as dependências, sistema operacional, hardware etc.).

### Executando o Aplicativo Web

O aplicativo web é desenvolvido com Flask. Execute-o com: ```python nlp.py```. Na janela de comando, você deverá ver algo como:

```
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http:/100.0.1.0:8000
```

Este é o endereço do seu aplicativo web (copie e cole no navegador para acessá-lo). Consulte a seção [Recursos](#recursos) para personalizar o aplicativo.

---

## Recursos

O seguinte pode ser configurado em `mylib/config.json`:

```json
{
    "qa_model_name": "deepset/roberta-base-squad2",
    "summary_model_name": "facebook/bart-large-cnn",
    "app_name": "",
    "use_stopwords": true
}
```

- `qa_model_name` é o modelo usado para respostas a perguntas (RoBERTa).
- `summary_model_name` é o modelo usado para resumo de texto (BART).
- `app_name` é opcional, caso queira exibir sua própria marca no aplicativo.
- `use_stopwords` removerá as palavras comuns em inglês para que os modelos processem as perguntas com mais precisão.

### Domínios

Definir domínios/tópicos é um componente essencial do chatbot, pois ele tem um desempenho melhor se os dados forem estruturados como um único domínio. Isso ajuda o bot a se lembrar do contexto por trás dos dados ao responder a perguntas.

### Perguntas e Respostas

Ao executar o aplicativo, você precisa selecionar um domínio para começar a fazer perguntas. Isso garante que você obtenha as melhores respostas possíveis! 😉 Selecione um domínio, faça sua pergunta e pressione `Enter` ou clique em `Submit`, como mostrado no exemplo no início.

### Resumo de Texto

Após selecionar um domínio, basta incluir as palavras-chave `summary` ou `summarize` em sua pergunta, por exemplo, "summary of transformers" ou "summarize nlp", para obter um resumo do domínio:

<div align="center">
    <img src="https://i.imgur.com/KV90xe9.gif" alt="ChatDOCx" width=""/>
</div>

> **Observação:** O resumo de texto pode ser um pouco lento. O desempenho provavelmente depende do modelo, da quantidade de dados etc.

### Personalização

O chatbot é altamente personalizável, pois muitas funções são projetadas do zero com flexibilidade. Por exemplo:

- **Adicionando dados:** Os dados são armazenados na pasta `data` como arquivos `.txt`.
- **Domínios/tópicos:** são exibidos automaticamente com base nos dados (nome do arquivo de texto). Vários domínios podem ser criados dependendo dos arquivos de texto na pasta `data`. A cor de um domínio também pode ser alterada modificando o seguinte trecho de código em `templates/ChatDOCx.html`:

```javascript
{% set topic_colors = {'Contacts': '#FFD700', 'Links': '#FFD700', 'Errors': '#f36262'} %}
```

- **Modelos:** os modelos usados são testados/selecionados com base nas respostas que fornecem, mas diferentes modelos do Hugging Face podem ser usados (consulte `mylib/config.json` para configurar o modelo e a seção [Referências](#referencias) para obter uma lista de modelos do Hugging Face).
- **Aplicativo Web:** é projetado do zero com estilo HTML/JavaScript e você pode personalizá-lo como desejar (consulte a pasta `templates`).
- **Links:** podem ser adicionados em `data/links.json`. Basta selecionar o domínio `Links` e incluir a palavra-chave `link` seguida de sua pergunta, por exemplo, "link to transformers".

> **Observação:** Os links também são correspondidos às suas perguntas. No exemplo abaixo, a palavra-chave `transformers` em sua pergunta também está no banco de dados `links.json`, o que fornece uma resposta direta para `saiba mais` sobre transformers como um link clicável.

- **Contatos:** podem ser adicionados em `data/contacts.json`. Basta selecionar o domínio `Contacts` e incluir a palavra-chave `contact` seguida de sua pergunta, por exemplo, "contact of huggingface".

<div align="center">
    <img src="https://i.imgur.com/MRqi30e.gif" alt="ChatDOCx" width=""/>
</div>

### Tratamento de Erros

Os erros serão mostrados na barra vermelha no aplicativo. A lógica implementada lida com a seleção de domínio, entradas vazias/curtas e perguntas fora do escopo do chatbot para evitar desinformação. Abaixo está uma demonstração, incluindo um exemplo onde o bot lida com perguntas fora de seu conhecimento (**Observação:** `use_stopwords` aprimorará esta função):

<div align="center">
    <img src="https://i.imgur.com/nEAShYw.gif" alt="ChatDOCx" width=""/>
</div>

---

## Próximos Passos

- Implementar RAG (Retrieval-Augmented Generation) para aprimorar o conhecimento específico do domínio.
- Função de memória para salvar o histórico do chat.
- Função para lidar com vários formatos de arquivo (atualmente, apenas arquivos .txt são suportados) ou uma maneira melhor de buscar os dados em tempo real.

---

## Referências

- Modelos de Perguntas e Respostas do Hugging Face: https://huggingface.co/models?pipeline_tag=question-answering&sort=trending
- Modelos de Resumo do Hugging Face: https://huggingface.co/models?pipeline_tag=summarization&sort=trending

---
