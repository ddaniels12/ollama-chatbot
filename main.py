import http.server
import socketserver
import urllib.parse
import json
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below in the same language as the question.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="deepseek-r1:14b")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def generate_response(user_input, context):
    # Detect language of the user input
    language = "es" if any(ord(char) > 127 for char in user_input) else "en"
    result = chain.invoke({"context": context, "question": user_input})
    context += f"\nUser: {user_input}\n\nBot: {result}\n"  # Added extra newline
    return result, context

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data = urllib.parse.parse_qs(post_data.decode('utf-8'))
        user_input = post_data['message'][0]
        context = post_data.get('context', [''])[0]
        response, context = generate_response(user_input, context)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"response": response, "context": context}).encode('utf-8'))

if __name__ == "__main__":
    PORT = 8000
    Handler = MyHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
