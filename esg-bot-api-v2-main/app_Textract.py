import json
import requests
from flask import Flask, request, jsonify, render_template
import io
import boto3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def api():
     if request.method == 'POST':
        # Retrieve the form input data 
        words = request.form['words']
        text = request.form['text']
        question = request.form['question']

        # Call Amazon Textract API to extract text
        client = boto3.client('textract')
        response0 = requests.get(text)
        file_stream = io.BytesIO(response0.content)
        response = client.detect_document_text(Document={'Bytes': file_stream.getvalue()})

        # Extract the text from the Amazon Textract response
        extracted_text = ''
        for item in response0["Blocks"]:
            if item["BlockType"] == "LINE":
                extracted_text += item["Text"] + '\n'
            
        # Create a question using the input fields
        question = f"I would like you to read this text: {extracted_text}. Then I would like you to provide an aswer to this question {question} in a maximum of {words} words while providing evidence you find in the given text."


        #Call ChatGPT API

        url2 = 'https://api.openai.com/v1/chat/completions'

        params = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "system", "content": "You are an expert financial ESG analyst reading a text and evaluating whether a given report provides an accurate description of the company ESG policy"},
                         {"role": "user", "content": question}
                        ]
                 }

        headers = {
              'Content-Type': 'application/json',
              'Authorization': 'Bearer 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'  # replace <API_KEY> with your API key
                 }
     
        #the request to chatGPT
        response = requests.post(url2, headers=headers, json=params)
        answer=response.json()

        # Create JSON response 
        output = {'answer': answer['choices'][0]['message']['content'] }  
        
        return render_template('index.html', output=output)

     else:
     
        return render_template('index.html')
     
if __name__ == '__main__':
    app.run()
